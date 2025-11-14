from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    img = Image.open(path)
    
    img = img.convert('RGB')
    
    width, height = img.size
    pixels = list(img.getdata())
    
    array_3d = np.array(img)
    
    print("The shape of image is:", (height, width, 3))
    
    print(array_3d[:10])
    
    return array_3d

ft_load("/home/anaouali/Firefox_wallpaper.png")