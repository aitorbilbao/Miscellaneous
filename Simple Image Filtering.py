import pygame
import numpy as np


def apply_filter(image,filter):
    height,width,channels = image.shape # Gets dimension of the input image
    filter_size = filter.shape[0] # The filter size is determined by the 1st dimension of filter array
    output = np.zeros((height,width,channels),dtype = np.uint8) # We create an output array with the same size as the input. The data type ensures that all values from 0-255 are represented.

    # The image is padded symmetrically to handle the edges. The mode ensures the padded values are constant and set to the edge values.
    padded_image = np.pad(image, ((filter_size // 2, filter_size // 2), (filter_size // 2, filter_size // 2), (0, 0)), mode='constant')
    
    # Apply convolution to each pixel in the image (We iterate over each pixel)
    for y in range(height):
        for x in range(width):
            region = padded_image[y:y+filter_size, x:x+filter_size, :] # We take a region of the padded image for each pixel, with the same size as the filter
            weighted_sum = np.sum(region * filter[..., np.newaxis], axis=(0, 1)) # the axis specifies that the summation should be performed over the last two dimensions (height,width)
                # We add a new axis to the filter array -> (h,w) => (h,w,1). This way we align the dimensions of the filter with the number of color channels in the region
                # We multiply the region and the filter (now that the elements are positioned correctly)
                # We sum the elements of this new array and obtain a single value that represents the convolution operation

            output[y, x] = np.clip(weighted_sum, 0, 255) # The weighted sum is clipped to ensure that the pixel value is inside 0-255. And we assign it to the output.

    return output

    #SAVE IMAGE IN FOLDER
def save_image(image, output_path):
    pygame.image.save(image, output_path)

def main():
    pygame.init()

    # Load the input image
    image = pygame.image.load("A6/beach_holiday.jpg")
    image_array = pygame.surfarray.array3d(image)
    
    # Define the filter matrix (choose one and comment the others)

    #Gaussian 5
    #filter_matrix = np.array([[0.00390625, 0.015625,   0.0234375,  0.015625,   0.00390625],
    #                        [0.015625,   0.0625,     0.09375,    0.0625,     0.015625],  
    #                        [0.0234375,  0.09375,    0.140625,   0.09375,    0.0234375], 
    #                        [0.015625,   0.0625,     0.09375,    0.0625,     0.015625],  
    #                        [0.00390625, 0.015625,   0.0234375,  0.015625,   0.00390625]])
    
    filter_matrix = np.array([[0.6, 0.3, 0.1],
                               [0.3, 0.7, 0.3],
                               [0.1, 0.3, 0.6]])


    #Gaussian 3
    #filter_matrix = np.array([[1/16, 1/8, 1/16],
    #                      [1/8,  1/4, 1/8],
    #                      [1/16, 1/8, 1/16]])


    #Sharpen
    # filter_matrix = np.array([[0, -1, 0],
    #                      [-1,  5, -1],
    #                      [0, -1, 0]])

    #Edge detect
    #filter_matrix = np.array([[1, 0, -1],
    #                      [0,  0, 0],
    #                      [-1, 0, 1]])

    #Unsharp
    #filter_matrix = np.array([[-0.00390625, -0.015625,  -0.0234375, -0.015625, -0.00390625],
    #                        [-0.015625,   -0.0625,    -0.09375,   -0.0625,   -0.015625],
    #                        [-0.0234375,  -0.09375,    1.859375,  -0.09375,  -0.0234375],
    #                        [-0.015625,   -0.0625,    -0.09375,   -0.0625,   -0.015625],
    #                        [-0.00390625, -0.015625,  -0.0234375, -0.015625, -0.00390625]])

    

    # Apply the filter
    filtered_array = apply_filter(image_array, filter_matrix)
    
    # Create a new surface from the filtered array
    filtered_surface = pygame.surfarray.make_surface(filtered_array)
    
    # Save the filtered image
    output_image_path = 'A6/filtered_image.png'
    save_image(filtered_surface, output_image_path)
    
    # Show the filtered image
    pygame.display.set_caption("Filtered Image")
    screen = pygame.display.set_mode((image.get_width(), image.get_height()*2))
    screen.blit(image,(0,0)) #Add image
    screen.blit(filtered_surface, (0, image.get_height())) #Add filtered image

    pygame.display.flip() # Update changes (blitting of image)
    



    # Wait for the user to close the window
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

#MAIN CODE
main()

