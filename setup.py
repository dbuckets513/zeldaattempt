import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # basic setup for "empty canvas"
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()

        self.level = Level()


    #function for exiting the game
    def run(self):
        while True:
            for event in pygame.mode.get():
                if event.type == pygame.QUIT():
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
if __name__ == '__main__':
    game = Game()
    game.run()
