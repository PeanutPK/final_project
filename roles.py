"""This roles.py contains all role class for uses in project_manage.py"""
import random
import sys
from datetime import date
from database import Read

# random project name generate by chatGPT
# https://chat.openai.com/share/33dfe95e-e1bf-4c6e-973f-f789567ab5be
random_project_title = ['QuantumHorizon', 'CipherCraft', 'NebulaForge',
                        'VelocityVista', 'SynthSphere', 'LuminaLink',
                        'PinnaclePulse', 'EchoEnigma', 'TerraTraverse',
                        'ZenithZoom', 'AetherAscent', 'PixelPioneer',
                        'CatalystCanvas', 'NovaNexis', 'ZenZone',
                        'SerenitySync', 'QuantumQuasar', 'ApexAlly',
                        'VortexVerve', 'NexusNurturer']

# keys for each csv file
person_key = ['ID', 'first', 'last', 'type']
login_key = ['ID', 'username', 'password', 'role']
project_key = ['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor',
               'Status', 'Detail', 'Comment', 'Evaluator']
advisor_key = ['ProjectID', 'Request', 'Response', 'Response_date']
member_key = ['ProjectID', 'Request', 'Response', 'Response_date']


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
        print("Your input has already taken try again")
        if new_value_method == 'name':  # normal string input
            new = input(f"{ask_message}")
        elif new_value_method == 'id':  # random id
            new = str(random.randint(1000000, 9999999))
    return new


def update_all_csv(my_db):
    """
    Read and update all csv files
    """
    Read("persons.csv").update_csv('persons', person_key, my_db)
    Read("login.csv").update_csv('login', login_key, my_db)
    Read("Project.csv").update_csv("project", project_key, my_db)
    Read("Advisor_pending_request.csv").update_csv("advisor_pending_request",
                                                   advisor_key, my_db)
    Read("Member_pending_request.csv").update_csv("member_pending_request",
                                                  member_key, my_db)


class Admin:
    """
    This class is for admin type
    """

    def __init__(self, database):
        self.__db = database

    def admin(self):
        """
        Admin is responsible for administering the database and manages users
        :return:
        """
        # let user pick an action
        choice = int(input("What do you want to do as admin\n"
                           "1. Add entry\n"
                           "2. Remove entry\n"
                           "3. Update\n"
                           "Pick a number: "))
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
        new_id = check(persons_table, 'ID', 'id')
        new_persons['ID'] = new_id
        new_login['ID'] = new_id

        # checking the existing name and store the name
        new_f_name = input("Enter your first name: ")
        new_l_name = input("Enter your last name: ")
        while persons_table.filter(lambda x: x['first'] + x['last'] == (
                new_f_name + new_l_name)).table:
            print('Name already taken enter new one')
            new_f_name = input("Enter your first name: ")
            new_l_name = input("Enter your last name: ")
        new_persons['first'] = new_f_name
        new_persons['last'] = new_l_name
        new_login['username'] = new_f_name + '.' + new_l_name[0]

        # checking the role and store the role
        new_type = input("What is your type (admin, faculty, student): ")
        while new_type not in ['admin', 'faculty', 'student']:
            new_type = input(
                "What is your type (admin, faculty, student): ")
        new_persons['type'] = new_type
        new_login['role'] = new_type

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
        delete_id = input("Enter the ID you want to delete: ")

        # Check value
        all_id = []
        for value in reference_table.table:
            all_id.append(value['ID'])
        while str(delete_id) not in all_id:
            print("invalid please enter again")
            delete_id = input("Enter the ID you want to delete: ")

        num = 0
        for name_id in reference_table.table:
            if name_id['ID'] == delete_id:
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
            key_check = input("What is the key for checking: ")
            val_check = input("What is the value for checking: ")
            key_change = input("What is the key for changing: ")
            val_change = input("What is the value for changing: ")
            self.db.search(table).update(key_check, val_check,
                                         key_change, val_change)
            update_all_csv(self.db)

    def show_table(self):
        """
        Showing all tables if someone wants
        """
        print("\nHere are the list of table")
        for name_list in self.db.name:
            print(f'- {name_list}')

    @property
    def db(self):
        """
        getter for db
        """
        return self.__db


