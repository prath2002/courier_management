
class Employee:
    def __init__(self, employee_id, name, email, contact_number, role, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__email = email
        self.__contact_number = contact_number
        self.__role = role
        self.__salary = salary

    # Property for EmployeeID
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

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

    # Property for ContactNumber
    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self.__contact_number = contact_number

    # Property for Role
    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    # Property for Salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary
