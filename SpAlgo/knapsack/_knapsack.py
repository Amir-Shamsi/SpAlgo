

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

