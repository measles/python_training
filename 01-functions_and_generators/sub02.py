#!/usr/bin/env python2

import urllib2
import json
import itertools


def reddit(keyword):
    url = "https://www.reddit.com/r/" + keyword + ".json"

    def get_list_from_reddit():
        response = urllib2.urlopen(url)
        response_dict = json.load(response)
        data = response_dict["data"]["children"]

        for key in data:
            yield key["data"]["title"]

    return get_list_from_reddit


def print_slice(sequense, number, use_repr=False):
    for title in itertools.islice(sequense, number):
        if use_repr:
            print repr(title)
        else:
            print title

clisp = reddit("common_lisp")
erlang = reddit("erlang")

# for title in clisp():
#    print title

# for title in erlang():
#    print repr(title)

print "Sliced versions:"
print_slice(clisp(), 3)
print_slice(erlang(), 5, True)
