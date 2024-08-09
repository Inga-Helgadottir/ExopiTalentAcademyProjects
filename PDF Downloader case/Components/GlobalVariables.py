# ----------------------------------------------------------------------- Data paths
dataPath = "./Data/GRI_2017_2020.csv"

aListOfTheAlreadyDownloadedPDFs = "./Data/aListOfTheAlreadyDownloadedPDFs.csv"
errorInPDF = "./Data/errorInPDF.csv"
allDownloadInfo = "./Data/informationAboutAllDownloadedPDFs.csv"

dropLocationForDownloadedPDFs = "./Data/alreadyDownloaded/"

# ----------------------------------------------------------------------- Variables
noErrorMessage = "NONE"
thisIsTheAllDownloadsMessage = "Data for both"
timeoutLengthInSeconds = (6,30)

CSVFileDataUseCols = ["id","pdf_url_1","pdf_url_2"]
errorCSVFileUseCols = ["id","link","errorcode"]
successCSVFileUseCols = ["id","link"]
bothCSVFileUseCols = ["id","link","status"]

textToAddToEmptyFile_success = "id,link"
textToAddToEmptyFile_error = "id,link,errorcode"
textToAddToEmptyFile_both = "id,link,status"

notAValidLinkText = "The link is not valid"
aValidLinkText = "The link is valid"

# ----------------------------------------------------------------------- Menu related 
defaultLanguage = "English"

whatLanguageIsInUse = "English"

startMessage = "Hello and welcome to the PDF downloader\n   -To Choose English enter E\n\n" + "Hej og velkommen til PDF downloaderen\n   -For at vælge Dansk skriv D\n"

# ---------------------------------------------------------------- English 
englishMessageOptions = [
    "To start downloading PDFs, enter 1\n"
    "To see all the information form the downloads, enter 2\n"
    "To see all the successfully downloaded files, enter 3\n"
    "To see all the failed downloaded files, enter 4\n"
    "To combine the downloaded information files in one file, enter 5\n"
    "To reset all information about the downloaded PDFs, enter 6\n"
    "To reset all information about the successful downloads, enter 7\n"
    "To reset all information about the failed downloads, enter 8\n"   
    "To reset all information in the combined downloads file, enter 9\n"   
    "To exit the program, enter x\n"
]

wrongInputEnglish = " is not a valid option"

# ---------------------------------------------------------------- Danish 
danishMessageOptions = [
    "For at downloade Pdf’erne, skriv 1\n"
    "For at se alle download informationer, skriv 2\n"
    "For at se alle succesfulde downloads, skriv 3\n"
    "For at se alle de mislykkede downloads, skriv 4\n"
    "For at kombinere alle download informationerne i en fil, skriv 5\n"
    "For at slette alt information om tidligere downloadede filer, skriv 6\n"
    "For at slette alt information om de succesfulde downloads, skriv 7\n"
    "For at slette alt information om de mislykkede downloads, skriv 8\n"
    "For at slette alt information fra den kombinerede fil, skriv 9\n"   
    "For at lukke programmet, skriv x\n"
]

wrongInputDanish = " er ikke en mulighed"

# -----------------------------------------------------------------------TEST related

smallTestdataPath = "../Tests/TestData/testData-smaller-GRI_2017_2020.csv"

fullTestdataPath = "../Tests/TestData/testData-GRI_2017_2020.csv"

testerrorInPDF = "../Tests/TestData/testData-errorInPDF.csv"

testaListOfTheAlreadyDownloadedPDFs = "../Tests/TestData/testData-aListOfTheAlreadyDownloadedPDFs.csv"

testdropLocationForDownloadedPDFs = "../Tests/TestData/downloadedByATest/"    
