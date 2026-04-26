# Write a program to print all Armstrong numbers between 1 to n where n is the input given by the user.

num = int(input("Enter the nth number: "))

armstrongNumbers = []

for n in range(1, num + 1):
    numLength = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** numLength
        temp //= 10

    if total == n:
        armstrongNumbers.append(n)

print(f"Armstrong numbers between 1 to {num} are: {armstrongNumbers}")