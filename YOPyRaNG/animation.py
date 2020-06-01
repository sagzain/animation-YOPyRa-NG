import auxfunct as YA
from vector import *
import math

class animation:
    def __init__(self, translate=None):
        self.translate = translate

    def calculate_t(self,position):
        frames = YA.FRAMES - 1 
        substraction = self.translate - position
        factor = vector(substraction.x/frames,substraction.y/frames,substraction.z/frames)

        return position + factor