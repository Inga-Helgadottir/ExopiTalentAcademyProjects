from Components.GetPDFfileData import GetPDFfileData
from Components.GlobalVariables import noErrorMessage, successCSVFileUseCols, errorCSVFileUseCols, bothCSVFileUseCols, thisIsTheAllDownloadsMessage

def AddToCSV(itemToAdd, addLocation, errorMsg):    
    try:
        # The errormessge tells me which file I need to get
        if errorMsg == noErrorMessage:
            df = GetPDFfileData(addLocation, successCSVFileUseCols)        
        elif errorMsg == thisIsTheAllDownloadsMessage:
            df = GetPDFfileData(addLocation, bothCSVFileUseCols)        
        else:
            df = GetPDFfileData(addLocation, errorCSVFileUseCols)            
        count = 0
    except: 
        # If it makes it here, the file is empty
        count = 9
    
    # Opens the chosen CSV file
    with open(addLocation, "a", encoding="utf-8", newline='') as f:
        # If the count is 9, the dataframe is not valid
        if count != 9:
            count = 0
            # Loop through the chosen dataframe
            for id, rowItem in df.iterrows():
                # Checks what the file is expecting and makes a variable 
                if errorMsg == noErrorMessage:
                    rowItemChanged = str(rowItem.id) + "," + str(rowItem.link)
                elif errorMsg == thisIsTheAllDownloadsMessage:
                    itemToAdd = str(itemToAdd)
                    rowItemChanged = str(rowItem.id) + "," + str(rowItem.link) + "," + str(errorMsg)
                else:
                    rowItemChanged = str(rowItem.id) + "," + str(rowItem.link) + "," + str(errorMsg)
                
                # If rowItemChanged and itemToAdd are the same, then this item is already in the file
                if rowItemChanged == itemToAdd:
                    count = 1
                    
        # If the item you want to add is not already in the file            
        if count != 1:
            # Add the item and return it
            f.write(itemToAdd+"\n")
            
            return itemToAdd
        