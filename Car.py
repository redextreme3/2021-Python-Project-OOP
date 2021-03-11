class Car:
    def __init__(self, brand, model, fuel_consumption, license_plate, price_per_hour):
        self.brand = brand
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.license_plate = license_plate
        self.price_per_hour = price_per_hour
        self.price_per_day = 24 * price_per_hour
        self.price_per_week = 24 * 7 * price_per_hour

    def get_price(self, types):
        if types == "hour":
            return self.price_per_hour
        elif types == "day":
            return 24 * self.price_per_hour
        elif types == "week":
            return 24 * 7 * self.price_per_hour

    def get_car(self):
        return self.brand, self.model, self.fuel_consumption, self.license_plate, self.price_per_hour

    def __str__(self):
        return f"{self.brand} {self.model}; Fuel Consumption = {self.fuel_consumption}; " \
               f"License Plate: {self.license_plate}; Price (Per Hour): {self.price_per_hour}"


