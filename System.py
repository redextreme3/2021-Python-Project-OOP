import json
from Car import Car as car
from Client import Client as client

available_cars_list = []
rented_cars_list = []
clients_list = []
orders_list = []

with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['car']:
        new_cars = car(p['brand'], p['model'], p['fuel_consumption'], p['license_plate'], int(p['price_per_hour']))
        available_cars_list.append(new_cars)

clients_list.append(client("Mr.", "Admin", 99, '1'))


def get_all_in_list(elements):
    if elements == "available":
        get_all_available_cars()
    elif elements == "rented":
        get_all_rented_cars()
    elif elements == "clients":
        get_all_clients()
    elif elements == "orders":
        get_all_orders()


def get_all_available_cars():
    if len(available_cars_list) < 1:
        print("No available cars at the moment.")
    else:
        print("All cars available for rent: ")
        for e in available_cars_list:
            print(e)


def get_all_rented_cars():
    if len(rented_cars_list) < 1:
        print("No rented cars at the moment.")
    else:
        print("All cars that are currently rented: ")
        for e in rented_cars_list:
            print(e)


def get_all_clients():
    if len(clients_list) < 1:
        print("No registered clients at the moment.")
    else:
        print("All registered clients: ")
        for e in clients_list:
            print(e)


def get_all_orders():
    if len(orders_list) < 1:
        print("No order has been made for the moment.")
    else:
        print("All orders: ")
        for e in orders_list:
            print(e)


def print_menu():
    print("\nTo add a new client type in 1. \n"
          "To add a new car type in 2. \n"
          "To rent a car type in 3. \n"
          "To list all clients type in 4.\n"
          "To list all available cars type in 5.\n"
          "To list all rented cars type in 6.\n"
          "To list all orders type in 7.\n"
          "To exit type in 8.\n"
          "To see this menu again type in 0.\n")


def add_client():
    client_fname = input("Please enter your first name: ")
    client_lname = input("Please enter your last name: ")
    client_age = int(input("Please enter your age: "))
    x = 0
    if client_age < 18:
        print("You must be at least 18 years old to rent a car.")
    else:
        client_number = input("Please enter client number: ")
        for c in clients_list:
            if client_number == c.client_number:
                print("A client with this number already exists. ")
                x = 1
                break
        if x == 0:
            new_client = client(client_fname, client_lname, client_age, client_number)
            clients_list.append(new_client)
            print("Client successfully added.")


def add_car():
    car_brand = input("Please enter brand: ")
    car_model = input("Please enter model: ")
    car_fuel_consumption = input("Please enter fuel consumption: ")
    car_license_plate = input("Please enter license plate: ")
    car_price_per_hour = int(input("Please enter price per hour: "))
    new_car = car(car_brand, car_model, car_fuel_consumption, car_license_plate, car_price_per_hour)
    available_cars_list.append(new_car)


def rent_car():
    discount = False
    total_price = 0
    selected_cars_license_plates_list = []
    client_number = input("Please enter client number: ")
    for cl in clients_list:
        if cl.client_number == client_number:
            count_cars = int(input("Please type in the number of cars you would like to rent: "))
            if count_cars > 3:
                print("Because you rent 3 or more cars at once, you get a 30% discount!")
                discount = True
            while count_cars > 0:
                chosen_car_license_plate = input("Please enter the license plate of the car you wish to rent: ")
                for c in available_cars_list:
                    if c.license_plate == chosen_car_license_plate:
                        rent_type = int(input("Please enter rent type. Type 1 for hours, 2 for a day, 3 for a week: "))
                        if rent_type == 1:
                            rent_time = int(
                                input("Please enter a number for how many hours you want to rent the car for: "))
                            total_price = total_price + (c.get_price("hour") * rent_time)
                        elif rent_type == 2:
                            total_price = total_price + c.get_price("day")
                        elif rent_type == 3:
                            total_price = total_price + c.get_price("week")
                        else:
                            print("Please enter a valid number for rent type.")
                        rented_cars_list.append(c)
                        available_cars_list.remove(c)
                        count_cars = count_cars - 1
                        selected_cars_license_plates_list.append(c.license_plate)
            if discount:
                total_price = total_price - (total_price * 0.3)
            order = cl.get_name(), selected_cars_license_plates_list, total_price
            orders_list.append(order)


if __name__ == "__main__":
    print_menu()
    command = 0
    while True:
        command = int(input("Choose your option: "))
        if command == 0:
            print_menu()
        elif command == 1:
            add_client()
        elif command == 2:
            add_car()
        elif command == 3:
            rent_car()
        elif command == 4:
            get_all_clients()
        elif command == 5:
            get_all_available_cars()
        elif command == 6:
            get_all_rented_cars()
        elif command == 7:
            get_all_orders()
        elif command == 8:
            print("Goodbye, thanks for using me!")
            break
        else:
            print("Please choose a number between 1 and 8.")
