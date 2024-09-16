import pygame
import os

# Initialize Pygame
pygame.init()

def resize_image(image_path, new_size, save_as):
    # Load the image
    image = pygame.image.load(image_path)
    
    # Resize the image
    resized_image = pygame.transform.scale(image, new_size)
    
    # Save the resized image
    pygame.image.save(resized_image, save_as)

def main():
    # Define image paths and sizes
    images = {
        'spaceship.png': (64, 64),   # Example size for spaceship
        'spacemissiles.png': (16, 64)  # Example size for missile
    }
    
    # Resize and save images
    for image_name, size in images.items():
        input_path = os.path.join('images', image_name)
        output_path = os.path.join('images', 'resized_' + image_name)
        resize_image(input_path, size, output_path)
        print(f"Resized image saved as {output_path}")

if __name__ == '__main__':
    main()
    pygame.quit()
