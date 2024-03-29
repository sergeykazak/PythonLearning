# int([1,2,3]) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#             #int() expects string but doesn't receive it

# int('Hello') #ValueError: invalid literal for int() with base 10: 'Hello'


# raise ValueError('Error')

class NotAdultError(Exception): # we create custom NotAdultError exception inherited from Exception to use it
                                # instead of standard ValueError
    pass

# pass is used to indicate that the NotAdultError class doesn't have any additional methods or attributes.
# It's essentially an empty class definition. The pass statement is necessary because Python requires
# at least one statement inside a class definition, even if that statement does nothing.

# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         raise NotAdultError('Access is denied!!!')
#
# is_adult(12) #ValueError: Access is denied

print('------------------------------------------------------------------')
# try:
#     result = int([1,2])
#     print(result)
# except:
#     print("Incorrect type was used for the agument. Fix it") # system catches all exceptions but continues.
#                                                             #so below we will specify which exceptions should be caught
# print("Program continued")

print('------------------------------------------------------------------')
# try:
#     result = int([12, 23]) # for this method there will be TypeError exception
#     print(result)
# except ValueError: # but here we're validating only for ValueError, TypeError happens and program run stops here
#     print("Problem with argument type")
# print("Program is over")

# below is the sample with tuple of Exceptions


try:
    result = int([12, 12])
    print(result)
except (TypeError, ValueError):
    print("One of the exceptions was raised. Check code above")
print("Program is over")

print('------------------------------------------------------------------')
# below is the sample with else statement fo case when exception was not raised

try:
    result = int('1')
    print(result)
except (TypeError, ValueError):
    print('Exception was raised')
else: # if there
    print('Code worked fine. No exceptions were raised')
print("Program completed successfully")

print('------------------------------------------------------------------')
# below is the sample with else and finally

try:
    result = int('bad')
    print(result)
except (TypeError, ValueError):
    print('Exception was raised for the code above')
else:
    print('Code worked fine. No exceptions were raised')
finally: # this part of code is executed always: with or without exceptions raised before
    print('This part of the code is executed always: either with or without exceptions raised')
print("Program is over")


# Good use cases that demonstrate when finally should be used:
# Sample 1: File Handling
# file = open('example.txt', 'r')
# try:
#     # Read from the file
#     data = file.read()
# finally:
#     # Always close the file
#     file.close()
#
# # Sample 2: Resource Cleanup:
#
# db = connect_to_database()
# try:
#     # Use the database connection
#     result = db.query("SELECT * FROM table")
# finally:
#     # Always close the database connection
#     db.close()


dict = {
    'name': 'John',
    'surname': 'Smith',
    'id': 12345
}

keys = ['name', 'surname', 'age', 'id']

#Task is solved using approach 'Leap of Faith':
#  "Leap of Faith" approach in testing is about focusing on the expected behavior and outcomes
#  rather than explicitly checking all conditions before performing an action. When an exception
#  is expected, try and except blocks (or assertRaises in unittest) are used to handle and verify
#  the expected behavior. This can lead to more concise and focused test code, especially for
#  situations where certain exceptions are expected under specific conditions.
for key in keys:
    try:
        print(dict[key])
    except KeyError:
        print(f'Attention: Key with name {key} does not exist in the dictionary dict')


#Task above can be solved differently using so call YBYL approach:
# LBYTL - look before your leap
# Look before you leap" provides more robustness by explicitly checking the system's state before
# performing an action, making tests less likely to fail due to unexpected conditions.

for key in keys:
    if key not in keys:
        print(f'Key {key} is not presented in the dictionary')
    else:
        print(dict[key])



