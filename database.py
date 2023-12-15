# try wrapping the code below that reads a persons.csv file in a class
# and make it more general such that it can read in any csv file

import csv
import os
import copy


class Read:
    def __init__(self, file):
        self.file = file

    def readCSV(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        _list = []
        with open(os.path.join(__location__, self.file)) as f:
            rows = csv.DictReader(f)
            for row in rows:
                _list.append(dict(row))
        return _list


# add in code for a Database class


class DB:
    def __init__(self):
        self.__database = []

    def insert(self, new_table):
        self.__database.append(new_table)

    def search(self, name):
        for data in self.__database:
            if data.name == name:
                return data
        print(f"No table name {name}. Please try again.")
        return None

    def delete(self, table_delete):
        if self.search(table_delete) is not None:
            self.__database.remove(table_delete)
        self.search(table_delete)

    def __str__(self):
        return f"{self.__database}"


# add in code for a Table class


class Table:
    def __init__(self, name, table):
        self.name = name
        self.table = table

    def update(self, userid, key, value):
        for data in self.table:
            if data['ID'] == userid:
                if isinstance(data[key], list):
                    data[key].append(value)
                elif data[key] == 'admin':
                    print("You don't have permission to change admin status.")
                else:
                    data[key] = value

    def search(self, name):
        for data in self.table:
            if data == name:
                return data
        print(f"No table name {name}. Please try again.")
        return None

    def insert(self, new_table):
        self.table.append(new_table)

    def join(self, other_table, key):
        joined_table = Table(self.name + "_joined_" + other_table.name, [])
        for tab1 in self.table:
            for tab2 in other_table.tabel:
                if tab1[key] == tab2[key]:
                    dict1 = copy.deepcopy(tab1)
                    dict2 = copy.deepcopy(tab2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.name + "_filtered", [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def __is_float(self, element):
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            if self.__is_float(item1[aggregation_key]):
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.name + ":" + str(self.table)


# modify the code in the Table class so that it supports the insert operation
# where an entry can be added to a list of dictionary


def test():
    persons = Read("persons.csv")
    login = Read("login.csv").readCSV()
    print("read")
    print(persons.readCSV())
    print()

    my_DB = DB()
    my_table = Table("persons", persons.readCSV())
    print("table")
    print(my_table)
    my_DB.insert(my_table)
    print()

    print("DB")
    print(my_DB.search("persons"))
    print()

    print('admin change admin status')
    my_table.update("7447677", "type", "faculty")
    print(my_table)
    print()

    print("update")
    my_table.update("9898118", "type", "lead")
    print(my_table.filter(lambda x: x["ID"] == "9898118"))
    print()

    print("insert login")
    login_table = Table('login', login)
    my_DB.insert(login_table)
    print(my_DB.search('login'))


test()
# modify the code in the Table class so that it supports the insert operation
# where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation
# where an entry's value associated with a key can be updated
