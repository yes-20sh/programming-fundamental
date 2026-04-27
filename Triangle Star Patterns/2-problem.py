'''
*
**
* *
*  *
*****
'''

rows = int(input("Enter the number of rows: "))

for row in range(1, rows + 1):
    for column in range(1, row + 1):
        if column == 1 or column == row or row == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()