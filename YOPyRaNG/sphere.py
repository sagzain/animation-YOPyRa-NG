from math import sqrt
import auxfunct as YA

class sphere:
    def __init__(self, position, radius, material):
        self.position = position
        self.radius = radius
        self.material = material

    def hit_update_n (self, t, r):
        p_hit = r.at(t)
        normal = (p_hit - self.position).unit()
        if (r.direction.dot(normal) > 0): normal = -normal
        return (True, p_hit, normal)

    def hit(self, r):
        oc = r.origin - self.position
        a = pow(r.direction.module(),2)
        b = oc.dot(r.direction)
        c = pow(oc.module(),2) - pow(self.radius,2)
        discriminant = b*b - c*a

        if (discriminant > 0):
            root = sqrt(discriminant)
            t = (-b-root) / a
            if (t > YA.EPSILON):
                return (self.hit_update_n(t,r))
            t = (-b+root) / a
            if (t > YA.EPSILON):
                return (self.hit_update_n(t,r))

        return (False, None, None)
