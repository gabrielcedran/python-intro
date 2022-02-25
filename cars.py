class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print("test")
        self.name = name
        #print(f"Does runs? {runs}")

    def __str__(self):
        return f"My car the {self.name} currently {self.runs}"

    def __repr__(self):
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started.")
        else:
            print(f"{self.name} is broken :(")

  
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels