import cv2
import numpy as np
import matplotlib.pyplot as plt

 def display_image(title, image):
     plt.figure(figsize=(8, 8))
     if len(image.shape) == 2:  # Grayscale image
         plt.imshow(image, cmap='gray')
     else:  # Color image
         plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
     plt.title(title)
     plt.axis('off')
     plt.show()

     def interactive_edge_protection(image_path):
        image = cv2.imread(image_path)
        if image is None:
            print(f"Image not found ")
            return
        
    