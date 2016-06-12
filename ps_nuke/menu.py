# Insert the following into Nuke's menu.py, e.g. the one on your server/global
# one all artists refer to. For personal testing, your home folder's 
# .nuke/menu.py would be sufficient

# ------------------------- BEGIN ----------------------------------------------
# State the directory to the root folder of the pipeline system code repository
# This will be error checked
pipelineSysDir = "D:/PipelineSystem/"
if os.path.isdir(pipelineSysDir):
    os.sys.path.append("D:/PipelineSystem/")
else:
    pathNotExistErrMsg = "Pipeline System folder, {}, does not exist or " \
                         "currently unavailable".format(pipelineSysDir)
    nuke.message(pathNotExistErrMsg)
    raise OSError(pathNotExistErrMsg)

# Next import the nuke modules from the pipeline system, run tests if chosen
import ps_nuke
if nuke.ask("Run tests?"):
    ps_nuke.runUnitTests()

# Then initialize the pipeline system for Nuke
ps_nuke.initialize()
# --------------------------- END ----------------------------------------------
