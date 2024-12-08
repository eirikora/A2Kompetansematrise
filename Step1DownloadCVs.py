import pandas as pd
import json
from dotenv import load_dotenv
import os
import shutil
import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
from sharepoint_fields.requestSharepointFields import requestSharepointFields

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler("pipeline_download.log")]
)

# Set the locale to Norwegian (use "nb_NO" or "no_NO" depending on your system)
try:
    locale.setlocale(locale.LC_TIME, "nb_NO")
except locale.Error:
    logging.error("Could not set locale to Norwegian. Ensure that 'nb_NO' is available on your system.")

# Load environment variables from .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
A2_PIPELINE = os.getenv("A2_PIPELINE")
A2_CV_FOLDER = os.getenv("A2_CV_FOLDER")
CONSULTANT_JSON_FILE = "consultant_cv_data.json"

# Load JSON data if file exists
consultant_data = {}
if os.path.exists(CONSULTANT_JSON_FILE):
    with open(CONSULTANT_JSON_FILE, "r") as f:
        consultant_data = json.load(f)
    logging.info("Consultant CV data loaded from existing JSON file.")

# Tracking variables
updated_consultants = []
removed_cvs = []

def GetPipelineData():
    """
    Downloads and processes Ressursdata from A-2 Pipeline.
    Returns:
        DataFrame: Processed dataframe with renamed columns and filtered data.
    """
    try:
        # Path to the Excel file on your OneDrive
        excel_file = A2_PIPELINE 
        logging.info("Loading pipeline data from Excel file.")

        # Read the Excel sheet "Ressursdisponering" with headers from row 3
        df = pd.read_excel(excel_file, sheet_name="Ressursdisponering", header=2)

        # Filter out rows where the 'e-post' column is empty
        df = df[df['e-post'].notna() & (df['e-post'] != "")]
        logging.info("Pipeline data loaded and filtered successfully.")

        # Trim relevant columns and perform transformations
        df['ID'] = df['ID'].str.strip().str.upper()
        df['e-post'] = df['e-post'].str.strip().str.lower()
        df['Ressurs'] = df['Ressurs'].str.strip()
        df['Mentor'] = df['Mentor'].str.strip().str.upper()

        # Generate month and year labels for L1-L6, S1-S6, and T1-T6 columns
        current_date = datetime.now()
        new_column_names = {}

        for i in range(6):
            future_date = current_date + relativedelta(months=i)
            month_name = future_date.strftime("%B").capitalize()
            year = future_date.year
            new_column_names[f'L{i+1}'] = f"Ledig {month_name} {year}"
            new_column_names[f'S{i+1}'] = f"Sannsynlig ledig {month_name} {year}"
            new_column_names[f'T{i+1}'] = f"Kapasitet {month_name} {year}"

        df.rename(columns=new_column_names, inplace=True)
        
        # Round specified columns to one decimal place
        for col in new_column_names.values():
            df[col] = df[col].round(1)
        
        logging.info("Columns renamed and rounded to one decimal place based on current month and year.")

        return df

    except Exception as e:
        logging.error(f"Error loading pipeline data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure

def download_CVs(df, base_folder, download_folder="downloaded_CVs"):
    """
    Downloads CVs for each consultant listed in the DataFrame if their SharePoint metadata has 'Documenttype' set to 'Standard CV'.
    
    Args:
        df (DataFrame): DataFrame containing consultant data with 'Ressurs' (consultant name) column.
        base_folder (str): Base directory where consultant folders are stored.
        download_folder (str): Directory to store downloaded CVs.
    """
    os.makedirs(download_folder, exist_ok=True)
    
    sharepoint_site = "a2norge.sharepoint.com"
    site_name = 'Intranett'
    drive_name = 'Ansatte'

    for _, row in df.iterrows():
        consultant_name = row['Ressurs']
        consultant_folder = os.path.join(base_folder, consultant_name)
        expected_file = f"{consultant_name}_CV.docx"
        expected_file_path = os.path.join(download_folder, expected_file)

        # Check if the CV file is missing from the download folder
        if not os.path.exists(expected_file_path):
            logging.info(f"{consultant_name}'s CV is missing in {download_folder}. Proceeding with download.")
            skip_download = False
        else:
            skip_download = False
            # Check if consultant data exists and if the file is already downloaded
            if consultant_name in consultant_data:
                last_downloaded_file = consultant_data[consultant_name].get("CV filnavn")
                last_downloaded_timestamp = consultant_data[consultant_name].get("CV timestamp")
                
                # Check if the file still exists and has the same modified time as recorded
                for file_name in os.listdir(consultant_folder):
                    if file_name == last_downloaded_file:
                        source_file = os.path.join(consultant_folder, file_name)
                        file_mod_timestamp = int(os.path.getmtime(source_file))
                        
                        if file_mod_timestamp == last_downloaded_timestamp:
                            logging.info(f"No change detected for {consultant_name}'s CV. Skipping download.")
                            skip_download = True
                            break
                        else:
                            logging.info(f"Change detected for {consultant_name}'s CV. Proceeding with metadata check.")
                            break
                else:
                    logging.warning(f"Expected file {last_downloaded_file} not found in {consultant_folder}. Proceeding with scan.")
        
        # Continue if no valid cached information or change detected
        if not skip_download and os.path.isdir(consultant_folder):
            for file_name in os.listdir(consultant_folder):
                if file_name.endswith(".docx"):
                    source_file = os.path.join(consultant_folder, file_name)
                    file_relative_path = f"{consultant_name}/{file_name}"
                    
                    try:
                        metadata = requestSharepointFields(sharepoint_site, site_name, drive_name, file_relative_path)

                        if metadata.get("Dokumenttype") == "Standard CV":
                            shutil.copy2(source_file, expected_file_path)
                            logging.info(f"Downloaded CV for {consultant_name}")
                            
                            # Update JSON data with new file and modification timestamp
                            consultant_data[consultant_name] = {
                                "konsulentnavn": consultant_name,
                                "CV filnavn": file_name,
                                "CV timestamp": int(os.path.getmtime(source_file))
                            }
                            
                            # Track the updated consultant
                            updated_consultants.append(consultant_name)
                            break
                    except Exception as e:
                        logging.error(f"Error retrieving metadata for {consultant_name}'s file '{file_name}': {e}")
                        continue
            else:
                logging.warning(f"No Standard CV found for {consultant_name} in {consultant_folder}")
        elif not os.path.isdir(consultant_folder):
            logging.warning(f"Folder not found for {consultant_name}")

def cleanup_old_cvs(download_folder="downloaded_CVs"):
    """
    Removes outdated CV files from the downloaded folder.
    
    Args:
        download_folder (str): Directory where downloaded CVs are stored.
    """
    valid_files = {f"{data['konsulentnavn']}_CV.docx" for data in consultant_data.values()}
    
    for file_name in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file_name)
        if file_name not in valid_files:
            try:
                os.remove(file_path)
                logging.info(f"Removed outdated CV file: {file_name}")
                
                # Track the removed CV
                removed_cvs.append(file_name)
            except Exception as e:
                logging.error(f"Error deleting file {file_name}: {e}")

