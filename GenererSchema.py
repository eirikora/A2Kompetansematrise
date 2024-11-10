import json

def generer_bransje_json(bransjer):
    json_data = {}
    json_data["Antall år i A-2"] = 0
    json_data["Sertifiseringer"] = "Sertifisering 1, Sertifisering 2, Sertifisering 3"

    for bransje in bransjer:
        json_data[f"{bransje}.måneder"] = 0
        json_data[f"{bransje}.sist"] = 0
        json_data[f"{bransje}.referanse"] = "Kort referanse til relevante prosjekter eller kunder."
    json_data["Andre bransjer"] = "Beskrivelse av andre viktige bransjer konsulenten har erfaring fra."
    return json_data

def generer_teknologi_json(teknologier):
    json_data = {}
    for teknologi in teknologier:
        json_data[f"{teknologi}.måneder"] = 0
        json_data[f"{teknologi}.sist"] = 0
    json_data["Andre teknologier"] = "Beskrivelse av andre viktige teknologier konsulenten har erfaring fra."
    return json_data

def generer_annen_kompetanse_json(kompetanser):
    json_data = {}
    for kompetanse in kompetanser:
        json_data[f"{kompetanse}.måneder"] = 0
        json_data[f"{kompetanse}.sist"] = 0
    return json_data

# Skap JSON for Bransjer
bransjer = [
    "Offentlig forvaltning",
    "Kommunesektor",
    "Helsesektor",
    "Telekomsektor",
    "Energisektor(ikke olje)",
    "Olje og gass-sektor",
    "Handel og industrisektor",
    "Bank og finanssektor",
    "Forsikring",
    "Pensjonsforvaltning",
    "Utdanningssektor",
    "Bibliotekssektor",
    "Transportsektor",
    "Forsvarssektor",
    "IKT-tjenester",
    "HR og Personal"
]
json_bransjer = generer_bransje_json(bransjer)
# For å skrive JSON-dataene til fil eller skrive ut
#json_str_bransjer = json.dumps(json_bransjer, ensure_ascii=False, indent=4)
#print(json_str_bransjer)

# Save the result to a file
with open("Schema_bransjeerfaring.json", "w", encoding="utf-8") as file:
    json.dump(json_bransjer, file, ensure_ascii=False, indent=4)


