from typing import Union


class MatrixPeak:
    _inner_matrix = None
    _column_size = None
    _row_size = None

    def __init__(self, matrix: list[list[Union[int, float]]]):
        """
        :param matrix: initial the _inner_matrix with matrix given
        to the MatrixPeak.
        we will initial these variables as well:
            * :var _column_size
            * :var _row_size
        """
        self._inner_matrix = matrix
        self._row_size = len(matrix)
        self._column_size = len(matrix[0])

    def _findMaxOfColumn(self, column):
        _max = - float('inf')
        _row = None
        for row in range(self._row_size):
            if _max < self._inner_matrix[row][column]:
                _max = self._inner_matrix[row][column]
                _row = row
        return _max, _row

    def findPeak(self) -> dict[str, Union[int, float]]:
        """
        Function will find a peak inside the given matrix.

        :return: a dictionary contains these elements->
            * :var peak: contain the peak found inside matrix.
            * :var column: the column of the peak has been found.
            * :var row: the row of the peak has been found.
        """
        _middle_column = (self._column_size - 1) // 2

        _middle_column_max_element, _max_element_row = self._findMaxOfColumn(column=_middle_column)

        _current_column = _middle_column
        _current_row = _max_element_row

        _any_step = False
        while True:
            current_element = self._inner_matrix[_current_row][_current_column]
            if _current_row + 1 <= self._row_size - 1:
                if self._inner_matrix[_current_row + 1][_current_column] > current_element:
                    _current_row += 1
                    _any_step = True

            if _current_row - 1 > 0:
                if self._inner_matrix[_current_row - 1][_current_column] > current_element:
                    _current_row -= 1
                    _any_step = True

            if _current_column + 1 <= self._column_size - 1:
                if self._inner_matrix[_current_row][_current_column + 1] > current_element:
                    _current_column += 1
                    _any_step = True

            if _current_column - 1 > 0:
                if self._inner_matrix[_current_row][_current_column - 1] > current_element:
                    _current_column -= 1
                    _any_step = True

            if not _any_step:
                break

            _any_step = False

            current_element = self._inner_matrix[_current_row][_current_column]

        return {'peak': current_element, 'column': _current_column, 'row': _current_row}
