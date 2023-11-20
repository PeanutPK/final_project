# try wrapping the code below that reads a persons.csv file in a class
# and make it more general such that it can read in any csv file

import csv
import os
import copy

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Read:
    def __init__(self, name):
        self.name = name

    def readCSV(self):
        _list = []
        with open(os.path.join(__location__, self.name)) as f:
            rows = csv.DictReader(f)
            for row in rows:
                _list.append(dict(row))
        return _list


def gen_comb_list(list_set):
    if len(list_set) == 1:
        start_list = []
        for item in list_set[0]:
            start_list.append([item])
        return start_list
    comb_list_temp = gen_comb_list(list_set[0:-1])
    start_list = []
    for list_item in comb_list_temp:
        for val in list_set[-1]:
            temp_item = copy.deepcopy(list_item)
            temp_item.append(val)
            start_list.append(temp_item)
    return start_list


# add in code for a Database class

class DB:
    def __init__(self):
        self.database = []

    def insert(self, new_table):
        self.database.append(new_table)

    def search(self, name):
        for data in self.database:
            if data == name:
                return data
        print(f"No table name {name}. Please try again")
        return None


# add in code for a Table class

class Table:
    def __init__(self, name, table):
        self.name = name
        self.table = table

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
        filtered_table = Table(self.name + '_filtered', [])
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

    def pivot_table(self, keys_to_pivot_list, keys_to_aggreagte_list,
                    aggregate_func_list):

        unique_values_list = []
        for key_item in keys_to_pivot_list:
            temp = []
            for _dict in self.table:
                if _dict[key_item] not in temp:
                    temp.append(_dict[key_item])
            unique_values_list.append(temp)

        # combination of unique value lists
        comb_list = gen_comb_list(unique_values_list)

        pivot_table = []
        # filter each combination
        for item in comb_list:
            temp_filter_table = self
            for i in range(len(item)):
                temp_filter_table = temp_filter_table.filter(
                    lambda x: x[keys_to_pivot_list[i]] == item[i])

            # aggregate over the filtered table
            aggregate_val_list = []
            for i in range(len(keys_to_aggreagte_list)):
                aggregate_val = temp_filter_table.aggregate(
                    aggregate_func_list[i], keys_to_aggreagte_list[i])
                aggregate_val_list.append(aggregate_val)
            pivot_table.append([item, aggregate_val_list])
        return pivot_table

    def __str__(self):
        return self.name + ':' + str(self.table)


# modify the code in the Table class so that it supports the insert operation
# where an entry can be added to a list of dictionary

def test():
    persons = Read('persons.csv')
    print(persons.readCSV())
