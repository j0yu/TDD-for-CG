# Insert the following into Maya's userSetup.py, e.g. the one on your #
# server/global one all artists refer to. For personal testing, your maya 
# folder's scripts/userSetup.py would be sufficient

# ------------------------- BEGIN ----------------------------------------------
import pymel.core as pm

# State the directory to the root folder of the pipeline system code repository
# This will be error checked
pipelineSysDir = "D:/PipelineSystem/"
if pm.os.path.isdir(pipelineSysDir):
    pm.os.sys.path.append("D:/PipelineSystem/")
else:
    pathNotExistErrMsg = "Pipeline System folder, {}, does not exist or " \
                         "currently unavailable".format(pipelineSysDir)
    pm.confirmDialog(message=pathNotExistErrMsg)
    raise OSError(pathNotExistErrMsg)

# Next import the Maya modules from the pipeline system, run tests if chosen
import ps_maya
buttonFlags = {
    title='Run tests', 
    message: "Run tests?", 
    button=['Yes','No'], 
    defaultButton='Yes', 
    cancelButton='No', 
    dismissString='No'
}
if pm.confirmDialog(**buttonFlags) == "Yes":
    ps_maya.runUnitTests()

# Then initialize the pipeline system for Nuke
ps_maya.initialize()
# ------------------------- END ----------------------------------------------
