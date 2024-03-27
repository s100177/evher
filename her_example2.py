import gym
from stable_baselines.common.bit_flipping_env import BitFlippingEnv
import os
from stable_baselines import HER, SAC, DDPG, TD3
import logging
import argparse
from stable_baselines.her import GoalSelectionStrategy, HERGoalEnvWrapper
print(list(list(GoalSelectionStrategy)))
# 创建一个日志文件

parser = argparse.ArgumentParser(description='HER Example')
parser.add_argument('--sample_method', type=str, default='random', choices=['final','episode','random','future','evher'], help='Sampling method (random or her)')
args = parser.parse_args()

log_dir = "./logs/"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "training_log.txt")

# 设置日志格式
logging.basicConfig(level=logging.INFO, filename=log_file, filemode="w", format="%(asctime)s - %(message)s")
method = ['final','episode','random','future','evher']
# method = ['future']
# 创建环境
N_BITS = 10  # 实验的env bit 长度为5bit
model_class = SAC
env = BitFlippingEnv(n_bits=N_BITS, continuous=model_class in [DDPG, SAC, TD3], max_steps=20)

# Create 4 artificial transitions per real transition
n_sampled_goal = 4

# SAC hyperparams:args.sample_method

model = HER('MlpPolicy', env, SAC, n_sampled_goal=n_sampled_goal,
            goal_selection_strategy=args.sample_method,
            verbose=1, buffer_size=int(1e6),
            learning_rate=1e-3,
            gamma=0.95, batch_size=256,
            policy_kwargs=dict(layers=[256, 256, 256]))

result = model.learn(int(12000.0), log_interval=10)
model.save('her_sac_highway')

# Load saved model
model = HER.load('her_sac_highway', env=env)

obs = env.reset()

# Evaluate the agent
episode_reward = 0
for _ in range(100):
  action, _ = model.predict(obs)
  obs, reward, done, info = env.step(action)
  env.render()
  episode_reward += reward
  if done or info.get('is_success', False):
    print("Reward:", episode_reward, "Success?", info.get('is_success', False))
    episode_reward = 0.0
    obs = env.reset()