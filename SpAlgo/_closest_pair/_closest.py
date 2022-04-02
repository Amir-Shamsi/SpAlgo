import math
import copy
from ._point import Point


class ClosestPair:
    _size = None
    _points_set: list[Point] = None
    _min_distance = None
    _min_pairs = {}

    """
    ClosestPair class to find the smallest distance from a given set of points.
    :argument _size
    :argument _points_set
    :argument _min_distance
    """

    def __init__(self, points_set: list[list[int, float]] | list[tuple] | list[Point]) -> None:
        """
        The Class that finds the smallest distance. This method mainly uses _closest_util()
        :param points_set: set of the Points
        """
        if not isinstance(points_set[0], Point):
            self._init_points(points_set)
        else:
            self._points_set = points_set

        self._points_set.sort(key=lambda point: point.x)
        self._size = len(points_set)
        _set_d_copy = copy.deepcopy(self._points_set)
        _set_d_copy.sort(key=lambda point: point.y)

        """Use recursive function _closest_unit() to find the smallest distance"""
        self._min_distance = self._closest_util(self._points_set, _set_d_copy, self._size)

    def _init_points(self, _points_set) -> None:
        self._points_set = [Point(point[0], point[1]) for point in _points_set]

    @staticmethod
    def _dist_cal(f_point, s_point):
        """
         A utility function to find the distance between two points
        :param f_point: first point
        :param s_point: second point
        :return: the calculated distance
        """
        return math.sqrt((f_point.x - s_point.x) *
                         (f_point.x - s_point.x) +
                         (f_point.y - s_point.y) *
                         (f_point.y - s_point.y))

    def _brute_force_algo(self, _points_set, _size):
        """
        A Brute Force method to return the smallest distance between two points in P[] of size _size
        this only use for the small size of _set
        :return: the distance of the closest pair
        """
        min_val = float('inf')
        for i in range(_size):
            for j in range(i + 1, _size):
                if self._dist_cal(_points_set[i], _points_set[j]) < min_val:
                    min_val = self._dist_cal(_points_set[i], _points_set[j])
                    self._min_pairs[min_val] = [_points_set[i], _points_set[j]]

        return min_val

    def _strip_closest(self, _strip, _size, _dist):
        """
        A utility function to find the distance between the closest points of
        strip of given size. All points in strip[] are sorted according to
        y coordinate. They all have an upper bound on minimum distance as d.
        Note that this method seems to be a O(n^2) method, but it's a O(n)
        method as the inner loop runs at most 6 times
        :param _strip:
        :param _size:
        :param _dist:
        :return:
        """

        """Initialize the minimum distance as _dist"""
        min_val = _dist

        """
        Pick all points one by one and
        try the next points till the difference
        between y coordinates is smaller than d.
        This is a proven fact that this loop
        runs at most 6 times
        """
        for i in range(_size):
            j = i + 1
            while j < _size and (_strip[j].y - _strip[i].y) < min_val:
                min_val = self._dist_cal(_strip[i], _strip[j])
                self._min_pairs[min_val] = [_strip[i], _strip[j]]
                j += 1

        return min_val

    def _closest_util(self, _point_set: list[Point], _set_d_copy: list[Point], _size: int):
        """
        A recursive function to find the smallest distance. The array P contains
        all points sorted according to x coordinate.
        :param _point_set: set of points
        :param _set_d_copy: the deep copy of the points set
        :param _size: size of the set
        :return: Find the closest points in strip. Return the minimum of d and closest distance is strip[]
        """
        """
        If there are 2 or 3 points, then use brute force to not take so much memory
        """
        if _size <= 3:
            return self._brute_force_algo(_point_set, _size)

        """Find the middle point"""
        mid = _size // 2
        midPoint = _point_set[mid]

        """keep a copy of left and right branch"""
        _set_l, _set_r = _point_set[:mid], _point_set[mid:]

        """
        Consider the vertical line passing through the middle point calculate
        the smallest distance dl on left of middle point and dr on right side
        """
        dl = self._closest_util(_set_l, _set_d_copy, mid)
        dr = self._closest_util(_set_r, _set_d_copy, _size - mid)
        di = min(dl, dr)

        """
        Build an array strip[] that contains points close (closer than d)
        to the line passing through the middle point
        """
        strip_p, strip_dp = [], []
        lr = _set_l + _set_r
        for i in range(_size):
            if abs(lr[i].x - midPoint.x) < di:
                strip_p.append(lr[i])
            if abs(_set_d_copy[i].x - midPoint.x) < di:
                strip_dp.append(_set_d_copy[i])

        strip_p.sort(key=lambda point: point.y)
        min_a = min(di, self._strip_closest(strip_p, len(strip_p), di))
        min_b = min(di, self._strip_closest(strip_dp, len(strip_dp), di))

        return min(min_a, min_b)

    def get_min_distance(self):
        return self._min_distance

    def get_closest_pair(self, _type: type = Point):
        pairs = self._min_pairs[self._min_distance]
        if _type == Point:
            return pairs
        return [_type([pairs[0].x, pairs[1].y]), _type([pairs[1].x, pairs[1].y])]
