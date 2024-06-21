# Installation Guide
Installation guide for a ***Python*** script that identifies the ***Coordinates*** and the ***Visibility*** of a specific part within an assembly.

## Environment Setup:
Ensure you have ***FreeCAD*** and ***Miniconda*** or ***Anaconda*** installed before running the commands below:

```
conda init
conda create -n hanomiAssignment python=3.8.10
conda activate hanomiAssignment
conda install -c conda-forge freecad
conda install -c conda-forge pythonocc-core
conda install -c conda-forge pyopengl
conda install -c conda-forge pillow
conda install -c conda-forge libgcc
```

## Script Execution:
Ensure you have updated ***FREECADPATH***, ***os.environ['QT_PLUGIN_PATH']*** & ***os.environ['PATH']*** from your code before running the commands below:

```
python script.py --filepath_assembly
```