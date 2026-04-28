'''
    *
   ***
  *****
 *******
*********
'''

rows = int(input("Enter the number of rows: "))

for row in range(rows):
    print(" " * (rows - row - 1) + "*" * (2 * row + 1))