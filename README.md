# TDD for CG
Basic setup for [Test Driven Development](https://www.google.co.uk/search?q=TDD) 
in Maya and Nuke.

We will be testing and creating a custom menu in Nuke and Maya.

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
3. Copy the entire contents of `ps_maya/userSetup.py` into your Maya scripts 
folder's `userSetup.py` e.g. in My Document's `maya/scripts/userSetup.py`

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
help menu.
    
    If not and you chosen `Yes`, then a test failure should appear in the
Nuke's console

3. Run Maya, you should be able to see a dialog at startup asking if you want to
run tests.
    
    - If you select `Yes`, then tests will be run to see if what we've 
        written/created satisfies the conditions that dictate we've successfully
        created a custom menu in Maya called 'My Menu'

        To see the results, check the Maya output window/console.
    
    - If you select `No`, then tests will NOT be run so whatever is written will
        just be executed without being tested.

2. Either way, a menu called "My Menu" should be created to the right of the 
help menu.
    
    If not and you chosen `Yes`, then a test failure should appear in the
Maya's output window/console

# More information
See screenshots in the doc folder for examples of the setup in action.

See the [Wiki (In Progress)](https://github.com/j0yu/TDD-for-CG/wiki) for more 
information