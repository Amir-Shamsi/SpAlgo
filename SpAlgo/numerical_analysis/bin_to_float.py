import re

class F32bit:
    def __init__(self, binary_sequence):
        try:
            if not re.match("^[01]+$", binary_sequence.strip()):
                raise ValueError

            self.bin_seq = [int(item) for item in binary_sequence]

            if len(self.bin_seq) != 32: raise IndexError(f'Binary sequence must be 32-bits but {len(self.bin_seq)}-bits given!')

        except ValueError:
            raise ValueError('Please make sure the binary sequence only contains 0 and 1!')

        self.__calc__()

    def __calc__(self):
        self._exponent = self._significand = 0

        for index in range(8, 0, -1):
            self._exponent += self.bin_seq[index] * (2 ** (abs(index - 8)))

        for index in range(30, 8, -1):
            self._significand += self.bin_seq[index] * (2 ** (-1 * (abs(index - 31))))

        self._floating_point = ((-1) ** self.bin_seq[0]) * (2 ** (self._exponent - 127)) * (1 + self._significand)

    def get_exponent(self):
        return self._exponent

    def get_significand(self):
        return self._significand

    def get_floating_point(self):
        return self._floating_point
