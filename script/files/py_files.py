"""
w = write mode (if the file doesn’t exist create it and open it in write mode)
r = read mode
a = append mode (if the file doesn’t exist create it and open it in append mode)
w+ = create a file – if it doesn’t exist and open it in write mode
r+ = open an existing file in read+write mode
a+ = create a file – if it doesn’t exist and open it in append mode
"""


def open_file_in_old_way():
    f = open("script/files/names.txt", "w+")
    f.write("Omar")
    f.write("\nHasan")
    f.write("\nRaju")
    f.write("\nTariq")
    f.close()


def read_file_content():
    f = open("script/files/names.txt", "r")
    print("Single line: ", f.readline())
    print("All linen: ", f.readlines())
    f.close()


def open_file_in_modern_way():
    # in this way we don't need to close the file, its by default
    with open("script/files/names.txt", "r") as f:
        print(f.readlines())


def check_file_exist(f_name):
    try:
        f = open(f_name, "r+")
        print(f_name, "found")
        f.write("Open existing file in read + write mode")
        f.close()
    except FileNotFoundError:
        print(f_name, " Not found")


if __name__ == "__main__":
    open_file_in_old_way()
    read_file_content()
    check_file_exist("script/files/names-list.txt")
