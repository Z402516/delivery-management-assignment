

'''

HardwareCompany
Order
DeliveryRider
Customer
Item

Scenario: Placing an Order
Main Use Case: Place Order (Customer)

Includes: Generate Invoice (every order requires an invoice)
Includes: Update Inventory (items must be deducted from stock)


2️⃣ Scenario: Delivering an Order
Main Use Case: Deliver Order (DeliveryRider)

Includes: Assign Delivery Rider (every order must be assigned to a rider)
Includes: Generate Delivery Note (to verify order details)

3️⃣ Scenario: Managing Inventory
Main Use Case: Update Inventory (HardwareCompany)

Includes: Check Stock Level (stock must be updated after each order)
Includes: Record New Stock (new inventory is added)
Extends: Reorder Items (only if stock is below a threshold)

'''


class HardwareCompany:
    def __init__(self, name, address, contact):
        self.__name = name
        self.__address = address
        self.__contact = contact
        self.__inventory = []
        self.__orders = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

    def get_inventory(self):
        return self.__inventory

    def get_orders(self):
        return self.__orders


class Order:
    def __init__(self, order_id, customer, items, total_price, status):
        self.__order_id = order_id
        self.__customer = customer
        self.__items = items
        self.__total_price = total_price
        self.__status = status

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_customer(self):
        return self.__customer

    def set_customer(self, customer):
        self.__customer = customer

    def get_items(self):
        return self.__items

    def set_items(self, items):
        self.__items = items

    def get_total_price(self):
        return self.__total_price

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status




class DeliveryRider:
    def __init__(self, rider_id, name, phone, vehicle, assigned_orders):
        self.__rider_id = rider_id
        self.__name = name
        self.__phone = phone
        self.__vehicle = vehicle
        self.__assigned_orders = assigned_orders

    def get_rider_id(self):
        return self.__rider_id

    def set_rider_id(self, rider_id):
        self.__rider_id = rider_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_vehicle(self):
        return self.__vehicle

    def set_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def get_assigned_orders(self):
        return self.__assigned_orders

    def set_assigned_orders(self, assigned_orders):
        self.__assigned_orders = assigned_orders


class Customer:
    def __init__(self, customer_id, name, phone, address, email):
        self.__customer_id = customer_id
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__email = email

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email


class Item:
    def __init__(self, item_code, description, price, weight):
        self.__item_code = item_code
        self.__description = description
        self.__price = price
        self.__weight = weight

    def get_item_code(self):
        return self.__item_code

    def set_item_code(self, item_code):
        self.__item_code = item_code

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight









