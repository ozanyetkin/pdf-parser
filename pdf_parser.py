import os
import fitz
import textract
import re
import pandas as pd
from glob import glob

files = []
start_dir = "/mnt/c/Users/Yetkin/Downloads/ARCH 282 All Sections-Mid Term Assignment-70029"
pattern   = "*.pdf"
df = pd.DataFrame(columns=["name", "page_count", "image_count", "word_count", "cities"])
cities_list = pd.read_csv("world-cities.csv")["name"].to_list()

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern)))

for i, file in enumerate(files):
    print(i)
    pdf_file = fitz.open(file)
    student_name = file.split("/")[-2].split("_")[0]
    page_count = len(pdf_file)
    
    image_count = 0
    for page_index in range(len(pdf_file)):
        image_list = pdf_file[page_index].get_images()
        
        if image_list:
            image_count += len(image_list)

    text = textract.process(file).decode('utf-8')
    words = re.findall(r"[^\W_]+", text, re.MULTILINE)
    word_count = len(words)
    found_cities = set()
    for word in words:
        for city in cities_list:
            if word.strip().lower() == city.lower():
                found_cities.add(word)

    df.loc[i] = [student_name, page_count, image_count, word_count, str(found_cities).replace("{", "").replace("}", "")]

    pdf_file.close()

print(df)
df.to_excel("output.xlsx")
