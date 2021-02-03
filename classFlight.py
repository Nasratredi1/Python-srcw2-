class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []  # i create a empty list for passengers.


    def add_passenger(self, name):
        self.passengers.append(name)
        if not self.open_seats(): # equalant to  if  self.open_seats()== 0:
            return False
        self.passengers.append(name)
        return True
        


    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Ahmad", "Mahmood", "Qasim", "Wareed"]
for person in people:
    Success = flight.add_passenger(person)
    if Success:# if flight.add_passenger(person):# you can write on those time when you remove the above l
         print(f"Added {person} to flight succssfully.")
    else:
            print(f" No available seats for {person}")