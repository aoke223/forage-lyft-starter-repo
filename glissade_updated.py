from datetime import datetime
from willoughby_updated import WilloughbyEngine
from spindler_battery import SpindlerBattery
from updated_car import Car

class Glissade:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, datetime.today().date())
        self.car = Car(self.engine, self.battery)
    
    def needs_service(self):
        return self.car.needs_service()