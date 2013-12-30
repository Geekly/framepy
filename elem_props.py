__author__ = 'ENG-5 USER'

class FrameElement2d:

    def __init__(self):
        self.E = 0.0
        self.A = 0.0
        self.I = 0.0
        self.x1 = 0.0
        self.y1 = 0.0
        self.x2 = 0.0
        self.y2 = 0.0

    def Coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        str = 'E: %(e)E, A: %(a)E, I: %(i)E' % {'e':self.E, 'a':self.A, 'i':self.I}
        return str