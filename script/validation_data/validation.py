
def list_validation():
    str_list = '1,2,3,   4,   '
    li = str_list.split(',')
    # data = [int(i) for i in li if i.isnumeric()]
    data = [int(i) for i in [x.strip() for x in li] if i.isnumeric()]
    print(data)

    # check empty list
    li2 = []
    if li2:
        print('list is not empty')
    else:
        print("list is empty")

    # check a value is in list or not
    li2 = ['Omar', '5', 'Hasan', 2, 4]
    if 'Omar' in li2:
        print("value found in the list")
    else:
        print('value not found in the list')

    # check type is list or not
    li3 = 'adjhdjk, eritertj5t6'
    if isinstance(li3, list):
        print("type is list")
    else:
        print("not list type")


def bool_validation():
    val = None
    if type(val) is bool:
        print("value is bool type")
    else:
        print("val is not bool type")

    if not val:
        print("val is false")
    else:
        print("val is true")


if __name__ == "__main__":
    list_validation()
    #bool_validation()


