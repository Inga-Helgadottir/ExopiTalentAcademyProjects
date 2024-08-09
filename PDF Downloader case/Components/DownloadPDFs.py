from multiprocessing.pool import ThreadPool as Pool
from Components.GetPDFfileData import GetPDFfileData
from Components.GlobalVariables import CSVFileDataUseCols
from Components.CheckAndDownloadPDF import CheckAndDownloadPDF

def DownloadPDFs(dataPath, isTest):
    # Notifying the user that the download has started
    print("Downloadig files...")        
    
    # Getting the dataframe for the chosen location
    df = GetPDFfileData(dataPath, CSVFileDataUseCols)
    # Renaming the columns, just to make it easier to look at
    df_new = df.rename(columns={"id": "id","pdf_url_1": "link", "pdf_url_2": "reservelink"})
    
    # Gets the ammount of rows and columns in the dataframe
    rows, columns = df_new.shape
    
    # Making an empty array to add the function parameters to 
    data_input = []
    # Looping through the dataframe
    for id, rowItem in df_new.iterrows():
        # Adding each line to the empty array data_input
        data_input.append((str(rowItem.link), str(rowItem.reservelink), str(rowItem.id), isTest, False))
    
    # if there are less than 300 rows
    if rows < 300:
        # We can run a new thread for each of them
        pool_size = rows 
    else:
        # Else we stick with 200
        pool_size = 200 
        
    # Looping through the Pool 
    with Pool(pool_size) as pool:
        # for each thread in the pool run this function with the data from data_input
        pool.starmap(CheckAndDownloadPDF, data_input)
    
    # Closes the pool
    pool.close()
    pool.join()
    pool.terminate()