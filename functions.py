# Includes all functions in main.py
import json
import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)

all_clients = {
    "Spiro" : ["onboard","paid",100], 
    "Harry" : ["onboard","paid",200], 
    "Steve" : ["offboard","not paid",300]
    }

# Function to add clients to data file
def add_client(all_clients_new, client, info):

    status = input("What is the status of the new client: ")
    info.append(status)
    pay_status = input("What is the payment status of the new client: ")
    info.append(pay_status)
    init_quote = input("What is the initial quote for the new client: ")    
    info.append(init_quote)
    
    all_clients_new[client] = info 

    file_handler = open("data", "w")
    json_string = json.dumps(all_clients_new)
    file_handler.write(json_string)
    file_handler.close()  

    return all_clients, client, info

def options_display():
    options_table = input("""
Here are your options:\n
Press "V" to view all clients info
Press "C" to view clients names
Press "A" to add client
Press "M" to see money you're owed currently
Press "U" to update client status\n
Type the letter here: """)
    options_table = options_table.upper().strip().replace(" ", "")
    
    if options_table == "V":
        
        file_handler = open("data", "r")
        contents = file_handler.read()
        file_handler.close()
        all_clients = json.loads(contents)

        return display_clients(all_clients)
    
    elif options_table == "C":
        print("All your client names are: ")
        file_handler = open("data", "r")
        contents = file_handler.read()
        file_handler.close()
        all_clients = json.loads(contents)
        list_clients(all_clients)
    
    elif options_table == "A":

# Adding a new client:
        client = input("New client name: ")
        file_handler = open("data", "r")
        contents = file_handler.read()
        file_handler.close()
        all_clients = json.loads(contents)      
        info = []
        all_clients_new = all_clients

        add_client(all_clients_new, client, info)

    
    elif options_table == "M":
        owed_money_total()

    elif options_table == "U":
        print("Which client would you like to update?\n")
        file_handler = open("data", "r")
        contents = file_handler.read()
        file_handler.close()
        all_clients = json.loads(contents)
        list_clients(all_clients)
        name = input("Type the name here: ")
        update_table = input("""\n
What would you like to update?\n
Press "S" to change status
Press "PS" to change payment status
Press "Q" to change quote\n
Type the letter here: """)
        update_table = options_table.upper().strip().replace(" ", "")



    else:
        print("That wasn't an option. Try again: \n")

#Coloured all client's table

def display_clients(clients):
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)
    print ('\033[31m' + f"{'Client Name':<20} {'Status':<20} {'Payment status':<20} {'Initial Quote':<20}")
    for client, values in all_clients.items():
        print (Back.CYAN + f"{client:<20} {values[0]:<20} {values[1]:<20} {values[2]:<20}")


# Clients List only (key in dictionary)
def list_clients(clients):
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients_new = json.loads(contents)
    for client,info in sorted(all_clients_new.items()):
        print(client)

#Money owed to me
def owed_money_total():
    money_owed = 0
    index = 0
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)
    for key,value in all_clients.items():
        if value[1] == "not paid":
            index += 1
            money_owed = money_owed + value[2]  
    print(f"People owe me ${money_owed}!")




