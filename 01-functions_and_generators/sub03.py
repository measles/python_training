#!/usr/bin/python

def planify(sequense):
    result = list()

    for element in sequense:
        element_type = type(element)
        if (element_type == list or element_type == tuple or
            element_type == MyList):
            result += plantify(element)
        else:
            result.append(element)

    return result

class MyList(list):
    def __str__(self):
        return "<MyList>"

seq = ('abc', 3, [8, ('x', 'y'), MyList(xrange(5)), [100, [99, [98, [97]]]]])

print plantify(seq)
