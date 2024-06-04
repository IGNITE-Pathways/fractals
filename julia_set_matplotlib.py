import numpy as np
import matplotlib.pyplot as plt

def julia_set(width, height, zoom, cX, cY, moveX, moveY, max_iter):
    # Create an image with the given dimensions
    image = np.zeros((width, height))
    
    # Calculate the scale based on the zoom factor
    scaleX = 1.5 / (0.5 * zoom * width)
    scaleY = 1.0 / (0.5 * zoom * height)
    
    # Generate the Julia set
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
            i = max_iter
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i -= 1

            # Normalize and store the value
            image[x, y] = i

    return image

def main():
    width, height = 800, 800
    zoom = 1
    cX, cY = -0.7, 0.27015
    moveX, moveY = 0.0, 0.0
    max_iter = 255

    # Generate the Julia set image
    fractal = julia_set(width, height, zoom, cX, cY, moveX, moveY, max_iter)
    
    # Plot the fractal
    plt.imshow(fractal.T, cmap='inferno', extent=[-1.5, 1.5, -1, 1])
    plt.colorbar()
    plt.title('Julia Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

if __name__ == '__main__':
    main()
