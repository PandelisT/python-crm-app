
# Clients List
inventory = {"Spiro" : ["onboard","paid",100], "Harry" : ["onboard","paid",200], "Steve" : ["offboard","not paid",300]}

#Money owed to me
profit = 0
index = 0

for key,value in inventory.items():
    if value[1] == "not paid":
        index += 1
        profit = profit + value[2]
    
print(f"People owe me {profit}!")


# Clients List
for key,value in inventory.items():
    print(key)


def add_client(inventory, key):
    value = inventory[key]
    return value

# print(add_client(inventory, key))
    # if value[2] == 300:
    #      print(key)



#Coloured client's table
from colorama import init, Fore, Back, Style
init(autoreset=True)
# print('\033[31m' + 'some red text')
def display_clients(inventory):
    print ('\033[31m' + f"{'Client Name':<20} {'Status':<20} {'Payment status':<20} {'Initial Quote':<20}")
    for client, values in inventory.items():
        print (Back.CYAN + f"{client:<20} {values[0]:<20} {values[1]:<20} {values[2]:<20}")

display_clients(inventory)
