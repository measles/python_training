#!/usr/bin/python

def is_list(element):
    element_type = type(element)
    if (element_type == list or element_type == tuple or
            element_type == MyList):
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
        if is_list(element):
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
