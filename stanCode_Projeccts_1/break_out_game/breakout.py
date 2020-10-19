"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
-----------------------------------
File: breakous.py
Name: Isabelle
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked
from campy.graphics.gobjects import GLabel
import random

# Constant
FRAME_RATE = 1000 / 120      # 120 frames per second.
NUM_LIVES = 3                # how many lives player has

# Global
graphics = BreakoutGraphics()
dx = graphics.get_dx()                        # horizontal velocity
dy = graphics.get_dy()                        # vertical velocity
lives = NUM_LIVES                             # the number of lives
score = 0                                     # score the player get
y_speed = -7.0                                # vertical speed which will be changed with score increasing
label_life = GLabel('LIFE:' + str(lives))     # lives on label
label_score = GLabel('SCORE: ' + str(score))  # score on label
img_speed = 1.0                               # images' vertical velocity


def main():
    onmouseclicked(start_the_game)
    label_1 = add_life()
    graphics.window.add(label_1, x=graphics.window.width - label_life.width, \
                        y=graphics.window.height - label_life.height)
    label_2 = add_score()
    graphics.window.add(label_2, x=0, y=graphics.window.height - label_life.height)


# Add animation loop here!
def start_the_game(mouse):
    """
    start the game by mouse clicking
    :param mouse: MouseEvent
    """
    global dx, dy, lives, score
    if 0 <= mouse.x <= graphics.window.width and lives != 0 and graphics.b_amount > 0:
        while True:
            graphics.ball.move(dx, dy)
            graphics.img.move(0, img_speed)
            pause(FRAME_RATE)
            # detect object to see if the ball hits paddle, bricks, or others
            detect_object()
            # if the ball hits the walls, the direction of bouncing will be changed
            change_direction()
            # when player didn't catch the ball
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                lives -= 1
                # change the word on label_life
                label_life.text = 'LIFE:' + str(lives)
                graphics.window.remove(graphics.ball)
                graphics.reset_ball()
                break
            elif graphics.b_amount <= 0:
                break
        # show player game is over
        if lives == 0:
            label_end = label_gameover()
            graphics.window.add(label_end, x=(graphics.window.width-label_end.width)/2, y=0+graphics.window.height/2)
        elif graphics.b_amount <= 0:
            label_win = label_win_the_game()
            graphics.window.add(label_win, x=(graphics.window.width-label_win.width)/2, y=0+graphics.window.height/2)


def change_direction():
    """
    change direction of bouncing
    """
    global dx, dy
    # horizontal velocity
    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
        dx = -dx
        graphics.reset_horizontal_velocity(dx)
    # vertical velocity
    if graphics.ball.y <= 0:
        dy = -dy
        graphics.reset_vertical_velocity(dy)


def add_score():
    """
    show the score
    :return: gobject, score on label
    """
    label_score.font = '-20'
    label_score.color = 'skyblue'
    return label_score


def add_life():
    """
    show lives
    :return: gobject, lives on label
    """
    label_life.font = '-20'
    label_life.color = 'skyblue'
    return label_life


def label_gameover():
    """
    show "Game over!" as game ends
    :return: gobject, show player the game is over
    """
    label = GLabel('Game over!')
    label.font = '-50'
    label.color = 'skyblue'
    return label


def label_win_the_game():
    """
    Show "You Win!" as user wins the game
    :return: gobject
    """
    label = GLabel('You Win!')
    label.font = '-50'
    label.color = 'skyblue'
    return label


def reset_speed():
    """
    reset vertical speed as score achieves certain level
    :return: float, new vertical speed
    """
    global y_speed
    # when score achieves 50
    if score == 50:
        # ball moves faster
        y_speed = y_speed * 1.2
        graphics.reset_vertical_velocity(dy)
    # when score achieves 70
    elif score == 70:
        # ball moves faster
        y_speed = y_speed * 1.2
        graphics.reset_vertical_velocity(dy)
    elif score == 120:
        # ball moves faster
        y_speed = y_speed * 1.3
        graphics.reset_vertical_velocity(dy)


def detect_object():
    """
    detect object is brick, paddle, or others
    """
    global score, dy
    # get object on the position of ball
    obj = graphics.detect_object()
    # ball hits the image
    if obj is not None and obj == graphics.img and obj is not label_life and obj is not label_score:
        # get 15 points on each image
        score += 15
        # change the word on label_score
        label_score.text = 'SCORE: ' + str(score)
        # when score achieves certain standard, the vertical will be increased
        reset_speed()
        # change ball's direction
        graphics.window.add(graphics.img, \
                            x=random.randint(0, (graphics.b_w + graphics.b_o) * graphics.b_c - graphics.img.width*2), \
                            y=(graphics.b_h + graphics.b_o))
        graphics.reset_vertical_velocity(dy)
    # ball hits the paddle
    elif obj is not None and obj == graphics.paddle and obj is not label_life and obj is not label_score:
        # change ball's direction
        dy = y_speed
        graphics.reset_vertical_velocity(dy)
    # ball hits bricks
    elif obj is not None and obj is not label_life and obj is not label_score:
        # get 5 points on each brick
        score += 5
        # change the word on label_score
        label_score.text = 'SCORE: ' + str(score)
        # when score achieves certain standard, the vertical will be increased
        reset_speed()
        # change ball's direction
        dy = -y_speed
        graphics.window.remove(obj)
        graphics.b_amount -= 1
        graphics.reset_vertical_velocity(dy)


if __name__ == '__main__':
    main()
