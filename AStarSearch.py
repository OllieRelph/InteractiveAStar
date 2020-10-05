import pygame
import sys

window_height = 750
window_width = 750
colour_black = (0,0,0)
colour_white = (255,255,255)
colour_red = (255,0,0)
colour_green = (0,255,0)
block_size = 25
clicked_pos = []
start_pos = (1,1)
end_pos = ( (int(window_height/block_size)-2) , (int(window_height/block_size)-2))


def main():
    pygame.init()
    window = pygame.display.set_mode((750,750))
    window.fill(colour_white)
    drag = False
    while True:
        draw(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drag = True
                pos = pygame.mouse.get_pos()
                block_coord_x = (int(pos[0]/block_size))
                block_coord_y = (int(pos[1]/block_size))
                if ((block_coord_x,block_coord_y)) not  in clicked_pos:
                    clicked_pos.append((block_coord_x,block_coord_y))
            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False
            elif event.type == pygame.MOUSEMOTION and drag == True:
                pos = pygame.mouse.get_pos()
                block_coord_x = (int(pos[0]/block_size))
                block_coord_y = (int(pos[1]/block_size))
                if ((block_coord_x,block_coord_y)) not  in clicked_pos:
                    clicked_pos.append((block_coord_x,block_coord_y))
                
                
              
        pygame.display.update()


def draw(window):
    for x in range(int(window_width/block_size)):
        for y in range(int(window_height/block_size)):
            
            if (x,y) in clicked_pos:
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(window, colour_red, rect, 0)
            elif (x,y) == start_pos or (x,y) == end_pos:
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(window, colour_green, rect, 0)
                
            else: 
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(window, colour_black, rect, 1)
    
    


    
            
main()