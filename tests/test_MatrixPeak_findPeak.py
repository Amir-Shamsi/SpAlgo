from SpAlgo.MatrixPeak import MatrixPeak

def test_findLongestMaxSubSeq():
    """
    :return: None
    """
    _mat = [[10, 8, 10, 10],
           [14, 13, 12, 11],
           [15, 9, 11, 21],
           [16, 17, 19, 20],
           [5, 7, 11, 4]]
    _matrix_peak = MatrixPeak(matrix=_mat)
    assert _matrix_peak.findPeak() == {'peak': 21, 'column': 3, 'row': 2}
