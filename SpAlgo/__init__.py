"""
The python source code.
"""

from SpAlgo._peak._array import Array
from SpAlgo._peak._matrix import Matrix
from SpAlgo._sequences._sequence import MaxSubseq
from SpAlgo._knapsack._knapsack import Knapsack
from SpAlgo._closest_pair._closest import ClosestPair
from SpAlgo._closest_pair._point import Point

__version__ = '0.3.1'
__all__ = ['Matrix', 'MaxSubseq', 'Array', 'Knapsack', 'ClosestPair',
           'Point']
