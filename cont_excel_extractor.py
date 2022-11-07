# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:05:41 2021

@author: Tim
"""


import numpy as np
import glob
import re

def text_retrieve_list(file, retriever, value_name):
    
    with open(file, 'r') as f:
        text = f.read()
    
    text_obj = retriever.search(text)
    text_output = text_obj.group(value_name).split()[1:-1]
    
weight_type = '_nw_'
file_list = glob.glob('*' + weight_type + '*.sim')

index_list_re = re.compile(r'Indices \s(?P<ind_list>.+)')
sim_re = re.compile(r"^Similarity \s(?P<sims>.+)")


    

for file in file_list:
    file_info = file.split('_')
    index_list = []
    sim_list = []
    data_source = file_info[0] + '_' + file_info[1]
    data_type = file_info[2]
    data_amount = file_info[3]
    c_threshold = file_info[4].strip('c')
    w_factor = file_info[5]
    norm_method = file_info[7].split('.')[0]
    