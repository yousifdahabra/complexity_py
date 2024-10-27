#Ex2: Pyramid of Odd Numbers
row_number = int(input('Enter a number: '))
odd = 1
odd_arr = []
odd_str = ''
for num in range(row_number) :
    odd_str = odd_str + str(odd) + " "
    odd_arr.append(odd_str) 
    odd += 2
for i in odd_arr:
    print(i)