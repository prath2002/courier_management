# entity/CourierServices.py

class CourierServices:
    def __init__(self, service_id, service_name, cost):
        self.__service_id = service_id
        self.__service_name = service_name
        self.__cost = cost

    # Property for ServiceID
    @property
    def service_id(self):
        return self.__service_id

    @service_id.setter
    def service_id(self, service_id):
        self.__service_id = service_id

    # Property for ServiceName
    @property
    def service_name(self):
        return self.__service_name

    @service_name.setter
    def service_name(self, service_name):
        self.__service_name = service_name

    # Property for Cost
    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost
