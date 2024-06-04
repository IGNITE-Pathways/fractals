import pygame
import numpy as np

# Screen dimensions
WIDTH, HEIGHT = 800, 800

# Mandelbrot set parameters
MAX_ITER = 100
X_MIN, X_MAX = -2.5, 1.5
Y_MIN, Y_MAX = -2.0, 2.0

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

def color_map(value, max_iter):
    t = float(value) / max_iter
    r = int(9 * (1 - t) * t * t * t * 255) % 8 * 32
    g = int(15 * (1 - t) * (1 - t) * t * t * 255) % 16 * 16
    b = int(8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255) % 32 * 8
    return (r, g, b)

def render(screen, width, height, mandelbrot_data):
    r1, r2, n3 = mandelbrot_data
    for x in range(width):
        for y in range(height):
            color = color_map(n3[x, y], MAX_ITER)
            screen.set_at((x, y), color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mandelbrot Set")
    
    mandelbrot_data = mandelbrot_set(WIDTH, HEIGHT, X_MIN, X_MAX, Y_MIN, Y_MAX, MAX_ITER)
    render(screen, WIDTH, HEIGHT, mandelbrot_data)
    
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
