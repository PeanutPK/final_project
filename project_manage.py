# import files that I use in this code
from database import DB, Read, Table
import sys
from Roles import Admin, Student
from csv_keys import *

my_db = DB()


def initializing():
    """
    Thia function initializing what you need in the main program.
    :return:
    """
    persons = Read("persons.csv").readCSV()
    login_t = Read("login.csv").readCSV()
    person_table = Table("persons", persons)
    login_table = Table("login", login_t)
    project_table = Table("project", Read("Project.csv").readCSV())
    Advisor_pending_request_table = Table(
        "advisor_pending_request",
        Read("Advisor_pending_request.csv").readCSV()
    )
    Member_pending_request_table = Table(
        "member_pending_request", Read("Member_pending_request.csv").readCSV()
    )

    # Enable the line below to test the table
    print(login_table)
    # print(project_table)
    # print(Advisor_pending_request_table)
    # print(Member_pending_request_table)

    # add tables to the database
    my_db.insert(person_table)
    my_db.insert(login_table)
    my_db.insert(project_table)
    my_db.insert(Advisor_pending_request_table)
    my_db.insert(Member_pending_request_table)


def login():
    """
    Using user's id and user's password to enter to a certain role.
    If the user enters the invalid user id or password return, None
    else return, [ID, role]
    :return:
    """
    # set variable for requirement table
    my_login = my_db.search("login")
    my_user = my_login.table

    # input username and password
    username = str(input("Type in username: "))
    password_enter = str(input("Type in the password: "))
    for data in my_user:
        if data["username"] == username and data["password"] == password_enter:
            print(f"Welcome {data['username']}")
            print(f"Permission: {data['role']}")
            return [data['ID'], data['role']]

    # If username or password is/are wrong, run the program again
    print("Your username or password is wrong please try again next time.")
    sys.exit()


def run(value):
    role = value[1]
    userID = value[0]
    if role == 'admin':
        user = Admin(my_db)
        user.admin()
    elif role == 'student':
        user = Student(my_db, userID)
        user.student(userID)
    elif role == 'member':
        pass
    elif role == 'lead':
        user = Student(my_db, userID)
        user.lead(userID)
    elif role == 'faculty':
        pass
    elif role == 'advisor':
        pass


# define a function called exit
def exit():
    """
    For exiting a program and update the csv files.
    :return:
    """
    # update persons.csv
    Read("persons.csv").update_csv('persons', person_key, my_db)

    # update login.csv
    Read("login.csv").update_csv('login', login_key, my_db)

    # update Project.csv
    Read("Project.csv").update_csv("project", project_key, my_db)

    # update Advisor_pending_request.csv
    Read("Advisor_pending_request.csv").update_csv("advisor_pending_request",
                                                   advisor_key, my_db)

    # update Member_pending_request.csv
    Read("Member_pending_request.csv").update_csv("member_pending_request",
                                                  member_key, my_db)

    print('\nprogram ends.........')
    sys.exit()


# link for the code writing down back to csv files
# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python

if __name__ == "__main__":
    initializing()
    val = login()
    run(val)
    exit()
