import pygame, sys

class Ball:
    def __init__(self, screen, color, x_coord, y_coord, radius):
        self.screen = screen
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x_coord, self.y_coord), self.radius)

    def start_game(self):
        self.dx = 15
        self.dy = 5

    def move(self):
        self.x_coord += self.dx
        self.y_coord += self.dy



class Paddle:
    def __init__(self, screen, color, x_coord, y_coord, width, height):
        self.screen = screen
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.x_coord, self.y_coord, self.width, self.height))

    def move(self):
        if self.state == 'up':
            self.y_coord -=10

        elif self.state == 'down':
            self.y_coord += 10

    def clamp(self):
        if self.y_coord <= 0:
            self.y_coord = 0
        if self.y_coord >= (600-110):
            self.y_coord = 490


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

playing = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ball.start_game()
                playing = True

            if event.key == pygame.K_a:
                left_paddle.state = 'up'

            if event.key == pygame.K_q:
                left_paddle.state = 'down'

            if event.key == pygame.K_p:
                right_paddle.state = 'up'

            if event.key == pygame.K_m:
                right_paddle.state = 'down'

        if event.type == pygame.KEYUP:
            left_paddle.state = 'stopped'
            right_paddle.state = 'stopped'


        if playing:
            line_and_background()

            ball.move()
            ball.show()

            left_paddle.clamp()
            left_paddle.show()
            left_paddle.move()

            right_paddle.clamp()
            right_paddle.show()
            right_paddle.move()

        pygame.display.update()

