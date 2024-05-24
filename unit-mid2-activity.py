# unit-mid2-activity
# Author: Zishen Gong
# 09 April 2024

# Custom finction to calculatethe factorial of a number
def factorial(n):
    result= 1
    for i in range(1, n +1):
        result *= i
    return result

# Get number from user
num = int(input("What number do you want to calculate the factorial for? "))

print(f"The factorial of  {num} is: {factorial(num)}")



