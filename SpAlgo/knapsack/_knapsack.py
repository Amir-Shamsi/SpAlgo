from typing import Union
from . import _qsort
from ._pack import Pack

class Knapsack:
    _weight = None
    _value = None
    _capacity = None
    _st_capacity = None
    _pack = None
    _cur_cap = None
    _cur_val = None
    _is_crumbly = None
    _total_value = None
    _crumbled_item = None
    _ultimate_item = None

    def __init__(self,
                 capacity: Union[int, float],
                 weight: list[Union[int, float]],
                 value: list[Union[int, float]],
                 is_crumbly: bool = False,
                 ultimate_item: bool = False):
        self._ultimate_item = ultimate_item
        self._value = value
        self._weight = weight
        self._capacity = capacity
        self._st_capacity = capacity
        self._is_crumbly = is_crumbly

        self._picker_()

    def _picker_(self):
        _val_pack = []
        self._pack = []
        for item in range(len(self._weight)):
            _val_pack.append(Pack(self._weight[item], self._value[item], item))

        _qsort._sort_(_val_pack, 0, len(_val_pack) - 1)
        _val_pack.reverse()

        self._total_value = 0

        if not self._ultimate_item:
            for item in _val_pack:
                _cur_wt = int(item.wt)
                _cur_val = int(item.val)
                if self._capacity - _cur_wt >= 0:
                    self._capacity -= _cur_wt
                    self._total_value += _cur_val
                    self._pack.append({'weight': _cur_wt, 'value': _cur_val})
                else:
                    if self._is_crumbly:
                        fraction = self._capacity / _cur_wt
                        self._total_value += _cur_val * fraction
                        self._capacity = int(self._capacity - (_cur_wt * fraction))
                        self._pack.append({'weight': _cur_wt * fraction, 'value': _cur_val * fraction})
                        self._crumbled_item = {'weight': _cur_wt * fraction, 'value': _cur_val * fraction,
                                               'original_weight': _cur_wt, 'original_value': _cur_val}
                    break
        else:
            _inner_index = 0
            while True:
                _cur_wt = _val_pack[_inner_index].wt
                _cur_val = _val_pack[_inner_index].val
                if _val_pack[_inner_index].wt <= self._capacity:
                    self._capacity -= _cur_wt
                    self._total_value += _cur_val
                    self._pack.append({'weight': _cur_wt, 'value': _cur_val})

                if _cur_wt > self._capacity:
                    _inner_index += 1

                if _inner_index == len(_val_pack):
                    break

    def getPack(self):
        return self._pack

    def getTotalValue(self):
        return self._total_value

    def getUsedWeight(self):
        return self._st_capacity - self._capacity

    def getWastedWeight(self):
        return self._capacity

    def getCrumbledItem(self):
        return self._crumbled_item
