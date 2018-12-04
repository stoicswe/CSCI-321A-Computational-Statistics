import gym
import numpy as np

env = gym.make('FrozenLake-v0')

def generate_q():
    Q = np.zeros([env.observation_space.n,env.action_space.n])
    lr = .8
    y = .95
    num_episodes = 5000
    rList = []
    for i in range(num_episodes):
        s = env.reset()
        rAll = 0
        d = False
        j = 0
        while j < 99:
            j+=1
            a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
            s1,r,d,_ = env.step(a)
            Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
            rAll += r
            s = s1
            if d == True:
                break
        rList.append(rAll)
        print("Score over time: " +  str(sum(rList)/num_episodes))
        print("Final Q-Table Values")
        print(Q)
    return Q

def find_best_action(state, Q):
    return np.argmax(Q[state,:])

def fitPolicy(policy, num_episodes, random_policy = False):
    jList = []
    rList = []
    successful = []
    prob_states = {}
    i = 0
    while i < num_episodes:
        s = env.reset()
        rAll = 0
        d = False
        j = 0
        while j < 99:
            j+=1
            i+=1
            a = 0
            if random_policy:
                a = env.action_space.sample()
            else:
                a = policy[s]
            s1,r,d,_ = env.step(a)

            if 'count' in prob_states:
                prob_states['count'] += 1
            else:
                prob_states['count'] = 1

            if s1 in prob_states:
                prob_states[s1] += 1
            else:
                prob_states[s1] = 1
            rAll += r
            s = s1
            if d == True:
                if r > 0:
                    jList.append(j)
                    successful.append(1)
                break
        rList.append(rAll)
        if len(jList) == 0:
            jList.append(100)
        s1_prob_keys = prob_states.keys()
        for sk in s1_prob_keys:
            if sk != 'count':
                prob_states[sk] = prob_states[sk] / prob_states['count']
    return np.mean(rList), round(np.mean(jList)), sum(successful), prob_states

#Q = generate_q()
#policy = np.zeros(env.observation_space.n)
#for p in range(len(policy)):
#    policy[p] = find_best_action(p, Q)
#print(policy)
#reward, step = fitPolicy(best_policy)
episodes = 10000
print('-'*50)
print("BEST POLICY")
print('-'*50)
best_policy = [0, 3, 3, 3, 0, 0, 2, 0, 3, 1, 0, 0, 0, 2, 3, 0]
print(best_policy)
reward, step, successes, state_probs = fitPolicy(best_policy, episodes)
print("Average Reward")
print(reward)
print("Average Steps")
print(step)
print("Number successful (out of " + str(episodes) + ')')
print(str(round((successes/episodes)*100, 3)) + '%')
print("Probabilities of visiting each state")
print(state_probs)
print('-'*50)
print("RANDOM POLICY")
print('-'*50)
reward, step, successes, state_probs = fitPolicy(best_policy, episodes, True)
print("Average Reward")
print(reward)
print("Average Steps")
print(step)
print("Number successful (out of " + str(episodes) + ')')
print(str(round((successes/episodes)*100, 3)) + '%')
print("Probabilities of visiting each state")
print(state_probs)
