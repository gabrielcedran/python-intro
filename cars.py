class Car:
  runs = True

  def __init__(self, name):
    print("test")
    self.name = name
    #print(f"Does runs? {runs}")

  def start(self):
    if self.runs:
      print(f"{self.name} car is started")
    else:
      print(f"{self.name} is broken :(")
