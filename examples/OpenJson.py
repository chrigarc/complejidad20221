import json

# Opening JSON file
f = open('data/example.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['clauses']:
    print(i)

print("num_clasues: " + str(data['num_clauses']))
# Closing file
f.close()