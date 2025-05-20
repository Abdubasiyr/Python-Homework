# Homework Exercises
# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input('Enter your name: ')
age = input('Enter your age: ')

print('Hello,', name, "you're", age, 'years old')


# 2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[0::2])

print(txt[1::2])


# 3. Extract Car Names
# Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[0::2])

print(txt[::-2])


# 4. Extract Residence Area
# Extract the residence area from the following text:

txt = "I'am John. I am from London"

print(txt[-6:])


# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

user_string = input('Enter your car name: ') 

print(user_string[::-1])


# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

text = input('Enter your string: ')
a_count = text.count("a")
o_count = text.count("o")
u_count = text.count("u")
i_count = text.count("i")
e_count = text.count("e")

print("a:", a_count)
print("o:", o_count)
print("u:", u_count)
print("i:", i_count)
print("e:", e_count)

# vowels = a,o,u,i,e


# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

# ввод чисел через пробел, например: 3 17 -5 22 9
nums = list(map(float, input("Введите числа через пробел: ").split()))
print("Максимальное значение:", max(nums))


# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("Enter a word: ").lower()   # приводим к одному регистру, чтобы «Anna» считалась палиндромом
if word == word[::-1]:                   # срез [::-1] разворачивает строку
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter an email address: ")
print(email.split('@'))

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

# Настройки
length = 12  # длина пароля

# Составные части пароля
letters = string.ascii_letters     # A-Z + a-z
digits = string.digits             # 0-9
specials = string.punctuation      # !@#$%^&*()_+ и т.д.

# Объединяем все символы
all_chars = letters + digits + specials

# Генерация пароля
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Случайный пароль:", password)




