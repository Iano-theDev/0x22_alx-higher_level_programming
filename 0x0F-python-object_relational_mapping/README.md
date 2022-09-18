# Python Object Relational Mapping
## Object-relational Mappers (ORMs)
An object-relational mapper (ORM) is a code library that
automates the transfer of data stored in relational 
database tables into objects that are more commonly used
in application code.

# TASKS
## 0 Get all states
Write a script that lists all states from the database 
hbtn_0e_0_usa

## 1 Filter states
Write a script that lists all states with a name starting 
with N (upper N) from the database hbtn_0e_0_usa:

## 2 Filter states by user input
Write a script that takes in an argument and displays all 
values in the states table of hbtn_0e_0_usa where name 
matches the argument

## 3 SQL Injection
Once again, write a script that takes in arguments and 
displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument. But this time, write one 
that is safe from MySQL injections!

## 4 Cities by states
Write a script that lists all cities from the database 
hbtn_0e_4_usa

## 5 All cities by state
Write a script that takes in the name of a state as an 
argument and lists all cities of that state, using the 
database hbtn_0e_4_usa

## 6 First State model
Write a python file that contains the class definition of a 
State and an instance Base = declarative_base()

## 7 All states via SQLAlchemy...
Write a script that lists all State objects from the database 
hbtn_0e_6_us

## 8 First State
Write a script that prints the first State object from the 
database hbtn_0e_6_usa

## 9 Contains 'a'
Write a script that lists all State objects that contain the 
letter a from the database hbtn_0e_6_usa

## 10 Get a state
Write a script that prints the State object with the name 
passed as argument from the database hbtn_0e_6_usa

## 11 Add a new state
Write a script that adds the State object “Louisiana” to the 
database hbtn_0e_6_usa

## 12 Update a state
Write a script that changes the name of a State object from 
the database hbtn_0e_6_usa

## 13 Delete states
Write a script that deletes all State objects with a name 
containing the letter a from the database hbtn_0e_6_usa

## 14 Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

* City class:
inherits from Base (imported from model_state)
links to the MySQL table cities
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string of 128 characters and can’t be null
class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id

* Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa 