class Vehicle:

    def __init__(self, maxSpeed, mileage, color="white"):
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        self.color = color

    def assignSeatingCapacity(self, seatingCapacity):
        self.seatingCapacity = seatingCapacity

    def displayProperties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.maxSpeed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seatingCapacity)


vehicle1 = Vehicle(180, 50000)
vehicle1.assignSeatingCapacity(5)
vehicle1.displayProperties()

vehicle2 = Vehicle(200, 75000)
vehicle2.assignSeatingCapacity(4)
vehicle2.displayProperties()
