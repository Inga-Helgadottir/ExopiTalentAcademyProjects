import pytest
import pandas
from Components.GetPDFfileData import GetPDFfileData
from Components.GlobalVariables import dataPath, CSVFileDataUseCols


def test_GetPDFfileData():
    validPDF = GetPDFfileData("."+dataPath, CSVFileDataUseCols)
    expectedValidOutput = pandas.read_csv("."+dataPath, usecols = CSVFileDataUseCols, skipinitialspace=True)
    assert(validPDF, expectedValidOutput)

    
