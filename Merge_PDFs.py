import os
import PyPDF2

src_folder = './images'
pdf_folder = './pdf'
filename = 'Memes'
file_List = []


def convert_merge(file_List):
    pdfMerge = PyPDF2.PdfMerger()
    for file in file_List:
        pdfFile = open(file, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfMerge.append(pdfReader)
        pdfFile.close()
    pdfMerge.write(os.path.join(pdf_folder, filename + '.pdf'))


for file in os.listdir(src_folder):
    if file.endswith('.pdf'):
        file_List.append(os.path.join(src_folder, file))

convert_merge(file_List)

