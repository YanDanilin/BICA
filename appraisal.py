import random
import numpy as np


class Appraisal:
    def __init__(self, friendliness=0, dominance=0, respect=0, trust=0,
                 random_init=False, eps=0.3):
        self.categories_ = ['friendliness', 'dominance', 'respect', 'trust']
        self.vector_ = None
        self.values = None
        if random_init == True:
            self.vector_ = eps * (np.random(len(self.categories_)) - 0.5)
        else:
            self.vector_ = [friendliness, dominance, respect, trust]
        self.values = dict(zip(self.categories_, self.vector))
    
    def __add__(self, another):
        res_vector = self.vector_ + another.vector_
        res_appraisal = Appraisal(*list(res_vector))
        return res_appraisal
    
    def __mul__(self, number):
        res_vector = self.vector_ * number
        res_appraisal = Appraisal(*list(res_vector))
    
    
    
    