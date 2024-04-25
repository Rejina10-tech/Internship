#if statement

phone_balance = 4
bank_balance = 8
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
    
print(phone_balance)     #prints 14
print(bank_balance)# prints -2


#If, Elif, Else
    
number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")
    
    #prints Number 145 is odd

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result) #prints Congratulations! You won a wafer-thin mint!


#truth value testing

errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")
    
#prints You have 3 errors to fix!    