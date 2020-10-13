import pygame
import sys

window_height = 1000
window_width = 1000
colour_black = (0,0,0)
colour_white = (255,255,255)
colour_red = (255,0,0)
colour_green = (0,255,0)
colour_teal = (0,255,255)
colour_purple = (255,0,255)
block_size = 25
clicked_pos = []
quit_clicked = False
go_clicked = False
start_pos = (1,1)
end_pos = ((int(window_height/block_size)-2) , (int((window_height/block_size)*0.8)))


def main():
    global go_clicked
    pygame.init()
    window = pygame.display.set_mode((window_height,window_width))
    window.fill(colour_white)
    pygame.display.set_caption('TBD NAME')
    font = pygame.font.Font('freesansbold.ttf',75)
    
    #Creeate text  for go button
    text_go = font.render('GO', True, colour_black)
    textRect_go = text_go.get_rect()
    textRect_go.center = ((window_width*0.25), (window_height*0.95))

    #Create text   for exit bubtton
    text_quit = font.render('QUIT', True, colour_black)
    textRect_quit = text_quit.get_rect()
    textRect_quit.center = ((window_width*0.75), (window_height*0.95))
    
    
    drag = False
    while True:
        draw(window)
        window.blit(text_go,textRect_go)
        window.blit(text_quit,textRect_quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                drag = True
                pos = pygame.mouse.get_pos()
                if (pos[1] > window_height * 0.9):
                    if (pos[0] > window_width /2):
                        quit_clicked = True
                        print("Quit Confirmed")
                        pygame.quit()
                        sys.exit()
                    else:
                        go_clicked = True
                if not go_clicked:
                    block_coord_x = (int(pos[0]/block_size))
                    block_coord_y = (int(pos[1]/block_size))
                    if ((block_coord_x,block_coord_y)) not  in clicked_pos:
                        clicked_pos.append((block_coord_x,block_coord_y))
            elif event.type == pygame.MOUSEBUTTONUP:
                drag = False
            elif event.type == pygame.MOUSEMOTION and drag == True and go_clicked == False:
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
                if go_clicked == False:
                    pygame.draw.rect(window, colour_red, rect, 0)
                elif go_clicked == True: 
                    pygame.draw.rect(window, colour_black, rect, 0)
                    
            elif (x,y) == start_pos or (x,y) == end_pos:
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(window, colour_green, rect, 0)
            
            elif (y > (window_height/block_size)*0.9) and (x < (window_width/block_size)*0.5):
                rect = pygame.Rect(0,window_height*0.9, window_width/2, window_height*0.1)
                pygame.draw.rect(window, colour_teal, rect, 0)
                
            elif (y > (window_height/block_size)*0.9) and (x > (window_width/block_size)*0.5):
                rect = pygame.Rect(window_width/2 ,window_height*0.9, window_width/2, window_height*0.1)
                pygame.draw.rect(window, colour_purple, rect, 0)

                
            else: 
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(window, colour_black, rect, 1)
    
    
        

    
            
main()