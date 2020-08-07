# Pandelis Toumbelekis' Customer Relationship Management Terminal App #

This is a README.md which includes instructions to run the application and the software development plan.

Here are the steps to run this application:

1. Execute **./main.py** in the src folder in the terminal to start the application. If you need to access these instructions please run **./main.py --help**.
2. Use the log in details in the **username.py** file to successfully log in and access the application. If you input the incorrect combination three times you will be exited from the application. 
3. Use username "a" and password "a" as default test account to log in.
4. Press the ENTER key after any input in the terminal to access the option you chose.
5. Make sure your input is as accurate as possible according to the prompts.
6. If you accidentally exit the program, any actions you did during the previous run will remain.
7. To run the program again simply follow Step 1. above.

This application has various features that you can access:

- Log your daily business goals
- Access all your clients' data
- Add, remove or update your client data
- Export client data to CSV file
- Log access times

## Software Development Plan ##

### Statement of Purpose and Scope ### 
The application described in this plan has been designed to work as a Customer Relationship Management system which keeps track of customers’ status in a given business. 
It allows the user to log in to access the application, receive daily motivation from inspirational quotes, keep track of their daily goals and perform specific functions such as viewing all clients, adding new clients and updating the status of each client. The program also allows the user to export the client data in csv format and logs time of log in and minutes spent in the program.
This application will allow users to successfully manage customers in their business by keeping track of their status (onboarded or offboarded), payment status and initial quote with the option to update all these details. 
The target audience is any business owners who would like to keep track of their customers in an easy to use and flexible application.

### List of Features ### 
**Feature 1: Login with username and password**

This feature allows multiple users to login to the application through username and password combinations stored in the username.py file as a dictionary data type. The program prompts for the correct username and password combination in a while loop which checks the username.py file and gives access to the application with the correct combination. An incorrect combination will loop three times before exiting the loop and the program completely which mimics being locked out of the program.

**Feature 2: Viewing and accessing client data**

The program allows users to access client data in multiple ways such as viewing all client data, client names and the total money owed by clients who haven’t paid. After the user selects one option and displays the data, the program loops until a condition is met to exit the loop i.e. the user selects “N” to the question “Would you like to do anything else?” The program reads the client information from the data file using JSON format as the data is stored as the dictionary data type. An example of the information in the data file is shown below where the Key of the dictionary is the client’s name, and the value of the dictionary is a list with the client status, payment status and initial quote:
{"Spiro": ["onboarded", "paid", 100]}

**Feature 3: Manipulating and adding new client data**

The program also allows the user to manipulate the data in the data file and write to it in JSON format either by adding a new client altogether or updating the values in the dictionary by accessing indexes in the list as shown above. All of these steps are handled by loops and error handling which checks the input from the user to make sure that the input is valid for e.g. if the initial quote is an integer otherwise an error message will be returned and prompt the user to input the correct value. The while loop continues until the user inputs “N” in the program at the prompt.  

**Feature 4: Storing log in times, daily goals and displaying random inspirational quotes**

The application stores the login times using the pytz module for writing the time based on Sydney time in the time_log file. It also prompts the user to write a daily goal which is stored in a separate file based on date (goal_log) and displays a random quote using the random module from the quotes.py file.

**Feature 5: Exporting all client data to CSV**

At the end of the application, the program prompts the user if they would like to export the client data in CSV format. If the user selects “Y”, the program reads the data file and writes it to the all_clients.csv file. If the user selects “N”, the program exists by displaying the goal submitted at the beginning of the program and a farewell message.

### User interaction and experience ### 

The user will interact through a series of prompts in the terminal. The prompts will assist the user to select the correct option and will display an error message if the user types the incorrect input.

The program is executed with "./main.py" or "./main.py --help" to view the instructions to run the app.

The program begins with a welcome message and sleeps for 2 seconds.

The program then prompts for the correct username and password combination at the beginning of the program and gives access to the application with the correct combination. If the user inputs 3 incorrect combinations in a row the program will exit the loop and stop the application.

The program displays the current time of log in and stores this data in the time_log file.

The program displays a random inspirational quote from list in quotes.py file.

The program prompts the user to enter a goal for the day which will be displayed before the user exits the program and logged in the goal_log file.

The program then asks if the user would like to do anything else in a while loop which exits by selecting “N”. If the user selects “Y” a table is displayed with various options as many times as the user chooses “Y”.

Once a listed option is chosen there are various prompts either for more user input or if there is only a display of information the previous loop starts again. If there is a prompt for user input there are conditional statements and try and except blocks to handle errors.

If the user needs to input information then loops and try and except blocks are used to handle any incorrect information inputted by the user.

If the user selects an option not in the table the user will be prompted again to select a listed option for as many times the user needs to select the correct option.

Once the user selects “N” in the above loop, they are asked if they would like to export the client data to CSV. Selecting “Y” or “N” will continue the program.

The program will display the overall time that the user was logged in in minutes.

The program will display the user’s goal for the day and then show a farewell message before exiting the program.

### Control Flow Diagram ### 

![Flow Diagram](docs/Pandelis-Toumbelekis-T1A3-Control-Flow-Diagram.JPG)

### Implementation Plan ### 

The priorities for this application were the core functionalities which included logging in, accessing and manipulating data and correctly executing the while loops to allow users to easily navigate the application. This is summed up below. Other features such as goal logging and csv exporting were secondary and so were not given a high priority but were included in the final version of this program. 

See spreadsheet PDF here:

[Implementation Plan spreadsheet](/docs/Pandelis-Toumbelekis-T1A3-Implementation-plan.pdf)

Screenshots of checklist here:

![Checklist 1](docs/Implementation_Checklist_1.JPG)
![Checklist 2](docs/Implementation_Checklist_2.JPG)
![Checklist 3](docs/Implementation_Checklist_3.JPG)


See screenshots for tracking of the plan in Trello:

![Day 1](docs/Implementation_Plan_1.JPG)
![Day 2](docs/Implementation_Plan_2.JPG)
![Day 3](docs/Implementation_Plan_3.JPG)
![Day 4](docs/Implementation_Plan_4.JPG)
![Day 5](docs/Implementation_Plan_5.JPG)
![Day 6](docs/Implementation_Plan_6.JPG)
![Day 7](docs/Implementation_Plan_7.JPG)

### Testing ### 

The testing procedure includes testing the log in function, the options displayed in the table during the application including viewing clients, adding clients, updating clients etc. The ID of the features tested are in the implementation plan checklist above.

The testing procedure and test cases are included in the PDF below:

[Manual Testing PDF](docs/Pandelis-Toumbelekis-T1A3-Manual-Testing.pdf)

![Manual Testing 1](/docs/Manual_Testing_1.JPG)
![Manual Testing 2](/docs/Manual_Testing_2.JPG)




