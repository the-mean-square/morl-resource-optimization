import sys
import os
sys.path.append("../../")
from app.environment.allocate import AirportEnv

# test 1: parse input_schedule file
input_schedule_file_path = "C:/Users/admin/Desktop/github/morl-gate-optimization/morl-resource-optimization/app/data/input_schedule.csv"
schedule_df = AirportEnv.parse_input_schedule(input_schedule_file_path)
print(schedule_df)

#test 2: 