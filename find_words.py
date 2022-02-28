#!/usr/bin/python
import os
import sys
import string

class GetWords(object):
    def __init__(self):
        self.alphabets = list(string.ascii_lowercase)
        self.words = []
        self.valid_words = self.load_words()
        return

    def load_words(self):
        valid_words = []
        with open('/usr/share/dict/words') as word_file:
            valid_words = word_file.read().split()
        return valid_words

    def letter_add(self, hints, words):
        for ind, s in enumerate(hints):
            if s == "_":
                for a in self.alphabets:
                    copy_hints = hints.copy()
                    copy_hints[ind] = a
                    words = self.letter_add(copy_hints, words)
                    word = ''.join([str(elem) for elem in copy_hints])
                    self.words.append(word)
        return

    def get_words(self):
        return self.words

    def check_validity(self):
        result = []
        # print("words:", self.words)
        for word in self.words:
            if word in self.valid_words:
                result.append(word)
        return result

    def remove_us(self):
        for s in self.word:
            if '_' in s:
                self.words.remove(s)
        return

def main():

    gw = GetWords()

    hints = sys.argv[1]
    hints = list(hints)

    words = []
    gw.letter_add(hints, words)
    gw.remove_us
    result = gw.check_validity()

    print("result:", result)

if __name__ == "__main__":
    main()