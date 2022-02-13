from typing import Union


def find_max_subsequence_in_array(seq: list[Union[int, float]]) -> tuple[Union[float, int], list[int]]:
    # variables
    _current_sum = 0
    max_sum = -float('inf')
    _indexes = []
    _last_index = -1
    """
        Calculate the maximum value of longest subsequence of the
         sequence given to the function;
        The given sequence is a list of type int or float by the
         other word must be a numerical list.

        All list's elements can have different type:
            * float
            * integer

       :param seq: sequence of numbers
       :return: returns a tuple of following information->
            |---- 1. first element is the max sum of the sequence
            +-----2. the second is a list of  start and end index
       :var _current_sum: every element of list we go through will
            be added to this variable
       :var _indexes: will hold the first index of the the subsequence
       :var max_sum: will hold the max sum of the longest subsequence
       :var _last_index: will hold the last index of subsequence
    """
    for _index in range(len(seq)):
        _current_sum += seq[_index]
        _indexes.append(_index)
        if _current_sum < 0:
            _current_sum = 0
            _indexes.clear()
        if _current_sum > max_sum:
            max_sum = _current_sum
            _last_index = _index
    return max_sum, [_indexes[0], _last_index]
