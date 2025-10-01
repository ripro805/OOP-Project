FIXED_FARE = 500

class Passenger:
    def __init__(self, name, phone, bus=None):
        self.name = name
        self.phone = phone
        self.bus = bus
        self.fare = FIXED_FARE
