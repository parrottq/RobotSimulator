from math import pi


class Angle:

    degree = "degree"
    pi = "pi"

    def __init__(self, value=0):
        self.pi_angle = 0
        self.degree_angle = 0
        self.set_degree(value)

    def __getitem__(self, item):
        if item == "pi" or item == 0:
            return self.pi_angle
        elif item == "degree" or item == 1:
            return self.degree_angle
        else:
            raise KeyError

    def __setitem__(self, item, value):
        if item == "pi" or item == 0:
            self.set_pi(value)
        elif item == "degree" or item == 1:
            self.set_degree(value)
        else:
            raise KeyError

    def set_pi(self, value):
        self.pi_angle = value
        self.degree_angle = value * (360 / (pi*2))

    def set_degree(self, value):
        self.degree_angle = value
        self.pi_angle = value * ((pi*2) / 360)


if __name__ == "__main__":
    a = Angle()
    # a["pi"] = pi * 1
    a["degree"] = 360

    print(a["pi"])
    print(a["degree"])
