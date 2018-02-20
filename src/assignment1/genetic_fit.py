#!/usr/bin/env python3


# MIT License
#
# Copyright (c) 2018 Tom Westerhout
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path
import os
import numpy as np
from gplearn.genetic import SymbolicRegressor


def _get_current_file_dir() -> Path:
    """Returns the directory of the script."""
    return Path(os.path.realpath(__file__)).parent


def read_data() -> np.array:
    return np.loadtxt(str(_get_current_file_dir() / '..' / '..' / 'data' /
                          'assignment1' / 'genetic_data.dat'))


def main():
    data = read_data()
    regressor = SymbolicRegressor(population_size=1000,
                                  generations=100,
                                  const_range=(.0, .0),
                                  init_depth=(2, 10),
                                  init_method='grow',
                                  function_set=('add', 'sub', 'mul', 'div',
                                                'log', 'sin', 'cos'),
                                  p_crossover=0.7,
                                  p_subtree_mutation=0.0,
                                  p_hoist_mutation=0.0,
                                  p_point_mutation=0.0,
                                  verbose=1,
                                  n_jobs=-1)
    (n, _) = data.shape
    regressor.fit(data[:, 0].reshape(n, 1), data[:, 1])
    print(regressor._program)


if __name__ == '__main__':
    main()
