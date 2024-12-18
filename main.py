# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gcBK-WUEn5FZIes7uvmAhn71qjCmx08S
"""

import matplotlib.pyplot as plt
import numpy as np
from preprocessing import preprocess_image
from cnn_model import SimpleCNN
from segmentation import fuzzy_cnn_segmentation, traditional_cnn_segmentation
from metrics import calculate_iou, calculate_dice

if __name__ == "__main__":
    # Load and preprocess the image
    input_image = plt.imread('/path/to/your/image.jpg')[:, :, 0]
    preprocessed_image = preprocess_image(input_image)

    # Simulated ground truth
    true_mask = np.random.randint(0, 2, size=preprocessed_image.shape)

    # Initialize CNN
    cnn_model = SimpleCNN(input_shape=preprocessed_image.shape, num_filters=3, kernel_size=3)

    # Perform segmentation
    traditional_segmented = traditional_cnn_segmentation(preprocessed_image, cnn_model)
    fuzzy_segmented = fuzzy_cnn_segmentation(preprocessed_image, cnn_model)

    # Evaluate
    iou_traditional = calculate_iou(true_mask, traditional_segmented)
    dice_traditional = calculate_dice(true_mask, traditional_segmented)

    iou_fuzzy = calculate_iou(true_mask, fuzzy_segmented)
    dice_fuzzy = calculate_dice(true_mask, fuzzy_segmented)

    # Visualize results
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(preprocessed_image, cmap='gray')
    plt.title("Input Image")

    plt.subplot(1, 3, 2)
    plt.imshow(traditional_segmented, cmap='jet')
    plt.title(f"Traditional CNN (IoU: {iou_traditional:.2f}, Dice: {dice_traditional:.2f})")

    plt.subplot(1, 3, 3)
    plt.imshow(fuzzy_segmented, cmap='jet')
    plt.title(f"Fuzzy-CNN (IoU: {iou_fuzzy:.2f}, Dice: {dice_fuzzy:.2f})")

    plt.tight_layout()
    plt.show()

