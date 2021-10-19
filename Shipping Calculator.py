# Assignment Week 3 - Shipping Calculator
# Author: Lyssette Williams

appname = 'Shipping Calculator\n'
print(appname)

#Setting the program to loop

choice = 'y'
while choice == 'y':

# User must input cost of items ordered inline
# Using tabs and extraneous print statements to make the program more readable

	userItem_order = float(input('Please enter the cost of items ordered:\t'))
	print ('')

# Conditional statements below figuring out shipping cost based on user input

	if userItem_order <= 0:
		print('You must enter a positive number. Please try again.')
		print('')
		continue
	elif userItem_order < 30:
		shippingCharges = 5.95
	elif userItem_order < 49.99:
		shippingCharges = 7.95
	elif userItem_order < 74.99:
		shippingCharges = 9.95
	else:
		shippingCharges = 0.00
		print('Shipping cost: FREE')

# Calculate total cost to print later

	total_cost = round(userItem_order + shippingCharges,2)	

#Provide the user with the answer
#Needed to look up more conditional formatting for the decimals

	print('Cost of items ordered:\t', '%0.2f' % userItem_order)
	print('Shipping cost:\t\t', '%0.2f' % shippingCharges)
	print('Total cost:\t\t', '%0.2f' % total_cost)
	choice = input('Continue? (y/n):\t')
	print ('')
print ('Thank you for using the Shipping Calculator!')