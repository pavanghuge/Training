#Exercise 7: Return the count of sub-string Emma appears in the given string

inputStr = "Emma is good developer. Emma is a writer"
inputList = inputStr.split()
count = 0

for word in inputList:
    if word == "Emma":
        count +=1
print("Emma appeared {0} times".format(count))
