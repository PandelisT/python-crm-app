import clients as c
import functions as f
import quotes as q
import random
import time

# 1. Log in to application w/ username and password

# print ("Welcome to Nerdy Pandy's CRM Application")

# CorrectUsername = "Pandelis"
# CorrectPassword = "NerdyPandy"

# attempt = True
# while attempt:
#     username = input("Please enter your username: ")
#     if username == CorrectUsername:
#     	password = input("Please enter your password: ")
#     else:
#         print ("Username incorrect!")
#         exit()
#     if password == CorrectPassword:
#         print ("Logged in successfully as " + username)
#         attempt = False
#     else:
#         print ("Password incorrect!")


# 2. Random inspirational quote:

# inspirational_quote = random.choice(q.quotes)
# print(inspirational_quote)

# # 3. Set goal for today:

# time.sleep(5)
# today_goal = input("What will your main goal be for today?\n")

# print("Good job! I will remind you at the end of your goal again!")

# 4. Show options table (view clients all info, view client names, add clients, update status of clients):


options_table = input("""
Press V to view all clients info
Press C to view clients names
Press A to add client
Press U to update client status
""")

if options_table == "V":
    f.display_clients(c.all_clients)
elif options_table == "C":
    print("All  your client names are: ")
    f.list_clients(c.all_clients)
elif options_table == "A":
# Adding a new client:
    client = input("New client name: ")
    info = []
    f.add_client(c.all_clients, client, info)
# Display all clients in table including new one:
    f.display_clients(c.all_clients)
# elif options_table == "U":

# else: 

# Display all clients in table:
# f.display_clients(c.all_clients)

# # function for total money owed by clients
# f.owed_money_total()

# # Clients List
# f.list_clients(c.all_clients)

# Adding a new client:
# client = input("New client name: ")
# info = []
# f.add_client(c.all_clients, client, info)
# # Display all clients in table including new one:
# f.display_clients(c.all_clients)

# dict.update([])








# file_handler = open("data.txt", "w")

# print(file_handler)

# file_handler.close()

 

