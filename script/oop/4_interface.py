from abc import ABC, abstractmethod


class CalculationService(ABC):

    @abstractmethod
    def add_number(self, number: int):
        pass

    @abstractmethod
    def show_sum_result(self):
        pass


class SimpleSum(CalculationService):
    def __init__(self):
        self.sum = 0

    def add_number(self, number: int):
        self.sum += number

    def show_sum_result(self):
        print(f'Total sum is {self.sum}')


class UniqueSum(CalculationService):
    def __init__(self):
        self.sum = 0
        self.numbers_set = set()

    def add_number(self, number: int):
        if number not in self.numbers_set:
            self.numbers_set.add(number)
            self.sum += number

    def show_sum_result(self):
        print(f'Total sum is {self.sum}')


class ExampleUsage:
    def __init__(self, calculation: CalculationService):
        self.calculation = calculation


if __name__ == '__main__':
    simple_sum = ExampleUsage(SimpleSum())
    simple_sum.calculation.add_number(10)
    simple_sum.calculation.add_number(10)
    simple_sum.calculation.add_number(20)

    simple_sum.calculation.show_sum_result()

    unique_sum = ExampleUsage(UniqueSum())
    unique_sum.calculation.add_number(10)
    unique_sum.calculation.add_number(10)
    unique_sum.calculation.add_number(20)

    unique_sum.calculation.show_sum_result()





