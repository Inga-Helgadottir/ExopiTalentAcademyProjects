import os
import urllib3
import requests
from Components.AddToCSV import AddToCSV
from Components.GlobalVariables import timeoutLengthInSeconds, aValidLinkText, notAValidLinkText, noErrorMessage, aListOfTheAlreadyDownloadedPDFs, dropLocationForDownloadedPDFs, errorInPDF, testerrorInPDF, testaListOfTheAlreadyDownloadedPDFs, testdropLocationForDownloadedPDFs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def CheckAndDownloadPDF(linkToHandle, reserveLink, id, isTest, isSecondLink):
    PDFstatus = "404"
    try:
        # Setting the variables I use in this function, if this is a test, the variables are different
        if isTest:
            csvFileForErrors = testerrorInPDF
            csvFileForSuccessFullDownloads = testaListOfTheAlreadyDownloadedPDFs
            downloadedPDFsFolder = testdropLocationForDownloadedPDFs
        else:
            csvFileForErrors = errorInPDF
            csvFileForSuccessFullDownloads = aListOfTheAlreadyDownloadedPDFs
            downloadedPDFsFolder = dropLocationForDownloadedPDFs
            
        # Gets the link
        response = requests.get(linkToHandle, stream=False, verify=False, timeout=timeoutLengthInSeconds, allow_redirects=False)
        # Checks what type of link this is
        content_type = response.headers.get('content-type')
        # Saves the status code in a variable
        PDFstatus = str(response.status_code)
       
        # Checks if this is a PDF
        if 'application/pdf' in content_type:
            # Saves the content of the PDF in a variable
            PDFcontent = response.content 
            # Saves the name of the PDF in a variable
            pdf_file_name = os.path.basename(linkToHandle)
            # Making the path to the file (where, what to call it)
            filepath = os.path.join(downloadedPDFsFolder, id + "-" + pdf_file_name)
                           
            # Creates and opens the file 
            with open(filepath, 'wb') as pdf_object:
                # Adds the content to the file
                pdf_object.write(PDFcontent)
                # Making the content for the CSV file
                addToCSV = id + "," + linkToHandle
                # Adding it in the success CSV file
                AddToCSV(addToCSV, csvFileForSuccessFullDownloads, noErrorMessage)
                # Returns a string teling you that the link succeeded
                return aValidLinkText
            
        elif PDFstatus == "200": 
            # HTTP files return a 200 status code, so to explain the error that occured
            PDFstatus = "This is not a valid PDF link"
            # When you raise an exception, you end in the except: on line 56
            raise Exception
        else:
            # When you raise an exception, you end in the except: on line 56
            raise Exception
    except:   
        # Making sure that the current link is not empty or invalid (I don't want to add them to the information files)
        notAnEmptyOrNullValue = linkToHandle != "" and linkToHandle != None and linkToHandle != "nan" 
        notAnEmptyOrNullValueBackUpLink = reserveLink != "" and reserveLink != None and reserveLink != "nan" 
        
        # This is a boolean I call with True for the second link 
        if isSecondLink:
            if notAnEmptyOrNullValue:
                # Adding the error to the error file
                responseForAddToErrorCSV = id + "," + linkToHandle + "," + PDFstatus
                AddToCSV(responseForAddToErrorCSV, csvFileForErrors, PDFstatus)
        else:
            if notAnEmptyOrNullValueBackUpLink:
                # Calling the function again with isSecondLink being true
                CheckAndDownloadPDF(reserveLink, linkToHandle, id, isTest, True)
            elif notAnEmptyOrNullValue:
                # Adding the error to the error file
                responseForAddToErrorCSV = id + "," + linkToHandle + "," + PDFstatus
                AddToCSV(responseForAddToErrorCSV, csvFileForErrors, PDFstatus)
                            
        # Returns a string teling you that the link is not valid
        return notAValidLinkText