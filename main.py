import pygame
from MainProgramV1 import MainProgramV1

pygame.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gears v1.1')
icon = pygame.image.load('Style//CalculateIcon.png')
pygame.display.set_icon(icon)

m = MainProgramV1(window, 0, 0)
while True:
    for ev in pygame.event.get():
        m.event_handler(ev)
        if ev.type == pygame.QUIT:
            exit()

    m.draw()
    pygame.display.flip()
    window.fill((0, 0, 0))
