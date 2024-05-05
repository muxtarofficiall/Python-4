def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

number = 1234
print("Product of digits:", product_of_digits(number))
