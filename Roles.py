import random


class Roles:
    def __init__(self, database):
        self.__db = database

    def admin(self):
        """
        Admin is responsible for administering the database and manages users
        :return:
        """
        print("What do you want to do")
        print("1. Add entry")
        print("2. Remove entry")
        choice = int(input("Pick a number: "))  # let user pick an action
        if choice not in [1, 2]:  # check if input is within the option
            raise ValueError
        # start the choice
        if choice == 1:
            self.add_entry()
        elif choice == 2:
            self.remove_entry()

    def add_entry(self):
        """
        Search and add dict to a table
        :return:
        Use this admin id to test
        'ID': '7447677'
        'username': 'Cristiano.R'
        'password': '2255'
        'role': 'admin'
        """
        # make a variable to store the searched table
        persons_table = self.db.search("persons")
        login_table = self.db.search("login")

        # making a dict for adding new entry for persons and login
        new_persons = {'ID': '', 'first': '', 'last': '', 'type': ''}
        new_login = {'ID': '', 'username': '', 'password': '', 'role': ''}

        # checking the existing id and store id
        new_ID = str(random.randint(1000000, 9999999))
        while persons_table.filter(lambda x: x['ID'] == new_ID).table:
            print('ID already taken generating new one')  # for easier debug
            new_ID = str(random.randint(1000000, 9999999))
        new_persons['ID'] = new_ID
        new_login['ID'] = new_ID
        print(new_ID)

        # checking the existing name and store the name
        new_F_name = input("Enter your first name: ")
        new_L_name = input("Enter your last name: ")
        while persons_table.filter(lambda x: x['first'] + x['last'] == (
                new_F_name + new_L_name)).table:
            print('Name already taken enter new one')
            new_F_name = input("Enter your first name: ")
            new_L_name = input("Enter your last name: ")
        new_persons['first'] = new_F_name
        new_persons['last'] = new_L_name
        new_login['username'] = new_F_name + '.' + new_L_name[0]

        # checking the role and store the role
        new_Type = input("What is your type (admin, faculty, student): ")
        while new_Type not in ['admin', 'faculty', 'student']:
            new_Type = input("What is your type (admin, faculty, student): ")
        new_persons['type'] = new_Type
        new_login['role'] = new_Type

        # choose password
        new_login['password'] = int(input("Please choose 4 digits password: "))

        # test before added
        print(persons_table, '\n')
        print(login_table, '\n')

        # insert the new entry
        persons_table.insert(new_persons)
        login_table.insert(new_login)

        # Test after added
        print(persons_table, '\n')
        print(login_table, '\n')

    def remove_entry(self):
        """
        Remove the ID of the specific
        :return:
        """
        # store a variable for a reference table
        reference_table = self.db.search("persons")
        delete_ID = input("Enter the ID you want to delete: ")

        all_id = []
        for value in reference_table.table:
            all_id.append(value['ID'])
        while str(delete_ID) not in all_id:
            print("invalid please enter again")
            delete_ID = input("Enter the ID you want to delete: ")

        num = 0
        for name_id in reference_table.table:
            if name_id['ID'] == delete_ID:
                break
            num += 1
        print(f"Are you sure you want to delete {reference_table.table[num]}")
        choice = input("(y/n): ")
        while choice not in ['y', 'n']:
            choice = input("Please enter 'y' or 'n': ")
        if choice == 'y':
            deleted_user = reference_table.table.pop(num)
            print(f"deleted: {deleted_user}")
            self.db.search("login").table.pop(num)

    def show_table(self):
        """
        Showing all tables if someone wants
        """
        print("\nHere are the list of table")
        for name_list in self.db.name:
            print(f'- {name_list}')

    @property
    def db(self):
        return self.__db
