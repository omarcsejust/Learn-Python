"""
1. filter function takes a function as argument which returns true for false
2. and only one iterable object
3. then filter out the items from iterable object based
on condition and return a iterable filter object
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


def filter_product_by_price(product):
    # if product.get('price', 0) > 100:
    #     return True
    return product.get('price', 0) > 100


# filter returns an iterable filter object
filtered_products = filter(filter_product_by_price, products)

print(filtered_products)

for product in filtered_products:
    print(product)


# We can convert into a list like below
filtered_products2 = list(filter(filter_product_by_price, products))
print(filtered_products2)


# Use of Lambda Function
# ----------------------
products_list = list(filter(lambda product: product['price'] > 100, products))
print("Using Lambda: ", products_list)


