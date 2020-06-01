# animation-YOPyRa-NG
YOPyRa-NG: Support for simple animations with changing object positions - Computer Graphics - UCLM

## Changes on the YOPyRa-NG

If you take a look to the [config](/config/config.ini) file you now will be able to indicate the number of frames that you want to generate for the animation.

```ini
[IMAGE]
width = 400
height = 200
output = out.jpg
quality = 95
sampling = 20
depth = 6

[ANIMATION]
frames = 60

[GUI]
update_time = 2
progress_bar_length = 36
```

Now the program is going to repeat the same process of generating an image for each frame we have indicated on the config file.
Each time a frame is generated, the position of the objects (if they have animation) is changed for the next image.

```python
for f in range(YA.FRAMES):
    world.update_world(f)
    for y in range(YA.HEIGHT):
        for x in range(YA.WIDTH):
            c = color((0,0,0))
            for s in range(YA.SAMPLING):
                if (YA.SAMPLING == 1): xr = 0.0; yr = 0.0
                else: xr = random(); yr = random()
                u = (x + xr) / YA.WIDTH; v = (y + yr) / YA.HEIGHT
                c += raytracing(world, world.camera.get_ray(u,v), YA.DEPTH)
            image[x,YA.HEIGHT-y-1] = c.write_color(YA.SAMPLING)
            YA.printProgressBar(f+1, y*YA.WIDTH+x, YA.WIDTH * YA.HEIGHT)
            if ((time.time() - loop_time) > YA.UPDATE_TIME):
                loop_time = time.time(); YA.saveImage(f)
```

The order to the program to give an object some animation is by adding the property animation inside an object.
This is the example of the structure you have to use, you can check it the rest in the [scene.json](/json/scene.json) file:
```json
{
    "type": 		"sphere",
    "material":	"red",
    "radius": 	1,
    "position": [2.5, 1, -4],
    "animation": {
                    "translate":[0, 2, -7],
                }
},
```

With animation we will indicate to the program that we are going to animate that specific object indicating inside that we want to translate that object to a new point.
The new point consist of a vector with three values corresponding to the X, Y and Z axis respectively.

So we have the initial position of the object in "position" and the final position in "animation" -> "translate".
Having that distance in mind, we just have to check the number of frames given by the user in the [config](/config/config.ini) file and then just split the translation in that number of frames.

```python
def calculate_t(self,position):
        frames = YA.FRAMES - 1 
        substraction = self.translate - position
        factor = vector(substraction.x/frames,substraction.y/frames,substraction.z/frames)

        return position + factor
```

For example if we indicate that we want 20 frames, the algorithm will calculate the distance from the origin to the final position and then divide into 20 segments that will correspond with the new position for the object on each frame to create the final movement.



## How to execute it

The following command will execute the program using the indicated configuration file inside the config file and the indicated json file inside the json folder:

```
python .\YOPyRaNG\yopyra.py ./config/config.ini ./json/scene.json
```

In this case we are using [config](/config/config.ini) for the configuration file and [json](/json/scene.json) for the json file.
The image name still can be ommited but now every image generated is going to be stored on the img folder and the final result, the animation, is going to be stored in the output folder.

## Author and Acknowledgment
The YOPyRa-NG code for this project was created by Carlos González Morcillo (Carlos.Gonzalez@uclm.es) for the Computer Graphics course at the University of Castilla-La Mancha.
For more information about the base YOPyRa-NG code, consult the [readme](./YOPyRaNG/README.md) inside its folder.

The development of the extension of the functionality for YOPyRa-NG to be able to generate simple animations has been done by @Samuglz6. 