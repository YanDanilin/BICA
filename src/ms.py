import numpy as np
from appraisal import Appraisal


class MS:
    def __init__(self, name, feeling, eps):
        self.name = name
        self.feeling = Appraisal(*feeling)
        self.eps = eps

    def near(self, appraisal):
        if Appraisal.euclidian_dist(self.feeling, appraisal) < self.eps:
            return True
        return False


MSs = {
    'self': MS('self', np.array([0, 0, 0]), eps=1),
    # дружба 1
    'friendship': MS('friendship', np.array([0, 1, 1]), 0.05),
    # вражда 1
    'feud': MS('feud', np.array([1, -1, -1]), 0.05),
    # лидерство 2
    'leadership': MS('leadership', np.array([1, 1, 0.5]), 0.05),
    # следование 2
    'following': MS('following', np.array([-1, 1, 1]), 0.05),
    # партнерство
    'cooperation': MS('cooperation', np.array([0, 1, 0.8]), 0.05),
    # равнодушие
    'equinodoses': MS('equinodoses', np.array([0, 0, 0]), 0.05),
    # поддержка
    'supporting': MS('supporting', np.array([0, 1, 0.9]), 0.05),
    # соперничество
    'rivalry': MS('rivalry', np.array([0.5, 0.5, 0]), 0.05),
    # осторожность
    'caution': MS('caution', np.array([0, 0, -0.5]), 0.05),
    # контроль
    'control': MS('control', np.array([1, 0, -1]), 0.05),
    # эмпатия
    'empathy': MS('empathy', np.array([-0.5, 1, 0.7]), 0.05),
}
