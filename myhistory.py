#!/usr/bin/env python
from __future__ import print_function
import readline

def hist():
    """Fetches command line history. Returns dict of all lines."""
    history_dict = {}
    # create history_list
    for i in range(readline.get_current_history_length()):
        history_dict[i+1] = (readline.get_history_item(i+1))
    return history_dict

def getline(number):
    """returns the line at said number"""
    number = int(number)
    return readline.get_history_item(number)

def shist(search_string):
    """Searches through the command line history. Returns dict of applicable lines."""
    # gets the full dict
    my_string = str(search_string)
    history_dict = hist()
    # creates the final history dict
    final_history_dict = {}
    for key in history_dict:
        if my_string in history_dict[key]:
            final_history_dict[key] = history_dict[key]
    return final_history_dict

def phist():
    """Prints the command line history."""
    history = hist();
    for line in history:
        print(line, ":", history[line])

def pshist(search_string):
    """Prints a search of the command line history"""
    history = shist(search_string)
    for line in history:
        print(line, ":", history[line])
