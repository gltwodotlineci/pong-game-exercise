import pygame, sys

pygame.init()

WIDTH = 800
HEIGHT = 650


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((127,255,0))
pygame.display.set_caption('Pong')

def line_and_background():
    screen.fill((127,255,0))
    pygame.draw.line(screen, (255,255,255),(WIDTH//2, 0),(WIDTH//2, HEIGHT), 5)

line_and_background()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()

