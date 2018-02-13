# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:47:49 2018

@author: jelmer
"""
import numpy as np


def fake_monte_carlo(f,n,iterations):
    x = max((np.random.choice([0,1],n) for i in range(iterations)),key=f)    
    return x, f(x)
    
def fake_monte_carlo(f,n,iterations):
    mutation rate = 1 / float(n)
    

def fitness(x):
    return sum(x)
   
print(fake_monte_carlo(fitness,8,100))