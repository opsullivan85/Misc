#Mitchel Francoeur
#10/23/18
import json

list = [[],{},{}]
name = list[0]
price = list[1]
amount = list[2]

print("Welcome to the ASD Python Online Store!")
print()

try:
    file = open("list.json","r")
except FileNotFoundError:
    file = open("list.json","w")
    json.dump(list, file)
    print("Store data not found! Please add items to the store.")
    file.close()
else:
    data = json.load(file)
    print("Files loaded")

#Modify list function
def modify(list):
    mod = 1
    while mod:
        print()
        mod_num = int(input("Enter the item number: "))
        if mod_num in name:
            #prints inventory for that item
            print()
            mod_cost = float(input("Enter the new price: "))
            #replaces old cost with new cost
            print()
            mod_qty = int(input("Enter the new quantity: "))
            #replaces old qty with new qty
            print()
            print("Item updated")
        else:
            print()
            print("Invalid response")
        print()    
        mod_check = input("Would you like to modify an item? (Y)/(N): ")
        if mod_check.lower() == "y":
            mod = True
        elif mod_check.lower() == "n":
            print()
            print("Returning to  store")
            mod = False
        else:
            print()
            print("Invalid response")
    
#Add to list function
def stock(list):
    add = 1
    while add:
        print()                
        item_name = input("Please enter the name of the item: ")
        name.append(item_name)
        print()
        item_val = float(input("Please enter the value of the item: "))
        price[item_name] = item_val
        print()
        item_qty = int(input("Please enter the quantity of the item: "))
        amount[item_name] = item_qty
        print()
        check = input("Would you like to add another item? (Y)/(N): ")
        if check.lower() == "y":
            add = True
        elif check.lower() == "n":
            print()
            print("Returning to store")
            add = False
        else:
            print()
            print("Invalid response")
            add = False
        file = open("list.json","r+")
        json.dump(list,file)
        file.close()

#Inventor function
def inventory():
    print("***Online Store Inventory***")
    sum = 0
    #for each key in list[0]
    #[[keys], {key: price}, {key: quantity}]
    for j in (data[0]):
        #print out key (>  KEY:)
        print(j + " :")
        #for each of the dictionaries at list[1 & 0]
        for i in range(len(data)-1):
            print("  ", end="")
            #print what the dictionary is
            print("Price: $", end="") if not(i) else print("Quantity: ", end="")
            #print value from dictionary at list[i+1] with key j
            print(data[i+1][j])
#find the item_name and find dictionary keys to find price and qty
    
start = 1
while start:
    print()
    menu = input("Select (P)urchase, (S)tock, (I)nventory, or (Q)uit: ")
    print()
    
    if menu.lower() == "s":
        question = input("Would you like to (A)dd a new item or (M)odify an existing item? ")
        if question.lower() == "a":
            stock(list)
        elif question.lower() == "m":
            modify(list)
        else:
            print("Invalid response")

    elif menu.lower() == "i":
        inventory()

    elif menu.lower() == "q":
        check = input("Are you sure you would like to exit? (Y)/(N): ")
        if check.lower() == "y":
            print()
            print ("Exiting Online Python Store. Thank you for shopping!")
            start = False
        elif check.lower() == "n":
            print()
            print ("Aborting exit...")
            start = True
        else:
            print()
            print ("Invalid response")
            start = True
    else:
        print("Invalid response")
