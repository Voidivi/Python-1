# !/usr/bin/env python3
# Assignment Week 8 - Wizard Inventory Game
# Author: Lyssette Williams


# Displays the title with formatting
def display_title():
	print('Welcome to the Wizard Inventory Program')
	print('Only for the most Discerning of Wizards!')
	print('='*36)

#display the command menu with formatting	
def display_menu():
	print('COMMAND MENU:')
	print('='*36)
	print('show - Show all items')
	print('grab - Grab an item')
	print('drop - Drop an item')
	print('exit - Exit program')
	print('='*36)

#main will hold the inventory list and call display title and display menu
def main():
	display_title()
	display_menu()
	inventory = ['Pointy Wizard Hat', 'Trash Pizza','Cursed Monkey Paw']

	while True:
		command = input('Enter Command: ')
		if command.lower() == 'show':
			show(inventory)
		elif command.lower() == 'grab':
			grab_item(inventory)
		elif command.lower() == 'drop':
			drop_item(inventory)	
		elif command.lower() == 'exit':
			print('Command: exit')
			break
		else:
			print('Not a valid command. Please try again.\n')
	print('Bye!')

#displays wizard's very awesome inventory when user prompts for it						
def show(inventory): 
	print('Command: show')
	i = 1
	for item in inventory:
		print(str(i) +''+ '.' + item)
		i += 1
	print()
	

#putting items into wizard inventory - (use .append() to add to the list)
def	grab_item(inventory):
	print('Command: grab')
	if len(inventory) >=4:
		print('You can\'t carry anymore items. Please drop an item.')
	else:	
		new_item = input('Enter Item Name: ')
		inventory.append(new_item)
		print(new_item + ' was added to your wizard inventory.\n')


#drop an item from inventory - (use .pop() to delete from the list)
def drop_item(inventory):
	print('Command: drop')
	number = int(input('What number would you like to drop:  '))
	if number < 1 or number > len(inventory):
		print('Invalid item number.\n')
	else:
		item = inventory.pop(number-1)
		print(item + ' was dropped.\n')	
	
if __name__ == "__main__":
  main() 
