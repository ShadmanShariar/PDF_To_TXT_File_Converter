import PyPDF2
##pdf name
pdffileobj=open('1.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(1) ##1 is the page number
text=pageobj.extractText()
##saving path
file1=open(r"C:\Users\defaultuser0\pythonProject\\2.txt","a")
file1.writelines(text)
file1.close()
