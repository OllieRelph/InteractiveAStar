import pygame
import sys

window_height = 750
window_width = 750
colour_black = (0,0,0)
colour_white = (200,200,200)
block_size = 10

def main():
    pygame.init()
    window = pygame.display.set_mode((750,750))
    window.fill(colour_white)
    while True:
        draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def draw(window):
    for x in range(int(window_width/block_size)):
        for y in range(int(window_height/block_size)):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(window, colour_black, rect, 1)
            
main()