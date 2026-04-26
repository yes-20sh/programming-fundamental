# Write a program to find all Perfect numbers between 1 to n where n is the input given by the user.


num = int(input("Enter the end number: "))

prefectNumber = []

for i in range(1, num):
    total = 0
    for n in range(1, i):
        if i % n == 0:
            total += n
    if total == i:
        prefectNumber.append(i)



print(f"Perfect number between 1 to 100: {str(prefectNumber)[1:-1]}")

