import os
from PIL import Image

src_folder = './images'
pdf_folder = './pdf'
filename = 'Deloitte_images'
file_List = []
# add max image pixels size if needed
# Image.MAX_IMAGE_PIXELS = 108000000

def convert_merge(file_List):
    converted_files = []  # New list to store converted files

    for i in file_List:
        img = Image.open(i)
        w, h = img.size

        if w > 1920:
            print('Image is too large: {}:{}, aspect ratio is {}'.format(w, h, w/h))
            ratio = w/h
            img = img.resize((1920, int(1920/ratio)))
            print('Image is resized to {}:{}'.format(img.size[0], img.size[1]))
        else:
            print('Image is good: {}:{}, aspect ratio is {}'.format(w, h, w/h))

        converted = img.convert('RGB')
        converted_files.append(converted)
    converted_files[0].save(os.path.join(pdf_folder, filename + '.pdf'), save_all=True,
                            append_images=converted_files[1:])


for file in os.listdir(src_folder):
    if file.endswith('.jpg') or file.endswith('jpeg') or file.endswith('png'):
        file_List.append(os.path.join(src_folder, file))

print(len(file_List))
print(file_List)
convert_merge(file_List)

