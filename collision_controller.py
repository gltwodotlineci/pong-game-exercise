import pygame


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

