import pygame, sys
sys.path.append(".")
from ball import Ball
from paddles import Paddle


class CollisionController:
    def between_ball_left_paddle(self, ball, left_paddle):
        if ball.y_coord + ball.radius > left_paddle.y_coord and ball.y_coord - ball.radius < left_paddle.y_coord + left_paddle.height:
            if ball.x_coord - ball.radius <= left_paddle.x_coord + left_paddle.width:
                return True

        return False

    def between_ball_right_paddle(self, ball, right_paddle):
        if ball.y_coord + ball.radius > right_paddle.y_coord and ball.y_coord - ball.radius < right_paddle.y_coord + right_paddle.height:
            if ball.x_coord - ball.radius >= right_paddle.x_coord:
                return True

        return False

    def ball_wall_controll(self, ball):
        if ball.y_coord - ball.radius <= 0:
            return True

        if ball.y_coord + ball.radius >= HEIGHT:
            return True

        return False

    def win_padle_left(self, ball):
        return ball.x_coord - ball.radius >= WIDTH

    def win_padle_right(self, ball):
        return ball.x_coord + ball.radius <= 0


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
rebound = CollisionController()
score_left = Score(screen, '0', WIDTH//4,15)
score_right = Score(screen, '0', WIDTH - WIDTH//4,15)

playing = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                ball.start_game()
                playing = True

        #if event.key == pygame.K_r and playing:
        #        restart()
        #        playing = False

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

            #check for rebound
            if rebound.between_ball_left_paddle(ball, left_paddle):
                ball.paddle_rebound()

            if rebound.between_ball_right_paddle(ball, right_paddle):
                ball.paddle_rebound()

            if rebound.ball_wall_controll(ball):
                ball.wall_rebound()

            #check Win
            if rebound.win_padle_left(ball):
                score_left.keep_score()
                ball.restart()

            if rebound.win_padle_right(ball):
                score_right.keep_score()
                ball.restart()




        score_left.show()
        score_right.show()

        pygame.display.update()

