import pygame, sys


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

