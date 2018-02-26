import sys

WORDLIST_PATH="c://githubs/english-words/words_alpha.txt"

class WordList:
    def __init__(self, path):
        self.words = []
        count = 0
        skipped = 0
        with open(path) as f:
            while True:
                str = f.readline()
                str = str.rstrip()
                str = str.lstrip()
                l = len(str)
                if l==0:
                    break
                if l > 2:
                    str = str.lower()
                    self.words.append(str)
                    count = count + 1
                else:
                    skipped = skipped + 1
        print("%d words read\n%d words skipped\n"%(count, skipped))

    def get_word_map(self, str):
        rv = {}
        for c in str:
            if c in rv:
                rv[c] = rv[c] + 1
            else:
                rv[c] = 1
        return rv

    def is_subset(self, source, target):
        for c in target.keys():
            if c in source:
                if target[c] > source[c]:
                    return False
            else:
                return False
        return True

    def find_words(self, str, strlen=-1):
        str = str.lower()
        wm1 = self.get_word_map(str)
        for w in self.words:
            if strlen != -1 and len(w) != strlen:
                continue
            wm2 = self.get_word_map(w)
            if self.is_subset(wm1, wm2):
                print(w)

def main():
    w = WordList(WORDLIST_PATH)
    if len(sys.argv) == 2:
        w.find_words(sys.argv[1])
    elif len(sys.argv)==3:
        w.find_words(sys.argv[1], int(sys.argv[2]))

if __name__ == "__main__":
    main()