import readline
from __future__ import print_function

def history():
    for i in range(readline.get_current_history_length()):
        print(i+1, ":", readline.get_history_item(i+1))

def getline(number):
    return readline.get_history_item(number)
