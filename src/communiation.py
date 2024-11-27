import pandas as pd
from agent import Agent
from appraisal import Appraisal
from actions import actions
from ms import MS, MSs


# agents_count = int(input("Enter agents count: "))
agents_count = 6
stop_flag = False


fr = 'friendship'
fe = 'feud'
fo = 'following'
l = 'leadership'
r = 'rivalry'
s = 'self'

relation_matrix = [[s, fr, fe, fe, fo, fo],
                   [fr, s, fe, fe, fo, fo],
                   [fe, fe, s, fr, fo, fo],
                   [fe, fe, fr, s, fo, fo],
                   [l, l, l, l, l, s, r],
                   [l, l, l, l, l, r, s]]

agents = []
agents = [Agent(id) for id in range(agents_count)]
for i in range(agents_count):
    agents[i].set_ids(set(range(agents_count)))
    for j in range(agents_count):
        if j != i:
            agents[i].set_feeling(j, MSs[relation_matrix[i][j]].feeling)


print((100 * Appraisal(1, 2, 3) - Appraisal(1, 2, 3)).vector_)
df = pd.DataFrame()

with open('./logs.csv', 'w+') as logf:
    logf.write(
        'iteration|from_id|to_id|action_name|action_author_dom|action_author_val|action_author_tr|action_target_dom|action_target_val|action_target_tr|author_dom|author_val|author_tr|target_dom|target_val|target_tr\n')
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
                    author_a = \
                        agents[agent_id].appraisals[receiver_id].vector_.tolist()
                    target_a = \
                        agents[receiver_id].appraisals[agent_id].vector_.tolist()
                    act_a = actions[action_name]["author"]
                    act_t = actions[action_name]["target"]
                    logf.write(
                        f'{it}|{agent_id}|{receiver_id}|{action_name}|{act_a[0]}|{act_a[1]}|{act_a[2]}|{act_t[0]}|{act_t[1]}|{act_t[2]}|{author_a[0]}|{author_a[1]}|{author_a[2]}|{target_a[0]}|{target_a[1]}|{target_a[2]}\n')
        total_iterations += iterations
