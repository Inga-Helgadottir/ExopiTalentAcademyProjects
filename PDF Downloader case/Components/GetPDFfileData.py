import pandas

def GetPDFfileData(dataLocation, useCols):   
    # Reading the CSV file from the dataLocation link 
    df = pandas.read_csv(dataLocation, usecols = useCols, skipinitialspace=True)
    return df