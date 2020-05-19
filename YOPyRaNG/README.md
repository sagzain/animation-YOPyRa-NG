# What is YOPyRa
YOPyRa is a Pathtracer developed entirely in Python for teaching purposes in 399 lines of code. 

Pathtracing is a Monte Carlo method for rendering images of 3D scenes with global illumination. It is based on the rendering equation proposed by Kajiya in 1986, which incorporates a non-deterministic variation on the classic Whitted RayTracing algorithm based on Monte Carlo methods. Pathtracing allows the simulation of many effects such as soft shadows, indirect lighting, diffuse reflections, etc. However, the convergence of the method is slow and a high number of samples per pixel is necessary to achieve an image with little visible noise. 

The current version of YOPyRa includes support for: 
- Specification of scenes in .json format
- Render parameter settings in external file
- Spheres
- Lambert type diffuse materials
- Metal materials with a diffusion index
- Glass type materials (dielectric)
- Chess type textures
- Fuzzy shadows
- Gradient on the horizon
- Multiple samples per pixel

The main objective of YOPyRa is to build a Pathtracer with a clean and clear code. Python has been used because it is a language known to computer engineering students, and because it allows to build programs with few lines of code. In this project no effort has been dedicated to optimization aspects (the execution is very slow, you are warned), nor to the detection of errors in the input/output (the program expects the input files to be correct). 

## Installation
To run YOPyRa you need Python 2.7 or higher. It has been developed on a GNU/Linux distribution with Python 3.6.9 and tested on Windows 10 with Python 3.7.7. The python environment needs to have installed Pillow (to save the resulting JPG image) and ConfigParser (to parse the configuration file). To do this, simply execute the following command: 

Windows: 
```bash
py.exe -m pip install --upgrade Pillow
py.exe -m pip install --upgrade configparser
```

GNU/Linux: 
```bash
python -m pip install --upgrade Pillow
python -m pip install --upgrade configparser
```

## Usage
To use YOPyRa two files must be edited, which will be indicated as arguments by the command line. Optionally the name of an output .jpg can be specified. If the name of the resulting file is not specified, YOPyRa will save the output image to out.jpg. 

For example, a valid call to YOPyRa would be 
```bash
python yopyra.py config.ini scene.json output.jpg
```

The arguments can be stated in any order. YOPyRa only checks the file extension for processing; the .ini file will contain the configuration settings, the .json the scene definition and the .jpg will be the result of the rendering process. 

## Config file (.ini)

The .ini configuration file has the following sections: 

```bash
[IMAGE]
width = 800   
height = 400
output = out.jpg
quality = 98
sampling = 100
depth = 8

[GUI]
update_time = 2
progress_bar_length = 36
```
Image quality properties
- **width**: Width of the resulting image (in pixels)
- **height**: Height of the resulting image (in pixels)
- **output**: If not specified per command line, name of the resulting image
- **quality**: Image compression level from 0 to 100. 0 maximum compression. 100 minimum compression. Keep the value between 85 and 100. 
- **sampling**: Number of samples per pixel. 
- **depth**: Number of recursive calls per sample; trace depth. 

Properties related to the user interface: 
- **update_time**: Seconds that elapse between the update of the output jpg
- **progress_bar_length**: Width in characters of the render progress bars

## Scene File (.json)

Below is a fragment of a scene specification file in .json format. The colors are specified in RGB with 1 byte per channel. 

```json
[
{
   "type":   "camera",
   "origin": [0,1,2],
   "to":     [0.2,1.2,-1],   "up": [0,1,0],
   "fov":    42
},

{
   "type":   "texture", "subtype":"checker",
   "id":     "chess",
   "size":   6,
   "color1": [128,128,128],
   "color2": [20,20,20]
},

{
   "type":   "material", "subtype":"metal",
   "id":     "red",
   "albedo": [255, 64, 64],
   "fuzzy": 0.05
},

{
   "type":   "material", "subtype":"lambertian",
   "id":     "ground",
   "albedo": [128, 128, 128],
   "texture": "chess"
},

{
   "type":   "material", "subtype":"glass",
   "id":     "glass",
   "ior":    1.9
},

{
    "type": 	 "sphere",
    "material":  "gray",
    "radius":    2,
    "position":  [0, 2, -7]
  },
]
```

## Contributing
You can add functionality to the project, or comment on errors found in the source code. If you wish, you can also create your own fork under the GPL.In any case, you can contact the author to comment your thoughts. 


## Author and Acknowledgment
The code for this project was created by Carlos González Morcillo (Carlos.Gonzalez@uclm.es), for the Computer Graphics course at the University of Castilla-La Mancha. It is based on his previous YoPyRA project (a Whitted type ray tracer) made by the same author, which was included in the official distribution of the Python to C++ Shed Skin compiler, made by Mark Dufour.

The general scheme of YoPyRA is based on the work of Peter Shirley. 
[RayTracing by Peter Shirley](https://raytracing.github.io/books/RayTracingInOneWeekend.html)

## License

This project is distributed under the GPL v3 license. 
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)
