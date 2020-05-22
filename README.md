# animation-YOPyRa-NG
YOPyRa-NG: Support for simple animations with changing object positions - Computer Graphics - UCLM

## Author and Acknowledgment
The YOPyRa-NG code for this project was created by Carlos González Morcillo (Carlos.Gonzalez@uclm.es) for the Computer Graphics course at the University of Castilla-La Mancha.

I'm extending the functionality of YOPyRa-NG to be able to generate simple animations.

For more information about the YOPyRa-NG code, consult the [readme](./YOPyRaNG/README.md) inside its folder.

## How to use the animation functionality
If you check the [config](./YOPyRaNG/config.ini) file you are now able to indicate the number of frames that you want to generate for the animation.

In order to give an object animation we have to add the following structure:
```json
                {
                    "type": 		"sphere",
                    "material":	"red",
                    "radius": 	1,
                    "position": [2.5, 1, -4],
                    "animation": {
                                    "translate":[0, 2, -7],
                                    "rotate": 100,
                                    "scale": 2
                                }
                    },
```
Any one of the three options inside animation can be ommited, but if animation key is on the json, at least one has to be inside (translate/rotate/scale).