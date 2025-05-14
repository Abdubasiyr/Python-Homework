# 1. Given a side of square. Find its perimeter and area.

side = int(input('Enter the side of the square: '))
perimeter = 4 * side
area = side**2

print('Perimeter =', perimeter)
print('Area =', area)


# 2. Given diameter of circle. Find its length.

diameter = int(input('Enter the diameter of circle: '))
length = diameter * 3.14

print('Length =', length)


# 3. Given two numbers a and b. Find their mean.

a = int(input("Enter the number 'a': "))
b = int(input("Enter the number 'b': "))
mean = (a+b)/2

print(mean)


# 4. Given two numbers a and b. Find their sum, product and square of each number.

a = int(input("Enter the number 'a': "))
b = int(input("Enter the number 'b': "))
sum = a+b
product = a*b
square_of_a = a**2
square_of_b = b**2

print('Sum =', sum)
print('Product =', product)
print('The square of a =', square_of_a)
print('The square of b =', square_of_b)


