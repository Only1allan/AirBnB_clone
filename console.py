#!/usr/bin/python3
"""Definition of a Airbnb shell"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpeter for our clone"""
    prompt = '(hbnb)'

    classes = {
                "BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity,
                "Place": Place, "Review": Review
              }

    def do_quit(self, args):
        """quitting"""
        return True

    def do_EOF(self, args):
        """End of file """
        return True

    def emptyline(self):
        """pass empty line"""
        pass

    def do_create(self, args):
        """create object from specific class"""
        if not args:
            print("** class name is missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class name missing **")
        else:
            new = HBNBCommand.classes[args]()
            storage.save()
            print(new.id)
            storage.save()

    def do_show(self, args):
        """Print str representation of instance"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        if len(arg) == 1:
            print("** instance id missing **")
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        if "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes object based on name and id"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif "{}.{}".format(arg[0], arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()

    def do_all(self, args):
        """show all objects of a class"""
        objects = []
        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    objects.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                objects.append(str(v))
        print(objects)

    def do_update(self, args):
        """updates an instance"""
        if len(arg) > 0:
            array = args.split()
            if len(array) > 0:
                name = array[0]
                if name in classes:
                    if len(array) > 1:
                        objs_dict = models.storage.all()
                        string = "{}.{}".format(class_name, args_array[1])
                        if string in objs_dict:
                            if len(array) > 2:
                                if len(array) > 3:
                                    if (array[3]
                                            not in
                                            ["created_at",
                                                "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(
                                            array[2]), str(array[3]))
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
