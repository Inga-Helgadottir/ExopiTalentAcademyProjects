from Components.AddToCSV import AddToCSV

def ResetCSVFile(fileToReset, textToAddAfterReset, errorMsg):
    # Emptying the file
    f = open(fileToReset, "w+")
    f.close()
    
    # adding the column names to the file
    AddToCSV(textToAddAfterReset, fileToReset, errorMsg)
    # Alerting the user that it is now empty
    print(fileToReset + " is now empty")