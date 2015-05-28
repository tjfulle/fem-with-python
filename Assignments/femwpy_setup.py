from os import getenv, listdir
from os.path import dirname, isdir, join, realpath
import sys

import numpy as np
import numpy.linalg as la
import sympy as sp

# Insert the fem-with-python directory in the system path.
D = getenv('FEMWPY', dirname(dirname(realpath(__file__))))
if not isdir(D):
    raise OSError('FEMWPY directory not found')
if 'femlib' not in [d for d in listdir(D) if isdir(join(D, d))]:
    raise OSError('Assignments directory does not appear to be '
                  'in the fem-with-python directory')
sys.path.insert(0, D)
