#!/usr/bin/python2

import functools

def add_factory_1(a):
    def magic_add(b):
        return a+b

    return magic_add

add5_1 = add_factory_1(5)
print add5_1(10)

def add_factory_2(a):
    def magic_sum(b):
        return sum([a,b])

    return magic_sum

add5_2 = add_factory_2(5)
print add5_2(10)
