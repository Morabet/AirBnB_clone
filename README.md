# 0x00. AirBnB clone - The console

![Project Image](https://github.com/Dikachis/AirBnB_clone/raw/main/web_static/images/65f4a1dd9c51265f49d0.png?raw=true)

## Project Description
This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

## Resources
* [HBNB videos](https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi)
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
    * [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
    * [Python packages](https://docs.python.org/3.4/tutorial/modules.html#packages)
    * [uuid module](https://docs.python.org/3.8/library/uuid.html)
    * [datetime](https://docs.python.org/3.8/library/datetime.html)
    * [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
    * [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
    * [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
    * [AirBnB website](https://www.airbnb.com/)

## Objectives of this project
* ```Creation of a new object (ex: a new "User" or a new "Place")```
* ```Retrieval of an object from a file storage, a database etc… ```
* ```Perform operations on objects (count, compute stats, etc…)```
* ```Update attributes of an object```
* ```Destroy an object```
## The created objects
#### The list of the objects (instances) that can be created are as follows:
* BaseModel
* User
* City
* Amenity
* State
* Review
* Place
## Files and Directories
* ```models``` directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
* ```tests``` directory contains all unit tests.
* ```console.py``` file is the entry point of our command interpreter.
* ```models/base_model.py``` file is the base class of all our models. It contains common elements:
    * attributes: ```id```, ```created_at``` and ```updated_at```
    * methods: ```save()``` and ```to_json()```
* ```models/engine``` directory contains all storage classes (using the same prototype). For the moment I will have only one: ```file_storage.py```. 

## Available commands and what they do
| Commands  | Description|
| ------------- |:-------------:|
| ```quit```      | This command quits or exits the console    |
| ```EOF```     | This command quits or exits the console interpreter when pressed Ctrl+D     |
| ```help``` or ```help <command>```    | Displays all commands or Displays instructions for a specific command (Ex: ```help``` or ```help quit```).    |
|```create <class>``` | Creates an object of type, saves it to a JSON file, and prints the objects ID (Ex: ```create BaseModel``` or ```BaseModel.create()```)|
| ```show <class> <ID>```| Shows string representation of an object (Ex: ```show BaseModel 1234-1234-1234``` or ```BaseModel.show("1234-1234-1234")```)|
| ```destroy <class> <ID>```|  Deletes an objects based on the class name and id (Ex: ```destroy BaseModel 1234-1234-1234``` or ```BaseModel.destroy("1234-1234-1234")```).|
| ```all or all <class>```| Prints all string representations of all objects or Prints all string representations of all objects of a specific class (Ex: ```all BaseModel``` or ```all``` or ```User.all()```). |
| ```update <class> <id> <attribute name> "<attribute value>"```      | Updates an object with a certain attribute (new or existing) (```Usage: update <class name> <id> <attribute name> "<attribute value>```).     |
| ```<class>.all()```      | Same as all ```<class>```     |
| ```<class>.count()```     |   Retrieves the number of objects of a certain class (```Usage: <class name>.count(), Example: User.count()```).   |
| ```<class>.show(<ID>)```     | Same as show ```<class> <ID>```     |
| ```<class>.destroy(<ID>)```      | Same as destroy ```<class> <ID>```     |
| ```<class>.update(<ID>, <attribute name>, <attribute value>```      | Same as update ```<class> <ID> <attribute name> <attribute value>```     |
| ```<class>.update(<ID>, <dictionary representation>)```      | Updates an objects based on a dictionary representation of attribute names and values     |
## How to use it

It can work in two different modes:

**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update 

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb) 
$
```
## Authors

* **Ali El Moussaoui :**  [github.com/AliMoussa-00](https://github.com/AliMoussa-00)

* **Ismail El Morabet :** [github.com/Morabet](https://github.com/Morabet)
