import auxfunct as YA
from vector import *

class animation:
    def __init__(self, translate=None, rotate=None, scale=None):
        self.translate = translate
        self.rotate = rotate 
        self.scale = scale


    def calculate_t(self,position):
        frames = YA.FRAMES - 1 
        substraction = self.translate - position
        factor = vector(substraction.x/frames,substraction.y/frames,substraction.z/frames)

        return position + factor