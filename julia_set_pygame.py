import pygame
import numpy as np

# Julia set parameters
WIDTH, HEIGHT = 800, 800
ZOOM = 1
CX, CY = -0.7, 0.27015
MOVEX, MOVEY = 0.0, 0.0
MAX_ITER = 255

def julia_set(surface, width, height, zoom, cX, cY, moveX, moveY, max_iter):
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
            i = max_iter
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i -= 1
            color = (i % 8 * 32, i % 16 * 16, i % 32 * 8)
            surface.set_at((x, y), color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Julia Set')
    
    # Create a surface to draw the Julia set
    surface = pygame.Surface((WIDTH, HEIGHT))
    
    julia_set(surface, WIDTH, HEIGHT, ZOOM, CX, CY, MOVEX, MOVEY, MAX_ITER)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(surface, (0, 0))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()