# Main execution
logging.info("DOWNLOADING A-2 PIPELINE:")
pipeline_df = GetPipelineData()

# Save pipeline as CSV file
pipeline_df.to_csv("a2pipeline.csv", index=False)
logging.info("A2 Pipeline is now saved as a2pipeline.csv.")

# Download all the CVs
if not pipeline_df.empty:
    logging.info("DOWNLOADING CONSULTANT CVs (Takes time because needs to check Sharepoint metadata for all files found!):")
    download_CVs(pipeline_df, A2_CV_FOLDER)

    # Clean up old CVs that are no longer in use
    logging.info("CLEANING UP OUTDATED CVs:")
    cleanup_old_cvs()
else:
    logging.error("Pipeline data could not be loaded. CV download aborted.")

# Save consultant data to JSON file
with open(CONSULTANT_JSON_FILE, "w") as f:
    json.dump(consultant_data, f, indent=4)
logging.info("Consultant CV data saved to JSON file.")

# Summary log
logging.info(f"COMPLETED! Summary:")
logging.info(f"Total consultants in pipeline: {len(pipeline_df)}")
logging.info(f"Updated CVs: {len(updated_consultants)} ({', '.join(updated_consultants)})")
logging.info(f"Removed outdated CVs: {len(removed_cvs)} ({', '.join(removed_cvs)})")