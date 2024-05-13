from dao.courier_service_DB import CourierServiceDb
from entity.courier import Courier
from entity.employee import Employee
from exceptions.my_exceptions import DatabaseConnectionError, InvalidEmployeeIDException, TrackingNumberNotFoundException

class MainModule:
    @staticmethod
    def login():
        print('Courier Management System Login')
        print("1. Customer Login")
        print("2. Admin Login")

    @staticmethod
    def user_menu(courier_service):
        print("Courier Management System Customer Menu")
        print("1. Place a new Courier Order")
        print("2. Get Order Status")
        print("3. Cancel a Courier Order")

        option = input("Enter the Operation number: ")
        if option == '1':
            try:
                user_id = input("Insert your user id: ")
                sender_name = input("Insert Sender name: ")
                sender_address = input("Insert Sender address: ")
                receiver_name = input("Insert Receiver name: ")
                receiver_address = input("Insert receiver address: ")
                weight = input("Insert weight of the courier: ")
                status = input("Insert courier status: ")
                tracking_number = input("Insert tracking number: ")
                delivery_date = input("Insert delivery date: ")

                courier = Courier(user_id, sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date)
                if courier_service.insert_order(courier):
                    print("Order Placed successfully.")
                else:
                    print("Failed to Place Order")
            except DatabaseConnectionError as e:
                print("Database connection error:", e)

        elif option == '2':
            try:
                tracking_number = input("Insert tracking id of courier: ")
                get_status = courier_service.get_order_status(tracking_number)
                print(get_status)
            except TrackingNumberNotFoundException as e:
                print("Tracking number not found:", e)
            except DatabaseConnectionError as e:
                print("Database connection error:", e)

        elif option == '3':
            try:
                tracking_number = input("Insert tracking id to cancel the order: ")
                cancel_order = courier_service.cancel_order(tracking_number)
            except TrackingNumberNotFoundException as e:
                print("Tracking number not found:", e)
            except DatabaseConnectionError as e:
                print("Database connection error:", e)

    @staticmethod
    def admin_menu(courier_service):
        print("Courier Management System Admin Menu")
        print("1. Add an Employee")
        print("2. Update an Employee")
        print("3. Delete an Employee")

        option = input("Enter the Operation Number: ")
        if option == '1':
            try:
                employee_name = input("Enter Employee Name: ")
                email = input("Enter E-mail ID: ")
                mobile_number = input("Enter Mobile No.: ")
                role = input("Enter Employee's Role: ")
                salary = input("Enter Employee's Salary: ")
                employee = Employee(employee_name, email, mobile_number, role, salary)
                courier_service.add_employee(employee)
                print("Employee added successfully.")
            except DatabaseConnectionError as e:
                print("Database connection error:", e)

        elif option == '2':
            try:
                employee_id = input("Enter Employee ID to update: ")
                employee_name = input("Enter Updated Employee Name: ")
                email = input("Enter Updated E-mail ID: ")
                mobile_number = input("Enter Updated Mobile No.: ")
                role = input("Enter Updated Employee's Role: ")
                salary = input("Enter Updated Employee's Salary: ")
                employee = Employee(employee_name, email, mobile_number, role, salary, employee_id)
                courier_service.update_employee(employee)
            except DatabaseConnectionError as e:
                print("Database connection error:", e)

        elif option == '3':
            try:
                employee_id = input("Enter Employee ID to delete: ")
                courier_service.delete_employee(employee_id)
            except InvalidEmployeeIDException as e:
                print("Invalid employee ID:", e)
            except DatabaseConnectionError as e:
                print("Database connection error:", e)

    @staticmethod
    def main():
        try:
            courier_service = CourierServiceDb()
            while True:
                MainModule.login()
                choice = input('Enter the User type: ')
                if choice == '1':
                    MainModule.user_menu(courier_service)
                elif choice == '2':
                    MainModule.admin_menu(courier_service)
                else:
                    print("Invalid choice. Please try again.")
        except DatabaseConnectionError as e:
            print("Database connection error:", e)

if __name__ == "__main__":
    MainModule.main()
