def move_to(direction: str, distance: float):
    if direction in {"north", "south", "east", "west"}:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

move_to("North", 2)


class Direction:
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

Direction.NORTH
Direction.SOUTH

def move_to(direction: Direction, distance: float):
    pass

from enum import Enum

class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


class DirectionOneLiner(Enum):
    NORTH = 0; SOUTH = 1; EAST = 2; WEST = 3


class DirectionRandomInt(Enum):
    NORTH = 100
    SOUTH = 200
    EAST = 300
    WEST = 400

class DirectionString(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"

north = Direction.NORTH
print("north type:", type(north))
print("north check instance of Direction:", isinstance(north, Direction))

print("north name:", north.name)
print("north value:", north.value)

direction_value = 2
direction = Direction(direction_value)
print("Direction to go:", direction)

unknown_direction = Direction(6)

all_directions = list(Direction)
print(all_directions)

def move_to(direction: Direction, distance: float):
    if direction in Direction:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

tasks_json = """
[
  {
    "title": "Laundry",
    "desc": "Wash clothes",
    "urgency": 3
  },
  {
    "title": "Homework",
    "desc": "Physics + Math",
    "urgency": 5
  }
]
"""    

import json


def get_followers(username):
    # get the followers from the server for the user
    usernames_fetched = ["John", "Aaron", "Zack"]
    followers = [User(username) for username in usernames_fetched]
    return followers

followers = get_followers("Ashley")


class User:
    def __init__(self, username):
        self.username = username
        print(f"### User {username} created")

    def __getattr__(self, item):
        print(f"__getattr__ called for {item}")
        if item == "profile_data":
            profile_data = self._get_profile_data()
            setattr(self, item, profile_data)
            return profile_data

    def _get_profile_data(self):
        # get the data from the server and load it into memory
        print("*** Run the expensive operation")
        fetched_data = "Extensive data, including thumbnail, followers, etc."
        return fetched_data

# Action 1
followers = get_followers("Ashley")
follower0 = followers[0]
follower0.profile_data
follower0.profile_data

class User:
    def __init__(self, username):
        self.username = username
        self._profile_data = None
        print(f"### User {username} created")

    @property
    def profile_data(self):
        if self._profile_data is None:
            print("_profile_data is None")
            self._profile_data = self._get_profile_data()
        else:
            print("_profile_data is set")
        return self._profile_data
    
    def _get_profile_data(self):
        # get the data from the server and load it into memory
        print("*** Run the expensive operation")
        fetched_data = "Extensive data, including thumbnail, followers, etc."
        return fetched_data

followers = get_followers("Ashley")
follower0 = followers[0]
follower0.profile_data
follower0.profile_data

from dataclasses import dataclass

@dataclass
class BaseBill:
    meal_amount: float = 50

@dataclass
class TippedBill(BaseBill):
    tip_amount: float = 0


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.account_number = self.get_account_number()
        self.balance = self.get_balance()
        age, gender, race = self.get_demographics()
        self.age = age
        self.gender = gender
        self.race = race

    def get_account_number(self):
        # query database to locate the account number using student_id
        account_number = 123456
        return account_number

    def get_balance(self):
        # query database to get the balance for the account number
        balance = 100.00
        return balance

    def get_demographics(self):
        # query database to get the demographics using student_id
        birthday = "08/14/2010"
        age = self.calculated_age(birthday)
        gender = "Female"
        race = "Black"
        return age, gender, race

    @staticmethod
    def calculated_age(birthday):
        # get today's date and calculate the difference from birthday
        age = 12
        return age

