from typing import Union
import _sp_sort


class Pack:
    def __init__(self, _weight, _value, index):
        self.wt = _weight
        self.val = _value
        self.ind = index
        self.cost = _value // _weight

    def __le__(self, other):
        return self.cost < other.cost


class Knapsack:
    _weight = None
    _value = None
    _capacity = None
    _pack = None
    _cur_cap = None
    _cur_val = None
    _is_crumbly = None

    def __init__(self,
                 capacity: Union[int, float],
                 weight: list[Union[int, float]],
                 value: list[Union[int, float]],
                 is_crumbly: bool = False):
        self._value = value
        self._weight = weight
        self._capacity = capacity
        self._is_crumbly = is_crumbly

    def _picker_(self):
        _val_pack = []
        for i in range(len(self._weight)):
            _val_pack.append(Pack(self._weight[i], self._value[i], i))

        _sp_sort._sort_(_val_pack, 0, len(_val_pack) - 1)
        _val_pack.reverse()

        totalValue = 0
        for i in _val_pack:
            curWt = int(i.wt)
            curVal = int(i.val)
            if self._capacity - curWt >= 0:
                self._capacity -= curWt
                totalValue += curVal
                print(curVal)
            else:
                if self._is_crumbly:
                    fraction = self._capacity / curWt
                    totalValue += curVal * fraction
                    self._capacity = int(self._capacity - (curWt * fraction))
                break
        return totalValue

