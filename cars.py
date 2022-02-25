class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        print("test")
        self.name = name
        #print(f"Does runs? {runs}")

    def start(self):
        if self.runs:
            print(f"{self.name} car is started.")
        else:
            print(f"{self.name} is broken :(")

  
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels