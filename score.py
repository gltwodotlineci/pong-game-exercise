import pygame, sys



class Score:
    def __init__(self, screen, points, x_coord, y_coord):
        self.screen = screen
        self.points = points
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.font = pygame.font.SysFont("monospace", 80, bold=True)
        self.label = self.font.render(self.points, 0, (0,0,0))
        self.show()

    def show(self):
        self.screen.blit(self.label, (self.x_coord - self.label.get_rect().width // 2, self.y_coord))

    def keep_score(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points, 0, (0,0,0))

    def restart(self):
        self.points = '0'
        self.label = self.font.render(self.points, 0, (0,0,0))

