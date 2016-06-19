## @package t_mainMenu
#
# Tests for the @p psMaya_mainMenu module
import unittest
import pymel.core as pm

from ps_maya import psMaya_mainMenu

class TestMenus(unittest.TestCase):
    mainMayaWindow = pm.ui.PyUI("MayaWindow")

    def setUp(self):
        self.myMenu = psMaya_mainMenu.pipelineMenu()
    
    ## Test for the pipeline system's menu
    def testRootMenuExists(self):
        self.assertIn(self.myMenu.rootMenu.shortName(), 
                      self.mainMayaWindow.getMenuArray())

    ## Test for the pipeline system's menu name
    def testRootMenuLabel(self):
        self.assertEqual(self.myMenu.rootMenu.getLabel(), 
                         "My Menu")
    
    def tearDown(self):
        self.myMenu.rootMenu.delete()