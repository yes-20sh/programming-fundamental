# Write a program to find power of a number using for loop

base, exponent =  map(int, input("Enter the base and exponent : ").split())

powerOfNumber = 1

for i in range(exponent):
    powerOfNumber *= base

print(f"Power of number {base} is {powerOfNumber}")
    