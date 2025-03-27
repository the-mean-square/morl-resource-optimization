import pytest
import os  # For handling file paths dynamically
from app.environment.allocate import AirportEnv

# ---- FIXTURE ----
# A pytest fixture to create and return an AirportEnv instance.
# This ensures a fresh instance is available for each test that needs it.
@pytest.fixture
def airport_env():
    return AirportEnv()

# ---- TESTS ----
def test_airport_env_instance(airport_env):
    """Verify that an AirportEnv instance is created successfully."""
    assert airport_env is not None

def test_parse_input_schedule(airport_env):
    """Check if parse_input_schedule processes the input file correctly."""
    input_schedule_file_path = os.path.abspath("app/data/input_schedule.csv")  # Get absolute path

    # Ensure the test file exists before proceeding
    assert os.path.exists(input_schedule_file_path), f"Test file missing: {input_schedule_file_path}"

    schedule_df = airport_env.parse_input_schedule(input_schedule_file_path)

    # Validate output
    assert schedule_df is not None  # Ensure function returns something
    assert not schedule_df.empty, "Parsed schedule is unexpectedly empty!"