class Student:
    """
    This class is for student type
    """

    def __init__(self, database, user_id):
        self.__id = user_id
        self.__db = database

        # set username
        for _user_id in self.db.search("login").table:
            if _user_id['ID'] == self.id:
                self.user_name = _user_id['username']

        # set project id
        for _user_id in self.db.search("project").table:
            if ((self.user_name in [_user_id['Lead'], _user_id['Member1'],
                                    _user_id['Member2']])):
                self.project_id = _user_id['ProjectID']

    def student(self):
        """
        Student can decide to become a member or lead
        :return:
        """
        # let user pick an action
        choice = int(input("What do you want to do as student\n"
                           "1. Become lead\n"
                           "2. Check member pending request\n"
                           "Pick a number or 'q' to exit: "))

        # check if input is within the option
        if choice not in range(1, 3):
            raise ValueError("Not in choice")

        # Become lead
        if choice == 1:
            # change only the role but the student is still a student
            self.db.search('login').update('ID', self.id, 'role', 'lead')
            self.add_project()

            # update login csv and project csv
            Read("login.csv").update_csv('login', login_key, self.db)
            Read("Project.csv").update_csv("project", project_key, self.db)
            print("Project added status changed to lead\n")
            update_all_csv(self.db)

            # Proceed to lead program instead
            print("Please login again to use lead")
            print('\nprogram ends.........')
            sys.exit()

        # Check incoming request
        if choice == 2:
            self.check_member_request()

    def add_project(self):
        """
        Search and add project dict to a table
        """
        # make a variable to store the searched table
        project_table = self.db.search("project")

        # making a dict for adding new entry for persons and login
        new_project = {'ProjectID': check(project_table, 'ProjectID', 'id'),
                       'Title': check(project_table, 'Title', 'name',
                                      'Enter project name: '),
                       'Lead': f'{self.user_name}',
                       'Member1': '',
                       'Member2': '',
                       'Advisor': '',
                       'Status': 'ongoing',
                       'Detail': input("What is your project detail: "),
                       'Comment': '',
                       'Evaluator': ''}

        # insert the new entry
        project_table.insert(new_project)

    def lead(self):  # super saiyan student
        """
        leader function with choices
        :return:
        """
        # let user pick an action
        choice = int(input("What do you want to do as lead\n"
                           "1. Send invitation to member/s\n"
                           "2. Change update project\n"
                           "3. Send request for advisor\n"
                           "4. Submit project for evaluation\n"
                           "5. Check status\n"
                           "Pick a number: "))
        if choice not in range(1, 6):  # check if input is within the option
            raise ValueError("Not in choice")
        if choice == 1:
            self.send_invite_member()
        elif choice == 2:
            self.update_project()
        elif choice == 3:
            self.send_invite_advisor()
        elif choice == 4:
            self.submit_project()
        elif choice == 5:
            self.check_stat()

    def send_invite_member(self):
        """
        Send an invitation to a student that doesn't belong in any project
        """
        # table for finding students
        student_table = self.db.search("login").filter(
            lambda x: x['role'] == 'student')

        # member table filter project
        member_table = self.db.search("member_pending_request")
        member_table_filter = member_table.filter(
            lambda x: x['ProjectID'] == self.project_id)

        # Make dict variable for inserting table
        request_invitation = {'ProjectID': self.project_id, 'Request': '',
                              'Response': 'pending', 'Response_date': ''}

        # Store username of wanted user and
        # Print table of any users who unoccupied
        print(student_table)
        request_user = input("Which username do you want "
                             "to send request to: ")

        # Check username already sent request or not
        while member_table_filter.filter(
                lambda x: x['Request'] == request_user).table:
            print("Invalid user occupied or pending request")
            request_user = input("Which username do you want to "
                                 "send request to: ")
        request_invitation['Request'] = request_user

        # send invitation
        print("\nInvitation sent......\n")
        member_table.insert(request_invitation)

        # update csv files to loop again
        update_all_csv(self.db)

    def send_invite_advisor(self):
        """
        Send an invitation to a faculty only one at a time
        """
        # make table for finding faculty and check pending
        if self.db.search("advisor_pending_request").filter(
                lambda x: x['ProjectID'] == self.project_id).table:
            print("There is still some pending request "
                  "or already have an advisor\n")
            return
        faculty_advisor_table = self.db.search("login").filter(
            lambda x: x['role'] in ['faculty', 'advisor'])

        # advisor table filter project
        advisor_table = self.db.search("advisor_pending_request")

        # Make dict variable for inserting table
        print(faculty_advisor_table)
        request_invitation = {'ProjectID': self.project_id,
                              'Request': input("Which username do you want "
                                               "to send request to: "),
                              'Response': 'pending', 'Response_date': ''}

        # Store username of wanted user and
        # Print table of any users who unoccupied
        print(faculty_advisor_table)

        # send invitation
        print("\nInvitation sent......\n")
        advisor_table.insert(request_invitation)

        # update csv files to loop again
        update_all_csv(self.db)

    def update_project(self):
        """
        Rename or change the detail of the project
        """
        project_table = self.db.search("project")
        choice = input("Which one do you want to change\n"
                       "1. Name\n"
                       "2. Detail\n"
                       "Pick a number: ")
        if choice == 1:
            project_table['Title'] = check(project_table, 'Title', 'name',
                                           'Enter a new project name: ')
        elif choice == 2:
            new = input("What is the new detail: ")
            project_table.update('ProjectID', self.project_id, 'Detail', new)
        Read("Project.csv").update_csv("project", project_key, self.db)

    def submit_project(self):
        """
        Submit project and change status to pending
        """
        # check condition first
        pending_member = self.db.search("member_pending_request").filter(
            lambda x: x['ProjectID'] == self.project_id)
        pending_advisor = self.db.search("advisor_pending_request").filter(
            lambda x: x['ProjectID'] == self.project_id)

        if (pending_member.filter(lambda x: x['Response'] == 'pending').table
                or pending_advisor.filter(
                    lambda x: x['Response'] == 'pending').table):
            print("\nThere is still some pending request")

        # check status
        project_table = self.db.search('project').filter(
            lambda x: x['ProjectID'] == self.project_id)

        # Check if already submitted or not
        # Already submitted
        if project_table.table[0]['Status'] == 'pending':
            print("\nYou already submit the project\n")
            return

        # Did not submit
        if project_table.table[0]['Status'] == 'ongoing':
            print("\nSubmitting a project\n")
            project_table.update('ProjectID', self.project_id,
                                 'Status', 'pending')

        update_all_csv(self.db)

    def check_stat(self):
        """
        Check the status for approval if > 2 then project complete
        """
        project = self.db.search('project').filter(
            lambda x: x['ProjectID'] == self.project_id)
        print(project)
        approve = project.table[0].get('Status').count('A')
        if project.table[0]['Status'] == 'finished':
            print("\n\nCongratulation this project is finished!!!")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        else:
            print(f"You currently have {approve} approve/s")

    def check_member_request(self):
        """
        Check the table of user invitation to accept or leave it
        """
        # Set variable for table
        user_request = self.db.search("member_pending_request").filter(
            lambda x: x['Request'] == self.user_name)
        login_table = self.db.search("login")
        project_table = self.db.search("project")

        # Get the current date from the internet
        current_date = date.today().strftime("%Y/%m/%d")

        # Show table and ask for choice
        print(user_request)

        # Check input for choice
        print('q for exit')
        choice = str(input("Which group ID do you want to accept the offer: "))
        if choice == 'q':
            return
        while not user_request.filter(lambda x: x['ProjectID'] == choice):
            print(f"No ProjectID name {choice} try again\n")
            print('q for exit')
            choice = str(input("Which group ID do you "
                               "want to accept the offer: "))
            if choice == 'q':
                return

        # Check for an available seat in a group
        # check Member1
        if not project_table.filter(
                lambda x: x['ProjectID'] == choice).table[0]['Member1']:
            project_table.update('ProjectID', choice,
                                 'Member1', self.user_name)

            # update accepted and declined projects
            user_request.update('Request', self.user_name,
                                'Response', 'declined')
            user_request.update('ProjectID', choice,
                                'Response', 'accepted')

            # update role
            login_table.update('ID', self.id, 'role', 'member')
            print("updated a role")

        # if Member1 is occupied
        elif not project_table.filter(
                lambda x: x['ProjectID'] == choice).table[0]['Member2']:
            project_table.update('ProjectID', choice,
                                 'Member2', self.user_name)

            # update accepted and declined projects
            user_request.update('Request', self.user_name,
                                'Response', 'declined')
            user_request.update('ProjectID', choice,
                                'Response', 'accepted')

            # update role
            login_table.update('ID', self.id, 'role', 'member')
            print("updated a role")

        else:  # in case a group is already full
            print("Sorry the group is full")
            user_request.update('ProjectID', choice,
                                'Response', 'cancel')

        user_request.update('ProjectID', choice,
                            'Response_date', [current_date])
        update_all_csv(self.db)

    def member(self):
        """
        Member function with choice
        watch and update project
        """
        # let user pick a choice
        choice = int(input("What do you want to do as member\n"
                           "1. Change update project\n"
                           "2. Check status\n"
                           "Pick a number: "))
        if choice not in range(1, 3):  # check if input is within the option
            raise ValueError("Not in choice")
        if choice == 1:
            self.update_project()
        elif choice == 2:
            self.check_stat()

    @property
    def db(self):
        """
        getter for db
        """
        return self.__db

    @property
    def id(self):
        """
        getter for id
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        setter for id
        """
        self.__id = value


