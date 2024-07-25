"""
1. Lambda is nameless anonymous function. Lambda function is defined without a name

2. "lambda" [parameter_list] ":" expression

3. Lambda function can contain zero or more than one argument,
but should contain only one expression

4. Lambda function returns a function object

5. In Lambda Function there is no need to write return Statement.

6. We can use all type of Actual Argument

7. It contains only expressions and can't contain statements(if, else, for, while) or annotations.

8. Lambda functions can be used along with built-in functions like
filter(), map() and reduce().
"""


def add(x, y):
    return x + y


# In Lambda expression we can write the above function like below
add_numbers = lambda x, y: x + y


print(add_numbers(10, 30))

