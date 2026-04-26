# Write a Program to input a number from user and find all factors of the given number using for loop. 

num = int(input("Enter the number: "))

factors = []

for i in range(1, num + 1):
    i *=2
    factors.append(i)

print(f"All factor of {num} are {(str(factors)[1:-1])} ")
