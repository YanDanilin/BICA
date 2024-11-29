import numpy as np
from appraisal import Appraisal
from agent import Agent


class MS:
    def __init__(self, name, feeling1, feeling2, eps):
        self.name = name
        self.feeling1 = Appraisal(*feeling1)
        self.feeling2 = Appraisal(*feeling2)
        self.eps = eps

    def is_appropriate_ms(self, appraisal1, appraisal2):
        return Appraisal.euclidean_dist(self.feeling1, appraisal1) < self.eps and Appraisal.euclidean_dist(self.feeling2, appraisal2) < self.eps

    def both_near_feelings(self, appraisal1, appraisal2):
        return Appraisal.euclidean_dist(self.feeling1, appraisal1) < Appraisal.euclidean_dist(self.feeling2, appraisal2)

    def near_feeling1(self, appraisal):
        return Appraisal.euclidean_dist(self.feeling1, appraisal) < self.eps

    def near_feeling2(self, appraisal):
        return Appraisal.euclidean_dist(self.feeling2, appraisal) < self.eps


feelings = {
    # дружелюбный
    'friendly': Appraisal(*[0, 40, 40]),
    # враждебный
    'hostility': Appraisal(*[40, -40, -40]),
    # лидер
    'leader': Appraisal(*[40, 40, 30]),
    # подчинённый
    'subordinate': Appraisal(*[-40, 40, 40]),
    # партнёр
    'parthner': Appraisal(*[0, 40, 36]),
    # равнодушный
    'indifference': Appraisal(*[0, 0, 0]),
    # поддержживающий
    'supporting': Appraisal(*[0, 40, 38]),
    # соперник
    'rival': Appraisal(*[35, 33, 0]),
    # осторожный
    'careful': Appraisal(*[0, 0, -33]),
    # контролирующий
    'controlling': Appraisal(*[40, 0, -40]),
    # подконтрольный
    'controlling': Appraisal(*[-40, 0, -37]),
    # эмпатичный
    'empathetic': Appraisal(*[-33, 40, 35]),
}


MSs = {
    'self': MS('self', np.array([0, 0, 0]), np.array([0, 0, 0]), eps=15),
    # дружба 1
    'friendship': MS('friendship', np.array([0, 40, 40]), np.array([0, 40, 40]), 5),
    # вражда 1
    'feud': MS('feud', np.array([40, -40, -40]), np.array([40, -40, -40]), 5),
    # лидерство 2
    'leadership': MS('leadership', np.array([40, 40, 30]), np.array([-40, 40, 40]), 5),
    # следование 2
    # 'following': MS('following', np.array([-40, 40, 40]), 5),
    # партнерство
    'cooperation': MS('cooperation', np.array([0, 40, 36]), np.array([0, 40, 36]), 5),
    # равнодушие
    'equinodoses': MS('equinodoses', np.array([0, 0, 0]), np.array([0, 0, 0]), 5),
    # поддержка
    'supporting': MS('supporting', np.array([0, 40, 38]), np.array([0, 40, 38]), 5),
    # соперничество
    'rivalry': MS('rivalry', np.array([40, 40, 30]), np.array([40, 40, 30]), 5),
    # осторожность
    'caution': MS('caution', np.array([0, 0, -33]), np.array([0, 0, -33]), 5),
    # контроль
    'control': MS('control', np.array([40, 0, -40]), np.array([-40, 0, -37]), 5),
    # эмпатия
    'empathy': MS('empathy', np.array([-33, 40, 35]), np.array([-33, 40, 35]), 5),
}


def check_moral_schema(author: Agent, target: Agent):
    author_a, target_a = author.appraisals[target.id], target.appraisals[author.id]
    for ms_name, moral_schema in MSs.items():
        if moral_schema.is_appropriate_ms(author_a, target_a):
            return 'ms', author.id, target.id, ms_name
        if moral_schema.is_appropriate_ms(target_a, author_a):
            return 'ms', target.id, author.id, ms_name
        if moral_schema.near_feeling1(author_a) and not moral_schema.near_feeling2(target_a):
            return 'change', target.id, author.id, moral_schema.feeling2
        elif moral_schema.near_feeling2(author_a) and not moral_schema.near_feeling1(target_a):
            return 'change', target.id, author.id, moral_schema.feeling1
        elif moral_schema.near_feeling1(target_a) and not moral_schema.near_feeling2(author_a):
            return 'change', author.id, target.id, moral_schema.feeling2
        elif moral_schema.near_feeling2(target_a) and not moral_schema.near_feeling1(author_a):
            return 'change', author.id, target.id, moral_schema.feeling1
    return -1