import gymnasium as gym
import random

class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env: gym.Env, epsilon: float = 0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon
        
    def action(self, action: gym.core.WrapperActType) -> gym.core.WrapperActType:
        if random.random() < self.epsilon:
            action = self.env.action_space.sample()
            print(f"Random action {action}")
            return action
        return action
        
if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1"))
    obs, _ = env.reset()
    total_reward = 0.0
    while True:
        obs, reward, is_done, _, _ = env.step(0)
        total_reward += reward
        if is_done:
            break
        
    print(f"Total reward got: {total_reward:.2f}")
