from SpAlgo import MaxSubseq

def test_findLongestMaxSubseq():
    _sequence = [-0.43935954,  0.36545751,  0.34194459,  1.17144381, 0.81346123,  1.11793036,
                 1.38030105,  0.01133961, -0.72806449,  0.6211909,  -0.49041476, -2.13556865,
                 -0.07442468,  0.59530056, -1.98011873,  0.61534235,  0.88164606,  1.54469791,
                 -1.68645546,  0.11235733]
    _res = MaxSubseq(_sequence)

    # checking the outputs
    assert _res.maximum_sum() == 5.20187816
    assert _res.start_index == 1
    assert _res.end_index == 7

    assert _res.subsequence() == [0.36545751,  0.34194459,  1.17144381, 0.81346123,  1.11793036,
                                 1.38030105,  0.01133961]