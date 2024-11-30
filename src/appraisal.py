import random
import numpy as np
from scipy.spatial import distance


class Appraisal:
    def __init__(self, *args, random_init=False, eps=0.3):
        self.categories_ = ['dominance', 'valence']  # временно 2 измерения
        self.vector_ = None
        self.values = None
        self.eps = eps
        if random_init:
            self.vector_ = eps * \
                (np.random.random(len(self.categories_)) - 0.5)
        else:
            self.vector_ = np.array(args)
        self.values = dict(zip(self.categories_, self.vector_))

    def __add__(self, another):
        res_vector = self.vector_ + another.vector_
        return Appraisal(*list(res_vector))

    def __sub__(self, another):
        res_vector = self.vector_ - another.vector_
        return Appraisal(*list(res_vector))

    def __mul__(self, number):
        res_vector = self.vector_ * number
        return Appraisal(*list(res_vector))

    def __rmul__(self, number):
        res_vector = self.vector_ * number
        return Appraisal(*list(res_vector))

    def __pow__(self, number):
        res_vector = self.vector_ ** 2
        return Appraisal(*res_vector)

    @staticmethod
    def euclidean_dist(a1, a2):
        return np.sqrt(np.sum((a1.vector_ - a2.vector_) ** 2))

    @staticmethod
    def cosine_dist(a1, a2):
        return distance.cosine(a1.vector_, a2.vector_)
