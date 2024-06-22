import sys
import os

FREECADPATH = "C:/Users/ASUS/AppData/Local/Programs/FreeCAD 0.21/bin"
sys.path.append(FREECADPATH)

os.environ['QT_PLUGIN_PATH'] = "C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/plugins"
os.environ['PATH'] += os.pathsep + 'C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/bin'

import FreeCAD
import Part

from getCoordinates import getCoordinates
from isHidden import isHidden

# Reference: https://forum.freecad.org/viewtopic.php?t=82545 and https://wiki.freecad.org/Part_Feature
def classifyParts(d):
    partStatus = {}

    for i in d.Objects:
        if i.TypeId == 'Part::Feature':
            partName = i.Label
            # print('\n'+partName+":")
            
            iCoordinates, iBox = getCoordinates(i)
            # print('Bounding Box Coordinates: ',iCoordinates)

            totalVolume = i.Shape.Volume
            # print('Total Volume: ',totalVolume)

            hiddenStatus = 0

            for j in d.Objects:
                if j != i and j.TypeId == 'Part::Feature':
                    jCoordinates, jBox = getCoordinates(j)
                    hiddenStatus = isHidden(iBox, jBox)

            if hiddenStatus==1:
                partStatus[partName] = 'Hidden'
            else:
                partStatus[partName] = 'Visible'

    return partStatus