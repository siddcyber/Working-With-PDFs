import os
from PIL import Image
import PyPDF2

src_folder = './images'
pdf_folder = './pdf'
filename = 'MCA Introduction to Computer & Programming Concepts'
file_List = []
file_type_list = []

def convert_merge(file_type_list, file_List):
    converted_files = []  # New list to store converted files

    if file_type_list == "Image":
        for i in file_List:
            img = Image.open(i)
            converted = img.convert('RGB')
            converted_files.append(converted)
        converted_files[0].save(os.path.join(pdf_folder, filename + '.pdf'), save_all=True,
                                append_images=converted_files[1:])

    elif file_type_list == "PDF":
        pdfMerge = PyPDF2.PdfMerger()
        for i in file_List:
            pdfFile = open(i, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFile)
            pdfMerge.append(pdfReader)
            pdfFile.close()
        pdfMerge.write(os.path.join(pdf_folder, filename + '.pdf'))

    elif file_type_list == "Word":
        pass

# List of files to convert and list of type of file
for file in os.listdir(src_folder):
    if file.endswith('.pdf'):
        file_List.append(os.path.join(src_folder, file))
        file_type_list.append('PDF')
    elif file.endswith('.jpg') or file.endswith('jpeg') or file.endswith('png'):
        file_List.append(os.path.join(src_folder, file))
        file_type_list.append('Image')
    elif file.endswith('.docx'):
        file_List.append(os.path.join(src_folder, file))
        file_type_list.append('Word')

print(file_type_list, file_List)
# convert_merge(file_type_list, file_List)

