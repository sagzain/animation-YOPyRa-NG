from math import sin

class texture:
    def __init__(self, id):
        self.id = id

class checker(texture):
    def __init__(self, id, col1, col2, size):
        texture.__init__(self, id)
        self.col1 = col1; self.col2 = col2
        self.size = size
    def getcolor (self, p, u=0, v=0):
        sines = sin(self.size*p.x)*sin(self.size*p.y)*sin(self.size*p.z)
        if (sines < 0): return self.col1
        else: return self.col2
