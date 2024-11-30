import pandas as pd
import numpy as np
from hmmlearn import hmm
from ms import feelings2d as feelings
from actions import actions2d as actions

logdf = pd.read_csv('./lofs.csv', sep='|')

one, two = 0, 1
df = logdf[(logdf['from_id'] == one) & (logdf['to_id'] == two)]

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

actions_encoded = dict(
    zip(list(actions.keys()), range(len(list(actions.keys())))))
observations = []
for i, row in df.iterrows():
    observations.append(actions_encoded[row['action_name']])

actions_list = dict(
    zip(list(actions.keys()), range(len(list(actions.keys())))))
n_states = len(list(feelings.keys()))
emission_labels =

model = hmm.CategoricalHMM(n_components=len(feelings), n_iter=logdf.shape[0])
model.startprob_ = np.ones(n_states) / n_states
model.transmat_ = np.ones((n_states, n_states)) / n_states
emission_probs = np.array(())
model.emissionprob_ =
