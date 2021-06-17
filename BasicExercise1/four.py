# Exercise 4: Given a string and an integer number n, remove characters from a string starting 
# from zero up to n and return a new string



def removeChar(inputStr,n):
    return inputStr[n:]

print(removeChar("pynative",4))