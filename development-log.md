**Status Updates**

1. Making client data changes persistent.

A significant challenge which I had to discuss with Garret was how to persist data so that any updates to the client details or new clients is saved when the program is exited. Used read/write in JSON format to access and manipulate data in the data file with client details which was a new concept for me. It was challenging to access and manipulate the correct data in the JSON file.

2. Testing input in the while loops when adding/updating client information.

Several loops had to be written to check the correct input when a user is prompted to add a new client or update client details. Testing involved inputting incorrect options for e.g. non-integer data types in the quotes section of the client data and handling that error appropriately. A challenge was accessing the data in the JSON file and being able to manipulate the data and make it persist.
