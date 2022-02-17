from SpAlgo import Array

def test_Array_findAllPeak():
    array = [7, 2, 22, 3, 17, 5, 2, 9, 22, 4]
    res = Array.Array(array)    

    # checking outputs
    assert res.findAllPeaks() == [(7, 0), (22, 2), (17, 4), (22, 8)]
    assert res.findFirstPeak() == (7, 0)
    assert res.findMaxPeak() == (22, 2)
    assert res.findMinPeak() == (7, 0)
    assert res.findPeak() == (17, 4)
    