#Convert a Python object containing all the legal data types ?

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

print(json.dumps(x))