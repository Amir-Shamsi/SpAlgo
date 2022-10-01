from typing import Callable


class Secant:
    def __init__(self, function: Callable):
        """
            Approximate solution of f(x)=0 on interval [a,b] by the secant method.

            Parameters
            ----------
            function : function
                The function for which we are trying to approximate a solution f(x)=0.

            Examples
            --------
            >>> f = lambda x: x**2 - x - 1
            >>> s = Secant(f)
            >>> s.solve(1, 2, 5)
            1.6180257510729614

        """

        self.func = function

    def solve(self, a: int | float, b: int | float, N) -> int | float:
        """
            Parameters
            ----------
            a, b : numbers
                The interval in which to search for a solution. The function returns
                None if f(a)*f(b) >= 0 since a solution is not guaranteed.
            N : (positive) integer
                The number of iterations to implement.

            Returns
            -------
            m_N : number
                The x intercept of the secant line on the Nth interval
                    m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
                The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
                for some intercept m_n then the function returns this solution.
                If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
                iterations, the secant method fails and return None.

        """
        if self.func(a) * self.func(b) >= 0:
            raise Exception('Secant method fails!')

        a_n, b_n = a, b

        for n in range(1, N + 1):
            m_n = a_n - self.func(a_n) * (b_n - a_n) / (self.func(b_n) - self.func(a_n))

            f_m_n = self.func(m_n)

            if self.func(a_n) * f_m_n < 0: a_n, b_n = a_n, m_n

            elif self.func(b_n) * f_m_n < 0: a_n, b_n = m_n, b_n

            elif f_m_n == 0: return m_n

            else: raise Exception('Secant method fails!')

        return a_n - self.func(a_n) * (b_n - a_n) / (self.func(b_n) - self.func(a_n))