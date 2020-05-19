from vector import *
from ray import *
from color import *
from texture import *
import auxfunct as YA

class material:
    def __init__(self, id, texture=None):
        self.id = id; self.texture = texture

class lambertian(material):
    def __init__(self, id, albedo, texture=None):
        material.__init__(self, id, texture)
        self.albedo = albedo
    def scatter(self, r, p, n):
        target = p + n + vector().rand_unit_sphere()
        scattered = target - p
        return (ray(p + n * YA.EPSILON, scattered.unit()))
    def attenuate(self, p, u=0, v=0):
        if (self.texture != None) :
            return self.texture.getcolor(p, u, v)
        else: return (self.albedo)

class metal(material):
    def __init__(self, id, albedo, fuzzy, texture=None):
        material.__init__(self, id, texture)
        self.albedo = albedo
        self.fuzzy = fuzzy if fuzzy < 1 else 1
    def scatter(self, r, p, n):
        dir = r.direction.unit()
        reflected = dir.reflect(n)
        dirscatt = reflected + vector().rand_unit_sphere() * self.fuzzy
        if (dirscatt.dot(n) > 0):
            return (ray(p + n * YA.EPSILON, dirscatt))
        else:
            return (None)
    def attenuate(self, p, u=0, v=0):
        if (self.texture != None) :
            return self.texture.getcolor(p, u, v)
        else: return (self.albedo)

class glass(material):
    def __init__(self, id, ior, texture=None):
        material.__init__(self, id, texture)
        self.ior = ior

    def scatter(self, r, p, n):
        etai = (1.0 / self.ior) if r.direction.is_front_face(n) else  self.ior
        unitdir = r.direction.unit()
        cos_theta = YA.ffmin(n.dot(-unitdir),1.0)
        sin_theta = sqrt(1.0 - pow(cos_theta,2))

        # Reflection ---------------------------------
        if (etai * sin_theta > 1.0):  # Must reflect
            reflected = unitdir.reflect(n)
            return (ray(p + n * YA.EPSILON, reflected))

        r0 = pow((1-etai) / (1+etai), 2)
        schlick = r0 + (1-r0) * pow((1-cos_theta), 5)
        if (random() < schlick):  # Can reflect
            reflected = unitdir.reflect(n)
            return (ray(p + n * YA.EPSILON, reflected))

        # Refraction ----------------------------------
        refracted = unitdir.refract(n, etai)
        return (ray(p - n * YA.EPSILON, refracted))

    def attenuate(self, p, u=0, v=0):
        return (color((225, 225, 225)))
