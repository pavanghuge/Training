#Exercise 11: Write a code to extract each digit from an integer, in the reverse order

number = 7563

while(number>0):
    remainder =number% 10
    print(remainder, end = " ")
    number = number //10
print("\n")