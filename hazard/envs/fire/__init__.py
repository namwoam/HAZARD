from hazard.envs.fire.fireagent_controller import FireAgentController
from hazard.envs.fire.fire_gym import FireEnv

from gym.envs.registration import register

register(
    id="fire-v0",
    entry_point="envs.fire.fire_gym:FireEnv"
)
