
import time
import os
import sys
from utils import time_limit, TimeoutException
from get_words import GetWords

def main():
    gw = GetWords()
    if sys.version_info.major == 3:
        neccessary_letter = input("Enter the necessary letter: ")
        include = input("include alphabets: ")
        min_length = int(input("minimum length of word: "))
        max_length = int(input("maximum length of word: "))
    else:
        neccessary_letter = raw_input("Enter the necessary letter: ")
        include = raw_input("include alphabets: ")
        min_length = int(raw_input("minimum length of word: "))
        max_length = int(raw_input("maximum length of word: "))

    t1 = time.time()

    include = list(include.lower())
    include.append(neccessary_letter)
    gw.remove = [char for char in gw.alphabets if char not in include]

    for i in range (min_length, max_length+1):
        hints = ['_'] * i
        words = []
        try:
            with time_limit(20):
                gw.letter_add(hints, words)
        except TimeoutException as e:
            print("\nREQUEST TIMED OUT!! \nPlease reduce the length.")
            os._exit(-1)
    gw.include_words(neccessary_letter)
    gw.check_validity()

    print("\nresult:")
    gw.print_words()

    t2 = time.time()
    print("time: {:.2f} seconds".format(t2-t1))

if __name__ == "__main__":
    main()