## @package psMaya_mainMenu 
# 
# Module responsible for the pipeline system's menu within Maya
import pymel.core as pm

## Class to handle and manage the pipeline system's menu within Maya
class pipelineMenu:

    def __init__(self):      
        # Name Autodesk gives to main Maya window  
        mainMayaWindow = pm.ui.PyUI("MayaWindow")

        # Check that it is actually created (just incase this is run before it)
        if type(mainMayaWindow) == pm.uitypes.Window:
            # Our menu 
            self.rootMenu = pm.menu("myMenu", parent=mainMayaWindow)
            self.rootMenu.setLabel("My Menu")
        else:
            pm.warning("WARNING! Maya main window is not initialized yet!")
            pm.warning("         Pipeline menu is not created")
