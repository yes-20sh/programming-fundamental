# Write a program to input two numbers from the user and find HCF (Highest Common Factor) / GCD (Greatest Common Divisor).

num1, num2 = map(int, input("Enter the 2 numbers: ").split())

hcf = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print(f"HCF of {num1} and {num2} is {hcf}")