import os
from PIL import Image
import PyPDF2
from pathlib import Path

src_folder = './images'
pdf_folder = './pdf'
filename = 'Memes'
file_List = []
file_type_list = []
names = []
def image_to_pdf(file, name):
    # converted_files = []  # New list to store converted files
    print(file)
    img = Image.open(file)
    converted = img.convert('RGB')
    # converted_files.append(converted)
    converted.save(os.path.join(pdf_folder, name + '.pdf'))


def convert_merge(file_type_list, file_List):
    if file_type_list == "PDF":
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
        names.append(Path(file).stem)
        file_type_list.append('PDF')
    elif file.endswith('.jpg') or file.endswith('jpeg') or file.endswith('png'):
        file_List.append(os.path.join(src_folder, file))
        names.append(Path(file).stem)
        file_type_list.append('Image')
    elif file.endswith('.docx'):
        file_List.append(os.path.join(src_folder, file))
        names.append(Path(file).stem)
        file_type_list.append('Word')

print(file_type_list, file_List)
print(names)

for i in range(len(file_List)):
    if file_type_list[i] == 'Image':
        image_to_pdf(file_List[i], names[i])
    else:
        pass


