# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:53:44 2018

@author: opuser1
"""

import itertools
comb_list=[]
combination=[]
a=['1',2,3,4,5]

for i in range(len(a)):
    combination.append(list(itertools.combinations(a,i+1)))
for i in range (len(combination)):
    for j in range(len(combination[i])):
        comb_list.append(list(combination[i][j]))
print comb_list        