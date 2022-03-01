import time
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
                    copy_hints = hints[:]
                    copy_hints[ind] = a
                    words = self.letter_add(copy_hints, words)
                    word = ''.join([str(elem) for elem in copy_hints])
                    self.words.append(word)
        return

    def get_words(self):
        return self.words

    def check_validity(self):
        result = list(set(self.words) & set(self.valid_words))
        # print("words:", self.words)
        return result

def main():

    gw = GetWords()
    if sys.version_info.major == 3:
        hints = input("Enter the incomplete word: ")
    else:
        hints = raw_input("Enter the incomplete word: ")

    hints = list(hints)
    t1 = time.time()

    words = []
    gw.letter_add(hints, words)

    result = gw.check_validity()
    t2 = time.time()

    print("result:", result)
    print("time:", t2-t1, " seconds")

if __name__ == "__main__":
    main()