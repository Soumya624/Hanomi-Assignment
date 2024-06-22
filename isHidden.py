import sys
import os

FREECADPATH = "C:/Users/ASUS/AppData/Local/Programs/FreeCAD 0.21/bin"
sys.path.append(FREECADPATH)

os.environ['QT_PLUGIN_PATH'] = "C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/plugins"
os.environ['PATH'] += os.pathsep + 'C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/bin'

import FreeCAD
import Part

def isHidden(iBox, jBox):
    iVolume = (iBox.XMax - iBox.XMin) * (iBox.YMax - iBox.YMin) * (iBox.ZMax - iBox.ZMin)
    
    intersected_XMin = max(iBox.XMin, jBox.XMin)
    intersected_XMax = min(iBox.XMax, jBox.XMax)
    intersected_YMin = max(iBox.YMin, jBox.YMin)
    intersected_YMax = min(iBox.YMax, jBox.YMax)
    intersected_ZMin = max(iBox.ZMin, jBox.ZMin)
    intersected_ZMax = min(iBox.ZMax, jBox.ZMax)

    intersectedVolume = 0
    
    if intersected_XMin < intersected_XMax and intersected_YMin < intersected_YMax and intersected_ZMin < intersected_ZMax:
        intersectedVolume = (intersected_XMax - intersected_XMin) * (intersected_YMax - intersected_YMin) * (intersected_ZMax - intersected_ZMin)
    
    if intersectedVolume >= 0.5 * iVolume:
        return 1
    else:
        return 0