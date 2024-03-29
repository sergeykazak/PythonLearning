from data import User
from faker import Faker
import random

faker_en = Faker('En')
faker_en.seed()


def generated_user():
    yield User(
        firstName=faker_en.first_name(),
        # firstName=generated_name(),
        lastName=faker_en.last_name(),
        fullName=generated_name(),
        # phoneNumber=faker_en.phone_number() #Python built-in method
        phoneNumber=generated_phone_number()  #custom method
    )

def generated_name():
    femaleName=faker_en.name_female()
    maleName=faker_en.name_male()
    return random.choice([femaleName,maleName])


def generated_phone_number(): #custom method to generate random phone numbers in range +1415........
    number = '+1415' + ''.join([str(random.randint(0,9)) for _ in range(7)])
    return number


# [str(random.randint(0,9)) for _ in range(7)]: This part of the code creates a list of 7 random digits from 0 to 9.
# The loop variable _ is used to indicate that the individual values generated in each iteration of
# the loop are not needed. The purpose is to generate a list of random digits without using the loop variable.


a = next(generated_user())
print(a)
print(a.firstName) #everytime new fake firstname fake value
print(a.lastName)
print(a.fullName)
print(a.phoneNumber)
