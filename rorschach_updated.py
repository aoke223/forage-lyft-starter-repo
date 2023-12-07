from datetime import datetime
from willoughby_updated import WilloughbyEngine
from nubbin_battery import NubbinBattery
from updated_car import Car

class Rorschach:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, datetime.today().date())
        self.car = Car(self.engine, self.battery)
    
    def needs_service(self):
        return self.car.needs_service()