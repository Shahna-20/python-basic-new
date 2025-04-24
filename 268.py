#Format the Result

#The example above prints a JSON string,
# but it is not very easy to read, with no indentations and line breaks.

#The json.dumps() method has parameters to make
# it easier to read the result:

#Use the indent parameter to define the numbers of indents ?


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

print(json.dumps(x, indent=5))