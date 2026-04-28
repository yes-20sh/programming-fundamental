'''
11111
22222
33333
44444
55555
'''

rows = int(input("Enter the number of rows: "))

for row in range(rows):
    print(str((row+1)) * rows)