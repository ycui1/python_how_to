#####################################################################################
#
# 9.1	How do I create enumerations?
#
#####################################################################################
#%%
def move_to(direction: str, distance: float):
    if direction in {"north", "south", "east", "west"}:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

#%%
move_to("North", 2)

# output: Wrong input for direction

#%%
class Direction:
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


#%%
print(Direction.NORTH)
# output: 0

print(Direction.SOUTH)
# output: 1

#%%
from enum import Enum

class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3


#%%
class DirectionOneLiner(Enum):
    NORTH = 0; SOUTH = 1; EAST = 2; WEST = 3

#%%
class DirectionRandomInt(Enum):
    NORTH = 100
    SOUTH = 200
    EAST = 300
    WEST = 400


#%%
class DirectionString(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


#%%
north = Direction.NORTH

print("north type:", type(north))
# output: north type: <enum 'Direction'>

print("north check instance of Direction:", isinstance(north, Direction))
# output: north check instance of Direction: True

#%%
print("north name:", north.name)
# output: north name: NORTH

print("north value:", north.value)
# output: north value: 0

#%%
direction_value = 2

direction = Direction(direction_value)

print("Direction to go:", direction)
# output: Direction to go: Direction.EAST


#%%
# expect the code to fail
unknown_direction = Direction(8)
# ERROR: ValueError: 8 is not a valid Direction

#%%
all_directions = list(Direction)

print(all_directions)
# output: [<Direction.NORTH: 0>, <Direction.SOUTH: 1>, <Direction.EAST: 2>, <Direction.WEST: 3>]

#%%
for direction in Direction:
    pass 


#%%
def move_to(direction: Direction, distance: float):
    if direction in Direction:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)


#%%
move_to(Direction.NORTH, 3)
# output: Go to the Direction.NORTH for 3 miles

#%%
class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    def __str__(self):
        return self.name.lower()


def move_to(direction: Direction, distance: float):
    if direction in Direction:
        message = f"Go to the {direction} for {distance} miles"
    else:
        message = "Wrong input for direction"
    print(message)

move_to(Direction.NORTH, 3)
# output: Go to the north for 3 miles

#####################################################################################
#
# 9.2	How do I use data classes to eliminate boilerplate code?
#
#####################################################################################

#%%
class CustomData:
    def __init__(self, attr0, attr1, attr2):
        self.attr0 = attr0
        self.attr1 = attr1
        self.attr2 = attr2
        
    def __repr__(self):
        return f"CustomData({self.attr0}, {self.attr1}, {self.attr2})"

#%%
from dataclasses import dataclass

@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float


#%%
bill0 = Bill(5, 60.5, "John", 10)

bill_output = f"Today's bill: {bill0}"

print(bill_output)
# output: Today's bill: Bill(table_number=5, meal_amount=60.5, served_by='John', tip_amount=10)

#%%
print(Bill.__annotations__)
# output: {'table_number': <class 'int'>, 'meal_amount': <class 'float'>, 'served_by': <class 'str'>, 'tip_amount': <class 'float'>}


#%%
@dataclass
class Bill:
    table_number: int
    meal_amount: float
    served_by: str
    tip_amount: float = 0


#%%
bill1 = Bill(5, 60.5, "John")

print(bill1)
# output: Bill(table_number=5, meal_amount=60.5, served_by='John', tip_amount=0)


#%%
# expect errors
@dataclass(frozen=True)
class ImmutableBill:
    meal_amount: float
    served_by: str
    
    
immutable_bill = ImmutableBill(50, "John")
immutable_bill.served_by = "David"

# ERROR: dataclasses.FrozenInstanceError: cannot assign to field 'served_by'

#%%
@dataclass
class BaseBill:
    meal_amount: float
    
@dataclass
class TippedBill(BaseBill):
    tip_amount: float

#%%
tipped_bill = TippedBill(60, 10)

print(tipped_bill)
# output: TippedBill(meal_amount=60, tip_amount=10)

#%%
# expect error
@dataclass
class BaseBill:
    meal_amount: float = 50

@dataclass
class TippedBill(BaseBill):
    tip_amount: float

# ERROR: TypeError: non-default argument 'tip_amount' follows default argument

#%%
@dataclass
class BaseBill:
    meal_amount: float = 50

@dataclass
class TippedBill(BaseBill):
    tip_amount: float = 0


#####################################################################################
#
# 9.3	How do I prepare and process JSON data?
#
#####################################################################################
#%%
{
  "title": "Laundry",
  "desc": "Wash clothes",
  "urgency": 3
}

#%%
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

