#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rest = a / b
    except ZeroDivisionError:
        rest = None
    finally:
        print("Inside result: {}".format(rest))
    return rest
