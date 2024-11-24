import json

def generer_bransje_json(bransjer):
    json_data = {}

    for bransje in bransjer.keys():
        json_data[f"{bransje}.ref"] = "Kort referanse. " + bransjer[bransje]
        json_data[f"{bransje}.mnd"] = 0
        json_data[f"{bransje}.sist"] = 0
    json_data["Andre bransjer"] = "Navn på andre viktige bransjer ikke nevnt over som konsulenten har erfaring fra."
    return json_data

def generer_teknologi_json(teknologier):
    json_data = {}
    for teknologi in teknologier.keys():
        json_data[f"{teknologi}.ref"] = "Kort referanse. " + teknologier[teknologi]
        json_data[f"{teknologi}.mnd"] = 0
        json_data[f"{teknologi}.sist"] = 0
    json_data["Andre teknologier"] = "Beskrivelse av andre viktige teknologier ikke nevnt over som konsulenten også har erfaring med."
    return json_data

def generer_annen_kompetanse_json(kompetanser):
    json_data = {}
    for kompetanse in kompetanser.keys():
        json_data[f"{kompetanse}.ref"] = "Kort referanse. " + kompetanser[kompetanse]
        json_data[f"{kompetanse}.mnd"] = 0
        json_data[f"{kompetanse}.sist"] = 0
    return json_data

# Skap JSON for Bransjer
bransjer = {
    "Offentlig": "Inkluderer nasjonale myndigheter, direktorater og etater som utfører administrative og regulatoriske oppgaver, for eksempel Skatteetaten, Helsedirektoratet, eller NAV.",
    "Kommune": "Lokale myndigheter og tilknyttede tjenester som drives av kommuner og fylkeskommuner, for eksempel Oslo kommune, Bærum kommune eller fylkesadministrasjonen i Viken.",
    "Helse": "Helseinstitusjoner og leverandører av helsetjenester, inkludert sykehus, legekontorer, private klinikker, og helseforetak som Helse Sør-Øst eller Volvat Medisinske Senter.",
    "Telekom": "Selskaper som tilbyr telekommunikasjonstjenester som mobilnett, bredbånd og TV, for eksempel Telenor, Telia eller Ice.",
    "Energi": "Virksomheter som produserer og distribuerer fornybar energi som vannkraft, vindkraft og solenergi, for eksempel Statkraft, Hafslund eller Agder Energi.",
    "Olje og gass": "Bedrifter innen leting, utvinning, foredling og distribusjon av olje og gass, som Equinor, Aker BP eller Shell.",
    "Handel og industri": "Produksjonsbedrifter, grossister, og detaljhandel som produserer eller distribuerer varer og tjenester, for eksempel Orkla, Elkjøp eller Jotun.",
    "Finans": "Finansinstitusjoner som banker, investeringsselskaper og låneinstitusjoner, for eksempel DNB, Nordea eller Danske Bank.",
    "Forsikring": "Selskaper som tilbyr forsikringsløsninger innen helse, liv, skade og eiendom, for eksempel Storebrand, Fremtind, Gjensidige, If eller Tryg Forsikring.",
    "Pensjon": "Organisasjoner som håndterer pensjonsordninger for individer eller bedrifter, for eksempel KLP, Storebrand eller Statens pensjonskasse.",
    "Utdanning": "Institusjoner som tilbyr utdanning og opplæring eller som leverer løsninger til utdanningssektoren, inkludert skoler, universiteter og høyskoler, for eksempel NTNU, Skoledata, Universitetet i Oslo eller BI.",
    "Bibliotek": "Offentlige og private biblioteker som støtter lesing, forskning og informasjonsformidling, for eksempel Deichman bibliotek eller Universitetsbiblioteket ved UiO.",
    "Transport": "Selskaper og enheter som leverer person- eller godstransport, inkludert reiselivsnæringen, for eksempel Vy, Posten, SAS, Berg Hansen, DHL, eller Widerøe.",
    "Forsvar": "Militære avdelinger, forsvarsleverandører og sikkerhetsorganisasjoner som Forsvaret, Kongsberg Gruppen eller NATO-relaterte enheter.",
    "IKT": "Bedrifter som er spesialiserte på programvareutvikling, IT drift, IT-infrastruktur og teknisk support, som Sopra Steria, Intility, Accenture eller Microsoft Norge.",
    "HR og Personal": "Organisasjoner og avdelinger som jobber med rekruttering, opplæring og personaladministrasjon, som Manpower, Adecco eller interne HR-avdelinger i større selskaper."
}
json_bransjer = generer_bransje_json(bransjer)
# For å skrive JSON-dataene til fil eller skrive ut
#json_str_bransjer = json.dumps(json_bransjer, ensure_ascii=False, indent=4)
#print(json_str_bransjer)

