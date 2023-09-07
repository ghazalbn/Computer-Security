import numpy as np
from PIL import Image

logo_addr=input("Enter watermark path: ")
base_path=input("Enter base image path: ")
out_path=input("Enter output image path: ")

logo = Image.open(logo_addr, 'r').resize((50,50))
l_width, l_height = logo.size
base_img=Image.open(base_path, 'r')
b_width, b_height = base_img.size
out_img=base_img.copy()
out_img.paste(logo,(5,5))
out_img.save(out_path)
print("Watermark added successfully")

