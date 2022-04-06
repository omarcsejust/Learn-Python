class Solution:
    def __init__(self):
        pass

    def coin_change(self, w, coins):
        print(w)
        if w == 0:
            return 1

        if w < 0:
            return 0

        for coin in coins:
            if w-coin >= 0:
                self.coin_change(w-coin, coins)


if __name__ == "__main__":
    s = Solution()
    w = 18
    coins = [7, 5, 1]
    print(s.coin_change(w, coins))


