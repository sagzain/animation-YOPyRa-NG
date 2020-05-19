from math import *
from vector import *
from ray import *

class camera:
    def __init__(self, p_origin, p_to, v_up, fov, aspect):
        self.p_origin = p_origin;  self.p_to = p_to;
        self.v_up = v_up;  self.fov = fov;  self.aspect = aspect

        half_height = tan((fov * 3.1415926 / 180.0) / 2.0)
        half_width = aspect * half_height
        w = p_origin - p_to;  w.unit()
        u = v_up.cross(w);  u.unit()
        v = w.cross(u)
        self.p_left_down = p_origin - u*half_width - v*half_height - w
        self.v_horiz = u * 2 * half_width
        self.v_vert = v * 2 * half_height

    def get_ray(self, u, v):
        dir = self.p_left_down + self.v_horiz * u + self.v_vert * v - self.p_origin
        dir.unit()
        return ray(self.p_origin, dir)
