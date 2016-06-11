import nuke

class pipelineMenu:
    def __init__(self):
        mainNukeMenu = nuke.menu('Nuke')
        self.rootMenu = mainNukeMenu.addMenu('My Menu') 