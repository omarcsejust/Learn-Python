"""
1. In Map we transform/map our original list to a different list

2. Map function takes a function as argument and one or more iterable object

3. Map function returns an iterable Map object

4. But in filter we do not modify the original list items structure, just
filter out unnecessary items from original list and form a new list
"""

products = [
    {
        'id': 1,
        'name': 'Product 1',
        'price': 80
    },
    {
        'id': 2,
        'name': 'Product 2',
        'price': 300
    },
    {
        'id': 3,
        'name': 'Product 3',
        'price': 150
    },
]


def get_price(product):
    return product.get('price', 0)


# make price list from products
mapped_product_price = map(get_price, products)  # map with user defined function
for price in mapped_product_price:
    print(price)

# or get list
mapped_product_price_list = list(map(get_price, products))
print("Price List: ", mapped_product_price_list)

# we can do the same stuff using lambda function: map with lambda function
# ------------------------------------------------------------------------
mapped_product_price_using_lambda = list(map(lambda product: product['price'], products))
print("Using lambda: ", mapped_product_price_using_lambda)


# two iterable object as argument in map function
# -----------------------------------------------
li1 = [10, 20, 30, 40, 50]
li2 = [10, 20, 30, 40, 50]

# add corresponding items of two list and make a single list
list_sum = list(map(lambda x, y: x+y, li1, li2))
print("Sum of two list using Lambda: ", list_sum)

# user defined function to perform the same task
# ----------------------------------------------


def add_two_list(x, y):
    return x+y


result = list(map(add_two_list, li1, li2))  # map with user defied function
print("Sum of two list using User Defined Function: ", result)


# filter with map
# ---------------
"""
Map only product prices from products and then 
filter out the prices are greater than 100
"""
res = filter(lambda price: price > 100, map(lambda product: product['price'], products))
print("Price List: ", tuple(res))
