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

    def findPeak(self) -> dict[str, Union[int, float]]:
        _middle_column = self._column_size // 2
        _middle_column_max_element = max(self._inner_matrix[_middle_column])

        _max_element_row = self._inner_matrix[_middle_column].index(_middle_column_max_element)
        
        _current_column = _middle_column_max_element
        _current_row = _max_element_row
        while True:
            current_element = self._inner_matrix[_current_column][_current_row]
            if self._inner_matrix[_current_column][_current_row + 1] > current_element:
                _current_row += 1

            elif self._inner_matrix[_current_column][_current_row - 1] > current_element:
                _current_row -= 1

            elif self._inner_matrix[_current_column + 1][_current_row] > current_element:
                _current_column += 1

            elif self._inner_matrix[_current_column - 1][_current_row] > current_element:
                _current_column -= 1

            else:
                break

            current_element = self._inner_matrix[_current_column][_current_row]

        return {'peak': current_element, 'column': _current_column, 'row': _current_row}
