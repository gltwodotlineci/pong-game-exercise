import pygame, sys

class Ball:
    def __init__(self, screen, color, x_coord, y_coord, radius):
        self.screen = screen
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x_coord, self.y_coord), self.radius)


class Paddle:
    def __init__(self, screen, color, x_coord, y_coord, width, height):
        self.screen = screen
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.x_coord, self.y_coord, self.width, self.height))



pygame.init()

WIDTH = 850
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((127,255,0))
pygame.display.set_caption('Pong')

def line_and_background():
    screen.fill((127,255,0))
    pygame.draw.line(screen, (255,255,255),(WIDTH//2, 0),(WIDTH//2, HEIGHT), 5)

line_and_background()

ball = Ball(screen, (255, 0, 0), WIDTH//2, HEIGHT//2, 10)
left_paddle = Paddle(screen, (20,144,255), 15, HEIGHT//2-55, 15, 110)
right_paddle = Paddle(screen, (255,255,0), 820, HEIGHT//2-55, 15, 110) # OR WIDTH-15-15


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pygame.display.update()




