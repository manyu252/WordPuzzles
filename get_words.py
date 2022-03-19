import string

class GetWords(object):
    def __init__(self):
        self.alphabets = list(string.ascii_lowercase)
        self.words = []
        self.remove = []
        self.valid_words = self.load_words()
        return

    def load_words(self):
        valid_words = []
        with open('words.txt') as word_file:
            valid_words = word_file.read().split()
        valid_words = (map(lambda x: x.lower(), valid_words))
        return valid_words

    def letter_add(self, hints, words):
        for ind, s in enumerate(hints):
            if s == "_":
                for a in self.alphabets:
                    if a in self.remove:
                        continue
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
        for word in self.words:
            print(word)
        print("\n")
        print(len(self.words), "possible outcomes.")
        return

    def include_words(self, include):
        self.words = [word for word in self.words if all(char in word for char in include)]
        return

    def remove_words(self, remove):
        self.words = [word for word in self.words if all(char not in word for char in remove)]
        return