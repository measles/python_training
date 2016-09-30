#!/usr/bin/env python2

import os
import re
import curses

#
# Assuming that .ssh/config is correct, there is no duplicating hosts or
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


def start_ncurses():
    # Initialize screen
    stdscr = curses.initscr()
    # Trun off keypress echoing to the screen
    curses.noecho()
    # Enable non-bufered keystroke read (need to get reaction without pressint Enter)
    curses.cbreak()
    # Get non-symbolic keys in human-readable format
    stdscr.keypad(1)
    # Hide a cursor
    curses.curs_set(0)
    # Enable colors (or, at least, try to)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    stdscr.bkgd(' ', curses.color_pair(1))

    y, x = stdscr.getmaxyx()
    init_main_window(y, x, stdscr)
    content = init_list_frame(y, x)

    return stdscr, content


def init_main_window(y, x, stdscr):
    stdscr.addstr(0, 0, "PythonSshInteractiveClient")
    stdscr.addstr(y-1, 0, "k,UpArrow: Up; j,DownArrow: Down; o,Enter: Open connection; q: exit")
    stdscr.refresh()


def init_list_frame(y, x):
    content = curses.newwin(y-2, x, 1, 0)
    content.bkgd(' ', curses.color_pair(2))

    content.addch(0, 0, curses.ACS_ULCORNER)
    content.addch(0, x-1, curses.ACS_URCORNER)
    content.addch(y-3, 0, curses.ACS_LLCORNER)
    content.addch(y-3, x-2, curses.ACS_LRCORNER)

    content.refresh()
    return content


def quit_ncurses():
    # Deactivate curses-specific screen settings
    curses.echo()
    curses.nocbreak()
    stdscr.keypad(0)
    curses.curs_set(1)
    # Get back to usual terminal
    curses.endwin()

config = parse_config()

stdscr, content = start_ncurses()

c = stdscr.getch()

quit_ncurses()
