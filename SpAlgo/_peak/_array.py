from typing import Union


class Array:
    _inner_array = []
    _size = 0
    _all_peaks = []
    """
    :var _inner_array: 
    """
    def __init__(self, array: list[Union[int, float]]):
        self._inner_array = array
        self._size = len(self._inner_array)
        self._all_peaks = Array.findAllPeaks(self)

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

    def findAllPeaks(self) -> list[tuple[Union[int, float]], int]:
        """
        :return: a list of tuples of All Peaks
        """
        list_of_peaks = []
        if self._inner_array[0] > self._inner_array[1]:
            list_of_peaks += [(self._inner_array[0], 0)]
        for i in range(1, self._size - 1):
            current_element = self._inner_array[i]
            if (current_element > self._inner_array[i + 1]) and (current_element > self._inner_array[i - 1]):
                list_of_peaks += [(self._inner_array[i], i)]

        if self._inner_array[self._size - 1] > self._inner_array[self._size - 2]:
            list_of_peaks += [(self._inner_array[self._size-1], self._size - 1)]

        return list_of_peaks


    
    """
        var _all_peaks defined to use in functions below
    """

    def findFirstPeak(self) -> tuple[int, int]:
        first_peak = self._all_peaks[0][0]
        return first_peak, self._inner_array.index(first_peak) 

    def findMaxPeak(self) -> tuple[int, int]:
        """
        :return the FIRST maximum peak
        """
        max_peak = max(self._all_peaks)[0]
        return max_peak, self._inner_array.index(max_peak) 

    def findMinPeak(self) -> tuple[int, int]:
        """
        :return the FIRST minimum peak
        """
        min_peak = min(self._all_peaks)[0]
        return min_peak, self._inner_array.index(min_peak)


    
        
    

