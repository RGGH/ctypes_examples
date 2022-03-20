"""
https://reptate.readthedocs.io/developers/python_c_interface.html

Define the C-variables and functions from the C-files that are needed in Python

"""

from ctypes import c_double, c_int, CDLL

import sys

import timeit


lib_path = "tractor/basic_function_%s.so" % (sys.platform)

try:

    basic_function_lib = CDLL(lib_path)

except:
    print("OS %s not recognized" % (sys.platform))


python_c_square = basic_function_lib.c_square
python_c_square.restype = None


def do_square_using_c(list_in):

    """Call C function to calculate squares"""

    n = len(list_in)

    c_arr_in = (c_double * n)(*list_in)
    # ctype array of double of size n that can be used by the C function.
    # initialised with the values of list_in.

    c_arr_out = (c_double * n)()

    python_c_square(c_int(n), c_arr_in, c_arr_out)

    return c_arr_out[:]


print(f"{do_square_using_c([3,6])} \n")


start_time = timeit.default_timer()

do_square_using_c([3, 6])
time_c = timeit.default_timer() - start_time
print("The C time difference is :", time_c)


# Compare versus using a python function #


def p_square(lst):
    for i in lst:
        i = i * i
        print(str(i))


start_time = timeit.default_timer()
p_square([3, 6])
time_p = timeit.default_timer() - start_time
print("The Python time difference is :", time_p)
