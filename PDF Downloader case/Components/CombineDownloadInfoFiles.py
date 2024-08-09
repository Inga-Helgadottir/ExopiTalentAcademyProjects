from Components.SortDataByID import SortDataByID
from Components.GetPDFfileData import GetPDFfileData
from Components.GlobalVariables import aListOfTheAlreadyDownloadedPDFs, successCSVFileUseCols, errorInPDF, errorCSVFileUseCols, allDownloadInfo, bothCSVFileUseCols

def CombineDownloadInfoFiles():
    # Getting data from the information files
    successDF = GetPDFfileData(aListOfTheAlreadyDownloadedPDFs, successCSVFileUseCols)
    errorDF = GetPDFfileData(errorInPDF, errorCSVFileUseCols)
    
    # Renameing columns so it fits with the new file
    errorDFRenamed = errorDF.rename(columns={"id": "id","link": "link", "errorcode": "status"})
    # Adding a column so it fits with the new file
    successDF.insert(2, "status", "The download was successful", True)
    
    # Open the new file
    with open(allDownloadInfo, "a", encoding="utf-8", newline='') as f:
        # Looping through both files and adding to the new file
        for id, rowItem in successDF.iterrows():
            f.write(str(rowItem.id)+","+str(rowItem.link)+","+str(rowItem.status)+"\n")
            
        for id, rowItem in errorDFRenamed.iterrows():
            f.write(str(rowItem.id)+","+str(rowItem.link)+","+str(rowItem.status)+"\n")
            
            
    SortDataByID(allDownloadInfo, bothCSVFileUseCols)