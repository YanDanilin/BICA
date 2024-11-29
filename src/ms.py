import numpy as np
from appraisal import Appraisal


import numpy as np
from appraisal import Appraisal


class MS:
    def __init__(self, name, feeling1, feeling2, eps):
        self.name = name
        self.feeling1 = Appraisal(*feeling1)
        self.feeling2 = Appraisal(*feeling2)
        self.eps = eps

    def get_feel_1(self):
        return self.feeling1
    
    def get_feel_2(self):
        return self.feeling2

    def find(self, appraisal1,appraisal2):
        if (Appraisal.euclidian_dist(self.feeling1, appraisal1) < self.eps and Appraisal.euclidian_dist(self.feeling2, appraisal2) < self.eps):
            return True
        return False
    
    def near(self, appraisal1,appraisal2):
        if (Appraisal.euclidian_dist(self.feeling1, appraisal1)  < Appraisal.euclidian_dist(self.feeling2, appraisal2) ):
            return True
        return False
    
    def near(self, appraisal1):
        if (Appraisal.euclidian_dist(self.feeling1, appraisal1) < self.eps):
            return True
        return False
        

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
    'partner': Appraisal(*[0, 40, 36]),
    # равнодушный
    'indifference': Appraisal(*[0, 0, 0]),
    # поддержживающий
    'supporting': Appraisal(*[0, 40, 38]),
    # соперник
    'rival': Appraisal(*[35, 33, 0]),
    # осторожный
    'careful': Appraisal(*[0, 0, -33]),
    # контролирующий
    'supervisory': Appraisal(*[40, 0, -40]),
    # подконтрольный
    'controlled': Appraisal(*[-40, 0, -37]),
    # эмпатичный
    'empathetic': Appraisal(*[-33, 40, 35]),
    'empathy': MS('empathy', np.array([-33, 40]), 5),
}
