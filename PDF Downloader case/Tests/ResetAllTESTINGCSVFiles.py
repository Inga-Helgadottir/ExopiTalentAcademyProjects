from Components.ResetCSVFile import ResetCSVFile
from Components.GlobalVariables import noErrorMessage, testerrorInPDF, textToAddToEmptyFile_error, testaListOfTheAlreadyDownloadedPDFs, textToAddToEmptyFile_success

def ResetAllTESTINGCSVFiles():
    ResetCSVFile(testerrorInPDF, textToAddToEmptyFile_error, "404")
    ResetCSVFile(testaListOfTheAlreadyDownloadedPDFs, textToAddToEmptyFile_success, noErrorMessage)
        
