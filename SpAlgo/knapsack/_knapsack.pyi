from ._pack import Pack as Pack
from typing import Union

class Knapsack:
    def __init__(self, capacity: Union[int, float], weight: list[Union[int, float]], value: list[Union[int, float]], is_crumbly: bool = ..., ultimate_item: bool = ...) -> None: ...
    def getPack(self): ...
    def getTotalValue(self): ...
    def getUsedWeight(self): ...
    def getWastedWeight(self): ...
    def getCrumbledItem(self): ...
