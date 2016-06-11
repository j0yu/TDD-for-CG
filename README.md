# TDD for CG
Basic setup for TDD in Maya and Nuke

This sets up a scenario where this git repository is the pipeline system's root
code repository, where all the artists pipeline tools and setup will be located.

Each folder within the repository are a module, either for a specific 
application like Nuke or Maya, or globally used routines, e.g. for file system.

## Instructions

1. Clone the repository to a foilder/location of your choice
2. Change the `pipelineSysDir` to the location where you cloned your repository
3. Copy the entire contents of `ps_nuke/menu.py` into your Nuke's `menu.py` e.g.
in your home folder's `.nuke/menu.py`
