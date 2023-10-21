custom_power = lambda x=0, e=1: x ** e

def custom_equation(x: int=0, y: int=0, /, a: int=1, b: int=1, *, c: int=1) -> float:
    """
    The function description

    :param x: the first number, x is positional-only
    :param y: the second number, y is positional-only
    :param a: exponent of the first number, a is positional-or-keyword
    :param b: exponent of the second number, b is positional-or-keyword
    :param c: divisor, c is keyword-only
    :return:  x to the power of a plus y to the power of b the total divided by c

    """
    if c==0:
        raise ZeroDivisionError()

    return (x**a + y**b) / c
print(custom_equation(1,2,5,7, c=4))

def fn_w_counter() -> (int, dict[str, int]):
    caller_name = __name__

    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0

        fn_w_counter.caller_callersCallCount_dict = {}

    fn_w_counter.call_count += 1

    if caller_name in fn_w_counter.caller_callersCallCount_dict:
        fn_w_counter.caller_callersCallCount_dict[caller_name] += 1
    else:
        fn_w_counter.caller_callersCallCount_dict[caller_name] = 1

    return fn_w_counter.call_count, fn_w_counter.caller_callersCallCount_dict
