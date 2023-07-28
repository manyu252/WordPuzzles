#!/usr/bin/python3

import os
import time
import sys
from utils import time_limit, TimeoutException
from get_words import GetWords

def main():

    gw = GetWords()
    if sys.version_info.major == 3:
        hints = input("Enter the incomplete word: ")
        print("Just press 'Enter' if you don't have any specific conditions. Conditions -")
        include = input("include alphabets: ")
        remove = input("omit alphabets: ")
    else:
        hints = raw_input("Enter the incomplete word: ")
        print("Just press 'Enter' if you don't have any specific conditions. Conditions -")
        include = raw_input("include alphabets: ")
        remove = raw_input("omit alphabets: ")

    t1 = time.time()

    hints = hints.lower()
    hints = hints.replace(" ", "")
    hints = list(hints)

    if '_' not in hints:
        print("Only 1 possible outcome: ", ''.join(hints))
        os._exit(-1)

    print("PROCESSING :: Wait for a few seconds.")

    if len(include) > 0:
        include = include.lower()
        include = include.replace(" ", "")
    else:
        include = None

    if len(remove) > 0:
        remove = remove.lower()
        remove = remove.replace(" ", "")
        if include is not None:
            remove = [char for char in remove if char not in include]
        remove = [char for char in remove if char not in hints]
        gw.remove = remove
    else:
        remove = None

    words = []
    try:
        with time_limit(20):
            gw.letter_add(hints, words)
    except TimeoutException as e:
        print("\nREQUEST TIMED OUT!! \nPlease reduce the number of '_' or give more alphabets to omit.")
        os._exit(-1)

    if not remove == None:
        gw.remove_words(remove)
    if not include == None:
        gw.include_words(include)
    gw.check_validity()

    print("\nresult:")
    gw.print_words()

    t2 = time.time()
    print("time: {:.2f} seconds".format(t2-t1))

if __name__ == "__main__":
    main()