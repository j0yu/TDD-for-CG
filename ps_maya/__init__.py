## @package ps_maya
#
# Main Maya package containing procedures and functions exclusive to Maya only
import os
import unittest

import pymel.core as pm

import psMaya_mainMenu


## Procedure to run the unit tests for Maya functions
#
# 1. Error test for parameters
# 2. Run each unit test for maya, extend the list per every new test module
#
# @param[in] exitAfterwards @p bool of whether to exit Maya after the unit tests
# are run, defult to @p False as we rarely want to exit Maya immediately after 
# opening it
def runUnitTests(exitAfterwards=False):
    print "\n\n\n\n\n\n\n\n{0:#^70}\n{1:^70}\n{2:^70}\n"\
          "{0:#^70}\n\n".format("","UNIT TESTS","See results in output window")

    # 1. Error test for parameters
    if type(exitAfterwards) != bool:
        print "exitAfterwards parameter passed in is not a boolean, "\
              "trying to convert it to boolean"
        exitAfterwards = bool(exitAfterwards) 
    
    # 2. Run each unit test for maya
    for testModule in ["t_mainMenu"]:
        unittest.main(module="ps_maya.test."+str(testModule),
                      verbosity=2, exit=exitAfterwards)

## Procedure to initialise and setup Maya for our pipeline system
#
# 1. Setup the pipeline menu
def initialize():
    print "\n\n\n\n\n\n\n\n{0:#^70}\n{1:^70}\n"\
          "{0:#^70}\n\n".format("","INITIALIZE")

    # 1. Setup the pipeline menu
    psMaya_mainMenu.pipelineMenu()