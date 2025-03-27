""" Airport class: Custom environment inheriting from gym.Env
- The base class for environments in the gymnasium (formerly open AI Gym) framework """

import pandas as pd
import numpy as np
import gym 

class AirportEnv(gym.Env):
    @staticmethod
    def parse_input_schedule(file_location):
        """ function to parse input schedule and return the schedule dataframe """
        schedule_df = pd.read_csv(file_location)
        return schedule_df