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

    def paddle_rebound(self):
        self.dx = -self.dx

    def wall_rebound(self):
        self.dy = -self.dy

    def restart(self):
        self.x_coord = 850//2
        self.y_coord = 600//2
        self.dx = 0
        self.dy = 0
        self.show()

