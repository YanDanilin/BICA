import numpy as np
class MS:
    def __init__(self,name,f,eps):
        self.name = name
        self.f = f
        self.e = eps
        
    def near(self,a):
        if(np.sqrt(np.sum(self.f-a)**2)<self.eps):
            return True
        else:
            return False
        
MSs = set(
    MS('friendship',np.array([0,1,1]),0.05),
    MS('feud',np.array([1,-1,-1]),0.05),
    MS('subordination',np.array([-1,1,1]),0.05),
    MS('cooperation',np.array([0,1,0,8]),0.05),
    MS('equinodoses',np.array([0,0,0]),0.05),
    MS('supporting',np.array([0,1,0.9]),0.05),
    MS('rivalry',np.array([0.5,0.5,0]),0.05),
    MS('meanness',np.array([1,-1,-1]),0.05),
    MS('following',np.array([-1,1,1]),0.05),
    MS('caution',np.array([0,0,-0.5]),0.05),
    MS('control',np.array([1,0,-1]),0.05),
    MS('empathy',np.array([-0.5,1,0.7]),0.05),
    MS('caution',np.array([0,0,-0.5]),0.05),
)