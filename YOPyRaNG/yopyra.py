import time
import auxfunct as YA   # YA = Yopyra Aux
from random import random
from vector import *
from ray import *
from camera import *
from sphere import *
from color import *
from world import *
import sys
import os

def raytracing(world, r, depth):
    if (depth <= 0): return color((0,0,0))

    hitp, n, obj = world.hit(r)

    if (hitp != None):
        scattered_ray = obj.material.scatter(r, hitp, n)
        if (scattered_ray != None):
            c = raytracing(world, scattered_ray, depth - 1)
        else:
            return color((0,0,0))
        attenuation = obj.material.attenuate(hitp)
        return c.mul_colors(attenuation)
    return world.get_background_color(r)

# Main --------------------------------------------------
start_time = time.time()

argoutput = ""; argconfig = ""; argscene = ""; argprog = ""

for a in sys.argv:
    larg = os.path.splitext(a)
    if (larg[1] == ".jpg"): argoutput = a;
    if (larg[1] == ".ini"): argconfig = a;
    if (larg[1] == ".json"): argscene = a;
    if (larg[1] == ".py"): argprog = a;

YA.showArgInfo(argconfig, argscene, argoutput);
if (argscene == ""): YA.showHelp(argprog);

YA.loadconfig(argconfig)
if (argoutput != ""): YA.OUTPUT = argoutput;

YA.printRenderInfo()
image = YA.getImagePixels()
world = world(argscene)
world.print_scene_info()

loop_time = time.time()
for y in range(YA.HEIGHT):
    for x in range(YA.WIDTH):
        c = color((0,0,0))
        for s in range(YA.SAMPLING):
            if (YA.SAMPLING == 1): xr = 0.0; yr = 0.0
            else: xr = random(); yr = random()
            u = (x + xr) / YA.WIDTH; v = (y + yr) / YA.HEIGHT
            c += raytracing(world, world.camera.get_ray(u,v), YA.DEPTH)
        image[x,YA.HEIGHT-y-1] = c.write_color(YA.SAMPLING)
        YA.printProgressBar(y*YA.WIDTH+x, YA.WIDTH * YA.HEIGHT)
        if ((time.time() - loop_time) > YA.UPDATE_TIME):
            loop_time = time.time(); YA.saveImage()

YA.saveImage(); #YA.showImage()
print("\nTotal time: %.2f seconds \n" % (time.time() - start_time))
