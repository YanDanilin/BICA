import numpy as np

actions = {
    'hi': {
        'author': [0, 0.1, 0.5],
        'target': [0, 0.5, 0.1]
    },
    'ignor': {
        'author': [0.1, -0.5, -0.1],
        'target': [0, -0.1, -0.5]
    },
    'insult': {
        'author': [0.5, -0.3, -0.4],
        'target': [-0.5, -0.2, -0.6]
    },
    'talk': {
        'author': [0, 0.6, 0.5],
        'target': [0, 0.6, 0.5]
    },
    'help': {
        'author': [0.2, 0.8, 0.2],
        'target': [-0.2, 0.5, 0.9]
    },
    'lie': {
        'author': [0.6, -0.1, 0],
        'target': [-0.3, -0.7, -0.4]
    },
    'kick': {
        'author': [0.1, 0.5, -0.1],
        'target': [-0.1, -0.5, -0.6]
    },
    'hit': {
        'author': [0.9, 0.5, -0.1],
        'target': [-0.9, -0.5, -0.6]
    }
}
