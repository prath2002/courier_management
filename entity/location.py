class Location:
    def __init__(self, location_id, location_name, address):
        self.__location_id = location_id
        self.__location_name = location_name
        self.__address = address

    # Property for LocationID
    @property
    def location_id(self):
        return self.__location_id

    @location_id.setter
    def location_id(self, location_id):
        self.__location_id = location_id

    # Property for LocationName
    @property
    def location_name(self):
        return self.__location_name

    @location_name.setter
    def location_name(self, location_name):
        self.__location_name = location_name

    # Property for Address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
