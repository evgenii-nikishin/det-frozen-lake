# det-frozen-lake

In a usual version of the FrozenLake environment, after executing action "Right" you go up, down or right with equal probabilities (after action "Up" you go either left, up or right, etc).

This repository provides a code that makes the environment deterministic.

Works for both 4x4 and 8x8 versions of the environment.

## Usage:
```
import gym
from det_utils import make_det

env = gym.make("FrozenLake-v0")   # or env = gym.make("FrozenLake8x8-v0")
env = make_det(env)
```
