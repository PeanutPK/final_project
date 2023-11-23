# import database module
from database import DB, Read, Table

# define a function called initializing
my_db = DB()


def initializing():
    """
    Thia function initializing what you need in the main program.
    :return:
    """
    # here are things to do in this function:
    # create an object to read an input csv file, persons.csv
    # create an object to read all csv files that will serve
    # as a persistent state for this program
    persons = Read("persons.csv").readCSV()
    login_t = Read("login.csv").readCSV()
    # create all the corresponding tables for those csv files
    # see the guide how many tables are needed
    person_table = Table("persons", persons)
    login_table = Table("login", login_t)
    project_table = Table(
        "project",
        [
            {
                "ProjectID": "",
                "Title": "",
                "Lead": "",
                "Member1": "",
                "Member2": "",
                "Advisor": "",
                "Status": "",
            }
        ],
    )
    Advisor_pending_request_table = Table(
        "Advisor_pending_request",
        [{"ProjectID": "", "Request": "", "Response": "", "Response_date": ""}],
    )
    Member_pending_request_table = Table(
        "Member_pending_request",
        [{"ProjectID": "", "Request": "", "Response": "", "Response_date": ""}],
    )

    # # Enable the line below to test the table
    # print(person_table)
    # print(login_table)
    # print(project_table)
    # print(Advisor_pending_request_table)
    # print(Member_pending_request_table)

    # add all these tables to the database
    my_db.insert(person_table)
    my_db.insert(login_table)
    my_db.insert(project_table)
    my_db.insert(Advisor_pending_request_table)
    my_db.insert(Member_pending_request_table)


# define a function called login


def login():
    ID = str(input("Type in username: "))
    password_enter = str(input("Type in the password: "))
    my_login = my_db.search("login")
    my_user = my_login.table
    for data in my_user:
        if data["ID"] == ID and data["password"] == password_enter:
            print(f"Welcome {data['username']}")
            print(f"Permission: {data['role']}")
            return data
    print("Your username or password is wrong please try again.")

# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None


# define a function called exit
def exit():
    pass


# Here are things to do in this function:
# write out all the tables that have been modified
# to the corresponding csv files
# By now, you know how to read in a csv file and
# transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse,
# i.e., writing out to a csv file given a list of dictionaries.
# See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that
# performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
