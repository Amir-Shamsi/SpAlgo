from typing import Any

class Pack:
    wt: Any
    val: Any
    ind: Any
    cost: Any
    def __init__(self, _weight, _value, index) -> None: ...
    def __le__(self, other): ...
