# Write a program to input two numbers from user and find LCM (Lowest Common Multiple).


num1, num2 = map(int, input("Enter the two number : ").split())

max = 0

if num1 > num2:
    max = num1
else:
    max = num2

while True:
    if max % num1 == 0 and max % num2 == 0:
        print(f"LCM of {num1} and {num2} is {max}")
        break
    max += 1
