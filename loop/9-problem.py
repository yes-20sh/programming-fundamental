# Write a program to input a number from user and find Prime factors of the given number using loop.

num = int(input("Enter the number : "))

primeFactor = []

for i in range(2, num + 1):
    if num % i == 0:  

        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primeFactor.append(i)
    
print(f" Prime Factor of {num} is {str(primeFactor)[1:-1]}")