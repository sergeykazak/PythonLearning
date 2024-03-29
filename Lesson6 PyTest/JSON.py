import json
import os

def return_file_path(file_name): # method that defines file location and its path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    return file_path

file_name = ".../data/json1.json"
path = return_file_path(file_name)
return_file_path(file_name)
print(path)


json_file = """
        {
            "key1": 1,
            "key2": 2

        }
        """

print(type(json_file)) # returns string

# json.dump()   # function is used to write JSON data to a file. It takes two parameters: a
#               # Python object to be serialized, and a file object to which the JSON data will be written.
# json.dumps()  #function serializes a Python object into a JSON formatted string. It takes a Python
#               # object as input and returns a JSON formatted string.
#
# json.loads() #function is used to convert a JSON formatted string to a Python object.
#              # It takes a JSON string as an argument, parses it, and returns a Python object.
# json.load() # function is used to read JSON data from a file-like object. It takes a file object (or any object
#             # with a read() method) as an argument and reads the JSON data from that object. It then parses the JSON
#             # data and returns a Python object.

json_file1 = json.loads(json_file)
print(json_file1) # {'key1': 1, 'key2': 2}
print(json_file1["key1"])

print("---------------------------------------------------")
dct = {
    "fname": "John",
    "lname": "Doe",
    "age": 45,
    "sex": "Male",
    "occupation": "engineer"
}

print(type(dct))
print(dct)
print("---------------------------------------------------")
json_file2 = json.dumps(dct)
print(type(json_file2))
print(json_file2)


#
# with open(path, "w") as f:
#     json.dump(dct, f)


with open(path, "r") as f:
    a = json.load(f)
print(a)

for key, value in a.items():
    print(key, value)


