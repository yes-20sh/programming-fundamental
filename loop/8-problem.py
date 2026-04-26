# Write a program to print all Prime numbers between 1 to n using loop

end = int(input("Enter the end for prime number : "))

primeNumber = []
for num in range(2, end + 1):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        primeNumber.append(num)

print("All prime number", str(primeNumber)[1:-1])  