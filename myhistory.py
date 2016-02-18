#!/usr/bin/env python
from __future__ import print_function
import readline

def rhist(p=True, r=False):
    """fetches command line history. prints if p=true. returns command history if r=true.
    otherwise, doesn't print and/or doesn't return command history."""
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

def shist(search_string, p=True, r=False):
    """Searches through the command line history. prints if p=true. returns command history if r=true.
    otherwise, doesn't print and/or doesn't return command history."""
    # gets the full list
    history_list = rhist(r=True, p=False)
    history_dict = {}
    for i in range(len(history_list)):
        history_dict[i+1] = history_list[i]
    # trims the list down
    history_list = []
    for key in history_dict:
        if search_string not in history_dict[key]:
            history_list.append(key)
    for key in history_list:
        if key in history_dict:
            del history_dict[key]
    # print if p==True
    if (p==True):
        for key in history_dict:
            print(key, ":", history_dict[key])
    # return partial history list
    if (r==True):
        return history_list
