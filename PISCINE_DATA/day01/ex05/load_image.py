from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

def ft_invert(array):
    inverted_img = 255 - array
    plt.imshow(inverted_img)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("inverted")
    plt.show()
    return inverted_img


def ft_blue(array):
    blue_img = array.copy()
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    
    plt.imshow(blue_img)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("Landscape")
    plt.show()
    return blue_img

def ft_green(array):
    green_img = array.copy()
    green_img[:, :, 0] = 0
    green_img[:, :, 2] = 0
    
    plt.imshow(green_img)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("Landscape")
    plt.show()
    return green_img

def ft_red(array):
    blue_img = array.copy()
    blue_img[:, :, 1] = 0
    blue_img[:, :, 2] = 0
    
    plt.imshow(blue_img)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("Landscape")
    plt.show()
    return blue_img

def ft_grey(array):
    img_gray = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)

    plt.imshow(img_gray, cmap='gray')
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("Landscape")
    plt.show()
    return img_gray

def load_image(path: str):

    img_color = cv2.imread(path)
    img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)
    if img_color is None:
        raise ValueError("Image introuvable")

    plt.imshow(img_color)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("Landscape")
    plt.show()

    print("The shape of image is:", img_color.shape)
    print(img_color)

    grey_image = ft_grey(img_color)
    blue_image = ft_red(img_color)
    green_image = ft_green(img_color)
    blue_image = ft_blue(img_color)
    inverted_image = ft_invert(img_color)

load_image("landscape.jpg")