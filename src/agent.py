from appraisal import Appraisal
import random
import numpy as np
from scipy import stats


class Agent:
    def __init__(self, id, r=0.01):
        self.id = id
        self.other_ids = None
        self.r = r
        self.appraisals = dict()
        self.feelings = dict()
        self.moral_schemas = None

    def set_ids(self, ids_list: set):
        '''
        {
            id1: A,
            ...
        }
        '''
        self.other_ids = ids_list - set([self.id])
        af_list = [Appraisal(random_init=True, eps=0.2)
                   for _ in range(len(self.other_ids))]
        self.appraisals = dict(zip(self.other_ids, af_list))
        self.moral_schemas = [['self'] * len(ids_list)] * len(ids_list)

    def set_id(self, id):
        if self.other_ids is not None and id not in self.appraisals:
            self.appraisals[id] = Appraisal(random_init=True, eps=0.2)

    def set_feeling(self, to_id: int, feeling: Appraisal):
        self.feelings[to_id] = feeling + Appraisal(random_init=True, eps=4)

    def send(self, possible_actions: dict):
        receivers = random.sample(
            list(self.other_ids), k=random.randint(0, len(self.other_ids)))
        actions_to_receivers = {}
        for r_id in receivers:
            res_action = None
            max_likelihood = -1
            for action_name, action in possible_actions.items():
                prob = stats.norm.pdf(Appraisal.euclidean_dist(
                    Appraisal(*action['author']), self.feelings[r_id]))
                if prob > max_likelihood:
                    max_likelihood = prob
                    res_action = action_name
            actions_to_receivers[r_id] = res_action
            self.appraisals[r_id] = (1 - self.r) * self.appraisals[r_id] + \
                self.r * \
                Appraisal(*list(possible_actions[res_action]['author']))
        return actions_to_receivers

    def receive(self, action_name, from_id, possible_actions: dict):
        self.appraisals[from_id] = (1 - self.r) * self.appraisals[from_id] + \
            self.r * Appraisal(*possible_actions[action_name]['target'])
            
    def appraisal_near_feeling(self, target_id):
        return Appraisal.euclidean_dist(self.appraisals[target_id], self.feelings[target_id]) < self.feelings[target_id].eps
