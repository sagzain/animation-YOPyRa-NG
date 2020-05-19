from math import sqrt

class color:
    def __init__(self, t):
        self.r, self.g, self.b = t[0], t[1], t[2]
    def __add__(self, t):
        return color((self.r+t.r, self.g+t.g, self.b+t.b))
    def __mul__(self, n):
        return color(n * self.r, n * self.g, n * self.b)
    def __sub__(self, t):
        return color((self.r - t.r, self.g - t.g, self.b - t.b))
    def __idiv__(self, n):
        return color((int(self.r / float(n)), int(self.g / float(n)), int(self.b / float(n))))
    def __truediv__(self, n):
        return color((int(self.r / float(n)), int(self.g / float(n)), int(self.b / float(n))))
    def distance(self):
        return (self.r + self.g + self.b)
    def write_color(self, samples):
        scale = 1.0 / float(samples)
        if (samples > 1):
            r = 0 if self.r < 0 else int(256 * sqrt(scale * (self.r / 255.0)))
            g = 0 if self.g < 0 else int(256 * sqrt(scale * (self.g / 255.0)))
            b = 0 if self.b < 0 else int(256 * sqrt(scale * (self.b / 255.0)))
            return (r,g,b)
        else:
            return (int(self.r), int(self.g), int(self.b))
    def mul_colors(self, other):
        return color((self.r * other.r / 255.0, self.g * other.g / 255.0, self.b * other.b / 255.0))
