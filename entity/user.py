class User:
    def __init__(self, user_id, name, email, password, contact_number, address):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address

    # Property for UserID
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    # Property for Name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Property for Email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # Property for Password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    # Property for ContactNumber
    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self.__contact_number = contact_number

    # Property for Address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
