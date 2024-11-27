import numpy as np

actions3d = {
    'hi': {
        'author': [0, 10, 15],
        'target': [0, 15, 10]
    },
    'ignor': {
        'author': [10, -15, -10],
        'target': [0, -10, -15]
    },
    'insult': {
        'author': [15, -13, -14],
        'target': [-15, -12, -17]
    },
    'talk': {
        'author': [0, 17, 15],
        'target': [0, 17, 15]
    },
    'help': {
        'author': [12, 19, 12],
        'target': [-12, 17, 20]
    },
    'lie': {
        'author': [17, -10, 0],
        'target': [-13, -17, -14]
    },
    'kick': {
        'author': [20, 15, -10],
        'target': [-20, -15, -17]
    },
    'hit': {
        'author': [18, 15, -10],
        'target': [-18, -15, -16]
    }
}

actions2d = {
    'hi': {
        'author': [0, 10],
        'target': [0, 15]
    },
    'ignor': {
        'author': [10, -15],
        'target': [0, -10]
    },
    'insult': {
        'author': [15, -13],
        'target': [-15, -12]
    },
    'talk': {
        'author': [0, 17],
        'target': [0, 17]
    },
    'help': {
        'author': [12, 19],
        'target': [-12, 17]
    },
    'lie': {
        'author': [17, -10],
        'target': [-13, -17]
    },
    'kick': {
        'author': [20, 15],
        'target': [-20, -15]
    },
    'hit': {
        'author': [18, 15],
        'target': [-18, -15]
    }
}
