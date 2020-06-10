import gym
import ptan
import numpy as np
import torch.nn as nn

env = gym.make("CartPole-v0")
net = nn.Sequential(
    nn.Linear(env.observation_space.shape[0], 256),
    nn.ReLU(),
    nn.Linear(256, env.action_space.n)
)

action_selector = ptan.actions.EpsilonGreedyActionSelector(epsilon=0.1)
agent = ptan.agent.DQNAgent(net, action_selector)

obs = np.array([env.reset()], dtype=np.float32)
print(agent(obs))

exp_source = ptan.experience.ExperienceSourceFirstLast(env, agent, gamma=0.99, steps_count=1)
it = iter(exp_source)

next(it)
