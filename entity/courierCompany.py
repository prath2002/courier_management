# entity/CourierCompany.py

class CourierCompany:
    def __init__(self, company_name, courier_details=None, employee_details=None, location_details=None):
        self.__company_name = company_name
        self.__courier_details = courier_details if courier_details is not None else []
        self.__employee_details = employee_details if employee_details is not None else []
        self.__location_details = location_details if location_details is not None else []

    # Property for CompanyName
    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name):
        self.__company_name = company_name

    # Property for CourierDetails
    @property
    def courier_details(self):
        return self.__courier_details

    @courier_details.setter
    def courier_details(self, courier_details):
        self.__courier_details = courier_details

    # Property for EmployeeDetails
    @property
    def employee_details(self):
        return self.__employee_details

    @employee_details.setter
    def employee_details(self, employee_details):
        self.__employee_details = employee_details

    # Property for LocationDetails
    @property
    def location_details(self):
        return self.__location_details

    @location_details.setter
    def location_details(self, location_details):
        self.__location_details = location_details

    # toString method
    def __str__(self):
        return f"Company Name: {self.__company_name}, " \
               f"Courier Details: {self.__courier_details}, " \
               f"Employee Details: {self.__employee_details}, " \
               f"Location Details: {self.__location_details}"
