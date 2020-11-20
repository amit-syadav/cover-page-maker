from fpdf import FPDF

def drawline():
    pdf.line(5.0,5.0,205.0,5.0) # top one
    pdf.line(5.0,292.0,205.0,292.0) # bottom one
    pdf.line(5.0,5.0,5.0,292.0) # left one
    pdf.line(205.0,5.0,205.0,292.0) # right one

def createPage(name, rollNo, expNo):
    pdf.add_page()
    drawline()
    pdf.set_font('Arial',"B", 60)
    pdf.cell(0, 50, f'MCC EXP-{expNo}', border=0, ln=8, align="C")

    pdf.set_font("Arial", style = '', size = 30)
    pdf.cell(0, 20, f'Name : {name}', border=0, ln=8, align="L")
    pdf.cell(0, 20, 'Class : BE Computer', border=0, ln=2, align="L")
    pdf.cell(0, 20, f'Roll NO : {rollNo}', border=0, ln=2, align="L")
    pdf.cell(0, 20, 'Subject : MCC', border=0, ln=2, align="L")

name = input("Enter Name")
rollNo = input("Enter roll NO")
name = name.title()

pdf = FPDF()

for i in range(1, 12):
    createPage(name, rollNo,i)


# pdf.cell(40, 10, 'Hello World!')

pdf.output('temp page title.pdf', 'F')






import PyPDF2 
import os


# Open the files that have to be merged one by one
mainFile = open(os.path.join(os.getcwd(),"mcc.pdf"), 'rb')
myNameFile = open(os.path.join(os.getcwd(),"temp page title.pdf"), 'rb')
 
# Read the files that you have opened
mainReader = PyPDF2.PdfFileReader(mainFile)
nameReader = PyPDF2.PdfFileReader(myNameFile)
 
# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()
 

pages  = set([3,6,8,13,17,20,22,27,30,33])
namePageNumber = 1
# Loop through all the pagenumbers for the first document
for pageNum in range(mainReader.numPages):
    if pageNum+1 in pages:
        print(namePageNumber)
        pageObj = nameReader.getPage(namePageNumber-1)
        pdfWriter.addPage(pageObj)
        namePageNumber += 1
    pageObj =  mainReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
 

 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open(f'{name}_RollNo{rollNo}.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

# Close all the files - Created as well as opened
pdfOutputFile.close()
mainFile.close()
myNameFile.close()