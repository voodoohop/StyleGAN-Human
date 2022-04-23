# Copyright (c) SenseTime Research. All rights reserved.

attr_dict = dict(
    interface_gan={ # strength
        'upper_length': [1], 
        'bottom_length': [1],
        'test_1': [2],
        'test_2': [3],
        'test_3': [4],
    },
    stylespace={ # layer, strength, threshold
        'upper_length': [5, 5, 0.0028], 
        'bottom_length': [3, 5, 0.003],
        'test_1': [6, 7, 0.03],
        'test_2': [4, 8, 0.003],
        'test_3': [5, 9, 0.003],
    },
    sefa={ # layer, strength
        'upper_length': [[4, 5, 6, 7], -5],
        'bottom_length': [[4, 5, 6, 7], 5],
        'test_1': [[9, 10, 11, 12], -5],
        'test_2': [[3, 4, 6, 7], -5],
    }
)
