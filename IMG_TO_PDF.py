import os
from PIL import Image
import PyPDF2

src_folder = './images'
pdf_folder = './pdf'
filename = 'MCA Introduction to Computer & Programming Concepts'
file_List = []


def convert_merge(fileType, file_List):
    converted_files = []  # New list to store converted files

    if fileType == "Image":
        for i in file_List:
            img = Image.open(i)
            converted = img.convert('RGB')
            converted_files.append(converted)
        converted_files[0].save(os.path.join(pdf_folder, filename + '.pdf'), save_all=True,
                                append_images=converted_files[1:])
    elif fileType == "PDF":
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
        fileType = 'PDF'
    elif file.endswith('.jpg') or file.endswith('jpeg') or file.endswith('png'):
        file_List.append(os.path.join(src_folder, file))
        fileType = 'Image'

# print(file_List)
convert_merge(fileType, file_List)

