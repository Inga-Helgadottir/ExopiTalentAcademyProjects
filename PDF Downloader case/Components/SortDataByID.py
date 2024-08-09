from Components.GetPDFfileData import GetPDFfileData 

def SortDataByID(dataPath, useCols):
    # Getting a dataframe of the CSV file dataPath given
    PDFFileData = GetPDFfileData(dataPath, useCols)
    # Drops the duplicates
    PDFFileData.drop_duplicates(inplace=True)
    # Sorts the file by the id and turns it back to CSV
    PDFFileData.sort_values(by=['id'], ascending=True).to_csv(dataPath, index=False)

        