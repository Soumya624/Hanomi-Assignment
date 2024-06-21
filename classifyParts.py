import sys
import os

FREECADPATH = "C:/Users/ASUS/AppData/Local/Programs/FreeCAD 0.21/bin"
sys.path.append(FREECADPATH)

os.environ['QT_PLUGIN_PATH'] = "C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/plugins"
os.environ['PATH'] += os.pathsep + 'C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/bin'

import FreeCAD
import Part

from getBoundingBox import getBoundingBox

# Reference: https://forum.freecad.org/viewtopic.php?t=82545
def classifyParts(d):
    partStatus = {}

    for i in d.Objects:
        if i.TypeId == 'Part::Feature':
            partName = i.Label
            print(partName)
            boundingBox = getBoundingBox(i)

            totalVolume = i.Shape.Volume
            hiddenVolume = 0

            for j in d.Objects:
                if j != i and j.TypeId == 'Part::Feature':
                    common = i.Shape.common(j.Shape)
                    hiddenVolume += common.Volume

            hiddenRatio = hiddenVolume / totalVolume
            if hiddenRatio > 0.5:
                partStatus[partName] = 'Hidden'
            else:
                partStatus[partName] = 'Visible'

    return partStatus