# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:07:22 2021

@author: Tim
"""
import numpy as np
import matplotlib.pyplot as plt
import re
import resultslist_02 as reslst

dataset_array = []
index_array = []
avg_on_array = []
avg_off_array = []
std_dev_on_array = []
std_dev_off_array = []
div_on_absolute_array = []
div_on_relative_array = []
div_off_absolute_array = []
div_off_relative_array = []

Indices_of_interest = ['BUB_1sim_dis', 'Fai_1sim_dis', 'JT_1sim_dis', 'SM_1sim_dis', 
                       'BUB_1sim_wdis', 'Fai_1sim_wdis', 'JT_1sim_wdis', 'SM_1sim_wdis']

index_type = 'nw'
f_weight = 'fraction' 
c_threshold = [1]
repetition_num = [1, 2, 3, 4, 5, 6, 7]
index_name_re = re.compile(r"\b(?P<indices>\w+_[\dsim]{3,4}_[wdis]{3,4})\b", re.IGNORECASE)
dataset_sim_re = re.compile(r"(?<=dataset)(?P<datasetvalues>.+)")
sim_on_avg_re = re.compile(r"(?<=random_on_dist)(?P<averages_on>.+)")
sim_off_avg_re = re.compile(r"(?<=random_off_dist)(?P<averages_off>.+)")
std_dev_on_re = re.compile(r"(?<=STD_on_dist)(?P<stddevs_on>.+)")
std_dev_off_re = re.compile(r"(?<=STD_off_dist)(?P<stddevs_off>.+)")
div_on_absolute_re = re.compile(r"(?<=diversity_1_on_dist)(?P<div_on_abs>.+)")
div_on_relative_re = re.compile(r"(?<=diversity_2_on_dist)(?P<div_on_rel>.+)")
div_off_absolute_re = re.compile(r"(?<=diversity_1_off_dist)(?P<div_off_abs>.+)")
div_off_relative_re = re.compile(r"(?<=diversity_2_off_dist)(?P<div_off_rel>.+)")

for rep in repetition_num:
    name = 'random_'+index_type+'FP24981m167c'+str(c_threshold[0])+'f'+f_weight+'MACCSrepnum'+str(rep)+'.sim'
    dataset_list = reslst.List_Values(name, dataset_sim_re, "datasetvalues")
    index_list = reslst.Index_Names(name, index_name_re)
    avg_on_list = reslst.List_Values(name, sim_on_avg_re, "averages_on")
    avg_off_list = reslst.List_Values(name, sim_off_avg_re, "averages_off")
    std_dev_on_list = reslst.List_Values(name, std_dev_on_re, "stddevs_on")
    std_dev_off_list = reslst.List_Values(name, std_dev_off_re, "stddevs_off")
    div_on_absolute_list = reslst.List_Values(name, div_on_absolute_re, "div_on_abs")
    div_on_relative_list = reslst.List_Values(name, div_on_relative_re, "div_on_rel")
    div_off_absolute_list = reslst.List_Values(name, div_off_absolute_re, "div_off_abs")
    div_off_relative_list = reslst.List_Values(name, div_off_relative_re, "div_off_rel")
    dataset_array.append(dataset_list)
    index_array.append(index_list)
    avg_on_array.append(avg_on_list)
    avg_off_array.append(avg_off_list)
    std_dev_on_array.append(std_dev_on_list)
    std_dev_off_array.append(std_dev_off_list)
    div_on_absolute_array.append(div_on_absolute_list)
    div_on_relative_array.append(div_on_relative_list)
    div_off_absolute_array.append(div_off_absolute_list)
    div_off_relative_array.append(div_off_relative_list)
    if rep == repetition_num[-1]:
        dataset_array = np.array([dataset_array]).reshape(len(repetition_num),len(dataset_list))
        index_array = np.array([index_array]).reshape(len(repetition_num), len(index_list))
        avg_on_array = np.array([avg_on_array]).reshape(len(repetition_num), len(avg_on_list))
        avg_off_array = np.array([avg_off_array]).reshape(len(repetition_num), len(avg_off_list))
        std_dev_on_array = np.array([std_dev_on_array]).reshape(len(repetition_num), len(std_dev_on_list))
        std_dev_off_array = np.array([std_dev_off_array]).reshape(len(repetition_num), len(std_dev_off_list))
        div_on_absolute_array = np.array([div_on_absolute_array]).reshape(len(repetition_num), len(div_on_absolute_list))
        div_on_relative_array = np.array([div_on_relative_array]).reshape(len(repetition_num), len(div_on_relative_list))
        div_off_absolute_array = np.array([div_off_absolute_array]).reshape(len(repetition_num), len(div_off_absolute_list))
        div_off_relative_array = np.array([div_off_relative_array]).reshape(len(repetition_num), len(div_off_relative_list))
        
   
dataset_trans = dataset_array.T
avg_on_trans = avg_on_array.T
avg_off_trans = avg_off_array.T
std_dev_on_trans = std_dev_on_array.T
std_dev_off_trans = std_dev_off_array.T
div_on_absolute_trans = div_on_absolute_array.T
div_on_relative_trans = div_on_relative_array.T
div_off_absolute_trans = div_off_absolute_array.T
div_off_relative_trans = div_off_relative_array.T

fig = plt.Figure()

std_dev_table_on = []
indices_table_row_on = []
for i in range(len(index_array[0])):
    plt.title(index_type+', w_factor = '+f_weight+', c_threshold = '+str(c_threshold[0]))
    plt.xlabel('Replica Number')
    plt.ylabel('Random On Dist Average Similarity')
    plt.ylim([0, 1.00])
    plt.tight_layout()
    replica_plot = []
    avg_sim_on_plot = []
    std_dev_plot = []
    if index_array[0][i] in Indices_of_interest:
        for h in range(len(repetition_num)):
            if avg_on_trans[i][h] != "-" and std_dev_on_trans[i][h] != "-" :
                replica_plot.append(repetition_num[h])
                avg_sim_on_plot.append(float(avg_on_trans[i][h]))
                std_dev_plot.append(float(std_dev_on_trans[i][h]))
                
                
            else:
                pass
        std_dev_table_on.append(list(std_dev_on_trans[i]))
        indices_table_row_on.append(index_array[0][i])    
        plt.scatter(replica_plot, avg_sim_on_plot, label = index_array[0][i])
        plt.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))  
    else:
        pass
    
    
plt.savefig('On Distribution Average Similarity vs Replica Number Indicies of Interest.png')
plt.clf()
plt.title('Std Dev On Dist Average Similarity vs Replica Number', loc = 'left')
plt.axis('off')
plt.tight_layout()
plt.table(std_dev_table_on, cellLoc = 'center', loc = 'center', rowLabels = indices_table_row_on, colLabels = repetition_num)
plt.subplots_adjust(left=0.2)
plt.savefig('Std Dev Of On Distribution Average Similarity vs Replica Number.png')
plt.clf()

for i in range(len(index_array[0])):
    plt.title(index_type+', w_factor = '+f_weight+', c_threshold = '+str(c_threshold[0])+' '+index_array[0][i])
    plt.xlabel('Replica Number')
    plt.ylabel('Random On Dist Average Similarity')
    plt.tight_layout()
    plt.ylim([0, 1.00])
    threshold_plot = []
    avg_sim_on_plot = []
    std_dev_on_plot = []
    for h in range(len(repetition_num)):
        if avg_on_trans[i][h] != "-" and std_dev_on_trans[i][h] != "-" :
            threshold_plot.append(repetition_num[h])
            avg_sim_on_plot.append(float(avg_on_trans[i][h]))
            std_dev_on_plot.append(float(std_dev_on_trans[i][h]))
                            
        else:
            pass
    
    plt.errorbar(threshold_plot, avg_sim_on_plot, yerr = std_dev_on_plot, label = index_array[0][i])
    plt.savefig('On Distribution Average Similarity vs Replica Number '+index_array[0][i]+'.png', bbox_inches = 'tight')
    plt.clf()
    
std_dev_table_off = []
indices_table_row_off = []
for i in range(len(index_array[0])):
    plt.title(index_type+', w_factor = '+f_weight+', c_threshold = '+str(c_threshold[0]))
    plt.xlabel('Replica Number')
    plt.ylabel('Random Off Dist Average Similarity')
    plt.tight_layout()
    plt.ylim([0, 1.00])
    replica_plot = []
    avg_sim_off_plot = []
    std_dev_off_plot = []
    if index_array[0][i] in Indices_of_interest:
        for h in range(len(repetition_num)):
            if avg_off_trans[i][h] != "-" and std_dev_off_trans[i][h] != "-" :
                replica_plot.append(repetition_num[h])
                avg_sim_off_plot.append(float(avg_off_trans[i][h]))
                std_dev_off_plot.append(float(std_dev_off_trans[i][h]))
            
            else:
                pass
        std_dev_table_off.append(list(std_dev_off_trans[i]))
        indices_table_row_off.append(index_array[0][i])
        plt.scatter(replica_plot, avg_sim_off_plot, label = index_array[0][i])
        plt.legend(loc = 'center left', bbox_to_anchor = (1.0, 0.5))     
    else:
        pass
    
    
plt.savefig('Off Distribution Average Similarity vs Replica Number Indices of Interest.png')
plt.clf()
plt.title('Std Dev Of Off Dist Average Similarity vs Replica Number', loc = 'left')
plt.axis('off')
plt.tight_layout()
plt.table(std_dev_table_off, cellLoc = 'center', loc = 'center', rowLabels = indices_table_row_off, colLabels = repetition_num)
plt.subplots_adjust(left=0.2)
plt.savefig('Std Dev Of Off Distribution Average Similarity vs Replica Number.png')
plt.clf()

for i in range(len(index_array[0])):
    plt.title(index_type+', w_factor = '+f_weight+', c_threshold = '+str(c_threshold[0])+' '+index_array[0][i])
    plt.xlabel('Replica Number')
    plt.ylabel('Random Off Dist Average Similarity')
    plt.tight_layout()
    plt.ylim([0, 1.00])
    threshold_plot = []
    avg_sim_off_plot = []
    std_dev_off_plot = []
    for h in range(len(repetition_num)):
        if avg_off_trans[i][h] != "-" and std_dev_off_trans[i][h] != "-" :
            threshold_plot.append(repetition_num[h])
            avg_sim_off_plot.append(float(avg_off_trans[i][h]))
            std_dev_off_plot.append(float(std_dev_off_trans[i][h]))
                            
        else:
            pass
    
    plt.errorbar(threshold_plot, avg_sim_off_plot, yerr = std_dev_off_plot, label = index_array[0][i])
    plt.savefig('Off Distribution Average Similarity vs Replica Number '+index_array[0][i]+'.png', bbox_inches = 'tight')
    plt.clf()