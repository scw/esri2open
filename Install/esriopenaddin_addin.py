import os
import sys
import webbrowser
from threading import Thread

import arcpy
import pythonaddins

# enable local imports
local_path = os.path.dirname(__file__)
sys.path.insert(0, local_path)

# get the path for our TBX
toolbox = os.path.join(local_path, "esri2open.tbx")

class OpenStandard(object):
    """Implementation for esriopen_standard.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, 'esri2open')

class OpenMerge(object):
    """Implementation for esriopen_merge.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, 'ESRI2OpenMerge')

class OpenMultiple(object):
    """Implementation for esriopen_multiple.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, 'ESRI2OpenMulti')
