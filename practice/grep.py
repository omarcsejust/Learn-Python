"""
Knuth–Morris–Pratt(KMP) Pattern Matching(Substring search)
Grep (Search for (a string of characters) using grep)
https://www.youtube.com/watch?v=sUi0GTk2_lc&t=442s
"""


class SubStr:

    def __init__(self, haystack: str, needle: str):
        self.haystack = haystack
        self.needle = needle
        self.index_li = []

    def find_indexes(self):
        for index, ch in enumerate(self.haystack):
            if ch == self.needle[0] and index <= (len(self.haystack) - len(self.needle)):
                if self.get_index(index):
                    self.index_li.append(index)

    def get_index(self, pos: int)->bool:
        p2 = pos + len(self.needle)
        if self.haystack[pos:p2] == self.needle:
            return True

        return False


if __name__ == "__main__":
    sbs = SubStr("aaabcbbbbbbbbdddddddabcdfreeabc", "abc")
    sbs.find_indexes()
    print(sbs.index_li)


