from typing import Union
from . import _qsort
from ._pack import Pack


class Knapsack:
    """
    The Knapsack Problem is a famous Dynamic Programming Problem that falls
     in the optimization category.

    It derives its name from a scenario where, given a set of items with
    specific weights and assigned values, the goal is to maximize the value
    in a knapsack while remaining within the weight constraint.

    Each item can only be selected once, as we don’t have multiple quantities
     of any item.
    """
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
    _infinite_item = None

    def __init__(self,
                 capacity: Union[int, float],
                 weight: list[Union[int, float]],
                 value: list[Union[int, float]],
                 is_crumbly: bool = False,
                 infinite_item: bool = False):
        """
        Initial class fields
        :param capacity: the capacity of the knapsack.
        :param weight: the array of item weights.
        :param value: the array of item values.
        :param is_crumbly: if items are crumbly so make it True. [default is False]
        :param infinite_item: if there is infinite count of items make it True. [default is False]
        """
        self._infinite_item = infinite_item
        self._value = value
        self._weight = weight
        self._capacity = capacity
        self._st_capacity = capacity
        self._is_crumbly = is_crumbly

        self._picker_()

    def getPack(self):
        """
        :return: items of knapsack
        """
        return self._pack

    def getTotalValue(self):
        """
        :return: knapsack total value
        """
        return self._total_value

    def getUsedWeight(self):
        """
        :return: used weight of the knapsack
        """
        return self._st_capacity - self._capacity

    def getWastedWeight(self):
        """
        :return: Wasted weight of the knapsack
        """
        return self._capacity

    def getCrumbledItem(self):
        """
        :return: the item which is crumbled
        the formate is:
             {
                'weight': ---,
                'value': ---,
                'original_weight': ---,
                'original_value': ---
            }
        """
        return self._crumbled_item

    def _picker_(self):
        """
        this will execute the knapsack problem
        """
        _val_pack = []
        self._pack = []
        for item in range(len(self._weight)):
            _val_pack.append(Pack(self._weight[item], self._value[item], item))

        _qsort._sort_(_val_pack, 0, len(_val_pack) - 1)
        _val_pack.reverse()

        self._total_value = 0

        if not self._infinite_item:
            for item in _val_pack:
                _cur_wt = int(item.wt)
                _cur_val = int(item.val)
                if self._capacity - _cur_wt >= 0:
                    self._itm_pack_(_cur_wt, _cur_val)
                else:
                    self._add_crumble_(_cur_wt, _cur_val)
                    break
        else:
            _inner_index = 0
            while True:
                _cur_wt = _val_pack[_inner_index].wt
                _cur_val = _val_pack[_inner_index].val

                if _val_pack[_inner_index].wt <= self._capacity:
                    self._itm_pack_(_cur_wt, _cur_val)

                if _cur_wt > self._capacity and not self._is_crumbly:
                    _inner_index += 1
                elif _cur_wt > self._capacity and self._is_crumbly:
                    self._add_crumble_(_cur_wt, _cur_val)
                    break

                if _inner_index == len(_val_pack):
                    self._add_crumble_(_cur_wt, _cur_val)
                    break

    def _add_crumble_(self, _cur_wt, _cur_val):
        """
        add crumbled item
        :param _cur_wt:
        :param _cur_val:
        :return:
        """
        if self._is_crumbly:
            fraction = self._capacity / _cur_wt
            self._total_value += _cur_val * fraction
            self._capacity = int(self._capacity - (_cur_wt * fraction))
            self._pack.append({'weight': _cur_wt * fraction, 'value': _cur_val * fraction})
            self._crumbled_item = {'weight': _cur_wt * fraction, 'value': _cur_val * fraction,
                                   'original_weight': _cur_wt, 'original_value': _cur_val}

    def _itm_pack_(self, _cur_wt, _cur_val):
        self._capacity -= _cur_wt
        self._total_value += _cur_val
        self._pack.append({'weight': _cur_wt, 'value': _cur_val})
