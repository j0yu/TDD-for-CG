## @package psNuke_mainMenu 
# 
# Module responsible for the pipeline system's menu within Nuke
import nuke

## Class to handle and manage the pipeline system's menu within Nuke
class pipelineMenu:
    def __init__(self):
        mainNukeMenu = nuke.menu('Nuke')
        self.rootMenu = mainNukeMenu.addMenu('My Menu') 