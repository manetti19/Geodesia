import cv2
import matplotlib.pyplot as plt
import numpy as np

img_PID_2025R = cv2.imread('./Captura de tela 2025-03-12 114819.png')

plt.imshow(img_PID_2025R, cmap='gray', vmin=0, vmax=255)
plt.show()