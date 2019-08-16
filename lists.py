# Handling a list

# Create an empty list
list = []

while True:
	action = input("What do you want to do?\n\
	(1)Add item to the list\n\
	(2)Remove item from the list\n\
	(3)Quit?: ")
	
	if action == "1":
		lisays = input("What do you want to add?: ")
		list.append(lisays)
	elif action == "2":
		list_length = len(list)
		print("List have",list_length,"items.")
		for i in list:
			print(i,"- number:",str(list.index(i)))
		delete_item = input("Which number you want to remove?: ")
		if int(delete_item) < int(list_length):
			item_name = list[int(delete_item)]
			list.remove(item_name)
		else:
			print("Item number",delete_item,"doesn't exist.")
	elif action == "3":
		print("Items in the list:")
		for i in list:
			print(i)
		break
	else:
		print("Unknown selection.")
