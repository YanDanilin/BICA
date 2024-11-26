from agent import Agent
from appraisal import Appraisal
from actions import actions


agents_count = int(input("Enter agents count: "))
stop_flag = False
agents = []
agents = [Agent(id) for id in range(agents_count)]
for i in range(agents_count):
    agents[i].set_ids(set(range(agents_count)))

with open('./logs.csv', 'w+') as logf:
    logf.write('iteration,from_id,to_id,action')
    total_iterations = 0
    while True:
        iterations = int(input("Enter iterations to communicate: "))
        if iterations == 0:
            break
        for it in range(total_iterations + 1, total_iterations + iterations + 1):
            for agent_id in range(agents_count):
                actions_to = agents[agent_id].send(actions)
                for receiver_id, action_name in actions_to.items():
                    agents[receiver_id].receive(action_name, agent_id, actions)
                    logf.write(f'{it},{agent_id},{receiver_id},{action_name}\n')
        total_iterations += iterations
