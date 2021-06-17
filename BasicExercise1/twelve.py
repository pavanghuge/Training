#Exercise 12: Calculate income tax for the given income by adhering to the below rules

income = 24000
remaining = income - 20000
if income <= 10000:
    tax = 0
elif income <=20000 and income > 10000:
    tax = 10000 * 0.1
else:
    tax = 10000*0 + 10000*.1 + remaining*0.2 

print("Tax is $",tax)