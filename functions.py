# Includes all functions in main.py

import clients as c
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Coloured all client's table
def display_clients(clients):
    print ('\033[31m' + f"{'Client Name':<20} {'Status':<20} {'Payment status':<20} {'Initial Quote':<20}")
    for client, values in c.all_clients.items():
        print (Back.CYAN + f"{client:<20} {values[0]:<20} {values[1]:<20} {values[2]:<20}")


# Clients List only (key in dictionary)
def list_clients(clients):
    for client,info in c.all_clients.items():
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


