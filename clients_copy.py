import json

all_clients = {
    "Spiro" : ["onboard","paid",100], 
    "Harry" : ["onboard","paid",200], 
    "Steve" : ["offboard","not paid",300]
    }

file_handler = open("data", "w")

json_string = json.dumps(all_clients)

file_handler.write(json_string)

file_handler.close()
