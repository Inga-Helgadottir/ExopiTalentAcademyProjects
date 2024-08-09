import os 

def GenerateFolderIfMissing(whichFolder):
    # Create folder if it doesn't exist 
    if not os.path.exists(whichFolder):os.mkdir(whichFolder)