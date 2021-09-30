# fibonacci using Generator
def fib(num):
    a, b = 0, 1
    while a < num:
        yield a
        a, b = b, a+b


def zip_demo():
    li1 = ['Omar', 'Kamal', 'Orin']
    li2 = [25, 29, 22]
    zip_res = list(zip(li1, li2))  # converts a list of tuples
    print(zip_res)
    for z in zip_res:
        print(z)


class Emp:

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def full_name(self):
        return "{} {}".format(self.f_name, self.l_name)


if __name__ == '__main__':
    # for fib_num in fib(100):
    #     print(fib_num)

    zip_demo()

    emp1 = Emp('Omar', 'Hasan')
    print(emp1.full_name())
    print(Emp.full_name(emp1))

