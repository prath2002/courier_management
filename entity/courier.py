# entity/Courier.py

class Courier:
    def __init__(self, CourierID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, Packages):
        self.__CourierID = CourierID
        self.__SenderName = SenderName
        self.__SenderAddress = SenderAddress
        self.__ReceiverName = ReceiverName
        self.__ReceiverAddress = ReceiverAddress
        self.__Weight = Weight
        self.__Status = Status
        self.__TrackingNumber = TrackingNumber
        self.__DeliveryDate = DeliveryDate
        self.__Packages = Packages

    @property
    def courier_id(self):
        return self.__CourierID

    @courier_id.setter
    def courier_id(self, CourierID):
        self.__CourierID = CourierID

    @property
    def sender_name(self):
        return self.__SenderName

    @sender_name.setter
    def sender_name(self, SenderName):
        self.__SenderName = SenderName

    @property
    def sender_address(self):
        return self.__SenderAddress

    @sender_address.setter
    def sender_address(self, SenderAddress):
        self.__SenderAddress = SenderAddress

    @property
    def receiver_name(self):
        return self.__ReceiverName

    @receiver_name.setter
    def receiver_name(self, ReceiverName):
        self.__ReceiverName = ReceiverName

    @property
    def receiver_address(self):
        return self.__ReceiverAddress

    @receiver_address.setter
    def receiver_address(self, ReceiverAddress):
        self.__ReceiverAddress = ReceiverAddress

    @property
    def weight(self):
        return self.__Weight

    @weight.setter
    def weight(self, Weight):
        self.__Weight = Weight

    @property
    def status(self):
        return self.__Status

    @status.setter
    def status(self, Status):
        self.__Status = Status

    @property
    def tracking_number(self):
        return self.__TrackingNumber

    @tracking_number.setter
    def tracking_number(self, TrackingNumber):
        self.__TrackingNumber = TrackingNumber

    @property
    def delivery_date(self):
        return self.__DeliveryDate

    @delivery_date.setter
    def delivery_date(self, DeliveryDate):
        self.__DeliveryDate = DeliveryDate

    @property
    def packages(self):
        return self.__Packages

    @packages.setter
    def packages(self, Packages):
        self.__Packages = Packages
