#!/usr/bin/env python
from __future__ import print_function
import readline

def rhist(p=False, r=False):
    """gets command line history. prints if p=true. returns command history if r=true.
    otherwise, doesn't print and doesn't return command history."""
    history_list = []
    # create history_list
    for i in range(readline.get_current_history_length()):
        history_list.append(readline.get_history_item(i+1))
    # print if p==True
    if (p==True):
        for i in range(len(history_list)):
            print(i+1, ":", history_list[i])
    # return total history list if p==True
    if (r==True):
        return history_list

def getline(number):
    """returns the line at said number"""
    return readline.get_history_item(number)

def shist(search_string, p=False, r=False):
    """Searches through the command line history. prints if p=true. returns command history if r=true.
    otherwise, doesn't print and doesn't return command history."""
    # gets the full list
    history_list = rhist(r=True)
    # trims the list down
    for item in reversed(history_list):
        if search_string not in item:
            history_list.remove(item)
    # print if p==True
    if (p==True):
        for i in range(len(history_list)):
            print(i+1, ":", history_list[i])
    # return partial history list
    if (r==True):
        return history_list
