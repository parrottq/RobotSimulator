from math import sin, sqrt
from unites import Angle


class Robot:

    def __init__(self):
        self.position = [10, 10]
        self.rotation = Angle(90)


def move_forward(robot, distance):
    relative_angle = robot.rotation["degree"] % 90

    # zone 0; x:pos y:pos
    # zone 1; x:pos y:neg
    # zone 2; x:neg y:neg
    # zone 3; x:neg y:pos
    zone = (robot.rotation["degree"] // 90) % 4

    opposite = sin(relative_angle) * distance
    adjacent = sqrt(distance**2 - opposite**2)

    if zone == 0:
        x = opposite * 1
        y = adjacent * 1
    elif zone == 1:
        x = adjacent * 1
        y = opposite * -1
    elif zone == 2:
        x = opposite * -1
        y = adjacent * -1
    elif zone == 3:
        x = adjacent * -1
        y = opposite * 1

    print((x, y))


if __name__ == "__main__":
    move_forward(Robot(), 10)