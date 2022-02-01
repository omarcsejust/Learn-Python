class SubStr:

    def __init__(self):
        self.haystack = "aaabcbbbbbbbbdddddddabcdfreeabc"
        self.needle = "abc"
        self.index_li = []

    def find_indexes(self):
        for index, ch in enumerate(self.haystack):
            if ch == self.needle[0] and index <= (len(self.haystack) - len(self.needle)):
                if self.get_index(index):
                    self.index_li.append(index)

    def get_index(self, pos: int):
        p2 = pos + len(self.needle)
        if self.haystack[pos:p2] == self.needle:
            return True

        return False


if __name__ == "__main__":
    sbs = SubStr()
    sbs.find_indexes()
    print(sbs.index_li)


