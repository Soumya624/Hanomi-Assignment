# Prepared By: Soumya Tarafder

import sys
import os

FREECADPATH = "C:/Users/ASUS/AppData/Local/Programs/FreeCAD 0.21/bin"
sys.path.append(FREECADPATH)

os.environ['QT_PLUGIN_PATH'] = "C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/plugins"
os.environ['PATH'] += os.pathsep + 'C:/Users/ASUS/miniconda3/envs/hanomiAssignment/Library/bin'

import FreeCAD
import Part

from loadSTP import loadSTP
from classifyParts import classifyParts

# Reference: https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
if len(sys.argv) != 2:
    print("Incorrect Instruction")
    sys.exit(1)

else:
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Filepath Doesn't Exist")
        sys.exit(1)
    
    doc = loadSTP(filepath)
    partStatus = classifyParts(doc)
    print(partStatus)