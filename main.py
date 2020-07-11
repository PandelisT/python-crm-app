# import clients as c
import functions as f
import quotes as q
import random
import time
import pytz
import json
from datetime import datetime
from colorama import init, Fore, Back, Style
init(autoreset=True)

# 1. Log in to application w/ username and password

# print(Fore.BLUE + "\n***** Welcome to Nerdy Pandy's CRM Application *****\n")

# time.sleep(2)

# print("Please enter the correct username and password combination to access this app:\n")

# count=3
# while count>0:
#     username=input("Enter username: ")
#     password=input("Enter password: ")
#     if username =="b" and password =="a":
#         print("\nCorrect combination. Access granted!")
#         break
#     elif username !="b" and password !="a":
#         print(f"Sorry, access denied. You have {count-1} attempts left.")      
#         count-=1 
            
# if count == 0:
#     print("Too many attempts. Bye!")
#     exit()

# # Show current time
# tz_Sydney = pytz.timezone('Australia/Sydney')
# datetime_Sydney = datetime.now(tz_Sydney)
# print("\nYou logged in at: ", datetime_Sydney.strftime("%H:%M:%S"))


# # 2. Random inspirational quote:
# time.sleep(2)
# print("\nReady to start? Here some inspiration for you today:\n")
# inspirational_quote = random.choice(q.quotes)
# print(inspirational_quote)

# # 3. Set goal for today:

# time.sleep(2)
# today_goal = input("\nWhat will your main goal be for today?\n")

# print("\nGood job! I will remind you when you're done here of your goal again!\n")

# 4. Show options table (view clients all info, view client names, add clients, update status of clients):

cont_display = True
while cont_display:   
    action = input("\nWould you like to do something else? (Y/N)\n")
    action = action.upper().strip().replace(" ", "")
    if action == "Y":
        f.options_display()
    elif action == "N":
        cont_display = False
    else:
        print("That wasn't an option. Try again please.")

print(f"Remember your goal for today: {today_goal.capitalize()}. Have a great day!")
 

