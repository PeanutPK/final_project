"""The main part to run and test program"""
import sys
from database import DB, Read, Table
from roles import Admin, Student, Faculty, update_all_csv

my_db = DB()


def initializing():
    """
    Thia function initializing what you need in the main program.
    :return:
    """
    persons = Read("persons.csv").read_csv()
    login_t = Read("login.csv").read_csv()
    person_table = Table("persons", persons)
    login_table = Table("login", login_t)
    project_table = Table("project", Read("Project.csv").read_csv())
    advisor_pending_request_table = Table(
        "advisor_pending_request",
        Read("Advisor_pending_request.csv").read_csv()
    )
    member_pending_request_table = Table(
        "member_pending_request", Read("Member_pending_request.csv").read_csv()
    )

    # Enable the line below to test the table
    print(login_table)

    # add tables to the database
    my_db.insert(person_table)
    my_db.insert(login_table)
    my_db.insert(project_table)
    my_db.insert(advisor_pending_request_table)
    my_db.insert(member_pending_request_table)


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
            print(f"\nWelcome {data['username']}")
            print(f"Permission: {data['role']}\n")
            return [data['ID'], data['role']]

    # If username or password is/are wrong, run the program again
    print("Your username or password is wrong please try again next time.")
    sys.exit()


def run(value):
    """
    The main function to operate the system
    """
    role = value[1]
    user_id = value[0]
    if role == 'admin':
        user = Admin(my_db)
        user.admin()
    elif role == 'student':
        user = Student(my_db, user_id)
        user.student()
    elif role == 'member':
        user = Student(my_db, user_id)
        user.member()
    elif role == 'lead':
        user = Student(my_db, user_id)
        user.lead()
    elif role == 'faculty':
        user = Faculty(my_db, user_id)
        user.faculty()
    elif role == 'advisor':
        user = Faculty(my_db, user_id)
        user.faculty()


# define a function called exit
def exit_program():
    """
    For exiting a program and update the csv files.
    :return:
    """
    update_all_csv(my_db)
    print('\nprogram ends.........')
    sys.exit()


if __name__ == "__main__":
    initializing()
    STOP = ''
    val = login()
    while STOP != 'n':
        run(val)
        STOP = input('\nContinue? (y/n): ')
        print("-" * 21)
    exit_program()
