class Roles:
    def __init__(self, database):
        self.__id = '9999999'
        self.__fName = 'Phiranath'
        self.__lName = 'Po-Ngern'
        self.__type = 'creator'
        self.__db = database

    def admin(self):
        """
        Admin is responsible for administering the database and manages users
        :return:
        """
        print("What do you want to do")
        print("1. Add entry")
        print("2. Remove entry")
        choice = int(input("Pick a number: "))
        if choice not in [1, 2]:
            raise ValueError

        self.add_entry({})

    def add_entry(self, _dict: dict):
        """
        Search and add dict to a table
        :param _dict:
        :return:
        """
        pass

    @property
    def id(self):
        return self.__id

    @property
    def fName(self):
        return self.__fName

    @property
    def lName(self):
        return self.__lName

    @property
    def type(self):
        return self.__type

    @property
    def db(self):
        return self.__db
