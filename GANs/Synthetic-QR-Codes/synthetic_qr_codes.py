# Import necessary libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import qrcode

# TensorFlow and Keras imports
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Reshape, LeakyReLU, BatchNormalization, Conv2DTranspose
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Import necessary layers and optimizers
from tensorflow.keras.layers import Conv2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam

# Create directory to store training QR codes
os.makedirs('qr_codes/train', exist_ok=True)

# Create directory to store validation QR codes
os.makedirs('qr_codes/val', exist_ok=True)

# Define a function to generate QR codes with embedded messages and save them as image files.
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Generate a set of 80 training QR codes
for i in range(80):
    generate_qr_code(f"Message {i}", f"qr_codes/train/qr_code_{i}.png")

# Generate a set of 20 validation QR codes
for i in range(20):
    generate_qr_code(f"Message {i + 80}", f"qr_codes/val/qr_code_{i}.png")

# Verify if the QR code images have successfully generated
# by counting the number of images in the training and validation directories.
train_images = os.listdir('qr_codes/train')
val_images = os.listdir('qr_codes/val')

# Print the number of generated training and validation images
print(f"Training images generated: {len(train_images)}")
print(f"Validation images generated: {len(val_images)}")

# Define a function to load images from a directory, resize them, and normalize pixel values for better GAN performance.
def load_images(image_dir, target_size=(100, 100)):
    images = []
    filenames = os.listdir(image_dir)
    for filename in filenames:
        img = load_img(os.path.join(image_dir, filename), target_size=target_size)
        img_array = img_to_array(img)
        images.append(img_array)
    return np.array(images)

# Load the training and validation images
train_images = load_images('qr_codes/train')
val_images = load_images('qr_codes/val')

# Normalize the images to the range [-1, 1]
train_images = (train_images - 127.5) / 127.5
val_images = (val_images - 127.5) / 127.5

# Print the shape of the training and validation images
print(f"Training images shape: {train_images.shape}")
print(f"Validation images shape: {val_images.shape}")

