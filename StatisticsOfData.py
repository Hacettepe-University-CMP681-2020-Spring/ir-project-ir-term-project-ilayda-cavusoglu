import json

# JSON file
f = open('data/data.json', "r", encoding="utf8")

# Reading from file
data = json.loads(f.read())

d = dict()

counter = 0
test_data = []
for i in data:
    json_data = i
    tag = json_data["tag"]
    try:
        d[tag] += 1
    except:
        d[tag] = 0
    counter = counter + 1


print(counter)
print(d)

def get_tag(tag):
    t = None
    if tag == "fire" or tag == "false" or tag == "mostly-false":
        t = "false"
    elif tag == "mostly-true" or tag == "true":
        t = "true"
    elif tag == "half-true":
        t = "half-true"
    return t

d = dict()

counter = 0
test_data = []
for i in data:
    json_data = i
    tag = get_tag(json_data["tag"])
    try:
        d[tag] += 1
    except:
        d[tag] = 0
    counter = counter + 1

print(d)
# Closing file
f.close()
