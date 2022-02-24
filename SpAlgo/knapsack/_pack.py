class Pack:
    def __init__(self, _weight, _value, index):
        self.wt = _weight
        self.val = _value
        self.ind = index
        self.cost = _value // _weight

    def __le__(self, other):
        return self.cost < other.cost

