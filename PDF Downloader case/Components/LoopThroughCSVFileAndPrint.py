from Components.GetPDFfileData import GetPDFfileData

def LoopThroughCSVFileAndPrint(CSVFileToLoopThrough, useCols):
    # Gets the CSV file in a dataframe
    df = GetPDFfileData(CSVFileToLoopThrough, useCols)     
    
    # Opens the file
    with open(CSVFileToLoopThrough, "r", encoding="utf-8", newline='') as f:
        # Loops through the dataframe
        for id, rowItem in df.iterrows():
            # Display the row to the user
            print(rowItem)
    