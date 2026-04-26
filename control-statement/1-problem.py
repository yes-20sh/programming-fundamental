# Write a program to find maximum between three numbers.

num1, num2, num3 = map(int, input("Enter num1, num2 and num3: ").split())

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is maximum")
elif num2 >= num3:
    print(f"{num2} is maximum")
else:
    print(f"{num3} is maximum")
