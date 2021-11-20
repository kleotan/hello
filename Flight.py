class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def open_seats(self):
        return self.capacity - len(self.passangers)

    def add_passanger(self, name):
            if not self.open_seats():
                return False
            self.passangers.append(name)
            return True
                
flight = Flight(4)
people = ["Sid", "Dru", "Carl", "Mrs. Marpl", "Patrik"]

for person in people:
    if flight.add_passanger(person):
        print (f"{person} was add seccussfully")

    else:
        print (f"Is not open seats for {person}")