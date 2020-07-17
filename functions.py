# Includes all functions in main.py
import sys
import functions as f
import quotes as q
import random
import time
import pytz
import json
from datetime import datetime
import csv
from colorama import init, Fore, Back, Style
init(autoreset=True)
import pandas as pd
from datetime import date
import username as un
from difflib import get_close_matches

all_clients = dict()

#Instructions
def instructions():
    print("""
Here are the steps to run this application:

1. Run the **./main.py** file in the terminal to start the application.
2. Use the log in details in the **username.py** file to successfully log in and access the application. If you input the incorrect combination three times you will be exited from the application.
3. Press the ENTER key after any input in the terminal to access the option you chose.
4. Make sure your input is as accurate as possible according to the prompts.
5. If you accidentally exit the program, any actions you did during the previous run will remain.
6. To run the program again simply follow Step 1. above. 
""")

# Log in process
def log_in():
    count=3
    while count>0:
        username=input("Enter username: ")
        password=input("Enter password: ")
        if username in un.usernames and password == un.usernames[username]:
            print("\nCorrect combination. Access granted!")
            break
        else:    
            count-=1 
            print(f"Incorrect combination. You have {count} attempts left.")
            
    if count == 0:
        print("Too many attempts. Bye!")
        exit()
        
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
    
# function to read json file
def json_read():
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)

# function to display options table and dealing with the user inputting options
def options_display():
    options_table = input("""
Here are your options:\n
Press "V" to view all clients info
Press "C" to view clients names
Press "A" to add client
Press "M" to see money you're owed currently
Press "U" to update client status
Press "R" to remove client\n
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

    elif options_table == "R":
        remove_a_client()

    elif options_table == "U":
        updating_client_details()

    else:
        print("That wasn't an option. Try again: \n")

#Coloured all client's table
def display_clients(clients):
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)
    print ('\033[31m' + f"{'Client Name':<20} {'Status':<20} {'Payment status':<20} {'Initial Quote':<20}")
    for client, values in sorted(all_clients.items()):
        print (Back.CYAN + f"{client:<20} {values[0]:<20} {values[1]:<20} {values[2]:<20}")

# Clients List only (key in dictionary)
def list_clients(clients):
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients_new = json.loads(contents)
    for client,info in sorted(all_clients_new.items()):
        print (client)

# Money owed to me
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

# Function to remove client
def remove_a_client():
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)
    list_clients(all_clients)
        
    while True:
        name = input("Type the name here that you wish to remove: \n")
        if name in all_clients:
            removed_name = all_clients.pop(name)             
            print(f"You removed {name} from the list of clients.")
            file_handler = open("data", "w")
            json_string = json.dumps(all_clients)
            file_handler.write(json_string)
            file_handler.close() 
            break
        else:
            print("This is not a current client. Try again.")
            continue

# Function called to update client details
def updating_client_details():
    print("Which client would you like to update?\n")
    file_handler = open("data", "r")
    contents = file_handler.read()
    file_handler.close()
    all_clients = json.loads(contents)
    list_clients(all_clients)
        
    while True:
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
            break
        else:
            print("This is not a current client. Try again.")
            continue
        
    table = True     
    while table:
        if update_table == "S":
            status_change = input("What would you like to change the status to? (onboarded/offboarded) \n")

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
            try: 
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
            except:
                print("That wasn't a number, try again.")
                continue                                              
        else:
            print("Unrecognisable option. Try again.")
            table = False
    else:
        print("This client doesn't exist.")