# Definerer variabelen med teknologiene
teknologier = [
    "Teknologi.Sky- og IT-infrastruktur.Snowflake",
    "Teknologi.Sky- og IT-infrastruktur.MS Azure",
    "Teknologi.Sky- og IT-infrastruktur.Lokalt datasenter etablering og drift",
    "Teknologi.Sky- og IT-infrastruktur.Google Cloud Services",
    "Teknologi.Sky- og IT-infrastruktur.Databricks",
    "Teknologi.Sky- og IT-infrastruktur.Amazon Web Services (AWS)",
    "Teknologi.Programmering.Python utvikling",
    "Teknologi.Programmering.Mobilapp utvikling",
    "Teknologi.Programmering.Java utvikling",
    "Teknologi.Programmering.Fullstack utvikling",
    "Teknologi.Programmering.Frontend utvikling",
    "Teknologi.Programmering.C++ utvikling",
    "Teknologi.Programmering.C#/.Net utvikling",
    "Teknologi.Programmering.Backend utvikling",
    "Teknologi.Maskinlæring og KI-verktøy.OpenAI ChatGPT",
    "Teknologi.Maskinlæring og KI-verktøy.MS Machine Learning",
    "Teknologi.Maskinlæring og KI-verktøy.MS CoPilot",
    "Teknologi.Maskinlæring og KI-verktøy.Maskinlæring",
    "Teknologi.Maskinlæring og KI-verktøy.Kunstig Intelligens (AI/KI)",
    "Teknologi.Maskinlæring og KI-verktøy.Google AI",
    "Teknologi.Maskinlæring og KI-verktøy.Generativ KI",
    "Teknologi.Digitalisering og automasjon.User Interface design",
    "Teknologi.Digitalisering og automasjon.Tjenestedesign/Design thinking",
    "Teknologi.Digitalisering og automasjon.MS Power Automate",
    "Teknologi.Digitalisering og automasjon.MS Power Applications",
    "Teknologi.DevOps og CI/CD.JIRA og Confluence",
    "Teknologi.DevOps og CI/CD.Continous Deployment (CICS, o.l.)",
    "Teknologi.Dataanalyse og BI-verktøy.Tableau",
    "Teknologi.Dataanalyse og BI-verktøy.Qlik",
    "Teknologi.Dataanalyse og BI-verktøy.MS PowerBI",
    "Teknologi.Dataanalyse og BI-verktøy.Dataanalyseverktøy",
    "Teknologi.Dataanalyse og BI-verktøy.Business Intelligence (BI)",
    "Teknologi.Datadrevet strategi og analyse.Datadrevet beslutningstakning",
    "Teknologi.Datadrevet strategi og analyse.Data governance og compliance",
    "Teknologi.Databaser og APIer.REST API",
    "Teknologi.Databaser og APIer.Relasjonelle databaser og SQL",
    "Teknologi.Databaser og APIer.GraphQL API",
    "Teknologi.Databaser og APIer.Grafdatabaser",
    "Arkitektur og modellering.Virksomhetsarkitektur",
    "Arkitektur og modellering.UML",
    "Arkitektur og modellering.TOGAF",
    "Arkitektur og modellering.Tjenestearkitektur",
    "Arkitektur og modellering.Løsnings- og teknisk arkitektur",
    "Arkitektur og modellering.Kafka",
    "Arkitektur og modellering.Informasjonsmodellering",
    "Arkitektur og modellering.Informasjonsarkitektur",
    "Arkitektur og modellering.Hendelsesorientert arkitektur",
    "Arkitektur og modellering.Feiltolerante systemer",
    "Arkitektur og modellering.Cyber-resiliente og sikre systemer",
    "Arkitektur og modellering.Arkitekturmodellering",
    "Arkitektur og modellering.Archimate"
]
# Generer JSON resultat
json_resultat_teknologi = generer_teknologi_json(teknologier)

# Skriver ut resultatet i JSON-format
#json_str = json.dumps(json_resultat_teknologi, ensure_ascii=False, indent=4)
#print(json_str)

# Save the result to a file
with open("Schema_teknologi_kompetanse.json", "w", encoding="utf-8") as file:
    json.dump(json_resultat_teknologi, file, ensure_ascii=False, indent=4)


