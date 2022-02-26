from SpAlgo import Knapsack

def test_Knapsack():
    _wt0 = [15, 10, 2, 4, 1]
    _val0 = [30, 25, 2, 6, 0.5]
    _cap0 = 30

    _ks0 = Knapsack(_cap0, _wt0, _val0)

    assert _ks0.getPack() == [{'weight': 10, 'value': 25},
                              {'weight': 15, 'value': 30},
                              {'weight': 4, 'value': 6}]

    assert _ks0.getTotalValue() == 61
    assert _ks0.getUsedWeight() == 29
    assert _ks0.getWastedWeight() == 1

    _wt1 = [15, 10, 2, 4, 1]
    _val1 = [30, 25, 2, 6, 0.5]
    _cap1 = 30.5

    _ks1 = Knapsack(_cap1, _wt1, _val1, is_crumbly=True)
    assert _ks1.getPack() == [{'weight': 10, 'value': 25},
                              {'weight': 15, 'value': 30},
                              {'weight': 4, 'value': 6},
                              {'weight': 1.5, 'value': 1.5}]

    assert _ks1.getTotalValue() == 62.5
    assert _ks1.getUsedWeight() == 30.5
    assert _ks1.getWastedWeight() == 0
    assert _ks1.getCrumbledItem() == {'original_value': 2, 'original_weight': 2, 'value': 1.5, 'weight': 1.5}

    _wt2 = [15, 10, 3, 7, 2]
    _val2 = [30, 25, 2, 6, 0.5]
    _cap2 = 48

    _ks2 = Knapsack(_cap2, _wt2, _val2, infinite_item=True)
    assert _ks2.getPack() == [{'weight': 10, 'value': 25},
                              {'weight': 10, 'value': 25},
                              {'weight': 10, 'value': 25},
                              {'weight': 10, 'value': 25},
                              {'weight': 7, 'value': 6}]

    assert _ks2.getTotalValue() == 106
    assert _ks2.getUsedWeight() == 47
    assert _ks2.getWastedWeight() == 1

    _wt3 = [15, 10, 3, 7, 2]
    _val3 = [30, 25, 2, 6, 0.5]
    _cap3 = 48

    _ks3 = Knapsack(_cap3, _wt3, _val3, is_crumbly=True, infinite_item=True)
    assert _ks3.getPack() == [{'weight': 10, 'value': 25},
                              {'weight': 10, 'value': 25},
                              {'weight': 10, 'value': 25},
                              {'weight': 10, 'value': 25},
                              {'weight': 8.0, 'value': 20.0}]

    assert _ks3.getTotalValue() == 120
    assert _ks3.getUsedWeight() == 48
    assert _ks3.getWastedWeight() == 0
