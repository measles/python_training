#!/usr/bin/env python2


def is_list(element):
    if isinstance(element, (list, tuple, MyList)):
        return True
    else:
        return False


def is_list_2(element):
    if issubclass(element.__class__, (list, tuple)):
        return True
    else:
        return False


def planify(sequense):
    result = list()

    for element in sequense:
        if is_list(element):
            result += planify(element)
        else:
            result.append(element)

    return result


def planify2(sequense):
    for element in sequense:
        if is_list_2(element):
            for sub_element in planify2(element):
                yield sub_element
        else:
            yield element


class MyList(list):
    def __str__(self):
        return "<MyList>"

seq = ('abc', 3, [8, ('x', 'y'), MyList(xrange(5)), [100, [99, [98, [97]]]]])

print planify(seq)
gen = planify2(seq)
print type(gen)
print list(gen)
