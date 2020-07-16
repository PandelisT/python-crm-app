# Includes all functions in main.py
import json
import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)
from difflib import get_close_matches

all_clients = {
    "Spiro" : ["onboard","paid",100], 
    "Harry" : ["onboard","paid",200], 
    "Steve" : ["offboard","not paid",300]
    }

# Function to add clients to data file
def add_client(all_clients_new, client, info):

    while True:
        status = input("What is the status of the new client (onboarded or offboarded): ")
        if status == "onboarded" or status == "offboarded":
            info.append(status)
            break
        elif len(get_close_matches(status, ["onboarded", "offboarded"])) > 0:
            yn = input("Did you mean %s instead? Enter Y is yes, or N if no: " % get_close_matches(status, ["onboarded", "offboarded"])[0])
            yn = yn.upper().strip().replace(" ", "")
            if yn == "Y":
                info.append(get_close_matches(status, ["onboarded", "offboarded"])[0])
                break
        else:
            print("That wasn't an option, try again.")
            continue  
    
    while True:
        pay_status = input("What is the payment status of the new client: ")
        if pay_status == "paid" or pay_status == "not paid":
            info.append(pay_status)
            break
        elif len(get_close_matches(pay_status, ["paid", "not paid"])) > 0:
            yn = input("Did you mean %s instead? Enter Y is yes, or N if no: " % get_close_matches(pay_status, ["paid", "not paid"])[0])
            yn = yn.upper().strip().replace(" ", "")
            if yn == "Y":
                info.append(get_close_matches(pay_status, ["paid", "not paid"])[0])
                break      
        else:
            print("That wasn't an option, try again.")
            continue 
    
    while True:
        try: 
            init_quote = int(input("What is the initial quote for the new client: "))
            info.append(init_quote)
            break
        except:
            print("That wasn't a number, try again.")
            continue            
    
    all_clients_new[client] = info 

    file_handler = open("data", "w")
    json_string = json.dumps(all_clients_new)
    file_handler.write(json_string)
    file_handler.close()  

    return all_clients, client, info

def json_read():
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)

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
    global all_clients
    if options_table == "V":       
        json_read()     
        return display_clients(all_clients)
    
    elif options_table == "C":
        print("All your client names are: ")
        json_read()
        return list_clients(all_clients)
    
    elif options_table == "A":
# Adding a new client:
        client = input("New client name: ")
        client = client.capitalize()
        file_handler = open("data", "r")
        contents = file_handler.read()
        file_handler.close()
        all_clients = json.loads(contents)     
        info = []
        all_clients_new = all_clients

        return add_client(all_clients_new, client, info)
   
    elif options_table == "M":
        print(owed_money_total())

    elif options_table == "U":
        print("Which client would you like to update?\n")
        file_handler = open("data", "r")
        contents = file_handler.read()
        file_handler.close()
        all_clients = json.loads(contents)
        list_clients(all_clients)
        name = input("Type the name here: \n")
        
        if name in all_clients:
            print("You are editing a current client.")
            update_table = input("""\n
What would you like to update?\n
Press "S" to change status
Press "PS" to change payment status
Press "Q" to change quote\n
Type the letter here: """)
        update_table = update_table.upper().strip().replace(" ", "")
        table = True
        
        while table:
            if update_table == "S":
                status_change = input("What would you like to change the status to? (onboard/offboard) \n")

                file_handler = open("data", "r")
                contents = file_handler.read()
                file_handler.close()
                all_clients = json.loads(contents)

                for key,value in all_clients.items():
                    
                    if key == name:
                         value[0] = status_change
                
                file_handler = open("data", "w")
                json_string = json.dumps(all_clients)
                file_handler.write(json_string)
                file_handler.close() 
                print(f"Status changed!")           
                break

            elif update_table == "PS":
                payment_status_change = input("What would you like to change the payment status to? (paid/not paid)\n")

                file_handler = open("data", "r")
                contents = file_handler.read()
                file_handler.close()
                all_clients = json.loads(contents)

                for key,value in all_clients.items():
                    
                    if key == name:
                         value[1] = payment_status_change
                
                file_handler = open("data", "w")
                json_string = json.dumps(all_clients)
                file_handler.write(json_string)
                file_handler.close() 
                print(f"Payment Status changed!")         
                break
                
            elif update_table == "Q":
                quote_change = int(input("What would you like to change the quote to? \n"))

                file_handler = open("data", "r")
                contents = file_handler.read()
                file_handler.close()
                all_clients = json.loads(contents)

                for key,value in all_clients.items():
                    
                    if key == name:
                         value[2] = quote_change
                
                file_handler = open("data", "w")
                json_string = json.dumps(all_clients)
                file_handler.write(json_string)
                file_handler.close() 
                print(f"Quote changed!")
                break
            
            else:
                print("Unrecognisable option. Try again.")
                table = False
        
        else:
            print("This client doesn't exist.")

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
        print (client)
    

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
    return (f"People owe me ${money_owed}!")

