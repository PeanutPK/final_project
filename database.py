"""This is the source of each important function use in project_manage.py"""

import csv
import os
import copy


class Read:
    """
    For reading csv files and use them in table
    """

    def __init__(self, file):
        """
        Initial attribute for reading csv
        :param file:
        """
        self.file = file

    def read_csv(self):
        """
        Read a csv file
        :return:
        """
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        _list = []
        with open(os.path.join(__location__, self.file),
                  encoding='UTF-8') as file:
            rows = csv.DictReader(file)
            for row in rows:
                _list.append(dict(row))
        return _list

    def update_csv(self, table_name: str, key_list: list, my_db):
        """
        Update a csv file
        """
        with open(self.file, "w", encoding='UTF-8') as my_file:
            writer = csv.writer(my_file)
            writer.writerow(key_list)
            for dictionary in my_db.search(table_name).table:
                writer.writerow(dictionary.values())
            my_file.close()


class DB:
    """
    Class for a database (list of table)
    """
    def __init__(self):
        """
        Initialize value to database
        """
        self.__database = []
        self.__name = []

    def search(self, name):
        """
        Search for a table with the given name in a database
        :param name:
        :return:
        """
        for data in self.database:
            if data.name == name:
                return data
        print(f"No table name {name}. Please try again.")
        return None

    def insert(self, new_table):
        """
        Insert a new table to a database and store all names in name list
        :param new_table:
        """
        self.database.append(new_table)
        self.name.append(new_table.name)

    def delete(self, table_delete):
        """
        Delete the table in the database and remove the name of the table from
        a name list
        :param table_delete:
        """
        if self.search(table_delete) is not None:
            self.name.remove(table_delete.name)
            self.database.remove(table_delete)
        self.search(table_delete)

    @property
    def database(self):
        """
        getter for database
        :return database:
        """
        return self.__database

    @property
    def name(self):
        """
        getter for name
        :return names:
        """
        return self.__name

    def list(self):
        """
        for return a name list
        :return name list:
        """
        return f"{self.name}"

    def __str__(self):
        """
        for default string of a database
        :return database:
        """
        return f"{self.database}"


class Table:
    """
    Class for table (list of dict)
    """
    def __init__(self, name, table):
        """
        Initialize attribute for table
        :param name:
        :param table:
        """
        self.name = name
        self.table = table

    def update(self, topic, check, key, value):
        """
        Update an existed table value to new one
        :param topic: What topic for checking
        :param check: Value to check the topic
        :param key: A key topic to change
        :param value: Value of a topic that wants to change
        """
        for data in self.table:
            if data[topic] == check:
                data[key] = value

    def insert(self, new_table):
        """
        Insert new data to the table
        :param new_table:
        """
        self.table.append(new_table)

    def join(self, other_table, key):
        """
        Join two tables into one table
        :param other_table:
        :param key:
        :return joined table:
        """
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
        """
        Filter a table using lambda to find a specific data set
        :param condition:
        :return:
        """
        filtered_table = Table(self.name + "_filtered", [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def select(self, attributes_list):
        """
        Select topics like filter value but filter only the topics
        :param attributes_list:
        :return table with only specific topics:
        """
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        """
        for printing out, the table doesn't perfect but usable
        :return:
        """
        print(self.name)
        _str = ''
        num = 1

        # print dict keys
        _dict_key = self.table[0].keys()
        print(f"{'num':<4}", end='')
        for key in _dict_key:
            print(f" | {key:>14}", end='')

        for num, _dict in enumerate(self.table, start=1):
            values = [f"{i:>14}" for i in _dict.values()]
            _string = " | ".join(values)
            _str += f'\n{num:<4}{_string}'
        return _str


def test():
    """
    For testing some of the function above
    """
    persons = Read("persons.csv")
    login = Read("login.csv").read_csv()
    print("read")
    print(persons.read_csv())
    print()

    my_db = DB()
    my_table = Table("persons", persons.read_csv())
    print("table")
    print(my_table)
    my_db.insert(my_table)
    print()

    print("DB")
    print(my_db.search("persons"))
    print()

    print('admin change admin status')
    my_table.update("ID", "7447677", "type", "faculty")
    print(my_table)
    print()

    print("update")
    my_table.update("ID", "9898118", "type", "lead")
    print(my_table.filter(lambda x: x["ID"] == "9898118"))
    print()

    print("insert login")
    login_table = Table('login', login)
    my_db.insert(login_table)
    print(my_db.search('login'))


if __name__ == "__main__":
    test()
