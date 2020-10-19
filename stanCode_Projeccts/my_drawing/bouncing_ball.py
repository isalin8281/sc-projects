"""
File: bouncing_ball.py
Name: Isabelle
-------------------------
The file shows how to start bouncing by mouse clicking
and the process of bouncing
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# horizontal velocity
VX = 3
DELAY = 10
# gravity
GRAVITY = 1
# The size of ball
SIZE = 20
# slow bouncing speed after the ball reaches to bottom
REDUCE = 0.9
# The initial position of the ball
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)
# x stands for the number of mouse click to start bouncing
x = 0
a = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing)


def bouncing(mouse):
    global x, a
    # mouse click will start bouncing.
    # if x == 3, mouse click can't start bouncing
    if 0 < mouse.x < 800 and x != 3 and a == 0:
        # vy stands for vertical velocity.
        vy = 0
        # when a == 1, the bouncing won't be impacted by mouse click
        a = 1
        # ball still within window
        while ball.x <= 800:
            vy += GRAVITY
            ball.move(VX, vy)
            # the ball reaches to the bottom of window
            if ball.y + SIZE >= 500:
                # the ball will be slowed and changed its bouncing direction after reaching to the bottom
                vy = -vy * REDUCE
                # bouncing speed reaches to 0
                while vy <= 0:
                    ball.move(VX, vy)
                    vy += GRAVITY
                    pause(DELAY)
            pause(DELAY)
        # after finishing bouncing, the ball goes back to the original position
        ball.x = START_X
        ball.y = START_Y
        x += 1
        a = 0


def set_up_oval():
    oval = GOval(SIZE, SIZE)
    oval.filled = True
    return oval


if __name__ == "__main__":
    main()
