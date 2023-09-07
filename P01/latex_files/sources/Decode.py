import numpy as np
from PIL import Image
end_str="$$\0"
def Decode():
    src = input("Enter source image path to be decoded:\n")

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, n):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0,len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-1*len(end_str):] == end_str:
            break
        
        message += chr(int(hidden_bits[i], 2))
    
    if end_str in message:
        
        print("Hidden Message:", message[:-1*len(end_str)])
        return
    else:
        print("No Hidden Message Found")
