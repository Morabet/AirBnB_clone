#!/usr/bin/python3
"""
Defining the 'console' module wich will contain the
the CMD interpreter code
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
# a dictionary contains all the classes and thier names
from models.engine.file_storage import classes
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """Implementing the Console command"""

    prompt = '(hbnb) '
    instances = storage.all()

    def do_EOF(self, line):
        """type 'EOF' or 'Ctr-D' to exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """override the 'emptyline' function"""
        pass

    def check_class(self, className):
        """a function to check if a className is valid"""
        if not className:
            print("** class name missing **")

        elif className not in classes.keys():
            print("** class doesn't exist **")
        else:
            return True

        return False

    # ------------------------------------------
    # ----------- create -----------------------
    def do_create(self, line):
        """Implementing the 'create' function"""

        className = line.split()[0] if line else None

        if self.check_class(className):

            obj = classes[className]()
            obj.save()
            print(obj.id)

    def help_create(self):
        """the descrption of the function 'create' when called by 'help'"""
        txt = "* Usage: create <className>\n"
        txt += "* Usage: <className>.create()\n"
        txt += "Creates a new instance of BaseModel, "
        txt += "saves it (to the JSON file) and prints the id"
        print(txt)

    def complete_create(self, text, line, begidx, endidx):
        """give completion suggestions"""
        if not text:
            completions = classes.keys()[:]

        else:
            completions = [f
                           for f in classes.keys()
                           if f.startswith(text)
                           ]
        return completions

    # ------------------------------------------
    # ----------- show -------------------------
    def do_show(self, line):
        """Implementing the 'show' function"""

        args = line.split() if line else []
        className = args[0] if len(args) > 0 else None
        obj_id = args[1] if len(args) > 1 else None

        if self.check_class(className):
            if not obj_id:
                print("** instance id missing **")
            else:
                key = f"{className}.{obj_id}"

                if key not in self.instances.keys():
                    print("** no instance found **")
                else:
                    obj = self.instances[key]
                    print(obj)

    def help_show(self):
        """the descrption of the function 'show' when called by 'help'"""
        txt = "* Usage: show <class name> <id>\n"
        txt += '* Usage: <className>.show("<id>")\n'
        txt += "Creates a new instance of BaseModel, "
        txt += "Prints the string representation of an instance "
        txt += "based on the class name and id"
        print(txt)

    # -------------------------------------------
    # ----------- destroy -----------------------
    def do_destroy(self, line):
        """Implementing the 'destroy' function"""

        args = line.split() if line else []
        className = args[0] if len(args) > 0 else None
        obj_id = args[1] if len(args) > 1 else None

        if self.check_class(className):
            if not obj_id:
                print("** instance id missing **")
            else:
                key = f"{className}.{obj_id}"

                if key not in self.instances.keys():
                    print("** no instance found **")

                else:
                    storage.all().pop(key)
                    storage.save()

    def help_destroy(self):
        """the descrption of the function 'destroy' when called by 'help'"""
        txt = "* Usgae: destroy <class name> <id>\n"
        txt += '* Usage: <className>.destroy("<id>")\n'
        txt += "Deletes an instance based on the class name and id "
        txt += "(save the change into the JSON file)"
        print(txt)

    # ------------------------------------------
    # ----------- all --------------------------
    def do_all(self, line):
        """Implementing the 'all' function"""

        className = line.split()[0] if line else None
        objs = []

        if len(self.instances) > 0:
            if className and className not in classes.keys():
                print("** class doesn't exist **")
                return

            # if no class name passed get all the classes
            # if a 'className' passed check if it is valid
            if not className or (className and className in classes.keys()):
                for key, obj in self.instances.items():
                    # get the objects from 'instances'(__objects)
                    # add string representation of object to 'objs' list

                    if className and className == obj.to_dict()["__class__"]:
                        objs.append(obj.__str__())
                        continue

                    # get all classes
                    if not className and \
                            obj.to_dict()["__class__"] in classes.keys():

                        objs.append(obj.__str__())
                        continue
        print(objs)

    def help_all(self):
        """the descrption of the function 'all' when called by 'help'"""
        txt = "* Usage: all <class name>(optional)\n"
        txt += '* Usage: <className>.all()\n'
        txt += "Prints all string representation of all instances"
        txt += "based or not on the class name"
        print(txt)

    def complete_all(self, text, line, begidx, endidx):
        """give completion suggestions"""
        if not text:
            completions = classes.keys()[:]

        else:
            completions = [f
                           for f in classes.keys()
                           if f.startswith(text)
                           ]
        return completions

    # ------------------------------------------
    # ----------- update -----------------------
    def do_update(self, line):
        """Implementing the 'update' function"""

        args = shlex.split(line) if line else []

        className = args[0] if len(args) > 0 else None
        obj_id = args[1] if len(args) > 1 else None
        att_name = args[2] if len(args) > 2 else None
        att_value = args[3] if len(args) > 3 else None

        if not self.check_class(className):
            return
        if not obj_id:
            print("** instance id missing **")
            return

        # creating the key to search for ' key = "className.id" '
        key = f"{className}.{obj_id}"

        # check if instance of the class name doesn’t exist for the id
        if key not in self.instances.keys():
            print("** no instance found **")
            return

        if not att_name:
            print("** attribute name missing **")
            return
        if not att_value:
            print("** value missing **")
            return

        # getting the instance from the data we have in Json file
        obj = self.instances[key]

        # check if attribute value is of the apropriate type
        # if it is a new attribute then there is no need to check
        if hasattr(obj, att_name):
            if type(getattr(obj, att_name)) != type(att_value):
                try:
                    att_value = type(getattr(obj, att_name))(att_value)
                except ValueError:
                    print("** wrong value **")

        setattr(obj, att_name, att_value)
        obj.save()

    def help_update(self):
        """the descrption of the function 'update' when called by 'help'"""
        txt = '* Usage: update <class name> <id> <attribute name> '
        txt += '"<attribute value>"\n'
        txt += '* Usage: <className>.update("<id>", "<attribute name>", '
        txt += '"<attribute value>")\n'
        txt += "Updates an instance based on the class name and id \n"
        txt += " by adding or updating attribute "
        txt += "(save the change into the JSON file)"
        print(txt)

    # ------------------------------------------
    # ----------- count ------------------------
    def do_count(self, line):
        """retrieve the number of instances of a class"""

        className = line.split()[0] if line else None
        if not self.check_class(className):
            return

        c = 0
        for item in self.instances.values():
            if className == item.to_dict()["__class__"]:
                c += 1
        print(c)

    def help_count(self):
        """the descrption of the function 'count' when called by 'help'"""

        txt = '* Usage: <class name>.count()\n'
        txt += "retrieve the number of instances of a class"
        print(txt)

    # ------------------------------------------
    # ----------- Default - --------------------
    # ------------------------------------------
    def default(self, line):
        """overriding the 'default' function"""

        cmds = {
                "all": self.do_all,
                "create": self.do_create,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
            }
        match = re.search(r"\.", line)

        if match:
            # split the line into two part based on '.'
            line_list = [line[:match.span()[0]], line[match.span()[1]:]]

            match = re.search(r"\((.*?)\)", line_list[1])

            if match:
                match = re.search(r"""(\w+)\.(\w+)\((.*?)\)$""", line)
                if match:
                    args = match.groups()

                    className = args[0]
                    command = args[1]
                    param = args[2]

                    # get all the parameters
                    matches = re.findall(r'"([^"]*)"', param)

                    parameters = ' '.join([
                        f"'{arg}'" if ' ' in arg else
                        arg for arg in matches
                             ])

                    if command in cmds.keys() and className in classes.keys():

                        return cmds[command](className + " " + parameters)

        print(f"*** Unknown syntax: {line}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
