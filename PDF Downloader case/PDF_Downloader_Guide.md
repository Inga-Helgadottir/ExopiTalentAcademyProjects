[Dansk Version](#velkommen-til-pdf-downloader-projektet) - Tryk på ctrl imens du klikker på linket

# Welcome to the PDF Downloader project

## Made by Sigurros Inga Helgadottir

With this project you can add a CSV file with ids and links to PDF files and download them all

Information about each link you have attempted to download will be written in files, there is one file for the successful downloads and one with the unsuccessful downloads

## Before you run the project

Make sure you have the ids and links of the desired PDFs in a CSV file named GRI_2017_2020.csv in the Data folder (id, pdf_url_1, pdf_url_2)

## General information

- All of the downloaded PDFs will be added to the [Data/alreadyDownloaded](Data/alreadyDownloaded/) folder starting with their "id-" then the name of the PDF itself

- Information from the successfully downloaded files will be added to /Data/aListOfTheAlreadyDownloadedPDFs.csv with the format (id,link)

- Information from the failed downloads will be added to /Data/errorInPDF.csv with the format (id,link,errorMessage)

- To start downloading PDFs, open a terminal in the root of this folder and write python go.py

### The options in this program will be shown after every action with a number value to specify which choice you made

- Download PDFs

- See all the information form the downloads

- See all the successfully downloaded files

- See all the failed downloaded files

- Combine the download informations in one file

- Reset all information about the downloaded PDFs

- Reset all information about the successful downloads

- Reset all information about the failed downloads

### To rename the CSV files go to [/Components/GlobalVariables.py](/Components/GlobalVariables.py), when you change it here, it changes EVERYWHERE

dataPath = "./Data/GRI_2017_2020.csv" - The original data path

aListOfTheAlreadyDownloadedPDFs = "./Data/aListOfTheAlreadyDownloadedPDFs.csv" - A list of the successful downloads

errorInPDF = "./Data/errorInPDF.csv" - A list of the unsuccessful downloads

allDownloadInfo = "./Data/informationAboutAllDownloadedPDFs.csv" - A list you can use the menu to generate, that shows the information about all downloads

dropLocationForDownloadedPDFs = "./Data/alreadyDownloaded/" - The folder where all the downloaded files go

---

# Velkommen til PDF Downloader projektet

## Lavet af Sigurros Inga Helgadottir

Dette projekt tager imod en CSV-fil, hver række i filen har et id og 2 links og downloade dem alle

Informationer om hvert link bliver tilføjet til en anden CSV-fil,

- der er en fil for de downloads som virkede

- der er en fil med dem som gav fejl, med en fejlbesked

## Før du kører projektet

Du skal være sikker på at de rigtige links ligger i en fil som hedder GRI_2017_2020.csv i Data folderen med kolonner som hedder (id, pdf_url_1, pdf_url_2)

## General information

- Alle de downloadede PDF filer bliver tilføjet til [Data/alreadyDownloaded](Data/alreadyDownloaded/) folderen, de hedder alle "id-" + navnet på filen

- Informationer om de downloads som lykkedes bliver tilføjet til [/Data/aListOfTheAlreadyDownloadedPDFs.csv](/Data/aListOfTheAlreadyDownloadedPDFs.csv) med formatet (id,link)

- Informationer om de mislykkede downloads bliver tilføjet til [/Data/errorInPDF.csv](/Data/errorInPDF.csv) med formatet (id,link,errorMessage)

- For at starte projektet, åbn en terminal og skriv: python go.py

- Efter det vælger du mellem Dansk og Engelsk og så får du alle dine muligheder skrevet op til dig

### Mulighederne i dette program bliver vist i en menu efter hver ændring

- Downloade Pdf’er

- Se alle download informationer

- Se informationer om alle succesfulde downloads

- Se informationer om alle de mislykkede downloads

- Kombinere informations filerne på et sted

- Slette alt information om tidligere downloadede filer

- Slette alt information om de succesfulde downloads

- Slette alt information om de mislykkede downloads

### For at ændre navne på de CSV-filerne der bliver brugt [/Components/GlobalVariables.py](/Components/GlobalVariables.py), når du ændrer det her, ændres det OVERALT

dataPath = "./Data/GRI_2017_2020.csv" - Dataet med PDF-links

aListOfTheAlreadyDownloadedPDFs = "./Data/aListOfTheAlreadyDownloadedPDFs.csv" - En liste af de succesfulde downloads

errorInPDF = "./Data/errorInPDF.csv" - En liste af de mislykkede downloads

allDownloadInfo = "./Data/informationAboutAllDownloadedPDFs.csv" - En liste man kan generere i menuen som viser alle informationer om downloads

dropLocationForDownloadedPDFs = "./Data/alreadyDownloaded/" - Folderen med alle downloadede PDF-filer
