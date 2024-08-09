from Components.CheckAndDownloadPDF import CheckAndDownloadPDF
from Components.GlobalVariables import aValidLinkText, notAValidLinkText

def test_CheckAndDownloadPDF():
    # linkToHandle, reserveLink, id, isTest, isSecondLink
    actualValidLink = CheckAndDownloadPDF("https://s21.q4cdn.com/374334112/files/doc_downloads/sd_reports/11239_AEM_2016-SDR_Typeset-Complete_v5b.pdf", "", "78", True, True)
    actualInValidLink = CheckAndDownloadPDF("https://www.abs.ch/?id=574", "", "10", True, True)
    
    expectedValidLink = aValidLinkText
    expectedInValidLink = notAValidLinkText
    
    assert(actualInValidLink, expectedInValidLink)
    assert(actualValidLink, expectedValidLink)