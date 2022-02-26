from ._pack import Pack as Pack
from typing import Union

class Knapsack:
    def __init__(self, capacity: Union[int, float], weight: list[Union[int, float]], value: list[Union[int, float]], is_crumbly: bool = ..., infinite_item: bool = ...) -> None:
        self._value = None
        self._weight = None
        self._infinite_item = None
        self._is_crumbly = None
        self._crumbled_item = None
        self._capacity = None
        self._st_capacity = None
        self._pack = None
        self._total_value = None
        ...
    def getPack(self): ...
    def getTotalValue(self): ...
    def getUsedWeight(self): ...
    def getWastedWeight(self): ...
    def getCrumbledItem(self): ...

    def _picker_(self):
        pass

    def _add_crumble_(self, _cur_wt, _cur_val):
        pass

    def _itm_pack_(self, _cur_wt, _cur_val):
        pass
