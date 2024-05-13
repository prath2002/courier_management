class InvalidEmployeeIDException(Exception):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        super().__init__(f"Invalid employee ID: {employee_id}. Employee ID must be an integer.")


class TrackingNumberNotFoundException(Exception):
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        super().__init__(f"Tracking number: {tracking_number} not found")


class DatabaseConnectionError(Exception):
    def __init__(self, message="Error connecting to the database"):
        super().__init__(message)