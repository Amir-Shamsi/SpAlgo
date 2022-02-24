from . import _pack


def _partition_(_items: list[_pack.Pack], low, high):
    i = low - 1
    pivot = _items[high]
    for j in range(low, high):
        if _items[j] <= pivot:
            i = i + 1
            _items[i], _items[j] = _items[j], _items[i]

    _items[i + 1], _items[high] = _items[high], _items[i + 1]
    return i + 1

def _sort_(_items, low, high):
    if len(_items) == 1:
        return _items
    if low < high:
        pi = _partition_(_items, low, high)
        _sort_(_items, low, pi - 1)
        _sort_(_items, pi + 1, high)