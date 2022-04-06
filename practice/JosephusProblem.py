def find_path(m, n):
    if m == 1 or n == 1:
        return 1

    return find_path(m-1, n) + find_path(m, n-1)


if __name__ == "__main__":
    print(find_path(4, 2))


