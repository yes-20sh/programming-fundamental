# Write a program to print Fibonacci series up to n terms using loop. 

nth = int(input("Enter the nth term : "))

th1 = 0
th2 = 1

for i in range(nth):
    print(th1)
    temp = th1 + th2
    th1 = th2
    th2 = temp