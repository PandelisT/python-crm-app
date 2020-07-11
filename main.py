import clients as c
import functions as f
import quotes as q
import random
import time

# 1. Log in to application w/ username and password

print ("Welcome to Nerdy Pandy's CRM Application\n")

time.sleep(2)

print("Enter the correct username and password combination to access this app:\n")

count=0
while count<4:
    username=input('Enter username: ')
    password=input('Enter password: ')
    if username =='b' and password =='a':
        print('\nAccess granted')
        break
    elif username !='b' and password !='a':
        print('Access denied. Try again.')
        count+=1       

if count == 4:
    print("Too many attempts. Bye!")
    exit()


# 2. Random inspirational quote:
time.sleep(2)
print("\nDaily inspiration for you today:\n")
inspirational_quote = random.choice(q.quotes)
print(inspirational_quote)

# # 3. Set goal for today:

time.sleep(2)
today_goal = input("\nWhat will your main goal be for today?\n")

print("Good job! I will remind you at the end of your goal again!\n")

# 4. Show options table (view clients all info, view client names, add clients, update status of clients):

cont = True
while cont:   
    action = input("\nWould you like to do something else? (Y/N)\n")
    if action == "Y":
        f.options_display()
    elif action == "N":
        cont = False

print(f"Remember your goal for today: {today_goal}. Have a great day!")



# if options_table == "V":
#     f.display_clients(c.all_clients)
# elif options_table == "C":
#     print("All  your client names are: ")
#     f.list_clients(c.all_clients)

# elif options_table == "A":
# # Adding a new client:
#     client = input("New client name: ")
#     info = []
#     f.add_client(c.all_clients, client, info)
# # Display all clients in table including new one:
#     f.display_clients(c.all_clients)
# # elif options_table == "U":

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

 

