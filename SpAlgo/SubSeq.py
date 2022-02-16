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
        self.__calculate_max_longest_subsequence()

    def __calculate_max_longest_subsequence(self):
        """
          the calculate_max_longest_subsequence will calculate the maximum value of the
            longest subsequence

            type:
           :return: returns no info but will store following information->
                |---- 1. first element is the max sum of the sequence
                +-----2. the second is index of start and end of the
                         subsequence
        """
        # variables
        _current_sum = 0
        max_sum = -float('inf')
        _indexes = []
        _last_index = -1
        """
          type:
           :var _current_sum: every element of list we go through will
                be added to this variable
           :var _indexes: will hold the first index of the the subsequence
           :var max_sum: will hold the max sum of the longest subsequence
           :var _last_index: will hold the last index of subsequence
        """
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

    def maximum_sum(self):
        """
        :return: the maximum value of the subsequence
        """
        return self._maximum_summation

    def subsequence(self):
        """
        :return: will return the subsequence which is found as longest with
                 maximum summation
        """
        return self.sequence[self.start_index: self.end_index + 1]