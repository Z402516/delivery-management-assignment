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
        weight = 0
        for item in self.get_items():
            quantity = item[0]
            item = item[1]
            weight += (quantity * item.get_weight())
        return weight

    def deliveryNote(self):
        print("************** Delivery Note **************")
        print("Thank you for using our delivery service! Please print your delivery receipt "
              "and present it upon receiving your items.")
        print("\n")
        self.get_customer().customer_details()
        print("\n\n")
        print("Delivery Information :")
        print("Order Number :",self.get_order_id())
        print("Reference Number :",self.get_reference_id())
        print("Delivery Date :",self.get_delivery_date())
        print("Delivery Method :",self.get_delivery_method())
        print("Total Weight :",self.calculate_weight())
        print("\n\n")
        print("Summary of Item Delivered")
        print("Item Code\t\tDescription\t\t\tQuantity\tUnit Price\tTotal Price")
        self.__total_price = 0
        for item in self.get_items():
            quantity = item[0]
            item = item[1]
            total_item_price = quantity * item.get_price()
            self.__total_price += total_item_price
            print("{}\t\t{}\t\t\t{}\t{}\t{}".format(item.get_item_code(),item.get_description(),
                                                    quantity,item.get_price(),total_item_price))
        print("\n\n")
        print("Subtotal : AED",self.__total_price)
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

