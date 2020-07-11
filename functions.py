# Includes all functions in main.py
import json
import clients as c
from colorama import init, Fore, Back, Style
init(autoreset=True)

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
        display_clients(c.all_clients)
    elif options_table == "C":
        print("All your client names are: ")
        list_clients(c.all_clients)
    elif options_table == "A":
# Adding a new client:
        client = input("New client name: ")
        info = []
        add_client(c.all_clients, client, info)
# Display all clients in table including new one:
        display_clients(c.all_clients)
    elif options_table == "M":
        owed_money_total()
# elif options_table == "U":
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
    for client,info in all_clients_new.items():
        print(client)

# Function to add clients to dictionary
def add_client(all_clients, client, info):
    # new_dict = dict()
    status = input("What is the status of the new client: ")
    info.append(status)
    pay_status = input("What is the payment status of the new client: ")
    info.append(pay_status)
    init_quote = input("What is the initial quote for the new client: ")
    info.append(init_quote)
    c.all_clients[client] = info
    
    file_handler = open("data", "w")
    json_string = json.dumps(all_clients)
    file_handler.write(json_string)
    file_handler.close() 
    
    return client, info


#Money owed to me
def owed_money_total():
    profit = 0
    index = 0

    for key,value in c.all_clients.items():
        if value[1] == "not paid":
            index += 1
            profit = profit + value[2]  
    print(f"People owe me {profit}!")


