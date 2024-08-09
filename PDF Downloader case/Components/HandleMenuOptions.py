import time
from Components.CheckIfExit import CheckIfExit
from Components.DownloadPDFs import DownloadPDFs
from Components.ResetCSVFile import ResetCSVFile
from Components.SortDataByID import SortDataByID
from Components.CombineDownloadInfoFiles import CombineDownloadInfoFiles
from Components.LoopThroughCSVFileAndPrint import LoopThroughCSVFileAndPrint
from Components.GenerateFolderIfMissing import GenerateFolderIfMissing
from Components.GlobalVariables import englishMessageOptions, dataPath, startMessage, danishMessageOptions, defaultLanguage, wrongInputEnglish, wrongInputDanish, noErrorMessage, aListOfTheAlreadyDownloadedPDFs, errorInPDF, textToAddToEmptyFile_error, textToAddToEmptyFile_success, errorCSVFileUseCols, successCSVFileUseCols, allDownloadInfo, bothCSVFileUseCols, thisIsTheAllDownloadsMessage, dropLocationForDownloadedPDFs, textToAddToEmptyFile_both 

def HandleMenuOptions(inputMessage):
    # Turns the input into a string
    input = str(inputMessage) 
    
    # If the input is capitalized
    if input.isupper():
        # Save it as is
        inputUppercase = input
    else: # Else capitalize it (so I don't have to check upper and lower case letters: e vs. E, english vs. ENGLISH)
        inputUppercase = input.upper()
        
        
    # Setting the language to the default, in case the user entered something invalid in the what language to use input
    whatLanguageIsInUse = defaultLanguage   
    # Creates a space between the menues and the responses   
    print("\n")
    
    # Prints the start message saying welcome and asking for a language for the menu
    if inputUppercase == "START": 
        print(startMessage)
        
    # Setting the language to English and printing the options menu in the chosen language
    elif inputUppercase == "E" or inputUppercase == "ENGLISH": 
        whatLanguageIsInUse = "English"
        for i in englishMessageOptions:
            print(i)         
            return whatLanguageIsInUse
        
    # Setting the language to Danish and printing the options menu in the chosen language
    elif inputUppercase == "D" or inputUppercase == "DANISH" or inputUppercase == "DANSK": 
        whatLanguageIsInUse = "Danish"
        for i in danishMessageOptions:
            print(i)      
            return whatLanguageIsInUse
        
    # "To start downloading PDFs, enter 1"
    elif input == "1":
        # Making sure the alreaydDownloaded folder is still there, if not make it
        GenerateFolderIfMissing(dropLocationForDownloadedPDFs)
        # Setting te start time of the "counter"
        start_time = time.time()
        # Checks and downloads the PDFs, then adds it to the relevant file
        DownloadPDFs(dataPath, False)
        # Using the start time to see how long the downloads took
        print("The downloads took ", time.time() - start_time, "seconds to run")
        # Sorting the data files by id
        SortDataByID(aListOfTheAlreadyDownloadedPDFs, successCSVFileUseCols)
        SortDataByID(errorInPDF, errorCSVFileUseCols)
        
    # "To see all the information form the downloads, enter 2"
    elif input == "2": 
        # Combining the two information files in one, allDownloadInfo = (aListOfTheAlreadyDownloadedPDFs, errorInPDF)
        CombineDownloadInfoFiles()
        # Looping through and print the contents of the newly created file
        LoopThroughCSVFileAndPrint(allDownloadInfo, bothCSVFileUseCols)
        
    # "To see all the successfully downloaded files, enter 3"
    elif input == "3": 
        # Sorting the data by id before showing it to the user
        SortDataByID(aListOfTheAlreadyDownloadedPDFs, successCSVFileUseCols)
        # Looping through and print the contents of the succesful downloads file
        LoopThroughCSVFileAndPrint(aListOfTheAlreadyDownloadedPDFs, successCSVFileUseCols)
        
    # "To see all the failed downloaded files, enter 4"
    elif input == "4": 
        # Sorting the data by id before showing it to the user
        SortDataByID(errorInPDF, errorCSVFileUseCols)
        # Looping through and print the contents of the unsuccesful downloads file
        LoopThroughCSVFileAndPrint(errorInPDF, errorCSVFileUseCols)
      
    # "To combine the downloaded information files in one file, enter 5"  
    elif input == "5": 
        # Combining the two information files in one, allDownloadInfo = (aListOfTheAlreadyDownloadedPDFs, errorInPDF)
        CombineDownloadInfoFiles()
        print("The files are now combined and can be found in this CSV file: /Data/informationAboutAllDownloadedPDFs.csv")
       
    # "To reset all information about the downloaded PDFs, enter 6" 
    elif input == "6": 
        # Resetting all three information files
        ResetCSVFile(aListOfTheAlreadyDownloadedPDFs, textToAddToEmptyFile_success, "")
        ResetCSVFile(errorInPDF, textToAddToEmptyFile_error, noErrorMessage)
        ResetCSVFile(allDownloadInfo, textToAddToEmptyFile_both, thisIsTheAllDownloadsMessage)
        
    # "To reset all information about the successful downloads, enter 7"
    elif input == "7": 
        # Resetting the successful information file
        ResetCSVFile(aListOfTheAlreadyDownloadedPDFs, textToAddToEmptyFile_success, "")
        
    # "To reset all information about the failed downloads, enter 8" 
    elif input == "8": 
        # Resetting the unsuccessful information file
        ResetCSVFile(errorInPDF, textToAddToEmptyFile_error, noErrorMessage)
        
    # "To reset all information in the combined downloads file, enter 9" 
    elif input == "9": 
        # Resetting the combined information file
        ResetCSVFile(allDownloadInfo, textToAddToEmptyFile_both, thisIsTheAllDownloadsMessage)
        
    # The input given is either wrong or an exit 
    else:     
        # CheckIfExit, exits the program if the input is an exit string
        CheckIfExit(input)           
        returnMessage = ""        
        
        # Checking what language is in use and printing a response telling the user that the input is wrong
        if whatLanguageIsInUse == "Danish":
            returnMessage = str(input) + wrongInputDanish + "\n"
            print(returnMessage)
        else:
            returnMessage = str(input) + wrongInputEnglish + "\n"
            print(returnMessage)
        
        return returnMessage
        
    return input
    
  
    

      