class Faculty:
    """
    This class is for faculty type
    """

    def __init__(self, database, user_id):
        self.__id = user_id
        self.__db = database
        # set username
        for _user_id in self.db.search("login").table:
            if _user_id['ID'] == self.id:
                self.user_name = _user_id['username']

    def faculty(self):
        """
        Student can decide to become a member or lead
        :return:
        """
        # let user pick an action
        choice = int(input("What do you want to do as faculty staff\n"
                           "1. Check advisor pending request\n"
                           "2. Evaluate projects\n"
                           "3. See all projects\n"
                           "Pick a number: "))

        # check if input is within the option
        if choice not in range(1, 4):
            raise ValueError("Not in choice")

        # check advisor table
        if choice == 1:
            self.check_faculty_request()

        # evaluate project
        elif choice == 2:
            self.evaluate()

        # show all projects
        elif choice == 3:
            self.show_project_table()

    def check_faculty_request(self):
        """
        Check the table of user invitation to accept or deny it
        """
        # Set variable for table
        user_request = self.db.search("advisor_pending_request").filter(
            lambda x: x['Request'] == self.user_name)
        login_table = self.db.search("login")
        project_table = self.db.search("project")

        # Show table and ask for choice
        print(user_request)

        # Get the current date from the internet
        current_date = date.today().strftime("%Y/%m/%d")

        # find project
        choice = self.project_find_id_consider()
        acceptance = input("Do you want to\n"
                           "1. accept\n"
                           "2. decline\n"
                           "Pick a number: ")

        if acceptance == '1':
            project_table.update('ProjectID', choice, 'Advisor',
                                 self.user_name)

            # update accepted project
            user_request.update('ProjectID', choice, 'Response', 'accepted')

            # update role
            login_table.update('ID', self.id, 'role', 'advisor')
            print("updated table and role")

        elif acceptance == '2':
            # update declined project
            user_request.update('ProjectID', choice, 'Response', 'declined')

            # update table
            print("updated table")

        user_request.update('ProjectID', choice,
                            'Response_date', [current_date])
        update_all_csv(self.db)

    def project_find_id_consider(self):
        """
        Find project of the group you want using id
        """
        print('q for exit')
        choice = str(input("Which group ID do you want to "
                           "accept/decline the offer: "))

        # Check if the user wants to quit or not
        if choice == 'q':
            return None
        user_request = self.db.search("advisor_pending_request").filter(
            lambda x: x['Request'] == self.user_name)
        while not user_request.filter(lambda x: x['ProjectID'] == choice):
            print(f"No ProjectID name {choice} try again\n")
            print('q for exit')
            choice = str(input("Which group ID do you want "
                               "to accept/decline the offer: "))
            if choice == 'q':
                return None

        return choice

    def show_project_table(self):
        """
        Show all projects
        """
        project_table = self.db.search("project")
        print(project_table)

    def evaluate(self):
        """
        Evaluation step:
        1. Let faculties pick the project to evaluate and approve
        2. Check the detail and vote for A (Approve) or D (Decline)
        3. For the project to be complete requirement is 2 A
        """
        # print all projects selected only ID and Title
        print("These are the projects")
        project_table = self.db.search("project").filter(
            lambda x: x['Status'] not in ['ongoing', 'finished'])
        project_title_id = project_table.select(['ProjectID', 'Title'])

        # formatting print value
        num = 1
        for _dict in project_title_id:
            str_num = str(num) + '.'
            print(f"{str_num:<4} {_dict}")
            num += 1
        project_name = input("\nWhich project do you want to evaluate\n"
                             "Choose the title: ")

        # Check a duplicate vote or not
        if self.db.search("project").filter(
                lambda x: self.user_name in x['Evaluator']).table:
            print("\nYou already evaluate this project no cheat")
            return

        # Take out only the dict of the table and
        # show the name and detail of the project
        evaluate_project = project_table.filter(
            lambda x: x['Title'] == project_name).table[0]
        print(f"Title:  {evaluate_project['Title']}\n"
              f"Detail: {evaluate_project['Detail']}")

        # Check faculty who evaluated the project
        if evaluate_project['Evaluator'] == '':
            evaluate_project['Evaluator'] = self.user_name
        if self.user_name not in evaluate_project['Evaluator'].split('+'):
            evaluate_project['Evaluator'] += f"+{self.user_name}"

        # Decide to approve or deny
        choice = input("Do you A (Approve) or D (Deny): ")
        while choice not in ['A', 'D']:
            print("Type only A or D")
            choice = input("Do you A (Approve) or D (Deny): ")

        # Choice Approve
        if choice == 'A':
            # Status checking
            if evaluate_project['Status'] == 'pending':
                evaluate_project['Status'] = choice
            else:
                evaluate_project['Status'] += choice
            # In case if they got more than 2 approve
            if evaluate_project['Status'].count('A') >= 2:
                print("This project is finished")
                evaluate_project['Status'] = 'finished'

        # Choice Deny
        else:
            reason = input("What is the reason of this deny please comment: ")
            if evaluate_project['Status'] == 'pending':
                evaluate_project['Status'] = choice
                evaluate_project['Comment'] = reason
            else:
                evaluate_project['Status'] += choice
                evaluate_project['Comment'] = f"/{reason}"

        update_all_csv(self.db)

    @property
    def db(self):
        """
        getter for db
        """
        return self.__db

    @property
    def id(self):
        """
        getter for id
        """
        return self.__id

    @id.setter
    def id(self, value):
        """
        setter for id
        """
        self.__id = value
