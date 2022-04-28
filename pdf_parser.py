import os
import fitz
from glob import glob

files = []
start_dir = "/mnt/c/Users/Yetkin/Downloads/ARCH 282 All Sections-Mid Term Assignment-70029"
pattern   = "*.pdf"

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern))) 

for file in files:
    pdf_file = fitz.open(file)
    student_name = file.split("/")[-2].split("_")[0]
    page_count = len(pdf_file)
    image_count = 0

    for page_index in range(len(pdf_file)):
        image_list = pdf_file[page_index].get_images()
        
        if image_list:
            image_count += len(image_list)

    print(student_name, f"page count: {page_count}",f"image count: {image_count}")
    pdf_file.close()
