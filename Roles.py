import random

# random project name generate by chatGPT
# https://chat.openai.com/share/33dfe95e-e1bf-4c6e-973f-f789567ab5be
random_project_title = ['QuantumHorizon', 'CipherCraft', 'NebulaForge',
                        'VelocityVista', 'SynthSphere', 'LuminaLink',
                        'PinnaclePulse', 'EchoEnigma', 'TerraTraverse',
                        'ZenithZoom', 'AetherAscent', 'PixelPioneer',
                        'CatalystCanvas', 'NovaNexis', 'ZenZone',
                        'SerenitySync', 'QuantumQuasar', 'ApexAlly',
                        'VortexVerve', 'NexusNurturer']


def check(table, topic, new_value_method, ask_message=''):
    """
    For checking, that may work just a prototype
    :param table: The self.db.search()
    :param topic: Such as 'ID' to check in table
    :param new_value_method: The method of checking new value such as
    using name (input message) or id (random from 10000000 to 9999999)
    :param ask_message: The message asks when user needs to type input
    :return new: new value
    """
    new = ''
    # choose between name and id check
    if new_value_method == 'name':  # normal string input
        new = input(f"{ask_message}")
    elif new_value_method == 'id':  # random ID
        new = str(random.randint(1000000, 9999999))
    # incase duplicate
    while table.filter(lambda x: x[topic] == new).table:
        print(f"Your input has already taken try again")  # for easier debug
        if new_value_method == 'name':  # normal string input
            new = input(f"{ask_message}")
        elif new_value_method == 'id':  # random id
            new = str(random.randint(1000000, 9999999))
    return new


class Admin:
    def __init__(self, database):
        self.__role = 'someone'
        self.__id = '9999999'
        self.__db = database

    def admin(self):
        """
        Admin is responsible for administering the database and manages users
        :return:
        """
        print("What do you want to do\n"
              "1. Add entry\n"
              "2. Remove entry\n"
              "3. Update")
        choice = int(input("Pick a number: "))  # let user pick an action
        if choice not in range(1, 4):  # check if input is within the option
            raise ValueError("Not in choice")
        # start the choice
        if choice == 1:
            self.add_entry()
        elif choice == 2:
            self.remove_entry()
        elif choice == 3:
            self.admin_update()

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
        new_ID = check(persons_table, 'ID', 'id')
        new_persons['ID'] = new_ID
        new_login['ID'] = new_ID

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
            new_Type = input(
                "What is your type (admin, faculty, student): ")
        new_persons['type'] = new_Type
        new_login['role'] = new_Type

        # choose password
        new_login['password'] = str(input("Please choose 4 digits password: "))

        # # Test before added
        # print(persons_table, '\n')
        # print(login_table, '\n')

        # insert the new entry
        persons_table.insert(new_persons)
        login_table.insert(new_login)

        # # Test after added
        # print(persons_table, '\n')
        # print(login_table, '\n')

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
        print(
            f"Are you sure you want to delete {reference_table.table[num]}")
        choice = input("(y/n): ")
        while choice not in ['y', 'n']:
            choice = input("Please enter 'y' or 'n': ")
        if choice == 'y':
            deleted_user = reference_table.table.pop(num)
            print(f"deleted: {deleted_user}")
            self.db.search("login").table.pop(num)

    def admin_update(self):
        """
        Update admin forever until press 'q'
        Always input a correct value or else, it will cause an error
        :return:
        """
        # loop until quit for multiple update
        choice = ''
        while choice != 'q':
            self.show_table()  # show table for choosing
            table = input("Which table is do you want to change: ")
            while table not in self.db.name:
                print("Invalid try again")
                table = input("Which table do you want to change: ")

            # assign all variables must be correct
            topic = input("What is the topic for checking: ")
            check = input("What is the value for checking: ")
            key = input("What is the key for changing: ")
            value = input("What is the value for changing: ")
            self.db.search(table).update(topic, check, key, value)

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


class Student:
    def __init__(self, database):
        self.__id = '9999999'
        self.__db = database

    def student(self, user_id):
        """
        Student can decide to become a member or lead
        :return:
        """
        self.id = user_id
        print("What do you want to do\n"
              "1. Become lead\n"
              "2. Check member pending request")
        choice = int(input("Pick a number: "))  # let user pick an action
        if choice not in range(1, 3):  # check if input is within the option
            raise ValueError("Not in choice")
        if choice == 1:
            # change only the role but the student is still a student
            self.db.search('login').update('ID', self.id, 'role', 'lead')
            self.add_project()

    def add_project(self):
        """
        Search and add dict to a table
        """
        # make a variable to store the searched table
        project_table = self.db.search("project")
        lead_username = ''
        for ID in self.db.search("login").table:
            if ID['ID'] == self.id:
                lead_username = ID['username']

        # making a dict for adding new entry for persons and login
        new_project = {'ProjectID': check(project_table, 'ProjectID', 'id'),
                       'Title': check(project_table, 'Title', 'name',
                                      'Enter project name: '),
                       'Lead': f'{lead_username}',
                       'Member1': '',
                       'Member2': '',
                       'Advisor': '',
                       'Status': 'ongoing'}

        # # Test before added
        # print(project_table, '\n')

        # insert the new entry
        project_table.insert(new_project)

        # # Test after added
        # print(project_table, '\n')

    def lead(self, user_id):  # super saiyan student
        """
        Use this student id to test
        'ID': '9898118'
        'username': 'Lionel.M'
        'password': '2977'
        'role': 'lead'
        :return:
        """
        self.id = user_id
        print("What do you want to do\n"
              "1. Send invitation to member/s\n"
              "2. Modify project\n"
              "3. Send request for advisor\n"
              "4. Submit project for evaluation")
        choice = int(input("Pick a number: "))  # let user pick an action
        if choice not in range(1, 5):  # check if input is within the option
            raise ValueError("Not in choice")
        if choice == 1:
            pass

    def send_invite(self, role):
        # set variable of choice and table
        choice = ''
        filter_table = self.db.search("login").filter(lambda x: x[role]).table
        while choice != 'q':
            pass

    @property
    def db(self):
        return self.__db

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
