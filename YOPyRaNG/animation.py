import auxfunct as YA

class animation:
    def __init__(self, translate=None, rotate=None, scale=None):
        self.translate = translate
        self.rotate = rotate 
        self.scale = scale


    def calculate_t(self):
        print(YA.FRAMES)