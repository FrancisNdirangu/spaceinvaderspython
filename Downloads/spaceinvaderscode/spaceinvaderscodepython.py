#spaceinvaderscode
import pygame,sys


class Game:
    def __init__(self): #where we load the sprites and initial stuff
        pass
    
    def run(self): #the main part of game
        pass
if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30,30,30))

        pygame.display.flip()
        clock.tick(60)