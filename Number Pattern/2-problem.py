'''
54321
4321
321
21
1
'''

rows = int(input("Enter the number of rows: "))

for row in range(rows + 1, 1, -1):
    for column in range(row -1, 0, -1):
        print((column), end="")
    print()
    