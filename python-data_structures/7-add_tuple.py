#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)  # append 0 to tuple_a
    tuple_b = tuple_b + (0, 0)  # append 0 to tuple_b
    # return sum of tuple_a and tuple_b
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
