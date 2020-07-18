#!/usr/sbin/python

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

if "--help" in sys.argv:
    f.instructions()
    time.sleep(10)
else:
    pass

print(Fore.BLUE + "\n***** Welcome to Nerdy Pandy's CRM Application *****\n")
time.sleep(2)

# 1. Log in to application w/ username and password

print("Please enter the correct username and password combination to access this app:\n")
f.log_in()

# 2. Show current time

tz_Sydney = pytz.timezone('Australia/Sydney')
datetime_Sydney = datetime.now(tz_Sydney)
print("\nYou logged in at: ", datetime_Sydney.strftime("%H:%M:%S"))

# 3. Start time to calculate total time in program
start_time = datetime.now()

# 4. Random inspirational quote:
time.sleep(2)
print("\nReady to start? Here some inspiration for you today:\n")
inspirational_quote = random.choice(q.quotes)
print(Fore.MAGENTA + inspirational_quote)

# 5. Set goal for today:
time.sleep(2)
today_goal = input("\nWhat will your main goal be for today?\n")
print("\nGood job! I will remind you when you're done here of your goal again!\n")

time.sleep(1)

# 6. Show options table (view clients all info, view client names, add clients, update status of clients):
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

# 7. CSV export options
csv_export = input("Would you like to export all clients data to csv? (Y/N)\n")
csv_export = csv_export.upper().strip().replace(" ", "")
if csv_export == "Y":
    df = pd.read_json(r'data')
    df.to_csv(r'all_clients.csv', index = None)
    print("\nClient data exported.\n")
else:
    pass

# 8. Show end time
tz_Sydney = pytz.timezone('Australia/Sydney')
datetime_Sydney_end = datetime.now(tz_Sydney)
print("\nYou finished at: ", datetime_Sydney_end.strftime("%H:%M:%S"))

# 9. Calculate and show total time spent in program
end_time = datetime.now()            
duration = end_time - start_time          
duration_in_seconds = duration.total_seconds()
minutes =  round(duration_in_seconds/60, 2)

# Log in time in time_log file
f = open("time_log", "a")
datetime_Sydney = str(datetime_Sydney)
f.write(f"\n{datetime_Sydney}")
f.close()

# 10. Log goal in goal_log file
f = open("goal_log", "a")
today = date.today()
datetime_Sydney = str(datetime_Sydney)
f.write(f"\n {today}: {today_goal.capitalize()}")
f.close()

# 11. Print time spent in program
print(f"\nYou spent {minutes} minutes logged on today.\n")

# 12. Exit message
print(f"Remember your goal for today: {today_goal.capitalize()}. Have a great day!")
 
