import operator

class MaximaSet:
    __set = None
    __maxima_point = None

    def __init__(self, points_set):  # list[Any[int, float]]
        self.__set = points_set

        self.__set = sorted(self.__set, key=operator.itemgetter(0))  # x
        self.__fine_maxima_set(begin=0, end=len(points_set))

    def __fine_maxima_set(self, begin, end):
        if end - begin == 1:
            return self.__set[begin]

        _l_set = self.__fine_maxima_set(begin=begin, end=end // 2)
        _r_set = self.__fine_maxima_set(begin=end - end // 2, end=end)

        _merged_set = [_l_set, _r_set]

        self.__maxima_point = []

        _merged_set = sorted(_merged_set, key=operator.itemgetter(1))  # y
        _merged_set.reverse()

        _right_point_skip_flag = False
        for _point in _merged_set:
            if _point[0] > end // 2:
                _right_point_skip_flag = True
                self.__maxima_point.append(_point)
            elif _point[0] < end // 2 and not _right_point_skip_flag:
                self.__maxima_point.append(_point)

    def getMaximaSet(self):
        return self.__maxima_point

    def getMaximaCount(self):
        return len(self.__maxima_point)
