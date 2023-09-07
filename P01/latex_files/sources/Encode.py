import numpy as np
from PIL import Image
end_str="$$\0"
def Encode():
    src, dest = input("Enter Source_path, destination_path in order seprted by space:\n").split()
    message=input("Enter Message:\n")
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    message += end_str
    b_message=""
    for ch in message:
        b_message+=format(ord(ch), "08b")

    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("File size is not enough!")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, n):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
                else:
                    break
                
            if index >= req_pixels:
                break

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Message Successfully Encoded")