from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

def pdf2txt(inPDFfile, outTXTFile):
    inFile = open(inPDFfile, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interprete = PDFPageInterpreter(resMgr, TxtConverter)
    for page in PDFPage.get_pages(inFile):
        interprete.process_page(page)

    txt = retData.getvalue()
    
    #salvar os dados de saída em um arquivo de texto
    with open(outTXTFile, 'w') as f:
        f.write(txt)
