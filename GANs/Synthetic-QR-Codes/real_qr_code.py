import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load and display a real QR code from the training dataset
def display_real_qr_code():
    real_image_path = 'qr_codes/generated/qr_code_0.png'  # You can change the filename to display another QR code
    real_image = load_img(real_image_path, target_size=(100, 100))
    
    # Convert the image to an array
    real_image_array = img_to_array(real_image) / 255.0  # Normalize to [0, 1] for display
    
    # Display the real QR code
    plt.imshow(real_image_array)
    plt.axis('off')  # Hide the axis
    plt.title('Real QR Code')
    plt.show()

display_real_qr_code()
