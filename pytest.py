# test_pong.py

import pytest
import pygame
from pong import Paddle, Ball, handle_collision, handle_paddle_movement

pytest.fixture
def paddle():
    return Paddle(10, 10, 20, 100)

pytest.fixture
def ball():
    return Ball(50, 50, 10)  

def test_paddle_movement(paddle):
    paddle.move(up=True)
    assert paddle.y == 6
    
    paddle.move(up=False)
    assert paddle.y == 10
    
def test_ball_movement(ball):
    x = ball.x
    y = ball.y
    
    ball.move()
    
    assert ball.x == x + ball.x_vel
    assert ball.y == y + ball.y_vel

def test_collision_detection(paddle, ball):
    ball.x = 30
    ball.y = 20
    
    handle_collision(ball, paddle, None)
    
    assert ball.x_vel == -ball.MAX_VEL
    
def test_handle_paddle(paddle):
    keys = {pygame.K_w: True}
    handle_paddle_movement(keys, paddle, None)
    
    assert paddle.y == paddle.original_y - paddle.VEL