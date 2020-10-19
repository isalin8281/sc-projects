"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
-----------------------
File: breakoutgraphics.py
Name: Isabelle
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause

import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 10      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 420      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.b_r = brick_rows
        self.b_c = brick_cols
        self.b_w = brick_width
        self.b_h = brick_height
        self.b_o = brick_offset
        self.b_s = brick_spacing
        self.b_amount = brick_rows * brick_cols
        self.ball_r = ball_radius
        self.paddle_o = paddle_offset

        # Create a graphical window, with some extra space.
        self.brick = GRect(brick_width, brick_height)
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # create an image
        self.img = GImage('luv.png')
        self.reset_img()

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'coral'
        self.paddle.color = 'coral'
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2, \
                        (self.window.height-paddle_offset))

        # Draw bricks.
        self.add_bricks()

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'royalblue'
        self.ball.color = 'royalblue'
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball.
        self.__dy = 0
        self.__dx = 0
        self.ball_velocity()

        # Initialize our mouse listeners.h
        onmousemoved(self.paddle_move)

    def add_bricks(self):
        """
        Make bricks
        """
        a = 0
        b = 0
        # brick rows
        for i in range(self.b_r):
            # bricks columns
            for j in range(self.b_c):
                self.brick = GRect(self.b_w, self.b_h)
                self.brick.filled = True
                # set colors
                if i % 4 == 1:
                    self.brick.fill_color = 'plum'
                    self.brick.color = 'plum'
                elif i % 4 == 2:
                    self.brick.fill_color = 'lightskyblue'
                    self.brick.color = 'lightskyblue'
                elif i % 4 == 3:
                    self.brick.fill_color = 'lawngreen'
                    self.brick.color = 'lawngreen'
                else:
                    self.brick.fill_color = 'coral'
                    self.brick.color = 'coral'
                self.window.add(self.brick, x=a, y=b + self.b_o)
                # space between columns
                a += self.b_s
                a += self.b_w
                # space between rows
                if j == self.b_c - 1:
                    a = 0
                    b += self.b_s
                    b += self.b_h

    def paddle_move(self, mouse):
        """
        paddle moves with mouse moving
        :param mouse: MouseEvent
        """
        self.paddle.x = mouse.x - self.window.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def ball_velocity(self):
        """
        reset ball vertical and horizontal velocity
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dy(self):
        """
        return vertical velocity to user
        :return: float, vertical velocity
        """
        return self.__dy

    def get_dx(self):
        """
        return horizontal velocity to user
        :return: float, horizontal velocity
        """
        return self.__dx

    def reset_vertical_velocity(self, new_dy):
        """
        reset vertical velocity
        :param new_dy: New vertical velocity
        """
        self.__dy = new_dy

    def reset_horizontal_velocity(self, new_dx):
        """
        reset horizontal velocity
        :param new_dx: New horizontal velocity
        """
        self.__dx = new_dx

    def detect_object(self):
        """
        detect if the ball hits paddle or bricks
        """
        # detect object by using each four point of the ball
        for i in range(0, self.ball.width*2, self.ball.width):
            for j in range(0, self.ball.height*2, self.ball.height):
                obj = self.window.get_object_at(self.ball.x + i, self.ball.y + j)
                if obj is not None:
                    return obj

    def reset_ball(self):
        """
        reset the ball as player lost each life
        :return: gobject, the ball
        """
        self.ball = GOval(self.ball_r * 2, self.ball_r * 2)
        self.ball.filled = True
        self.ball.fill_color = 'royalblue'
        self.ball.color = 'royalblue'
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)
        self.ball_velocity()
        return self.ball

    def reset_img(self):
        """
        add image
        """
        self.set_img_position()
        while self.img.y >= self.window.height:
            self.set_img_position()
        self.window.add(self.img)

    def set_img_position(self):
        """
        reset image position
        """
        self.img.x = random.randint(0, (self.b_w + self.b_o) * self.b_c - self.img.width)
        self.img.y = 0































