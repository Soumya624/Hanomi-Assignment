import sys
import os

FREECADPATH = "C:/Users/ASUS/AppData/Local/Programs/FreeCAD 0.21/bin"
sys.path.append(FREECADPATH)

os.environ['QT_PLUGIN_PATH'] = "C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/plugins"
os.environ['PATH'] += os.pathsep + 'C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/bin'

import FreeCAD
import Import

# Reference: https://cultured-geometry-986.notion.site/installation-and-usage-steps-for-freecad-and-occ-83ad60ee068849d3bdfaa0a31670e138 and https://wiki.freecad.org/FreeCAD_API
def loadSTP(filename):
    # print('Started Loading the File')

    doc = FreeCAD.newDocument('test')
    Import.insert(filename, doc.Name)
    doc.recompute()
    
    # print('Ended Loading the File')
    return doc