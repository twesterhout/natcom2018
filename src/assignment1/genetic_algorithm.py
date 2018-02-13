# -*- coding: utf-8 -*-
# MIT License

# Copyright (c) 2018 Jelmer Jansen

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from pathlib import Path
    
def ten_runs(runs,iterations):
    #metascores = []    
    for i in range(0,runs):
        _,_,scores = genetic_one_plus_one(fitness,8,100)
        plt.plot(range(0,iterations),scores)
        plt.xlabel('Iteration')
        plt.ylabel('Fitness')
        plt.savefig(str(_get_current_file_dir() / '..' / '..' / 'doc' /
                  'source' / 'genetic_algorithm.png'))      
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

def _get_current_file_dir() -> Path:
    """Returns the directory of the script."""
    return Path(os.path.realpath(__file__)).parent

def fitness(x):
    return sum(x)
   
ten_runs(10,100)
