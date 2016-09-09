#!/usr/bin/python

import os, re

#
# Assuming that .ssh/config is correct, there is no duplcating hosts or 
# host information fields
#

def parse_config():

    results = []

    try:
        infile = open(os.environ["HOME"] + '/.ssh/config')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        exit(1)

    # Defining RE which will be used duting parsing
    re_host = re.compile('Host[ \t]+.+', re.DOTALL)
    re_hostname = re.compile('HostName', re.IGNORECASE)
    re_username = re.compile('User', re.IGNORECASE)
    re_port = re.compile('Port', re.IGNORECASE)
    re_idfile = re.compile('IdentityFile', re.IGNORECASE)
    re_comment = re.compile('#')
    re_empty = re.compile('^[ \t]*$')

    host = {}

    for i in infile.readlines():
        i = i.strip()
        if re_host.match(i):
            if host != {} and host["host"] != "*":
                results.append(host)
                host = {}

            host["host"] = i.split()[1]
        elif re_hostname.match(i):
            host["hostname"] = i.split()[1]
        elif re_username.match(i):
            host["username"] = i.split()[1]
        elif re_idfile.match(i):
            pass
#            host["idfile"] = i.split()[1]
        elif re_port.match(i):
            host["port"] = i.split()[1]
        elif re_comment.match(i) or re_empty.match(i):
            continue

    return results
        
print parse_config()
