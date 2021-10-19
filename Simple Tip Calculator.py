# Assignment Week 2 - tip calculator
# Author: Lyssette Williams

#displaying welcome message
print("="*36)
appname = "Welcome to the Tip Calculator"
print(appname)
print("="*36)


prompt1 = 'how much did the meal cost?'
prompt2 = 'enter tip percent:'

#getting input from the user
meal_cost = float(input(prompt1))
tip_percent = float(input(prompt2))

#doing that math magic for tip and total amount
tip = meal_cost * (tip_percent / 100)
tip = round(tip,2)
total = tip + meal_cost

#displaying for the user
print("Tip amount: ", tip)
print("Total amount: ",total)