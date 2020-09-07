"""
1. Lambda is nameless anonymous function. Lambda function is defined without a name

2. "lambda" [parameter_list] ":" expression

3. Lambda function can contain one or more tan one argument,
but should contain only one expr

4. Lambda function returns a function object

5. Note that functions created with lambda expressions
can not contain statements or annotations.

6. Lambda functions can be used along with built-in functions like
filter(), map() and reduce().
"""


def add(x, y):
    return x + y


# In Lambda expression we can write the above function like below
add_numbers = lambda x, y: x + y


print(add_numbers(10, 30))