# Definerer variabelen med annen kompetanse
annen_kompetanse = [
    "Rammeverk og smidige metodikker.Valuestream mapping",
    "Rammeverk og smidige metodikker.Smidig metodikk (Scrum, Kanban, SAFE)",
    "Rammeverk og smidige metodikker.LEAN metodikker",
    "Rammeverk prosjekt- og programledelse.Prosjektledelse",
    "Rammeverk prosjekt- og programledelse.PRINCE2 Agile",
    "Rammeverk prosjekt- og programledelse.PRINCE2",
    "Rammeverk prosjekt- og programledelse.MSP (Managing Successful Programmes)",
    "Rammeverk prosjekt- og programledelse.MoP (Management of Portfolios)",
    "Rammeverk prosjekt- og programledelse.Gartner metodikk",
    "Rammeverk prosjekt- og programledelse.Accenture metodikk",
    "Rammeverk prosjekt- og programledelse.A-2 metodikk",
    "Rammeverk prosjekt- og programledelse.ITIL-rammeverket",
    "Rammeverk kvalitetssikring.Kvalitetssikring og systemtesting",
    "Rammeverk kvalitetssikring.Kvalitetssikring av styringsunderlag samt kostnadsoverslag (KS2)",
    "Rammeverk kvalitetssikring.Kvalitetssikring av konseptvalg (KS1)",
    "Rammeverk kvalitetssikring.Akseptansetesting",
    "Offentlig sektor.Sak- og arkivsystemer.P360/Public 360",
    "Offentlig sektor.Sak- og arkivsystemer.ePhorte",
    "Offentlig sektor.Sak- og arkivsystemer.Elements",
    "Offentlig sektor.Sak- og arkivsystemer.Documentum",
    "Offentlig sektor.Sak- og arkivsystemer.ACOS WebSak",
    "Offentlig sektor.Lovverk.SORA",
    "Offentlig sektor.Lovverk.Offentlige anskaffelser",
    "Offentlig sektor.Lovverk.NOARK",
    "Offentlig sektor.Lovverk.Lov om offentlige anskaffelser",
    "Offentlig sektor.Lovverk.GDPR",
    "Offentlig sektor.Lovverk.EU AI Act",
    "Offentlig sektor.Lovverk.Bokføringsloven",
    "Offentlig sektor.Lovverk.Arbeidsmiljøloven",
    "Ledelse og strategisk kompetanse.Virksomhetsstrategi",
    "Ledelse og strategisk kompetanse.Situasjonskartlegging",
    "Ledelse og strategisk kompetanse.Gevinstrealisering",
    "Ledelse og strategisk kompetanse.Digitaliseringsstrategi",
    "Ledelse og evaluering av risiko.Statens prosjektmodell/veiviser",
    "Ledelse og evaluering av risiko.Risiko og sårbarhetsanalyse (ROS)",
    "Ledelse og evaluering av risiko.Offentlige utredninger og utredningsinstruksen",
    "Ledelse og teamstyring.Ledelse i smidig miljø",
    "Ledelse og teamstyring.Ledelse i DevOps miljø",
    "Ledelse og teamstyring.Ledelse av utviklingsteam",
    "Ledelse og teamstyring.Ledelse av større programmer",
    "Ledelse og teamstyring.Ledelse av hybride team",
    "Ledelse og teamstyring.Ledelse av globale team med kulturell forståelse",
    "Ledelse og teamstyring.Ledelse av funksjon for sikkerhet og beredskap",
    "Ledelse og teamstyring.Innovasjonsledelse",
    "Ledelse og teamstyring.Avdeling/Personalledelse",
    "Endringsledelse.Kultur- og organisasjonsforståelse",
    "Endringsledelse.Endringsledelse og adopsjon",
    "Bransjeløsninger.SAP",
    "Bransjeløsninger.Oracle",
    "Bransjeløsninger.Regnskapssystemer",
    "Bransjeløsninger.Personalsystemer",
    "Bransjeløsninger.Logistikkløsninger",
    "Bransjeløsninger.Industristyring",
    "Bransjeløsninger.Fakturasystemer",
    "Bransjeløsninger.ERP-systemer",
    "Spesialteknologi.Digital radioteknologi (GSM, NFC, Bluetooth, o.l.)",
    "Prosess- og tjenesteforbedring.workshops og møter",
    "Prosess- og tjenesteforbedring.Prosessforbedringer",
    "Prosess- og tjenesteforbedring.Kartlegging av prosesser og IT-løsninger",
    "Prosess- og tjenesteforbedring.Fasilitering av prosesser",
    "Kunde/brukerperspektiv.Customer Experience (CX) og Customer Journey Mapping",
    "Kunde/brukerperspektiv.Adferdspsykologi",
    "Kommunikasjon og forhandling.Konflikthåndtering",
    "Kommunikasjon og forhandling.Kommunikasjonskompetanse",
    "Kommunikasjon og forhandling.Forhandlingsteknikker"
]

# Generer JSON resultat
json_resultat_annen = generer_annen_kompetanse_json(annen_kompetanse)

# Skriver ut resultatet i JSON-format
#json_str = json.dumps(json_resultat_annen, ensure_ascii=False, indent=4)
#print(json_str)

# Save the result to a file
with open("Schema_annen_kompetanse.json", "w", encoding="utf-8") as file:
    json.dump(json_resultat_annen, file, ensure_ascii=False, indent=4)