import pandas as pd
import numpy as np
from hmmlearn import hmm
from appraisal import Appraisal
from agent import Agent
from ms import feelings2d as feelings
from actions import actions2d as actions

actions_list = list(actions.keys())
actions_encoded = dict(
    zip(list(actions.keys()), range(len(list(actions.keys())))))

states_list = list(feelings.keys())
n_emits = len(list(actions.keys()))
n_states = len(states_list)
emission_probs = np.ones((n_states, n_emits))
for i_state, state in enumerate(states_list):
    row = [0] * n_emits
    for action, action_label in actions_encoded.items():
        row[action_label] = (
            1 / (Appraisal.cosine_dist(Appraisal(*actions[action]['author']), feelings[state]) + 0.00001))
    row = np.array(row)
    row /= np.sum(row)
    for action, action_label in actions_encoded.items():
        emission_probs[i_state][action_label] = row[action_label]

logdf = pd.read_csv('./logs.csv', sep='|')
agents_ids = list(map(int, list(logdf['from_id'].unique())))
all_agents_ids = list(sorted(list(set(agents_ids).union(set(logdf['to_id'].unique())))))

new_id = all_agents_ids[-1] + 1
new_agent = Agent(id=new_id, r=0.1)
new_agent.set_ids(set(all_agents_ids))
all_agents_ids.append(new_id)

mutual_feelings = dict()
for id in all_agents_ids:
    mutual_feelings[id] = dict(zip(all_agents_ids, ['self'] * len(all_agents_ids)))

for agent_id in agents_ids:
    df_from_agent_id = logdf[logdf['from_id'] == agent_id]
    to_ids = list(df_from_agent_id['to_id'].unique())
    for to_id in to_ids:
        df = df_from_agent_id[df_from_agent_id['to_id'] == to_id]
        observations = []
        for i, row in df.iterrows():
            observations.append(actions_encoded[row['action_name']])
        observations = np.array(observations)
        model = hmm.CategoricalHMM(n_components=len(
            feelings), n_iter=logdf.shape[0], params='s', init_params='s')
        model.startprob_ = np.ones(n_states) / n_states
        model.transmat_ = np.ones((n_states, n_states)) / n_states
        model.emissionprob_ = emission_probs

        model.fit(observations.reshape(-1, 1))
        preds = model.predict(observations.reshape(-1, 1))
        mutual_feelings[agent_id][to_id] = states_list[preds[-1]]

for id, row in mutual_feelings.items():
    print(id, ' - ', row)
