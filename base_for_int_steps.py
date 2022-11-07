# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:20:17 2021

@author: Tim
"""

import numpy as np

max_value = 10003

min_value = max_value%2

test_value = min_value

step_fraction = 20

for r in range(step_fraction):
    step_size = int((max_value-min_value)/step_fraction)
    test_value = (r)*step_size
    print(test_value)