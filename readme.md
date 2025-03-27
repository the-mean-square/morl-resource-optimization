morl-resource-optimization 
---------------------------
- app: contains the codebase
    - data: contains 3 input matrices and the input schedule file
    - environment: contains the airport env class (inherited from gymnasium)
    - training: notebook to train the rl agent
***********
Environment Setup: 
 (using python 3.9)
- Since ray and certain dependencies are supported on python 3.12 or lesser
- Setup a venv using:
    If default python version, use --> python -m venv venv
    If specific version --> & "C:\Users\admin\AppData\Local\Programs\Python\Python39\python.exe" -m venv venv
- This should create the venv. 
    - --> venv\Scripts\Activate (To activate the venv -- make sure you run this in the right folder!)
    - Verify --> python --version (mine is 3.9 in the venv)
***********
Package Management:
-Use requirements.txt to install necessary packages
    --> pip install -r requirements.txt
    (I'm incrementally updating requirements file for now!)

- Once done: try this to see installed libraries
    --> pip list

********
Exit:
Once you are done working, deactivate the virtual environment by running:
    --> deactivate

********

Note: *Use .gitignore to exclude venv *

Inside your project root (morl-resource-optimization/), create a file named .gitignore and add the following:
    venv/
    __pycache__/
    *.pyc
    *.pyo


*****
Key notes:
- Where to Place __init__.py?
- Inside any directory that contains Python modules (.py files) and needs to be imported
- os.path.abspath("app/data/input_schedule.csv")
- Finds the correct path relative to your project directory. This makes the code portable and works across any system.
- test assertions need to be improved to make testing comprehensive 
****