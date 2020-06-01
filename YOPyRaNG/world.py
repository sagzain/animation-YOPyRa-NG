import auxfunct as YA
import json
from sphere import *
from vector import *
from color import *
from ray import *
from camera import *
from material import *
from texture import *
from animation import *

def get_nearest_point(r,p,n,d,nearestobj,obj, obj_p, obj_n):
    drp = (r.origin - obj_p).module()
    if ((drp > YA.EPSILON) & (drp < d)):
        return (obj_p,obj_n,drp,obj)
    return (p,n,d,nearestobj)

class world:
    def __init__(self, file):
        self.objects = []; self.materials = []; self.textures = []
        self.camera = None
        if (file != ""): self.loadscene(file);
        else:
            self.camera = camera(vector(0,0,0), vector(0,0,-1), vector(0,1,0), 90, YA.WIDTH / YA.HEIGHT)

    def getmaterial(self, id):
        for m in self.materials:
            if (m.id == id): return m
        return None

    def gettexture(self, id):
        for t in self.textures:
            if (t.id == id): return t
        return None


    def loadscene (self, file):
        with open(file, 'r') as f:
            data = json.load(f)

        for e in data:
            if (e['type'] == "camera"):
                o = vector(*tuple(e['origin']))
                to = vector(*tuple(e['to']))
                up = vector(*tuple(e['up']))
                fov = e['fov']
                ratio = float(YA.WIDTH / YA.HEIGHT)
                self.camera = camera(o, to, up, fov, ratio)

            if (e['type'] == "sphere"):
                p = vector(*tuple(e['position']))
                r = e['radius']
                idmaterial = e['material']
                material = self.getmaterial(idmaterial)
                if (material == None):
                    print ("\n\nERROR [Material \"%s\" not found]:  Please, check material id and define it *before* objects in .json file" % (idmaterial))
                    quit()
                if("animation" in e):
                    anim = animation()
                    if('translate' in e['animation']):
                        anim.translate = vector(*tuple(e['animation']['translate']))
                else:
                    anim = None

                obj = sphere(p, r, material, anim)
                self.objects.append(obj)

            if (e['type'] == "material"):
                idmaterial = e['id']
                texture = None
                if (e.get('texture') != None):
                    texture = self.gettexture(e['texture'])

                if (e['subtype'] == "lambertian"):
                    albedo = color(tuple(e['albedo']))
                    material = lambertian(idmaterial, albedo, texture)
                if (e['subtype'] == "metal"):
                    albedo = color(tuple(e['albedo']))
                    fuzzy = e['fuzzy']
                    material = metal(idmaterial, albedo, fuzzy, texture)
                if (e['subtype'] == "glass"):
                    ior = e['ior']
                    material = glass(idmaterial, ior, texture)

                self.materials.append(material)

            if (e['type'] == "texture"):
                idtexture = e['id']
                if (e['subtype'] == "checker"):
                    col1 = color(tuple(e['color1']))
                    col2 = color(tuple(e['color2']))
                    size = e['size']
                    texture = checker(idtexture, col1, col2, size)
                self.textures.append(texture)
        
        #Here we check if there is an object with animation so we use
        #the frame number in the config file, otherwise its value will be 1
        found = 0
        for o in self.objects:
            if(o.animation != None):
                found = 1

        if(found == 0): YA.FRAMES = 1

    def hit(self, r):
        p = None; n = None; d = YA.INFINITE; nearestobj = None
        for obj in self.objects:
            obj_hitted, obj_p, obj_n = obj.hit(r)
            if (obj_hitted):
                p,n,d,nearestobj = get_nearest_point (r,p,n,d,nearestobj,obj, obj_p, obj_n)
        return (p, n, nearestobj)

    def get_background_color(self, r):
        return color((int((r.direction.y+1)*128), 255, 255))

    def print_scene_info(self):
        print ("\n>> Scene Info: Objects [%d] - Materials [%d] - Textures[%d]" % (len(self.objects), len(self.materials), len(self.textures)))

    def update_world(self, frame):
        if frame > 0:
            for o in self.objects:
                if o.animation != None:
                    o.position = o.animation.calculate_t(o.position)