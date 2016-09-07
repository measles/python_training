#!/usr/bin/python2

import urllib2, json, itertools

def reddit(keyword):
    def get_list_from_reddit():
        url = "https://www.reddit.com/r/" + keyword + ".json"
        response = urllib2.urlopen(url)
        response_dict = json.load(response)   
        data = response_dict["data"]["children"]

        for key in data:
            yield key["data"]["title"]

    return get_list_from_reddit

def print_slice(sequense, number):
    titles = itertools.islice(sequense, number)
    print titles

clisp = reddit("common_lisp")
erlang = reddit("erlang")

for title in clisp():
    print title

for title in erlang():
    print repr(title)

#print_slice(clisp(), 3)
#print_slice(erlang(), 5)
