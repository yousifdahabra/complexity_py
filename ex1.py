# Ex1: Diamond
row_number = int(input('Enter a number of row: '))
odd = 1
max_star = 0
stars = []
for num in range(row_number) :
    stars.append(odd) 
    odd += 2
max_star = odd
for num in range(row_number) :
    stars.append(odd) 
    odd -= 2
stars.append(odd) 
for i in stars:
    space = (max_star - i)//2
    print(" "*space,"*"*i," "*space)