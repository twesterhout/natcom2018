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


from typing import TypeVar, Callable, Tuple
from pathlib import Path
import os
import sys
import numpy as np

T = TypeVar('T')

def _get_current_file_dir() -> Path:
    """Returns the directory of the script."""
    return Path(os.path.realpath(__file__)).parent


def fake_monte_carlo(f: Callable[[int], T], n: int, iterations: int,
                     out = None) -> Tuple[np.array, T]:
    max_f = 0
    max_x = None
    for (x, fx) in map(lambda y: (y, f(y)),
                       (np.random.choice([0, 1], n) for i in
                        range(iterations))):
        max_x, max_f = (x, fx) if fx > max_f else (max_x, max_f)
        if out:
            print(max_f, file=out)
    return max_x, max_f


def fitness(x):
    return sum(x)


def main():

    for i in range(1, 11):
        with open(_get_current_file_dir() / '..' / '..' / 'data' /
                  'assignment1' / Path('fake_monte_carlo_' + str(i) + '.dat'),
                  'w') as out:
            fake_monte_carlo(fitness, 100, 1500, out)


if __name__ == '__main__':
    main()
