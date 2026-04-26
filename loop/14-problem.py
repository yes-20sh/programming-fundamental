# Write a program to input a number and check whether the number is a Perfect number or not. 

num = int(input("Enter the number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")