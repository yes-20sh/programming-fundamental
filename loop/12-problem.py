# Write a program to input a number from the user and check whether the given number is an Armstrong number or not.

num = input("Enter the number: ")

numLength = len(num)
total = 0

for n in num:
    total += int(n) ** numLength

if total == int(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

