from SpAlgo import Matrix


def test_Matrix_findPeak():
    """
    :return: None
    """
    _mat = [[10, 8, 10, 10],
            [14, 13, 12, 11],
            [15, 9, 11, 21],
            [16, 17, 19, 20],
            [5, 7, 11, 4]]
    _matrix_peak = Matrix(matrix=_mat)
    assert _matrix_peak.findPeak() == {'peak': 21, 'column': 3, 'row': 2}


def test_Matrix_findAllPeak():
    """
    :return: None
    """
    _mat = [[10, 18, 10, 10],
            [14, 13, 12, 11],
            [15, 9, 11, 21],
            [20, 17, 19, 20],
            [5, 7, 11, 4]]

    _matrix_all_peak = Matrix(matrix=_mat)
    assert _matrix_all_peak.findAllPeak() == [{'peak': 18, 'column': 1, 'row': 0},
                                              {'peak': 21, 'column': 3, 'row': 2},
                                              {'peak': 20, 'column': 0, 'row': 3}]
