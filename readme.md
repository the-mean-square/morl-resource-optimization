morl-resource-optimization 
---------------------------
- app: contains the codebase
    -data: contains 3 input matrices and the input schedule file
    environment: contains the airport env class (inherited from gymnasium)
    training: notebook to train the rl agent

Environment Setup: 
 (using python 3.9)
- Since ray and certain dependencies are supported on python 3.12 or lesser
- Setup a venv using:
    If default python version, use --> python -m venv venv
    If specific version --> & "C:\Users\admin\AppData\Local\Programs\Python\Python39\python.exe" -m venv venv
- This should create the venv. 
    - Now run: venv\Scripts\Activate
    - Verify python --version (mine is 3.9 in the venv)

-Use requirements.txt to install necessary packages
    run --> pip install -r requirements.txt
    (I'm incrementally updating requirements file for now!)

- Once done: try pip list to see installed libraries

********

Once you are done working, deactivate the virtual environment by running:

run --> deactivate

********