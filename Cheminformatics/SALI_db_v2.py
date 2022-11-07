# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:02:58 2022

@author: Tim
"""
import pandas as pd
import glob
# org_file = glob.glob('*.csv')[0]
# db_list = ['Tubuline', 'ST-protein kinase AKT', 'Protein-tyrosine phosphatase 1B',
#              'Peroxisome proliferator-activated receptor gamma', 'Peroxisome proliferator-activated receptor alpha',
#              'G9a', 'Free fatty acid receptor 1', 'Epidermal growth factor receptor erbB1',
#              'Beta-secretase 1', 'Aldose reductase']
# org_df = pd.read_csv(org_file)
# org_list = org_df['Dataset'].to_list()
# my_list=[]
# for x in org_list:
#     fn = x.split('_')[0]
#     my_list.append(fn)

# for a in db_list:
#     if not a in my_list:
        # print(a)
        
    
# for index, ds in enumerate(db_list):
#     print(index, ds)
abb_list = ['MAACS', 'SM','JT','FAI','BUB','HTS','ADMET','HTVS','QSAR','SAR','ML','SALI','SARI','ROGI','CSN','CLN','ANOVA',
            'SRD','ESALI','CYP','QSPR','RR','CT1','MODI','ROGI']
df = pd.DataFrame(data = sorted(abb_list),columns = ['abbrev'])
df.to_csv('abbreviations.csv')