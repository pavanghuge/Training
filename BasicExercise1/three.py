#Exercise 3: Given a string, display only those characters which are present at an even index number.
inputStr = "pynative"

print("Original string", inputStr)
print("Printing only even index chars")
for i in range(0,len(inputStr),2):
    print(inputStr[i])
