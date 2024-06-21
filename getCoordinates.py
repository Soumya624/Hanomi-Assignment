import sys
import os

FREECADPATH = "C:/Users/ASUS/AppData/Local/Programs/FreeCAD 0.21/bin"
sys.path.append(FREECADPATH)

os.environ['QT_PLUGIN_PATH'] = "C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/plugins"
os.environ['PATH'] += os.pathsep + 'C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/bin'

import FreeCAD

# Reference: https://wiki.freecad.org/Base_API and http://raytracerchallenge.com/bonus/bounding-boxes.html
def getCoordinates(x):
    boundBox = x.Shape.BoundBox

    xmin = boundBox.XMin
    xmax = boundBox.XMax

    ymin = boundBox.YMin
    ymax = boundBox.YMax

    zmin = boundBox.ZMin
    zmax = boundBox.ZMax

    xc = 0
    yc = 0
    zc = 0

    cuboidCoordinates = {
        'min': (xmin-xc, ymin-yc, zmin-zc),
        'max': (xmax-xc, ymax-yc, zmax-zc)
    }

    return cuboidCoordinates