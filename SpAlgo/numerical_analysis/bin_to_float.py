import re

class F32bit:
    def __init__(self, binary_sequence: str | list) -> None:
        """
        A number in 32 bit single precision IEEE 754 binary floating point standard representation requires three
         building elements:
            * sign (it takes 1 bit, and it's either 0 for positive or 1 for negative numbers)
            * exponent (8 bits)
            * mantissa (23 bits)

        binary_sequence: The binary sequence in shap of string of list of 0 and 1

        Example
        -------
        >>> bin_seq = '00000100010001000100010010111010'
        >>> f = F32bit(binary_sequence=bin_seq)
        >>> f.get_exponent()
        >>> f.get_significand()
        >>> f.get_floating_point()
        """

        binary_sequence = ''.join(binary_sequence) if isinstance(binary_sequence, list) else binary_sequence

        try:
            if not re.match("^[01]+$", binary_sequence.strip()):
                raise ValueError

            self.bin_seq = [int(item) for item in binary_sequence]

            if len(self.bin_seq) != 32: raise IndexError(f'Binary sequence must be 32-bits but {len(self.bin_seq)}-bits given!')

        except ValueError:
            raise ValueError('Please make sure the binary sequence only contains 0 and 1!')

        self.__calc__()

    def __calc__(self) -> None:
        self._exponent = self._significand = 0

        for index in range(8, 0, -1):
            self._exponent += self.bin_seq[index] * (2 ** (abs(index - 8)))

        for index in range(30, 8, -1):
            self._significand += self.bin_seq[index] * (2 ** (-1 * (abs(index - 31))))

        self._floating_point = ((-1) ** self.bin_seq[0]) * (2 ** (self._exponent - 127)) * (1 + self._significand)

    def get_exponent(self) -> int | float:
        return self._exponent

    def get_significand(self) -> int | float:
        return self._significand

    def get_floating_point(self) -> int | float:
        return self._floating_point


class F64bit:
    def __init__(self, binary_sequence: str) -> None:
        """
        A number in 64 bit single precision IEEE 754 binary floating point standard representation requires three
         building elements:
            * sign (it takes 1 bit, and it's either 0 for positive or 1 for negative numbers)
            * exponent (11 bits)
            * mantissa (52 bits)

        binary_sequence: The binary sequence in shap of string of list of 0 and 1

        Example
        -------
        >>> bin_seq = '0000010001000100010001001011101011010100010001000100010010111010'
        >>> f = F64bit(binary_sequence=bin_seq)
        >>> f.get_exponent()
        >>> f.get_significand()
        >>> f.get_floating_point()
        """
        binary_sequence = ''.join(binary_sequence) if isinstance(binary_sequence, list) else binary_sequence

        try:
            if not re.match("^[01]+$", binary_sequence.strip()):
                raise ValueError

            self.bin_seq = [int(item) for item in binary_sequence]

            if len(self.bin_seq) != 64: raise IndexError(f'Binary sequence must be 64-bits but {len(self.bin_seq)}-bits given!')

        except ValueError:
            raise ValueError('Please make sure the binary sequence only contains 0 and 1!')

        self.__calc__()

    def __calc__(self) -> None:
        self._exponent = self._significand = 0

        for index in range(11, 0, -1):
            self._exponent += self.bin_seq[index] * (2 ** (abs(index - 11)))

        for index in range(63, 11, -1):
            self._significand += self.bin_seq[index] / (2 ** (52 - abs(index - 63)))

        self._floating_point = ((-1) ** self.bin_seq[0]) * (2 ** (self._exponent - 1023)) * (1 + self._significand)

    def get_exponent(self) -> int | float:
        return self._exponent

    def get_significand(self) -> int | float:
        return self._significand

    def get_floating_point(self) -> int | float:
        return self._floating_point