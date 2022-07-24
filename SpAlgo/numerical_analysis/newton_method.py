from typing import Callable, Any

class Newton:
    def __init__(self, function: Callable, derivative_function: Callable) -> None:
        """Approximate solution of f(x)=0 by Newton's method.

            Parameters
            ----------
            function : `function`
                Function for which we are searching for a solution f(x)=0.
            derivative_function : `function`
                Derivative of f(x).

            Examples
            --------
            >>> f = lambda x: x**2 - x - 1
            >>> Df = lambda x: 2*x - 1
            >>> N = Newton(f, Df)
            >>> N.solve(1, 1e-8, 10)
            Found solution after 5 iterations.
            1.618033988749989
        """

        self.func = function
        self.de_func = derivative_function

    def solve(self, x0: int | float, epsilon: int | float, max_iter: int) -> tuple[int | float | Any, int]:
        """
            Parameters
                ----------
                x0 : `number`
                    Initial guess for a solution f(x)=0.
                epsilon : `number`
                    Stopping criteria is abs(f(x)) < epsilon.
                max_iter : `integer`
                    Maximum number of iterations of Newton's method.

            Returns
            -------
                xn : `number`
                    Implement Newton's method: compute the linear approximation
                    of f(x) at xn and find x intercept by the formula
                        x = xn - f(xn)/Df(xn)
                    Continue until abs(f(xn)) < epsilon and return xn.
                    If Df(xn) == 0, return None. If the number of iterations
                    exceeds max_iter, then return None.

        """
        xn = x0

        for n in range(0, max_iter):
            fxn = self.func(xn)

            if abs(fxn) < epsilon:
                return xn, n

            de_f_xn = self.de_func(xn)

            if de_f_xn == 0:
                raise ZeroDivisionError('Zero derivative. No solution found.')

            xn = xn - fxn / de_f_xn

        raise Exception('Exceeded maximum iterations. No solution found.')