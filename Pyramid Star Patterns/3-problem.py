'''
*********
 *******
  *****
   ***
    *  
'''

rows = int(input("Enter the number of row : "))

for row in range(rows, 0, -1):
    print(" " * (rows - row) + "*" * (2 * row - 1))