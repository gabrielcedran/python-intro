from operator import mod


class Vehicle:

    def __init__(self, make, model, fuel="petrol"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "petrol":
            return False
        else:
            return True

class Car(Vehicle):
    def __init__(self, make, model, fuel="petrol", num_of_wheels=4):
        super().__init__(make, model, fuel)
        self.num_of_wheels = num_of_wheels