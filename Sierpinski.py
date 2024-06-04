import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fractal Generation - Sierpinski Triangle')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Initial points of the triangle
points = [(400, 50), (50, 750), (750, 750)]

# Function to draw the Sierpinski Triangle
def draw_sierpinski(points, depth, max_depth):
    if depth == max_depth:
        pygame.draw.polygon(screen, white, points, 1)
        pygame.display.flip()
        return

    # Calculate midpoints of the triangle
    midpoints = [
        ((points[0][0] + points[1][0]) // 2, (points[0][1] + points[1][1]) // 2),
        ((points[1][0] + points[2][0]) // 2, (points[1][1] + points[2][1]) // 2),
        ((points[2][0] + points[0][0]) // 2, (points[2][1] + points[0][1]) // 2)
    ]

    # Recursive calls for the three smaller triangles
    draw_sierpinski([points[0], midpoints[0], midpoints[2]], depth + 1, max_depth)
    draw_sierpinski([points[1], midpoints[0], midpoints[1]], depth + 1, max_depth)
    draw_sierpinski([points[2], midpoints[1], midpoints[2]], depth + 1, max_depth)

    # Slow down the drawing to make it peaceful to watch
    time.sleep(0.5)

# Main function
def main():
    screen.fill(black)
    max_depth = 5  # You can change this to make the fractal more or less detailed
    draw_sierpinski(points, 0, max_depth)

    # Keep the screen open to admire the fractal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
