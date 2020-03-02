import numpy as np
from .multiwalker import env as _env
import time

n_walkers = 3

env = _env(n_walkers=n_walkers)
env.reset()

done = False
total_reward = 0

# start = time.time()
while not done:
    # game should run at 15 FPS when rendering
    env.render()
    time.sleep(0.04)

    action_list = np.array([env.action_spaces[i].sample() for i in range(env.num_agents)])

    for a in action_list:
        r, d, i = env.last_cycle()
        observation = env.step(a)
        if d:
            done = True
        total_reward += r
    print("step reward", sum(total_reward))
    if done:
        print("Total reward", total_reward, "done", done)

# end = time.time()
# print("FPS = ", 100/(end-start))
env.render()
time.sleep(2)
env.close()

#  # for random trials
#  num_trials = 1000
#  total_reward = [0.0]*num_trials
#  for i in range(num_trials):
#      env.reset()
#      done = False
#      while not done:
#          action_list = np.array([env.action_spaces[i].sample() for i in range(env.num_agents)])
#          action_dict = dict(zip(env.agents, action_list))
#
#          observation, rewards, done_dict, info = env.step(action_dict)
#          done = any(list(done_dict.values()))
#          total_reward[i] += sum(rewards.values())
#          # print("step reward = ", sum(rewards.values()))
#          if done:
#              print("Total reward of iter ", i, total_reward[i], done)
#
#  print("Average over all trials = ", sum(total_reward)/num_trials)
#  env.close()
