
import tensorflow as tf
import numpy as np
import cv2
from image_processing import normalize

"""
def load_cifar():
    # Load the CIFAR-10 dataset
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

    # Convert the images to LAB color space
    train_lab = [cv2.cvtColor(image, cv2.COLOR_RGB2LAB) for image in train_images]
    test_lab = [cv2.cvtColor(image, cv2.COLOR_RGB2LAB) for image in test_images]

    # Convert the lists back to NumPy arrays
    train_lab = np.array(train_lab)
    test_lab = np.array(test_lab)

    # Normalize the LAB color space values
    train_lab = normalize(train_lab)
    test_lab = normalize(test_lab)

    # Extract the grayscale channel (L channel) and expand its dimensions
    train_gray = [np.expand_dims(img[:, :, 0], axis=-1) for img in train_lab]
    test_gray = [np.expand_dims(img[:, :, 0], axis=-1) for img in test_lab]

    # Create TensorFlow datasets from the grayscale and LAB images
    train_ds = tf.data.Dataset.from_tensor_slices((train_gray, train_lab))
    test_ds = tf.data.Dataset.from_tensor_slices((test_gray, test_lab))

    return train_ds, test_ds
"""


DIMENSION = 1024
def resizeWithPadding(image, target_size=(DIMENSION, DIMENSION)):
    h, w, _ = image.shape
    scale = min(target_size[0] / h, target_size[1] / w)

    resized = cv2.resize(image, (int(w * scale), int(h * scale)))

    delta_w = target_size[1] - resized.shape[1]
    delta_h = target_size[0] - resized.shape[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    color = [255, 255, 255]  # White padding
    return cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)


def load_images():
    fileName = "chapter1-page1.jpg"
    img = cv2.imread(f"color/Bleach-Color/{fileName}")

    #cv2.imshow("Original Image", img)
    #cv2.waitKey(0)

    img = resizeWithPadding(img)
    cv2.imshow("Square Image with Padding", img)

    cv2.imwrite(f"res_testing/chapter1-page1-size{DIMENSION}.jpg", img) 

load_images()