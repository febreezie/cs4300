# Calculates the final price of a product after applying a given discount percentage inside of a function 
def calculate_discount(price, discount):

    finalPrice = price * (1-discount/100)

    return round(finalPrice,2)


print("Original Price: $100 \nDiscount: 20%")
print("Discounted Price:", calculate_discount(100,20))
print()

print("Original Price: $36.0 \nDiscount: 15.0%")
print("Discounted Price:", calculate_discount(36.0,15.0))
print()




#Testing Integers
def test_discountInt():
    assert calculate_discount(100,20) == 80
    assert calculate_discount(50,10) == 45

#Testing Floats
def test_discountFloat():
    assert calculate_discount (36.0, 15.0) == 30.60
    assert calculate_discount (45.0, 10.0) == 40.50


