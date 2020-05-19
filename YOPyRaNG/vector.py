from math import sqrt, pow
from random import random
import auxfunct as YA

class vector:

    def __init__(self, vx=0.0, vy=0.0, vz=0.0):
        self.x, self.y, self.z = vx, vy, vz

    def __add__(self, other):
        return vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        return vector(self.x*other, self.y*other, self.z*other)

    def __neg__(self):
        return vector(-self.x, -self.y, -self.z)

    def dot(self, vv):
        return (self.x * vv.x + self.y * vv.y + self.z * vv.z)

    def cross(self, vv):
        x = (vv.y*self.z) - (vv.z*self.y)
        y = (vv.z*self.x) - (vv.x*self.z)
        z = (vv.x*self.y) - (vv.y*self.x)
        return (vector(x,y,z))

    def module(self):
        return (sqrt(pow(self.x,2) + pow(self.y,2) + pow(self.z,2)))

    def unit(self):
        m = float(self.module())
        if (m != 0.0):
            self.x /= m;  self.y /= m; self.z /= m
        return self

    def rand_unit_cube(self):
        return vector(random()*2-1, random()*2-1, random()*2-1)

    def rand_unit_sphere(self):
        while(True):
            v = vector().rand_unit_cube()
            if (v.module() < 1): return v

    def reflect(self, n):
        return (self - n*2*self.dot(n))

    def refract(self, n, etai):
        cos_theta = YA.ffmin(-self.dot(n), 1.0)
        r_out_parallel = (self + n*cos_theta) * etai
        r_out_perp = n * -sqrt(1.0 - pow(r_out_parallel.module(),2))
        return (r_out_parallel + r_out_perp)

    def is_front_face(self, normal): # self is input direction
        return (self.dot(normal) < 0)
