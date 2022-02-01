def is_palindrome(num):
    if num < 10:
        return True

    s_num = str(num)
    r_num = s_num[::-1]
    if s_num == r_num:
        return True
    else:
        return False


if __name__ == "__main__":
    c = int(input())
    for case in range(1, c + 1):
        count = 0

        x = int(input())
        y = int(input())

        max = y
        min = x
        if x > y:
            max = x
            min = y

        for i in range(min, max + 1):
            res = is_palindrome(i)
            if res:
                count += 1
        print("Case {}: {}".format(case, count))
