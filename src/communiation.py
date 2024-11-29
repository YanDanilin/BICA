import pandas as pd
import numpy as np
from agent import Agent
from appraisal import Appraisal
from actions import actions3d as actions
from ms import MS, MSs, feelings, check_moral_schema


# agents_count = int(input("Enter agents count: "))
agents_count = 6
stop_flag = False

log_columns = 'iteration|from_id|to_id|action_name|action_author_dom|action_author_val|action_author_tr|action_target_dom|action_target_val|action_target_tr|author_dom|author_val|author_tr|target_dom|target_val|target_tr\n'

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

init_feelings = ['friendly', 'friendly',
                 'hostility', 'hostility', 'leader', 'leader']

agents = []
agents = [Agent(id) for id in range(agents_count)]
for i in range(agents_count):
    agents[i].set_ids(set(range(agents_count)))
    for j in range(agents_count):
        if i != j:
            agents[i].set_feeling(j, feelings[init_feelings[j]])

with open('./logs.csv', 'w+') as logf:
    logf.write()
    total_iterations = 0
    while True:
        iterations = int(input("Enter iterations to communicate: "))
        if iterations == 0:
            break
        for it in range(total_iterations + 1, total_iterations + iterations + 1):
            log_row = [str(it)]
            for agent_id in range(agents_count):
                log_row.append(str(agent_id))
                actions_to = agents[agent_id].send(actions)
                for receiver_id, action_name in actions_to.items():
                    log_row.append(str(receiver_id))
                    agents[receiver_id].receive(action_name, agent_id, actions)
                    # проверка на срабатывание МС
                    if iterations % 10 == 0 and \
                            agents[agent_id].appraisal_near_feeling(receiver_id) and agents[receiver_id].appraisal_near_feeling(agent_id):
                        result = check_moral_schema(
                            agents[agent_id], agents[receiver_id])
                        if result != -1:
                            if result[0] == 'change':
                                agents[result[1]].feelings[result[2]] = result[3]
                            elif result[0] == 'ms':
                                for id in range(agents_count):
                                    agents[id].moral_schemas[result[1]][result[2]] = result[3]
                                    agents[id].moral_schemas[result[2]][result[1]] = result[3]
                    author_a = \
                        agents[agent_id].appraisals[receiver_id].vector_.tolist()
                    target_a = \
                        agents[receiver_id].appraisals[agent_id].vector_.tolist()
                    act_a = actions[action_name]["author"]
                    act_t = actions[action_name]["target"]
                    log_row += list(map(str,
                                    agents[agent_id].appraisals[receiver_id].vector_.tolist()))
                    log_row += list(map(str,
                                    agents[receiver_id].appraisals[agent_id].vector_.tolist()))
                    log_row += list(map(str, actions[action_name]["author"]))
                    log_row += list(map(str, actions[action_name]["target"]))
                    logf.write('|'.join(log_row) + '\n')
        total_iterations += iterations
