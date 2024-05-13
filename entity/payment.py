class Payment:
    def __init__(self, payment_id, courier_id, location_id, amount, payment_date):
        self.__payment_id = payment_id
        self.__courier_id = courier_id
        self.__location_id = location_id
        self.__amount = amount
        self.__payment_date = payment_date

    # Property for PaymentID
    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        self.__payment_id = payment_id

    # Property for CourierID
    @property
    def courier_id(self):
        return self.__courier_id

    @courier_id.setter
    def courier_id(self, courier_id):
        self.__courier_id = courier_id

    # Property for LocationID
    @property
    def location_id(self):
        return self.__location_id

    @location_id.setter
    def location_id(self, location_id):
        self.__location_id = location_id

    # Property for Amount
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    # Property for PaymentDate
    @property
    def payment_date(self):
        return self.__payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self.__payment_date = payment_date
