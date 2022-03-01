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
        valid_words = (map(lambda x: x.lower(), valid_words))
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
        self.words = list(set(self.words) & set(self.valid_words))
        # print("words:", self.words)
        return

    def print_words(self):
        if len(self.words) == 0:
            print("No such word exists. Please check your conditions and the incomplete word you entered")
            return
        print(len(self.words), "possible outcomes -")
        for word in self.words:
            print(word)
        return

    def include_words(self, include):
        self.words = [word for word in self.words if all(char in word for char in include)]
        return

    def remove_words(self, remove):
        self.words = [word for word in self.words if all(char not in word for char in remove)]
        return

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
    if len(include) > 0:
        include = include.lower()
    else:
        include = None

    if len(remove) > 0:
        remove = remove.lower()
    else:
        remove = None

    hints = hints.lower()
    hints = list(hints)

    words = []
    gw.letter_add(hints, words)
    if not remove == None:
        gw.remove_words(remove)
    if not include == None:
        gw.include_words(include)
    gw.check_validity()

    print("\nresult:")
    gw.print_words()

    t2 = time.time()
    print('\n')
    print("time:", t2-t1, " seconds")

if __name__ == "__main__":
    main()