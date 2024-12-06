import pandas as pd
import numpy as np
from hmmlearn import hmm
from appraisal import Appraisal
from ms import feelings2d as feelings
from actions import actions2d as actions

logdf = pd.read_csv('./logs.csv', sep='|')


from_id, to_id = 0, 1

df = logdf[(logdf['from_id'] == from_id) & (logdf['to_id'] == to_id)]
print(df)
path0_dom, path0_val = [], []
path1_dom, path1_val = [], []
for i, row in df.iterrows():
    if row['from_id'] == 0:
        path0_dom.append(row['author_dom'])
        path0_val.append(row['author_val'])
        path1_dom.append(row['target_dom'])
        path1_val.append(row['target_val'])
    else:
        path1_dom.append(row['author_dom'])
        path1_val.append(row['author_val'])
        path0_dom.append(row['target_dom'])
        path0_val.append(row['target_val'])

actions_list = list(actions.keys())
actions_encoded = dict(
    zip(list(actions.keys()), range(len(list(actions.keys())))))
observations = []
for i, row in df.iterrows():
    observations.append(actions_encoded[row['action_name']])
observations = np.array(observations)

print('observations - ', observations)
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

print("Actions encoded - ", actions_encoded)
print("Emission probs - ", emission_probs)
print(emission_probs[1].sum())

model = hmm.CategoricalHMM(n_components=len(
    feelings), n_iter=logdf.shape[0], params='s', init_params='s')
model.startprob_ = np.ones(n_states) / n_states
model.transmat_ = np.ones((n_states, n_states)) / n_states
model.emissionprob_ = emission_probs

model.fit(observations.reshape(-1, 1))
preds = model.predict(observations.reshape(-1, 1))
print(preds)
print(preds.shape)
print(states_list[preds[-1]])
print(model.predict_proba(observations.reshape(-1, 1)))
