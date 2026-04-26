# Write a program to input a number and find the sum of first and last digit of the number using a for loop. 

num = input("Enter the number : ")

sum = 0

for i in range(len(num)):
    if i == 0 or i == len(num) -1 :
        sum += int(num[i])

print("Sum of first and last digit", sum)    