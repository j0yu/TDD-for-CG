## @package t_mainMenu
#
# Tests for the @p psMaya_mainMenu module
import unittest
import pymel.core as pm

from ps_maya import psMaya_mainMenu

class TestMenus(unittest.TestCase):
    # mainMayaMenu = maya.menu('Maya')

    def setUp(self):
        psMaya_mainMenu.pipelineMenu()
    
    ## Test for the pipeline system's menu
    def testRootMenu(self):
        raise NotImplementedError("Implement test routine for Maya menu")
        # self.assertEqual(type(self.mainMayaMenu.findItem('My Menu')), 
        #                  maya.MenuItem)  # Copied from Nuke
    
    def tearDown(self):
        raise NotImplementedError("Implement tear down routine for Maya menu")
        # maya.menu('Maya').removeItem('My Menu')  # Copied from Nuke