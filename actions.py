import numpy as np

actions = {
    'hi':{
        'auhtor': [0,0.01,0.05],
        'target': [0,0.05,0.01]
    },
    'ignor':{
        'auhtor': [0.01,-0.05,-0.01],
        'target': [0,-0.01,-0.05]
    },
    'insult':{
        'auhtor': [0.05,-0.03,-0.04],
        'target': [-0.05,-0.02,-0.06]
    },
    'neutral talk':{
        'auhtor': [0,0.06,0.01],
        'target': [0,0.02,0.02]
    },
    'help':{
        'auhtor': [0.02,0.08,0.02],
        'target': [-0.02,0.05,0.09]
    },
    'lie':{
        'auhtor': [0.06,-0.01,0],
        'target': [-0.03,-0.07,-0.04]
    },
    'kick':{
        'auhtor': [0.1,0.05,-0.01],
        'target': [-0.1,-0.05,-0.06]
    },
    'hit':{
        'auhtor': [0.09,0.05,-0.01],
        'target': [-0.09,-0.05,-0.06]
    },
    'hug':{
        'auhtor': [0.1,0.05,0.05],
        'target': [0.1,0.05,0.06]
    },
    'agresive talk':{
        'auhtor': [0.09,-0.02,-0.03],
        'target': [-0.09,-0.05,-0.06]
    },
    'joke':{
        'auhtor': [0.03,0.03,0.02],
        'target': [-0.03,0.01,-0.01]
    },
    'serious talk':{
        'auhtor': [0.03,0.03,0.03],
        'target': [-0.04,0.05,0.02]
    },
    'compliment':{
        'auhtor': [0.01,0.03,0.01],
        'target': [-0.01,0.02,0.01]
    }
    
}