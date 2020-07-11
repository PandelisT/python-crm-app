import json

file_handler = open("data", "r")

contents = file_handler.read()

file_handler.close()

all_clients = json.loads(contents)

print(all_clients["Spiro"])


