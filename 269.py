#You can also define the separators,

# default value is (", "     ": "),

# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator ?

import json

x = {
    "name": "john",
    "age":30,
    "married":True,
    "divorced":False,
    "childern":("Ann","Billy"),
    "pets":None,
    "cars": [
        {"model":" 230", "mpg": 27.5},
        {"model":"ford edge", "mpg":25.2}
    ]
}

# use . and a space to separate objects,
# and a space, a = and a space to separate keys from their values

print(json.dumps(x, indent=5, separators=(". " ," = ")))