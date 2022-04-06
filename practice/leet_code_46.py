def permutation(nums):
    res = []
    stack = []
    used = []
    for _ in nums:
        used.append(False)

    def back_track(used):
        if len(stack) == len(nums):
            res.append(stack.copy())
            return

        for i, ch in enumerate(nums):
            if not used[i]:
                stack.append(ch)
                used[i] = True
                back_track(used)
                stack.pop()
                used[i] = False

    back_track(used)
    print(res)


permutation([1, 2, 3])

