import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "centered"
import pygame

from classes.map.biomes.plains import Plains
from classes.map.hex import hex_points

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
HEX_SIZE = 30  # centro ao vértice, em pixels


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), display=0)
    pygame.display.set_caption("Simulation")
    clock = pygame.time.Clock()

    tile = Plains()
    center = (screen.get_width() // 2, screen.get_height() // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30)) #cor de fundo

        pygame.draw.polygon(screen, tile.color, hex_points(*center, HEX_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
