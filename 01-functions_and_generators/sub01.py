#!/usr/bin/env python2

import functools


# First method to created factory to calculate sum
def add_factory_1(addend_a):
    def magic_add(addend_b):
        return addend_a+addend_b

    return magic_add

add5_1 = add_factory_1(5)
print add5_1(10)


def add_factory_1_2(addend_a):
    def magic_sum(addend_b):
        return sum([addend_a, addend_b])

    return magic_sum

add5_1_2 = add_factory_1_2(5)
print add5_1_2(10)


# Second method to create factory to calculate sum
def add_factory_2(addend_a):
    return lambda addend_b: addend_a+addend_b

add5_2 = add_factory_2(5)
print add5_2(10)