#%%
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
"""    #A

#%%
import json

tasks_read = json.loads(tasks_json)

print(tasks_read)
# output: [{'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3}, {'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5}]

#%%
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    desc: str
    urgency: int
        
    @classmethod
    def task_from_dict(cls, task_dict):
        return cls(**task_dict)

tasks = [Task.task_from_dict(x) for x in tasks_read]

print(tasks)
# output: [Task(title='Laundry', desc='Wash clothes', urgency=3), Task(title='Homework', desc='Physics + Math', urgency=5)]

#%%
json.loads("2.2")
# output: 2.2

json.loads('"A string"')
# output: 'A string'

json.loads('false')    #A
# output: False

json.loads('null') is None    #B
# output: True

#%%
builtin_data = ['text', False, {"0": None, 1: [1.0, 2.0]}]

builtin_json = repr(json.dumps(builtin_data))    #A

print(builtin_json)
# output: '["text", false, {"0": null, "1": [1.0, 2.0]}]'

#%%
json.dumps(tasks[0])

# ERROR: TypeError: Object of type Task is not JSON serializable

#%%
dumped_task = json.dumps(tasks[0], default=lambda x: x.__dict__)

print(dumped_task)
# output: {"title": "Laundry", "desc": "Wash clothes", "urgency": 3}

#%%
task_dict = {"title": "Laundry", "desc": "Wash clothes", "urgency": 3}

print(json.dumps(task_dict, indent=2))
# output the following lines:
{
  "title": "Laundry",
  "desc": "Wash clothes",
  "urgency": 3
}

#%%
user_info = {"name": "John", "age": 35, "city": "San Francisco", "home": "123 Main St.", "zip_code": 12345, "sex": "Male"}

print(json.dumps(user_info, indent=2, sort_keys=True))
# output the following lines:
{
  "age": 35,
  "city": "San Francisco",
  "home": "123 Main St.",
  "name": "John",
  "sex": "Male",
  "zip_code": 12345
}


#####################################################################################
#
# 9.4	How do I create lazy attributes to improve performance?
#
#####################################################################################
#%%
class User:
    def __init__(self, username):
        self.username = username
        self.profile_data = self._get_profile_data()
        print(f"### User {username} created")

    def _get_profile_data(self):
        # get the data from the server and load it into memory
        print("*** Run the expensive operation")
        fetched_data = " Extensive data, including thumbnail, followers, etc."
        return fetched_data


def get_followers(username):
    # get the followers from the server for the user
    usernames_fetched = ["John", "Aaron", "Zack"]
    followers = [User(username) for username in usernames_fetched]
    return followers

#%%
followers = get_followers("Ashley")

#%%
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

#%%
followers = get_followers("Ashley")    #A

follower0 = followers[0]

follower0.profile_data    #C

#%%
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

#%%
followers = get_followers("Ashley")

follower0 = followers[0]
follower0.profile_data

follower0.profile_data


#####################################################################################
#
# 9.5	How do I define classes to have distinct concerns?
#
#####################################################################################
#%%
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

#%%
class Account:
    def __init__(self, student_id):
        # query the database to get additional information using student_id
        self.account_number = 123456
        self.balance = 100

class Demographics:
    def __init__(self, student_id):
        # query the database to get additional information using student_id
        self.age = 12
        self.gender = "Female"
        self.race = "Black"
        
class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.account = Account(self.student_id)
        self.demographics = Demographics(self.student_id)

#%%
student = Student("John", "Smith", "987654")
print(student.account.__dict__)
# output: {'account_number': 123456, 'balance': 100}

print(student.demographics.__dict__)
# output: {'age': 12, 'gender': 'Female', 'race': 'Black'}

#%%
class Account:
    def __init__(self, student_id):
        self.student_id = student_id
        # query the database to get additional information using student_id
        self.account_number = self.get_account_number_from_db()
        self.balance = self.get_balance_from_db()

    def get_account_number_from_db(self):
        # query database to locate the account number using student_id
        account_number = 123456
        return account_number

    def get_balance_from_db(self):
        # query database to get the balance for the account number
        balance = 100.00
        return balance


class Demographics:
    def __init__(self, student_id):
        self.student_id = student_id
        # query the database to get additional information
        age, gender, race = self.get_demographics_from_db()
        self.age = age
        self.gender = gender
        self.race = race

    def get_demographics_from_db(self):
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


#%%
balance_output = f"Balance: {student.account.balance}"

print(balance_output)
# output: Balance: 100.0

#%%
demo = student.demographics

demo_output = f"Age: {demo.age}; Gender: {demo.gender}; Race: {demo.race}"

print(demo_output)
# output: Age: 12; Gender: Female; Race: Black

#%%
class Student:
    # __init__ stays the same

    def get_account_balance(self):
        return self.account.balance
    
    def get_demographics(self):
        demo = self.demographics
        return demo.age, demo.gender, demo.race