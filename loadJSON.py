import json

with open('data.txt') as json_file:
    dat = json.load(json_file)

print(json.dumps(dat, indent=4))