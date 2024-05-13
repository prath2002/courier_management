# entity/CourierCompanyCollection.py

class CourierCompanyCollection:
    def __init__(self):
        self.__companies = []

    def add_company(self, company):
        self.__companies.append(company)

    def remove_company(self, company):
        self.__companies.remove(company)

    @property
    def companies(self):
        return self.__companies

    @companies.setter
    def companies(self, companies):
        self.__companies = companies

    def __str__(self):
        return f"Companies: {self.__companies}"
