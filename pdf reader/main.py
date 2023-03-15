import PyPDF2
pdf_path = r"C:\Users\user\OneDrive\Desktop\hp warranty certificate.pdf"
pdfFileObj = open(pdf_path, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pageObj = pdfReader.pages[0]
print(pageObj.extract_text())
pdfFileObj.close()