# Define and construct the generator model for the GAN.
# The model takes random noise as input and generates QR code images.
def build_generator():
    model = Sequential()
    
    # Initial dense layer to project the input noise into a higher-dimensional space
    model.add(Dense(256 * 25 * 25, input_dim=100))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Reshape((25, 25, 256)))  # Reshape to a 3D tensor
    
    # First upsampling layer: Upsample to 50x50
    model.add(Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization())

    # Second upsampling layer: Upsample to 100x100
    model.add(Conv2DTranspose(64, (4, 4), strides=(2, 2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization())

    # Output layer: Generates a 100x100 image with 3 color channels
    model.add(Conv2DTranspose(3, (4, 4), activation='tanh', padding='same'))
    
    return model

# Build the generator model and display the model's architecture
generator = build_generator()
generator.summary()

# Define and construct the discriminator model for the GAN.
# The model classifies images as real or fake QR codes.
def build_discriminator():
    model = Sequential()
    
    # First convolutional layer: 64 filters, 3x3 kernel, same padding
    model.add(Conv2D(64, (3, 3), padding='same', input_shape=(100, 100, 3)))
    model.add(LeakyReLU(alpha=0.2))  # Leaky ReLU activation
    model.add(Dropout(0.4))  # Dropout for regularization
    
    # Second convolutional layer: 128 filters, 3x3 kernel, downsampled by 2
    model.add(Conv2D(128, (3, 3), strides=(2, 2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dropout(0.4))

    # Third convolutional layer: 256 filters, 3x3 kernel, downsampled by 2
    model.add(Conv2D(256, (3, 3), strides=(2, 2), padding='same'))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dropout(0.4))
    
    # Flatten the output for the final dense layer
    model.add(Flatten())
    
    # Output layer: Single neuron for binary classification with sigmoid activation
    model.add(Dense(1, activation='sigmoid'))
    
    return model

# Build, compile the discriminator model with binary crossentropy loss and Adam optimizer, and display its architecture
discriminator = build_discriminator()
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
discriminator.summary()

# Combine the generator and discriminator into a single model,
# allowing the generator to be trained through the discriminator's feedback.
def build_gan(generator, discriminator):
    discriminator.trainable = False  # Freeze the discriminator during GAN training
    
    # Define the input and output for the GAN model
    gan_input = generator.input
    gan_output = discriminator(generator.output)
    
    # Create the GAN model
    gan = Model(gan_input, gan_output)
    
    # Compile the GAN model with binary crossentropy loss and Adam optimizer
    gan.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))
    
    return gan

# Build the GAN model and display its architecture
gan = build_gan(generator, discriminator)
gan.summary()

# Train the GAN
'''
You can experiment with different epoch values to find the optimal training duration. Be aware that running a large number of epochs may lead to kernel issues due to high resource usage.

Note: Please be patient, as the execution may take some time.
'''

# Directory for saving model checkpoints
checkpoint_dir = 'gan_checkpoints'
os.makedirs(checkpoint_dir, exist_ok=True)

# Define a training function for the GAN, which alternates between
# training the discriminator on real and fake images and training the generator.
def train_gan(generator, discriminator, gan, epochs, batch_size, checkpoint_interval=100):
    for epoch in range(epochs):
        # Train the discriminator
        idx = np.random.randint(0, train_images.shape[0], batch_size)  # Randomly select real images
        real_images = train_images[idx]

        noise = np.random.normal(0, 1, (batch_size, 100))  # Generate random noise
        fake_images = generator.predict(noise)  # Generate fake images from noise

        # Train the discriminator on real and fake images
        d_loss_real = discriminator.train_on_batch(real_images, np.ones((batch_size, 1)))  # Real images labeled as 1
        d_loss_fake = discriminator.train_on_batch(fake_images, np.zeros((batch_size, 1)))  # Fake images labeled as 0
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)  # Average loss

        # Train the generator
        noise = np.random.normal(0, 1, (batch_size, 100))  # Generate new noise
        g_loss = gan.train_on_batch(noise, np.ones((batch_size, 1)))  # Label as 1 to fool the discriminator

        # Print the progress every 100 epochs
        if epoch % 100 == 0:
            print(f"{epoch} [D loss: {d_loss[0]} | D acc: {d_loss[1]}] [G loss: {g_loss}]")
        
        # Save the model every checkpoint_interval epochs
        if epoch % checkpoint_interval == 0:
            generator.save(os.path.join(checkpoint_dir, f"generator_epoch_{epoch}.h5"))
            discriminator.save(os.path.join(checkpoint_dir, f"discriminator_epoch_{epoch}.h5"))

# Start training the GAN with 5000 epochs and a batch size of 32
train_gan(generator, discriminator, gan, epochs=5000, batch_size=32)

# Function to generate and save QR codes from the trained generator
def generate_and_save_qr_codes(generator, n_samples):
    # Generate noise as input for the generator
    noise = np.random.normal(0, 1, (n_samples, 100))
    
    # Use the generator to create fake images (QR codes)
    generated_images = generator.predict(noise)
    
    # Rescale images from [-1, 1] to [0, 1] for proper display and saving
    generated_images = 0.5 * generated_images + 0.5
    
    # Ensure the output directory exists
    os.makedirs('qr_codes/generated', exist_ok=True)
    
    # Save each generated QR code as an image
    for i in range(n_samples):
        plt.imshow(generated_images[i])
        plt.axis('off')  # Turn off the axis for a cleaner look
        plt.savefig(f"qr_codes/generated/qr_code_{i}.png")
        plt.close()  # Close the figure to prevent memory overflow

# Generate 10 QR codes using the trained generator
generate_and_save_qr_codes(generator, 10)

'''
Note: The list of QR codes will be available in the internal environment. You can see the image below the path for the QR codes. Inside the 'qr_codes' folder, there are two additional folders: one for 'train' QR codes and another for 'generated' QR codes. The code above uses 'train' data to generate 10 QR codes, so you can use the code below to display both the trained and generated QR codes here.


    Path for the Trained QR code: qr_codes/train/qr_code_1.png
    Path for the Generated QR code: qr_codes/generated/qr_code_1.png

You can change the last number from 1 to 9 in the path, such as qr_codes/generated/qr_code_9.png, to display the corresponding QR code.
'''


