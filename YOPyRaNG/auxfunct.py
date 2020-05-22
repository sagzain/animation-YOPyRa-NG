import sys
import time
import configparser
import glob
from PIL import Image

OUTPUT = "out.jpg"
QUALITY = 95
WIDTH = 200
HEIGHT = 100
UPDATE_TIME = 2
PROGRESS_BAR_LENGTH = 50
SAMPLING = 3
DEPTH = 3
IMAGE_CANVAS = Image.new('RGB', (WIDTH, HEIGHT), color = 'gray')

INFINITE = 9999999999.9
EPSILON = 0.00000001

#Number of frames that are going to be generated for the animation.
FRAMES = 0

def ffmin(a,b):
    result = a if a <= b else b; return (result)

def degree_to_radians(degree):
    return ( degree * 3.1415926 / 180.0)

def loadconfig(cfgfile):
    global OUTPUT, QUALITY, WIDTH, HEIGHT, SAMPLING, DEPTH
    global UPDATE_TIME, PROGRESS_BAR_LENGTH
    global IMAGE_CANVAS
    global FRAMES

    if (cfgfile != ""):
        config = configparser.ConfigParser()
        config.read(cfgfile)

        OUTPUT = config.get('IMAGE', 'output')
        QUALITY = int(config.get('IMAGE', 'quality'))
        WIDTH = int(config.get('IMAGE', 'width'))
        HEIGHT = int(config.get('IMAGE', 'height'))
        SAMPLING = int(config.get('IMAGE', 'sampling'))
        DEPTH = int(config.get('IMAGE', 'depth'))
        UPDATE_TIME = float(config.get('GUI', 'update_time'))
        PROGRESS_BAR_LENGTH = int(config.get('GUI', 'progress_bar_length'))
        IMAGE_CANVAS = Image.new('RGB', (WIDTH, HEIGHT), color = 'gray')

        #Here we set the number of frames by getting it from the config file
        FRAMES = int(config.get('ANIMATION','frames'))
        if FRAMES == 0: FRAMES = 1 


def printProgressBar (frame, iteration, total):
    percent = ("{0:.2f}").format(100 * (iteration / float(total)))
    filledLength = int(PROGRESS_BAR_LENGTH * iteration // total)
    bar = '#' * filledLength + '-' * (PROGRESS_BAR_LENGTH - filledLength)

    sys.stdout.write("\rRendering frame %d/%d [%s] %s%%" % (frame, FRAMES, bar, percent))
    sys.stdout.flush()

def getImagePixels ():
    return IMAGE_CANVAS.load()

def saveImage (frame):
    if(len(str(frame)) == 1): number = '00'+str(frame)
    if(len(str(frame)) == 2): number = '0'+str(frame)
    if(len(str(frame)) == 3): number = str(frame)
    IMAGE_CANVAS.save('./output/img/'+OUTPUT.split('.')[0]+number+'.'+OUTPUT.split('.')[1], quality=QUALITY)

def showImage ():
    IMAGE_CANVAS.show()

def printRenderInfo():
    print ("\n=======================================================")
    print ("YOPyRa NG :: Yet One Python Raytracer (Next Generation)")
    print ("=======================================================")
    print ("Image Size: %dx%d" % (WIDTH, HEIGHT))
    print ("Sampling: %d" % SAMPLING)
    print ("Tracing depth: %d" % DEPTH)
    print ("Frames: %d" % FRAMES)
    print ("=======================================================")

def showArgInfo(config, scene, output):
    if (config != ""): print ("Configuration file: %s" % config);
    if (scene != ""): print ("Scene file: %s" % scene);
    if (output != ""): print ("Output file: %s" % output);

def showHelp(arg0):
    print ("\n=======================================================")
    print ("YOPyRa NG Help")
    print ("=======================================================")
    print ("You can specify up to 3 parameters: an .ini file with")
    print ("the raytracer settings, a .json file with the scene")
    print ("definition and the name of the resulting image .jpg in")
    print ("any order. Important: keep file extension in lowercase.")
    print ("Example: >> python %s config.ini scene.json out.jpg" % arg0)

def save_animation():
    print("Generating video...")

    inp = "./output/img/*.jpg"
    outp = "./output/gif/out.gif"

    img, *imgs = [Image.open(f) for f in sorted(glob.glob(inp))]
    img.save(fp=outp, format='GIF', append_images=imgs, save_all=True, duration=FRAMES, loop=0)
