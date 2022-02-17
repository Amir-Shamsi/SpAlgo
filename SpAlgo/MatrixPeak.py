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

    def _is_edge(self, side, row=None, column=None):
        """
        :param row:
        :param column:
        :param side: is one of ['u', 'd', 'l', 'r']
        :return: boolean
        """

        if side == 'u':  # up
            if row - 1 < 0:
                return False
            return True
        elif side == 'd':  # down
            if row + 1 > self._row_size - 1:
                return False
            return True
        elif side == 'l':  # left
            if column - 1 < 0:
                return False
            return True
        elif side == 'r':  # right
            if column + 1 > self._column_size - 1:
                return False
            return True
        return False

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
            if self._is_edge(side='d', row=_current_row):
                if self._inner_matrix[_current_row + 1][_current_column] > current_element:
                    _current_row += 1
                    _any_step = True

            if self._is_edge(side='u', row=_current_row):
                if self._inner_matrix[_current_row - 1][_current_column] > current_element:
                    _current_row -= 1
                    _any_step = True

            if self._is_edge(side='r', column=_current_column):
                if self._inner_matrix[_current_row][_current_column + 1] > current_element:
                    _current_column += 1
                    _any_step = True

            if self._is_edge(side='l', column=_current_column):
                if self._inner_matrix[_current_row][_current_column - 1] > current_element:
                    _current_column -= 1
                    _any_step = True

            if not _any_step:
                break

            _any_step = False

            current_element = self._inner_matrix[_current_row][_current_column]

        return {'peak': current_element, 'column': _current_column, 'row': _current_row}

    def _matrix_next_step(self, row, column, step=1):
        """
        this function help to go through the matrix cells.

        :param row: current row
        :param column: current column
        :param step: step forward
        :return: next row and next column
        """
        _next_row = row
        _next_column = column
        for _s_f in range(step):
            _next_column = (column + 1) % self._column_size
            if _next_column == 0:
                _next_row = (row + 1)

        return _next_row, _next_column

    def findAllPeak(self) -> list[dict[str, Union[int, float]]]:
        _status_matrix = []
        _col_mat_st = []
        for column in range(self._column_size):
            _col_mat_st.append(True)
        for row in range(self._row_size):
            _status_matrix.append(_col_mat_st.copy())

        _found_peaks = []

        _current_column = 0
        _current_row = 0
        _any_step = False

        while True:

            if _current_row > self._row_size - 1:
                break

            current_element = self._inner_matrix[_current_row][_current_column]
            _status = _status_matrix[_current_row][_current_column]
            _side_status = 0
            _complete_side_status = 0
            _forward_step = 1

            if not _status:
                _current_row, _current_column = self._matrix_next_step(_current_row, _current_column)
                continue

            if self._is_edge(side='u', row=_current_row):
                _complete_side_status += 1
                if current_element >= self._inner_matrix[_current_row - 1][_current_column]:
                    _side_status += 1
                    if current_element != self._inner_matrix[_current_row - 1][_current_column]:
                        _status_matrix[_current_row - 1][_current_column] = False

            if self._is_edge(side='d', row=_current_row):
                _complete_side_status += 1
                if current_element >= self._inner_matrix[_current_row + 1][_current_column]:
                    _side_status += 1
                    if current_element != self._inner_matrix[_current_row + 1][_current_column]:
                        _status_matrix[_current_row + 1][_current_column] = False

            if self._is_edge(side='r', column=_current_column):
                _complete_side_status += 1
                if current_element >= self._inner_matrix[_current_row][_current_column + 1]:
                    _side_status += 1
                    if current_element != self._inner_matrix[_current_row][_current_column + 1]:
                        _status_matrix[_current_row][_current_column + 1] = False
                        _forward_step = 2

            if self._is_edge(side='l', column=_current_column):
                _complete_side_status += 1
                if current_element >= self._inner_matrix[_current_row][_current_column - 1]:
                    _side_status += 1
                    if current_element != self._inner_matrix[_current_row][_current_column - 1]:
                        _status_matrix[_current_row][_current_column - 1] = False

            if _side_status == _complete_side_status:
                _found_peaks.append({'peak': current_element, 'column': _current_column, 'row': _current_row})

            _current_row, _current_column = self._matrix_next_step(_current_row, _current_column, _forward_step)

        return _found_peaks
