# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:07:22 2021

@author: Tim
"""
import numpy as np
import matplotlib.pyplot as plt
import re
import resultslist as reslst

index_array = []
avg_array = []
std_dev_array = []
index_type = 'w'
f_weight = 'power_2' 
c_threshold = '1'
repetition_num = [1, 2, 3, 4, 5, 6, 7]
index_name_re = re.compile(r"\b(?P<indices>\w+_[\dsim]{3,4}_[wdis]{3,4})\b", re.IGNORECASE)
sim_avg_re = re.compile(r"(?<=random)(?P<averages>.+)")
std_dev_re = re.compile(r"(?<=STD)(?P<stddevs>.+)")

for rep in repetition_num:
    name = 'random_'+index_type+'FP24981m167c'+c_threshold+'f'+f_weight+'MACCSrepnum'+str(rep)+'.sim'
    index_values_list = reslst.Index_Names(name, index_name_re)
    avg_values_list = reslst.Avg_Values_Results(name, sim_avg_re)
    std_dev_list = reslst.Std_Dev_Results(name, std_dev_re)
    index_array.append(index_values_list)
    avg_array.append(avg_values_list)
    std_dev_array.append(std_dev_list)
    if rep == len(repetition_num):
        index_array = np.array([index_array]).reshape(rep, len(index_values_list))
        avg_array = np.array([avg_array]).reshape(rep, len(avg_values_list))
        std_dev_array = np.array([std_dev_array]).reshape(rep, len(std_dev_list))
    else:
        pass


avg_array_plot = avg_array.T
std_dev_array_plot = std_dev_array.T

fig = plt.figure(1)
x = repetition_num
plt.title(index_type+', w_factor = '+f_weight+', c_threshold = '+c_threshold)
plt.xlabel('Number of Repetitions')
plt.ylabel('Average of the Similarity Values')
plt.tight_layout()
plt.ylim(-0.20, 1.20)

for reps in repetition_num:
    y = avg_array_plot[reps-1]
    yerr = std_dev_array_plot[reps-1]
    plt.errorbar(x, y, yerr, label = index_array[0][reps-1])
    plt.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))

fig.savefig('All-Indices_'+index_type+'_'+c_threshold+'_'+f_weight+'.png', bbox_inches = 'tight')    
    
for repss in repetition_num:
    fig, ax = plt.subplots()
    y = avg_array_plot[repss-1]
    yerr = std_dev_array_plot[repss-1]
    plt.errorbar(x, y, yerr, color = 'black', ecolor = 'red')
    ax.set_xlabel('Number of Repetitions')
    ax.set_ylabel('Average of the Similarity Values')
    ax.set_title(index_array[0][repss-1]+', '+index_type+', w_factor = '+f_weight+', c_threshold = '+c_threshold)
    plt.tight_layout()
    fig.savefig(index_array[0][repss-1]+'_'+index_type+'_'+c_threshold+'_'+f_weight+'.png', bbox_inches = 'tight')
    
