from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np


def zoom(img, x1, y1, x2, y2):
    sliced = img[y1:y2, x1:x2]

    plt.imshow(sliced, cmap='gray')
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title(f"Zone découpée ({x1},{y1}) → ({x2},{y2})")
    plt.show()

    new_sliced = sliced[:, :, np.newaxis] 
    print("New shape after slicing:", new_sliced.shape, "or", sliced.shape)
    print(new_sliced)


def load_image(path: str):

    img_color = cv2.imread(path)
    if img_color is None:
        raise ValueError("Image introuvable")

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

    plt.imshow(img_color)
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.title("Image avec axes")
    plt.show()

    print("The shape of image is:", img_color.shape)
    print(img_color)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    sliced_img = zoom(img_gray, x1=50, y1=50, x2=450, y2=450)


load_image("animal.jpeg")