# Save the result to a file
with open("Schema_bransjeerfaring.json", "w", encoding="utf-8") as file:
    json.dump(json_bransjer, file, ensure_ascii=False, indent=4)


# Definerer variabelen med teknologiene
teknologier = {
    "Digitalisering.UX": "Erfaring fra design eller utvikling av brukervennlige brukergrensesnitt.",
    "Digitalisering.Tjenestedesign": "Erfaring fra bruk av metoder for å utvikle tjenester basert på brukerbehov og iterativ testing, som f.eks. Design Thinking.",
    "KI.Generelt": "Erfaring fra konkret bruk av Kunstig intelligens i prosjekter.",
    "KI.OpenAI": "Erfaring fra konkret bruk av OpenAI verktøy som ChatGPT og OpenAI API i prosjekter.",
    "KI.MS Machine Learning": "Erfaring fra konkret bruk av Microsofts verktøy for å bygge og deploye maskinlæringsmodeller.",
    "KI.MS CoPilot": "Erfaring fra konkret bruk av Microsofts AI-assistent i prosjekter eller egen produktivitet.",
    "KI.Maskinlæring": "Erfaring fra konkret bruk av algoritmer og modeller for å analysere data og forutsi utfall.",
    "KI.Google": "Erfaring fra konkret bruk av Googles AI-verktøy og løsninger for maskinlæring og databehandling.",
    "KI.GenKI": "Erfaring fra konkret bruk av AI i prosjekter som lager nytt innhold basert på eksisterende data.",
    "Sky.MS Azure": "Erfaring fra bruk av Microsoft Azure skyplattform som tilbyr tjenester som lagring, maskinlæring, utvikling og applikasjonsdrift.",
    "Sky.Lokalt datasenter": "Erfaring fra planlegging, anskaffelse, etablering, bygging og administrasjon av datasentre for organisasjoners IT-behov.",
    "Sky.Google Cloud": "Erfaring med Google Cloud Services skyplattform som tilbyr tjenester og verktøy for lagring, maskinlæring, utvikling og applikasjonsdrift.",
    "Sky.AWS": "Erfaring fra Amazon Web Services (AWS) sin tjenester for utvikling, datahåndtering, AI og applikasjonsdrift.",
    "Utvikling.Python": "Erfaring fra utvikling med Python.",
    "Utvikling.Mobilapp": "Erfaring fra utvikling av applikasjoner for mobile enheter, inkludert iOS og Android.",
    "Utvikling.Java": "Erfaring fra utvikling med Java.",
    "Utvikling.Fullstack": "Erfaring fra utvikling som dekker både frontend (brukergrensesnitt) og backend (serverlogikk).",
    "Utvikling.Frontend": "Erfaring fra design og utvikling av brukergrensesnitt og visuelle komponenter, ofte med HTML, CSS og JavaScript.",
    "Utvikling.C++": "Erfaring fra utvikling med C++.",
    "Utvikling.Microsoft": "Erfaring fra utvikling på Windowsplattformen med rammeverk og språk som C# og .Net.",
    "Utvikling.Backend": "Erfaring fra utvikling av serversiden som håndterer data og forretningslogikk for applikasjoner.",
    "Utvikling.Lavkode": "Erfaring fra lavekode utvikling i prosjekter.",
    "DevOps.JIRA og Confluence": "Erfaring fra bruk av verktøy fra Atlassian for prosjektstyring og dokumentasjon i utviklingsteam.",
    "DevOps.CICD": "Erfaring fra automatisering av prosesser for å bygge, teste og deploye kode kontinuerlig.",
    "Lavkode.MS Power Automate": "Erfaring fra bruk av Microsofts verktøy for å automatisere arbeidsflyter og prosesser.",
    "Lavkode.MS Power Apps": "Erfaring fra bruk av Microsofts plattform for å lage tilpassede forretningsapplikasjoner.",
    "Lavkode.Zoho": "Erfaring fra bruk av Zoho Creator for å lage tilpassede forretningsapplikasjoner.",
    "Dataanalyse.Databricks": "Erfaring fra bruk av Databricks plattform og Apache Spark for datalagring, dataprosessering, analyse, maskinlæring eller datavarehus.",
    "Dataanalyse.Snowflake": "Erfaring fra bruk av Snowflake for datalagring, dataprosessering, analyse, maskinlæring eller datavarehus.",
    "Dataanalyse.Tableau": "Erfaring fra bruk av Tableau for business intelligence, data visualisering, dataanalyse og innsiktsdeling.",
    "Dataanalyse.Qlik": "Erfaring fra bruk av Qlik for business intelligence, data visualisering, dataanalyse og innsiktsdeling.",
    "Dataanalyse.MS PowerBI": "Erfaring fra bruk Microsofts PowerBI verktøy for business intelligence, data visualisering, dataanalyse og innsiktsdeling.",
    "Dataanalyse.Dataanalyseverktøy": "Erfaring fra bruk av data analyseverktøy for å analysere og tolke store datasett.",
    "Dataanalyse.BI": "Erfaring fra bruk av business intelligence verktøy som kombinerer dataanalyse, visualisering og rapportering.",
    "Database.Relasjonell": "Erfaring fra bruk av Relasjonelle Databaser basert på tabellstrukturer og spørring med SQL.",
    "Database.SQL": "Erfaring fra bruk av SQL verktøy til å spørre Relasjonelle Databaser.",
    "Database.Grafdata": "Erfaring fra bruk av databaser som organiserer data i grafer for komplekse relasjoner, som Neo4j eller GraphDB",
    "API.REST": "Erfaring fra bruk av REST-API standarden som lar systemer utveksle data via HTTP.",
    "API.GraphQL": "Erfaring fra bruk av GraphQL for spørring av spesifikke data.",
    "Arkitektur.Virksomhetsarkitektur": "Erfaring fra arbeid med virksomhetsarkitektur eller forretningsarkitektur for planlegging og styring av en organisasjons prosesser, teknologi og ressurser.",
    "Arkitektur.Tjenestearkitektur": "Erfaring fra arbeid med tjenestearkitekturer og design og strukturering av tjenester for samhandling mellom systemer.",
    "Arkitektur.Løsningsarkitektur": "Erfaring fra arbeid med løsningsarkitektur og teknisk arkitektur for å møte krav og behov.",
    "Arkitektur.Informasjonsarkitektur": "Erfaring fra arbeid med informasjonsmodellering, strukturering og organisering av informasjon i prosjekter.",
    "Arkitektur.Hendelsesorientert": "Erfaring fra arbeid med hendelsesorientert arkitektur.",
    "Arkitektur.Datadrevet": "Erfaring fra arbeid med metoder og strategier for å ta beslutninger basert på analyser og data.",
    "Arkitektur.Governance": "Erfaring fra arbeid med governance og styring av IT funksjoner som arkitektur, datahåndtering, mm. for å sikre samsvar med regelverk og beste praksis.",
    "Arkitektur.UML": "Erfaring fra bruk av UML for å visualisere systemdesign og strukturer.",
    "Arkitektur.TOGAF": "Erfaring fra arbeid med TOGAF rammeverket for utvikling av virksomhetsarkitektur.",
    "Arkitektur.Kafka": "Erfaring fra bruk av Kafka for sanntids dataflyt og meldingskøer.",
    "Arkitektur.Feiltoleranse": "Erfaring fra arbeid med feiltoleranse i systemer for å fortsette å fungere under feilforhold.",
    "Arkitektur.Cybersikkerhet": "Erfaring fra arbeid med cybersikkerhet og systemer som beskytter mot og gjenoppretter etter cyberangrep.",
    "Arkitektur.Archimate": "Erfaring fra bruk av Archimate for modellering av arkitektur i et prosjekt.",
    "Teknologi.Radio": "Erfaring med digital radioteknologi som GSM, NFC eller Bluetooth."
}

