import os
import nuke
import unittest

import psNuke_mainMenu


def runUnitTests(exitAfterwards=False):
    # Unit tests, before initialisation
    print("\n\n\n\n\n\n\n\n{0:#^70}\n{1:^70}\n"
          "{0:#^70}\n\n".format("","UNIT TESTS"))
    
    unittest.main(module="ps_nuke.test.t_mainMenu",
                  verbosity=2, exit=exitAfterwards)

def initialize():
    print("\n\n\n\n\n\n\n\n{0:#^70}\n{1:^70}\n"
          "{0:#^70}\n\n".format(""," INITIALIZE"))
    psNuke_mainMenu.pipelineMenu()