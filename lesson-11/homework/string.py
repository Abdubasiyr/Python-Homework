# === math_operations ===

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# === string_utils ===

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# === geometry.circle ===

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


# === file_operations.file_reader ===

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# === file_operations.file_writer ===

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


# === Пример использования ===

print("=== Math Operations ===")
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

print("\n=== String Utils ===")
print("Reversed:", reverse_string("hello"))
print("Vowels:", count_vowels("hello"))

print("\n=== Geometry ===")
print("Area:", calculate_area(7))
print("Circumference:", calculate_circumference(7))

print("\n=== File Operations ===")
write_file("example.txt", "This is a test message.")
print("File content:", read_file("example.txt"))
