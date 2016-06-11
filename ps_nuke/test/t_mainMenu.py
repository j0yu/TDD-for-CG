import unittest
import nuke

from ps_nuke import psNuke_mainMenu

class TestMenus(unittest.TestCase):
    mainNukeMenu = nuke.menu('Nuke')

    def setUp(self):
        psNuke_mainMenu.pipelineMenu()
    
    def testMissingMenu(self):
        self.assertEqual(type(self.mainNukeMenu.findItem('My Menu')), 
                         nuke.MenuItem)  # Menu item object returned
    
    def tearDown(self):
        nuke.menu('Nuke').removeItem('My Menu')