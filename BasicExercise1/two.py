#Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number, and 
# In each iteration print the sum of the current number and previous number

current = 0
previous = 0

for i in range(10):
    sum =current + previous
    print('Current Number {0} Previous Number  {1}  Sum:  {2}'.format(current,previous,sum))
    previous = current
    current += 1