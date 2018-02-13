# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:47:49 2018

@author: jelmer
"""
import numpy as np
import matplotlib.pyplot as plt
    
def ten_runs(runs,iterations):
    #metascores = []    
    for i in range(0,runs):
        _,_,scores = genetic_one_plus_one(fitness,8,100)
        plt.plot(range(0,iterations),scores)
        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.savefig('genetic_algorithm.png')        
        #metascores.append(scores)
    
def genetic_one_plus_one(f,n,iterations):
    mutation_rate = 1 / float(n)
    x = np.random.choice([0,1],n)
    scores = []
    for i in range(0,iterations):
        x2 = np.array([0 for x in range(0,n)])
        for i in range(n):
            if(np.random.uniform() < mutation_rate):
                x2[i] = 1 - x[i]
            else:
                x2[i] = x[i]
        if(f(x2) > f(x)):
            x = x2
        scores.append(f(x))
    return x, f(x), scores
        

def fitness(x):
    return sum(x)
   
ten_runs(10,100)