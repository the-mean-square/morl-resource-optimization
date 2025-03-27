test_parsing.py summary: 

- import os -->Helps work with file paths dynamically.
- @pytest.fixture --> Creates a reusable test setup.
- test_airport_env_instance --> Ensures AirportEnv can be created.
- assert os.path.exists(...)--> Ensures the test file exists before running.
- assert not schedule_df.empty -->Ensures the function returns real data.

****