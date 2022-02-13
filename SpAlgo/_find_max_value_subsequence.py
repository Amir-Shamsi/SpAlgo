from typing import Union


def find_max_subsequence_in_array(seq: list[Union[int, float]]) -> tuple[Union[float, int], list[int]]:
    # variables
    _current_sum = 0
    max_sum = -float('inf')
    _indexes = []
    _last_index = -1
