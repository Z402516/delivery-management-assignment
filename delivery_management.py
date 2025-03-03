

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

    def update_inventory(self,items):
        '''
        This method deducts items from inventory.
        :param items:
        :return:
        '''
        pass

    def reorder_items(self,items):
        '''
        This method will allow the company to reorder items in case the items are not enough in the inventory
        :param items:
        :return:
        '''
        pass

    def assign_order(self,order_id,rider):
        '''
        This method takes the order id and the rider and then assign that order to the delivery rider
        for the delivery. We also update the inventory after placing this order.
        :param rider:
        :return:
        '''
        pass


class Order:
    def __init__(self, order_id, reference_id, delivery_date, customer, status):
        self.__order_id = order_id
        self.__reference_id = reference_id
        self.__delivery_date = delivery_date
        self.__delivery_method = "Courier"
        self.__customer = customer
        self.__items = []
        self.__total_price = 0
        self.__status = status

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_reference_id(self):
        return self.__reference_id

    def set_reference_id(self, reference_id):
        self.__reference_id = reference_id
        
    def get_delivery_date(self):
        return self.__delivery_date

    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date
        
    def get_delivery_method(self):
        return self.__delivery_method

    def set_delivery_method(self, delivery_method):
        self.__delivery_method = delivery_method

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

    def generate_invoice(self,customer):
        '''
        This method generates invoice for the customer with their ordered items details.
        :param customer:
        :return:
        '''
        pass

    def calculate_weight(self):
        '''
        This method loops over all the items and calculates the total weight of
        the items which are included in this order.
        :return: 
        '''
        weight = 0
        for item in self.get_items():
            quantity = item[0]
            item = item[1]
            weight += (quantity * item.get_weight())
        return weight

    def deliveryNote(self):
        '''
        This method displays all the information of the delivery items along with the 
        customer information in a delivery note.
        :return: 
        '''
        print("************** Delivery Note **************")
        print("Thank you for using our delivery service! Please print your delivery receipt "
              "and present it upon receiving your items.")
        print("")
        self.get_customer().customer_details()
        print("")
        print("Delivery Information :")
        print("Order Number :",self.get_order_id())
        print("Reference Number :",self.get_reference_id())
        print("Delivery Date :",self.get_delivery_date())
        print("Delivery Method :",self.get_delivery_method())
        print("Total Weight :",self.calculate_weight())
        print("")
        print("Summary of Item Delivered")
        print("Item Code\t\tDescription\t\tQuantity\tUnit Price\tTotal Price")
        self.__total_price = 0
        for item in self.get_items():
            quantity = item[0]
            item = item[1]
            total_item_price = quantity * item.get_price()
            self.__total_price += total_item_price
            print("{}\t\t\t{}\t\t{}\t\t{}\t\t\t{}".format(item.get_item_code(),item.get_description(),
                                                    quantity,item.get_price(),total_item_price))

        print("\nSubtotal : AED",self.__total_price)
        print("Tax (5%): AED",self.__total_price * 0.05)
        print("Total Charges : AED",self.__total_price + (self.__total_price * 0.05))


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

    def deliver_order(self,order_id):
        '''
        This method takes the order id and rider delivers that order. Rider also prints the delivery note for this
        order and presents it upon delivery of the order to the customer. Rider also collects the cash if
        the order is cash on delivery.
        :return:
        '''
        pass

    def collect_cash(self,order_id):
        '''
        This method allows the rider to collect the cash for the order if the order is cash on delivery.
        :param order_id:
        :return:
        '''
        pass


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

    def customer_details(self):
        '''
        This method is for displaying all the information of a customer.
        :return: 
        '''
        print("Recipient Details:")
        print("Name :",self.get_name())
        print("Contact :",self.get_phone())
        print("Delivery Address :",self.get_address())

    def place_order(self,order):
        '''
        This method places an order for the customer, generates invoice for their order and finally deducts the
        ordered items from the inventory.
        :param order:
        :return:
        '''
        pass


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


# Test Objects

# Creating HardwareCompany object
hardware_company = HardwareCompany("Tech Store", "Downtown, Dubai, UAE", "+971-50-1234567")

# Creating Customers
customer1 = Customer(101, "Sarah Williams", "+971-55-9876543", "Business Bay, Dubai, UAE", "sarah@example.com")
customer2 = Customer(102, "Johnson Smith", "+971-52-8765432", "Jumeirah, Dubai, UAE", "johnson@example.com")
customer3 = Customer(103, "Robin Adams", "+971-56-7654321", "Marina, Dubai, UAE", "robin@example.com")

# Creating Items
item1 = Item("KBD101", "RGB Keyboard", 250, 1.2)
item2 = Item("MSE202", "Wireless Mouse", 120, 0.3)
item3 = Item("CAM303", "HD Webcam", 350, 0.8)
item4 = Item("CPAD404", "Cooling Pad", 180, 1.0)
item5 = Item("HSET505", "Gaming Headset", 280, 0.9)
item6 = Item("MON606", "Monitor 4K  ", 900, 3.5)

# Creating Orders
order1 = Order(201, "REF001", "2025-03-05", customer1, "Ready to Deliver")
order2 = Order(202, "REF002", "2025-03-06", customer2, "Ready to Deliver")
order3 = Order(203, "REF003", "2025-03-07", customer3, "Ready to Deliver")

# Adding items to orders (Quantity, Item)
order1.set_items([(1, item1), (1, item2), (1, item5)])
order2.set_items([(2, item3), (1, item4)])
order3.set_items([(1, item6), (1, item2), (1, item1)])

# Creating Delivery Riders
rider1 = DeliveryRider(301, "Ahmed Hassan", "+971-50-6543210", "Bike", [order1])
rider2 = DeliveryRider(302, "Omar Khalid", "+971-55-1239876", "Van", [order2, order3])

# Assigning orders to riders
hardware_company.assign_order(201, rider1)
hardware_company.assign_order(202, rider2)
hardware_company.assign_order(203, rider2)

print("Delivery Note for Order 1")
order1.deliveryNote()
print("\n")
print("Delivery Note for Order 2")
order2.deliveryNote()
print("\n")
print("Delivery Note for Order 3")
order3.deliveryNote()



