import pandas as pd
import numpy as np
import random
from agent import Agent
from appraisal import Appraisal
from actions import actions2d as actions
from ms import MS, MSs2d, check_moral_schema
from ms import feelings2d as feelings

# agents_count = int(input("Enter agents count: "))
agents_count = 6
stop_flag = False

log_columns = 'iteration|from_id|to_id|action_name|action_author_dom|action_author_val|action_target_dom|action_target_val|author_dom|author_val|target_dom|target_val\n'

init_feelings = ['friendly', 'friendly',
                 'hostility', 'hostility', 'leader', 'leader']

agents = []
agents = [Agent(id, r=0.1) for id in range(agents_count)]
for i in range(agents_count):
    agents[i].set_ids(set(range(agents_count)))
    for j in range(agents_count):
        if i != j:
            agents[i].set_feeling(j, feelings[init_feelings[i]])


with open('./logs.csv', 'w+') as logf:
    logf.write(log_columns)
    total_iterations = 0
    while True:
        iterations = int(input("Enter iterations to communicate: "))
        if iterations == 0:
            break
        for it in range(total_iterations + 1, total_iterations + iterations + 1):
            for agent_id in range(agents_count):
                actions_to = agents[agent_id].send(actions)
                for receiver_id, action_name in actions_to.items():
                    log_row = [str(it), str(agent_id), str(
                        receiver_id), action_name]
                    agents[receiver_id].receive(action_name, agent_id, actions)
                    # проверка на срабатывание МС
                    if (agents[agent_id].appraisal_near_feeling(receiver_id) or agents[receiver_id].appraisal_near_feeling(agent_id)) and \
                            agents[agent_id].moral_schemas[agent_id][receiver_id] == 'self':
                        result = check_moral_schema(
                            agents[agent_id], agents[receiver_id])
                        if result != -1:
                            if result[0] == 'change':
                                agents[result[1]].feelings[result[2]] = result[3]
                            elif result[0] == 'ms':
                                for id in range(agents_count):
                                    agents[id].moral_schemas[result[1]
                                                             ][result[2]] = result[3]
                                    agents[id].moral_schemas[result[2]
                                                             ][result[1]] = result[3]
                        else:
                            print(
                                f'Moral scheme not found yet.\nit:{it}\nagent1: {agent_id}\nagent2: {receiver_id}')
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
                    logf.write('|'.join(log_row))
                    logf.write('\n')
            if it % 300 == 0:
                for id1 in range(agents_count):
                    for id2 in range(id1 + 1, agents_count):
                        if id1 != id2 and agents[id1].moral_schemas[id1][id2] == "self":
                            if MS.first_nearer_than_second(agents[id1].feelings[id2], agents[id1].appraisals[id2], agents[id2].feelings[id1], agents[id2].appraisals[id1]):
                                agents[id2].set_feeling(id1, random.sample(
                                    list(feelings.values()), 1)[0])
                                print(f'Чувство у {id2} к {id1} поменяно')
                            else:
                                agents[id1].set_feeling(id2, random.sample(
                                    list(feelings.values()), 1)[0])
                                print(f'Чувство у {id1} к {id2} поменяно')
                for id, row in agents[0].moral_schemas.items():
                    print(id, row)
        total_iterations += iterations


with open('./res_feelings.csv', 'w+') as res_file:
    res_file.write(
        'from_id|to_id|app1|app2|app3|feeling1|feeling2|feeling3\n')
    for agent_id in range(agents_count):
        for to_id in range(agents_count):
            if agent_id != to_id:
                appraisal_vec = agents[agent_id].appraisals[to_id].vector_
                feelings_vec = agents[agent_id].feelings[to_id].vector_
                res_file.write(
                    f'{agent_id}|{to_id}|{appraisal_vec[0]}|{appraisal_vec[1]}|')
                res_file.write(
                    f'{feelings_vec[0]}|{feelings_vec[1]}|{agents[agent_id].moral_schemas[agent_id][to_id]}|{agents[agent_id].moral_schemas[to_id][agent_id]}\n')
