from gym.envs.registration import register
from hazard.envs.wind.wind_gym import WindEnv

register(id="wind-v0", entry_point="envs.wind.wind_gym:WindEnv")
