import gymnasium as gym

if __name__ == "__main__":
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    env = gym.wrappers.HumanRendering(env)
    
    total_reward = 0.0
    total_steps = 0
    obs, _ = env.reset()
    
    while True:
        action = env.action_space.sample()
        obs, reward, is_done, _, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if is_done:
            break
            
    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
    env.close()
