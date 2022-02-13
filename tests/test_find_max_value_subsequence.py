from SpAlgo import _find_max_value_subsequence

def test_find_max_value_subsequence():
    _sequence = [-0.43935954,  0.36545751,  0.34194459,  1.17144381, 0.81346123,  1.11793036,
                 1.38030105,  0.01133961, -0.72806449,  0.6211909,  -0.49041476, -2.13556865,
                 -0.07442468,  0.59530056, -1.98011873,  0.61534235,  0.88164606,  1.54469791,
                 -1.68645546,  0.11235733]
    assert _find_max_value_subsequence.find_max_subsequence_in_array(_sequence) == (5.20187816, [1, 7])