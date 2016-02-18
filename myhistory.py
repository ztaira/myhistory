from __future__ import print_function
import readline

def rhist(p):
    """Returns the command line history. Short for 'return history'. p is for print."""
    history_list = []

    # create history_list
    for i in range(readline.get_current_history_length()):
        history_list.append[readline.get_history_item(i+1)]

    # print if p==True
    if (p == True):
        for i in range(history_list.len()):
            print(history_list[i])

    # return total history list
    return history_list

def getline(number):
    """returns the line at said number"""
    return readline.get_history_item(number)

def shist(search_string, p=False):
    """Searches through the command line history and returns valid lines. Short for 'search hist'"""
    # gets the full list
    history_list = rhist()

    # trims the list down
    for item in history_list:
        if search_string not in item:
            history_list.remove(item)

    # print if p==True
    if (p==True):
        for i in range(history_list.len()):
            print(history_list[i])

    # return partial history list
    return in_lines
