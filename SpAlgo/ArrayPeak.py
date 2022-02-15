from typing import Union


class ArrayPeak:
    _inner_array = []
    _size = 0
    """
    :var _inner_array: 
    """
    def __init__(self, array: list[Union[int, float]]):
        self._inner_array = array
        self._size = len(self._inner_array)

    def findPeak(self) -> tuple[Union[int, float], int]:
        """
        :return: a tuple of peak value and index
        """
        # if there is one element in array return it
        if self._size < 2:
            return self._inner_array[0], 0
    
        # if the first or last element of data array
        if self._inner_array[0] > self._inner_array[1]:
            return self._inner_array[0], 0
        if self._inner_array[(self._size - 1)] > self._inner_array[(self._size - 2)]:
            return self._inner_array[(self._size - 1)], (self._size - 1)
    
        # otherwise
        pointer = self._size // 2
        while True:
            current_element = self._inner_array[pointer]
            if self._inner_array[pointer + 1] > current_element:
                pointer += 1
                current_element = self._inner_array[pointer]
    
            elif self._inner_array[pointer - 1] > current_element:
                pointer -= 1
                current_element = self._inner_array[pointer]
    
            else:
                break
        return current_element, pointer