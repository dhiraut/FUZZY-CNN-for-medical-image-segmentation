# -*- coding: utf-8 -*-
"""metrices.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gcBK-WUEn5FZIes7uvmAhn71qjCmx08S
"""

import numpy as np

def calculate_iou(true_mask, predicted_mask):
    intersection = np.logical_and(true_mask, predicted_mask).sum()
    union = np.logical_or(true_mask, predicted_mask).sum()
    return intersection / union if union > 0 else 0

def calculate_dice(true_mask, predicted_mask):
    intersection = np.logical_and(true_mask, predicted_mask).sum()
    return (2 * intersection) / (true_mask.sum() + predicted_mask.sum())
