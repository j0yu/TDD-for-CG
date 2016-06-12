es# TDD for CG
Basic setup for TDD in Maya and Nuke.

We will be testing and creating a custom menu in
Nuke and Maya.

This sets up a scenario where this git repository is the pipeline system's root
code repository, where all the artists pipeline tools and setup will be located.

The setup is not perfect, it is just for demonstration purposes.

Each folder within the repository are a module, either for a specific 
application like Nuke or Maya, or globally used routines, e.g. for file system.

## Instructions

1. Clone the repository to a foilder/location of your choice
2. Change the `pipelineSysDir` to the location where you cloned your repository
3. Copy the entire contents of `ps_nuke/menu.py` into your Nuke's `menu.py` e.g.
in your home folder's `.nuke/menu.py`

## Running and expectations

1. Run Nuke, you should be able to see a dialog at startup asking if you want to
run tests.
    
    - If you select `Yes`, then tests will be run to see if what we've 
        written/created satisfies the conditions that dictate we've successfully
        created a custom menu in Nuke called 'My Menu'

        To see the results, check the Nuke console.
    
    - If you select `No`, then tests will NOT be run so whatever is written will
        just be executed without being tested.

2. Either way, a menu called "My Menu" should be created to the right of the 
help menu, if not and you chosen `Yes`, then a test failure should appear in the
Nuke's console
