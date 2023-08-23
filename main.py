import pygame
import Object_3d

FPS = 60
SIZE = (1200, 600)


class Game:

    def __init__(self):
        self.FPS = 60
        self.caption = "Sprite stacking"
        self.size = (1200, 800)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)
        clock = pygame.time.Clock()

        obg = Object_3d.Object3D(self.size[0] // 2, self.size[1] // 2, "img/", 7, screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            screen.fill((60, 60, 60))

            obg.blit_me()
            obg.rotate_me()

            pygame.display.flip()
            clock.tick(self.FPS)


game = Game()
game.run()