from typing import Union

class LongestMax:
    _sequence = None
    _maximum_summation = None
    start_index = -1
    end_index = -1
    """
        :var sequence: sequence of numbers which will be given at first
    """

    def __init__(self, sequence: list[Union[int, float]]):
        """
            The given sequence is a list of type int or float by the
             other word must be a numerical list.

            All list's elements can have different types:
                * float
                * integer
            :param sequence: sequence of numbers which will be given at first
        """
        self.sequence = sequence
    def __calculate_max_longest_subsequence(self):
        # variables
        _current_sum = 0
        max_sum = -float('inf')
        _indexes = []
        _last_index = -1
        for _index in range(len(self.sequence)):
            _current_sum += self.sequence[_index]
            _indexes.append(_index)
            if _current_sum < 0:
                _current_sum = 0
                _indexes.clear()
            if _current_sum > max_sum:
                max_sum = _current_sum
                _last_index = _index

        self._maximum_summation = max_sum
        self.start_index = _indexes[0]
        self.end_index = _last_index
        return

