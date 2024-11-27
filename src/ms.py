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
    'self': MS('self', np.array([0, 0]), eps=15),
    # дружба 1
    'friendship': MS('friendship', np.array([0, 40]), 5),
    # вражда 1
    'feud': MS('feud', np.array([40, -40]), 5),
    # лидерство 2
    'leadership': MS('leadership', np.array([40, 40]), 5),
    # следование 2
    'following': MS('following', np.array([-40, 40]), 5),
    # партнерство
    'cooperation': MS('cooperation', np.array([0, 40]), 5),
    # равнодушие
    'equinodoses': MS('equinodoses', np.array([0, 0]), 5),
    # поддержка
    'supporting': MS('supporting', np.array([0, 40]), 5),
    # соперничество
    'rivalry': MS('rivalry', np.array([35, 33]), 5),
    # осторожность
    'caution': MS('caution', np.array([0, 0]), 5),
    # контроль
    'control': MS('control', np.array([40, 0]), 5),
    # эмпатия
    'empathy': MS('empathy', np.array([-33, 40]), 5),
}
