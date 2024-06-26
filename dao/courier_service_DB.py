from util.db_connection import DBConnUtil
from entity.courier import Courier
import mysql.connector
from mysql.connector import Error

class CourierServiceDb:
    connection = DBConnUtil.get_connection()

    @staticmethod
    def insert_order(courier: Courier) -> bool:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "INSERT INTO Courier (SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, Packages) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (courier.sender_name, courier.sender_address, courier.receiver_name, courier.receiver_address, courier.weight, courier.status, courier.tracking_number, courier.delivery_date, courier.packages))
            CourierServiceDb.connection.commit()
            cursor.close()
            print("Order inserted successfully.")
            return True
        except Error as e:
            print("Error inserting order:", e)
            return False

    @staticmethod
    def update_courier_status(tracking_number: str, new_status: str) -> bool:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "UPDATE Courier SET Status = %s WHERE TrackingNumber = %s"
            cursor.execute(query, (new_status, tracking_number))
            CourierServiceDb.connection.commit()
            cursor.close()
            print("Courier status updated successfully.")
            return True
        except Error as e:
            print("Error updating courier status:", e)
            return False

    @staticmethod
    def retrieve_delivery_history(tracking_number: str) -> list:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT * FROM Courier WHERE TrackingNumber = %s"
            cursor.execute(query, (tracking_number,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print("Error retrieving delivery history:", e)
            return []

    @staticmethod
    def generate_shipment_status_report() -> list:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT TrackingNumber, Status FROM Courier"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print("Error generating shipment status report:", e)
            return []

    @staticmethod
    def generate_revenue_report() -> list:
        try:
            cursor = CourierServiceDb.connection.cursor()
            query = "SELECT TrackingNumber, Status FROM Courier WHERE Status = 'Delivered'"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print("Error generating revenue report:", e)
            return []
