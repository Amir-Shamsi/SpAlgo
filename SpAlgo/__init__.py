"""
The python source code.
"""

from SpAlgo._peak._array import Array
from SpAlgo._peak._matrix import Matrix
from SpAlgo._sequences._sequence import MaxSubseq
from SpAlgo._knapsack._knapsack import Knapsack
from SpAlgo._closest_pair._closest import ClosestPair
from SpAlgo._closest_pair._point import Point
from SpAlgo.numerical_analysis.bin_to_float import F32bit, F64bit
from SpAlgo.numerical_analysis.newton_method import Newton
from SpAlgo.numerical_analysis.secant_method import Secant

__version__ = '0.3.1'
__all__ = ['Matrix', 'MaxSubseq', 'Array', 'Knapsack', 'ClosestPair',
           'Point', 'F32bit', 'F64bit', 'Newton', 'Secant']
