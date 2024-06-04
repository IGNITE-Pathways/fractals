import pygame
import sys
import time
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fractal Generation - Koch Snowflake')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Function to draw a Koch Snowflake
def draw_koch_snowflake(order, scale):
    def koch_curve(order, p1, p2):
        if order == 0:
            pygame.draw.line(screen, white, p1, p2, 1)
            pygame.display.flip()
            # time.sleep(0.001)
        else:
            x1, y1 = p1
            x2, y2 = p2

            # Calculate points
            dx = (x2 - x1) / 3
            dy = (y2 - y1) / 3

            x3 = x1 + dx
            y3 = y1 + dy

            x5 = x1 + 2 * dx
            y5 = y1 + 2 * dy

            # Point of the equilateral triangle
            x4 = 0.5 * (x1 + x2) + math.sqrt(3) * (y1 - y2) / 6
            y4 = 0.5 * (y1 + y2) + math.sqrt(3) * (x2 - x1) / 6

            # Recursive calls
            koch_curve(order - 1, p1, (x3, y3))
            koch_curve(order - 1, (x3, y3), (x4, y4))
            koch_curve(order - 1, (x4, y4), (x5, y5))
            koch_curve(order - 1, (x5, y5), p2)

    # Equilateral triangle vertices
    p1 = (width // 2, height // 2 - scale * math.sqrt(3) / 3)
    p2 = (width // 2 - scale / 2, height // 2 + scale * math.sqrt(3) / 6)
    p3 = (width // 2 + scale / 2, height // 2 + scale * math.sqrt(3) / 6)

    # Draw the three sides of the triangle
    koch_curve(order, p1, p2)
    koch_curve(order, p2, p3)
    koch_curve(order, p3, p1)

# Main function
def main():
    screen.fill(black)
    order = 4  # You can change this to make the fractal more or less detailed
    scale = 400  # Scale of the snowflake
    draw_koch_snowflake(order, scale)

    # Keep the screen open to admire the fractal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
