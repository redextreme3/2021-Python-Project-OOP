class Client:

    def __init__(self, fname, lname, age, client_number):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.client_number = client_number

    def get_name(self):
        return self.fname + " " + self.lname

    def get_client(self):
        return self.get_name(), self.age, self.client_number

    def __str__(self):
        return f"{self.get_name()}, Age: {str(self.age)}, Client Number: {str(self.client_number)}"

