
custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculate the result of (x**a + y**b) / c.

    :param x: First base
    :param y: Second base
    :param a: Exponent of x
    :param b: Exponent of y
    :param c: Divisor
    :return: Result of the equation as a float
    """
    return (x ** a + y ** b) / c


def fn_w_counter() -> tuple(int, dict[str, int]):
    if not hasattr(fn_w_counter, "call_counter"):
        fn_w_counter.call_counter = 0
        fn_w_counter.caller_dict = {}

    fn_w_counter.call_counter += 1

    caller = __name__
    fn_w_counter.caller_dict[caller] = (
        fn_w_counter.caller_dict.get(caller, 0) + 1
    )

    return fn_w_counter.call_counter, fn_w_counter.caller_dict
