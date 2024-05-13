from abc import ABC, abstractmethod
from entity.employee import Employee
from courier_user_service import ICourierUserService

class ICourierAdminService(ICourierUserService):
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        pass