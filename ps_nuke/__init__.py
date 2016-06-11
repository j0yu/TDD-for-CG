## @package ps_nuke
#
# Main Nuke package containing procedures and functions exclusive to Nuke only
import os
import unittest

import nuke

import psNuke_mainMenu


## Procedure to run the unit tests for Nuke functions
#
# 1. Error test for parameters
# 2. Run each unit test for nuke, extend the list per every new test module
#
# @param[in] exitAfterwards @p bool of whether to exit Nuke after the unit tests
# are run, defult to @p False as we rarely want to exit Nuke immediately after 
# opening it
def runUnitTests(exitAfterwards=False):
    print "\n\n\n\n\n\n\n\n{0:#^70}\n{1:^70}\n"\
          "{0:#^70}\n\n".format("","UNIT TESTS")

    # 1. Error test for parameters
    if type(exitAfterwards) != bool:
        print "exitAfterwards parameter passed in is not a boolean, "\
              "trying to convert it to boolean"
        exitAfterwards = bool(exitAfterwards) 
    
    # 2. Run each unit test for nuke
    for testModule in ["t_mainMenu"]:
        unittest.main(module="ps_nuke.test."+str(testModule),
                      verbosity=2, exit=exitAfterwards)

## Procedure to initialise and setup Nuke for our pipeline system
#
# 1. Setup the pipeline menu
def initialize():
    print "\n\n\n\n\n\n\n\n{0:#^70}\n{1:^70}\n"\
          "{0:#^70}\n\n".format(""," INITIALIZE")

    # 1. Setup the pipeline menu
    psNuke_mainMenu.pipelineMenu()