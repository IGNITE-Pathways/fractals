import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fractal Generation - Colorful Dragon Curve')

# Colors
black = (0, 0, 0)

# Function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    return (
        int(color1[0] + (color2[0] - color1[0]) * factor),
        int(color1[1] + (color2[1] - color1[1]) * factor),
        int(color1[2] + (color2[2] - color1[2]) * factor),
    )

# Function to draw the Dragon Curve
def draw_dragon_curve(order, p1, p2, color1, color2):
    if order == 0:
        pygame.draw.line(screen, color1, p1, p2, 1)
        pygame.display.flip()
        time.sleep(0.001)
    else:
        # Calculate the midpoint and the new point to form the Dragon Curve
        mid = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
        new_point = (mid[0] + (p1[1] - p2[1]) // 2, mid[1] - (p1[0] - p2[0]) // 2)
        
        # Interpolate colors
        new_color = interpolate_color(color1, color2, 0.5)
        
        draw_dragon_curve(order - 1, p1, new_point, color1, new_color)
        draw_dragon_curve(order - 1, p2, new_point, color2, new_color)

# Main function
def main():
    screen.fill(black)
    order = 15  # You can change this to make the fractal more or less detailed

    # Initial points for the Dragon Curve
    p1 = (200, 400)
    p2 = (600, 400)

    # Initial colors for the gradient
    color1 = (255, 0, 0)  # Red
    color2 = (0, 0, 255)  # Blue

    draw_dragon_curve(order, p1, p2, color1, color2)

    # Keep the screen open to admire the fractal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
