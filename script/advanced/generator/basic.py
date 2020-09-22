"""
 1. A generator-function is defined like a normal function.

 2. If the body of a function contains yield, the function
 automatically becomes a generator function.

 3. Generator functions generate values using yield keyword rather than return

 4. Generator functions return a generator-iterator object with a sequence of values

 5. We can get value from generator object by calling next(gen_obj) method
 or
 using generator object in "for in" loop. In this case,the next() function
 is called implicitly and StopIteration is also automatically taken care of.

 6. *** The generator function cannot include the return keyword,
 If you include it then it will terminate the function ***

Note:
One of the advantages of the generator over the iterator is that elements are generated
dynamically. **Since the next item is generated only after the first is consumed,**
it is more memory efficient than the iterator.
"""


def simple_generator_fun():
    yield 1
    yield 2
    yield 3


gen_obj = simple_generator_fun()

# Get value using next(gen_obj) method
print("Get value using next() method: ", next(gen_obj))
print("Get value using next() method: ", next(gen_obj))
print("Get value using next() method: ", next(gen_obj))

# Get value using "for in" loop
for i in simple_generator_fun():
    print("Get value using for loop: ", i)


def fib_gen(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b


print(type(fib_gen(100)))

for n in fib_gen(100):
    print(n)


"""
Generator Expression
--------------------
Generator expression is an anonymous generator.

In the below example, (x*x for x in range(5)) is a generator expression. 
The first part of an expression is the yield value and the second part is 
the for loop with the collection.
"""

squares = (x*x for x in range(5))
print("Generator Expression: ", next(squares))
print("Generator Expression: ", next(squares))
print("Generator Expression: ", next(squares))


"""
The generator expression can also be passed in a function. 
It should be passed without parentheses, as shown below.
"""
sum_result = sum(x*x for x in range(5))
print("Generator as Function Argument: ", sum_result)


