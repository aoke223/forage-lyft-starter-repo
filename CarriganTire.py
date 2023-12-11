from tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear):
        self.wear = wear
    
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wear)