# Generer JSON resultat
json_resultat_teknologi = generer_teknologi_json(teknologier)

# Skriver ut resultatet i JSON-format
#json_str = json.dumps(json_resultat_teknologi, ensure_ascii=False, indent=4)
#print(json_str)

# Save the result to a file
with open("Schema_teknologi_kompetanse.json", "w", encoding="utf-8") as file:
    json.dump(json_resultat_teknologi, file, ensure_ascii=False, indent=4)


# Definerer variabelen med annen kompetanse
annen_kompetanse = {
    "Ledelse.Prosjekt": "Erfaring med prosjektledelse, inkludert planlegging, styring og gjennomføring av prosjekter.",
    "Ledelse.DevOps": "Erfaring med ledelse i DevOps-miljøer med fokus på automatisering og samarbeid.",
    "Ledelse.Endringsledelse": "Erfaring med ledelse og styring av endringsprosesser og brukeradopsjon.",
    "Ledelse.utvikling": "Erfaring med ledelse av team eller prosjekter for programvareutvikling.",
    "Ledelse.program": "Erfaring med styring og koordinering av større eller komplekse programmer.",
    "Ledelse.hybrid": "Erfaring med ledelse av team som kombinerer fysiske og fjernarbeidende medlemmer.",
    "Ledelse.global": "Erfaring med ledelse av internasjonale team med behov for å forstå kulturelle forskjeller.",
    "Ledelse.sikkerhet": "Erfaring med ledelse av sikkerhets- og beredskapsfunksjoner, prosjekter eller miljøer.",
    "Ledelse.innovasjon": "Erfaring med ledelse av innovasjonsprosesser og løsninger.",
    "Ledelse.personell": "Erfaring med personalledelse og/eller ledelse av avdelinger.",
    "Ledelse.konflikthåndtering": "Erfaring med håndtering av konflikter og problemløsning i team.",
    "Ledelse.kommunikasjon": "Erfaring med metoder for effektiv kommunikasjon i komplekse prosjekter og team.",
    "Ledelse.forhandling": "Erfaring med metoder for forhandlinger i forretnings- eller prosjektkontekster.",
    "Ledelse.endring": "Erfaring med endringsledelse og endring av organisasjonskultur og tilpasning av organisasjonsstrukturer.",
    "Strategi.Virksomhet": "Erfaring med utredning for, utvikling av og implementering av virksomhetsstrategier.",
    "Strategi.Situasjonskartlegging": "Erfaring med situasjonskartlegging (AS-IS) for å identifisere muligheter og utfordringer.",
    "Strategi.Gevinstrealisering": "Erfaring med å utrede, planlegge eller sikre gevinstrealisering fra prosjekter og programmer.",
    "Strategi.Digitaliseringsstrategi": "Erfaring med utredning for, eller utvikling av strategier for digital transformasjon.",
    "Rammeverk.Gartner": "Erfaring med Gartner-rammeverk for IT-strategi og organisasjonsutvikling.",
    "Rammeverk.Accenture": "Erfaring med Accentures rammeverk og tilnærming til prosjektstyring og digital transformasjon.",
    "Rammeverk.A-2": "Erfaring med A-2 sitt rammeverk for digitalisering og metodikk for systemutvikling og prosjektstyring.",
    "Rammeverk.ITIL": "Erfaring med ITIL rammeverket for styring av IT-tjenester og prosesser.",
    "Rammeverk.Statens prosjektmodell": "Erfaring med bruk av Statens prosjektmodell eller veiviser for offentlige prosjekter.",
    "Rammeverk.OffUtredninger": "Erfaring med offentlige utredninger i henhold til utredningsinstruksen.",
    "Rammeverk.OffAnskaffelse": "Erfaring med eller bruk av lov og praksis for offentlige anskaffelser.",
    "Rammeverk.KS2": "Erfaring med KS2 for kvalitetssikring av styringsunderlag og kostnadsoverslag.",
    "Rammeverk.KS1": "Erfaring med KS1 for kvalitetssikring av konseptvalg i offentlige prosjekter.",
    "Regulering.SORA": "Erfaring med sikkerhetsrisikoanalyse i henhold til SORA-rammeverket.",
    "Regulering.NOARK": "Erfaring med NOARK-standarden for elektronisk arkivering i offentlig sektor.",
    "Regulering.GDPR": "Erfaring med prosjekter relatert til etterlevelse av GDPR for personvern og databeskyttelse.",
    "Regulering.EU AI Act": "Erfaring med vurdering av samsvar med EU AI Act for kunstig intelligens.",
    "Regulering.Bokføringsloven": "Erfaring med etterlevelse av Bokføringsloven for økonomiske systemer.",
    "Regulering.Arbeidsmiljøloven": "Erfaring med implementering av tiltak for å etterleve Arbeidsmiljøloven.",
    "Metode.PRINCE2 Agile": "Erfaring med PRINCE2 Agile for prosjektstyring som kombinerer smidige prinsipper med PRINCE2.",
    "Metode.PRINCE2": "Erfaring med PRINCE2 for strukturert prosjektstyring.",
    "Metode.MSP": "Erfaring med MSP  (Managing Successful Programmes)for styring av komplekse programmer med flere prosjekter.",
    "Metode.MoP": "Erfaring med MoP (Management of Portfolios) for porteføljestyring og optimalisering av investeringer.",
    "Metode.Valuestream mapping": "Erfaring med verdistrømskartlegging for å optimalisere prosesser og redusere flaskehalser.",
    "Metode.Smidig": "Erfaring med bruk av smidige metoder som Scrum, Kanban eller SAFe for teamarbeid og prosjektstyring.",
    "Metode.LEAN": "Erfaring med Lean-metodikker for å forbedre effektivitet og redusere sløsing i prosesser.",
    "Metode.systemtesting": "Erfaring med kvalitetssikring og testing av IT-leveranse, systemer og applikasjoner.",
    "Metode.Akseptansetesting": "Erfaring med akseptansetesting for å sikre at systemer møter krav og forventninger.",
    "Metode.ROS": "Erfaring med Risiko- og sårbarhetsanalyser (ROS) for prosjekter og organisasjoner.",
    "Metode.møter": "Erfaring med metoder for fasilitering av workshops og effektive møter.",
    "Metode.Prosessforbedringer": "Erfaring med metoder for analyse av prosesser og fasilitering av prosessforbedringsprosjekter.",
    "Metode.Kartlegging": "Erfaring med metoder for kartlegging av eksisterende prosesser og IT-systemer.",
    "Metode.kundereise": "Erfaring med metoder for å kartlegge og jobbe med kundereiser (Customer Journey Mapping) og forbedre kundeopplevelser (Customer Experience - CX).",
    "Metode.adferdspsykologi": "Erfaring med bruk av adferdspsykologi for å forstå og påvirke brukeratferd.",
    "Løsning.SAP": "Erfaring med SAP-systemer for virksomhetsstyring.",
    "Løsning.Oracle": "Erfaring med Oracles løsninger for databaser og ERP.",
    "Løsning.Saksbehandling": "Erfaring med implementering og bruk av saksbehandlingssystemer, som P360, Elements, ServiceNow, mm.",
    "Løsning.Arkiv": "Erfaring med implementering og bruk av arkivsystemer som P360, ePhorte, Sikri, ACOS.",
    "Løsning.Regnskap": "Erfaring med implementering og bruk av regnskapssystemer.",
    "Løsning.HR": "Erfaring med systemer for personaladministrasjon og HR.",
    "Løsning.Logistikk": "Erfaring med løsninger for logistikkstyring.",
    "Løsning.Industri": "Erfaring med systemer for produksjonsstyring og industrielle prosesser.",
    "Løsning.Faktura": "Erfaring med systemer for fakturering og betalingshåndtering.",
    "Løsning.ERP": "Erfaring med ERP-systemer for integrert virksomhetsstyring."
}


# Generer JSON resultat
json_resultat_annen = generer_annen_kompetanse_json(annen_kompetanse)

# Skriver ut resultatet i JSON-format
#json_str = json.dumps(json_resultat_annen, ensure_ascii=False, indent=4)
#print(json_str)

# Save the result to a file
with open("Schema_annen_kompetanse.json", "w", encoding="utf-8") as file:
    json.dump(json_resultat_annen, file, ensure_ascii=False, indent=4)