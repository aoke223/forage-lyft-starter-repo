from datetime import datetime
from capulet_updated import CapuletEngine
from nubbin_battery import NubbinBattery
from car import Car

class Thovex:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, datetime.today().date())
        self.car = Car(self.engine, self.battery)
    
    def needs_service(self):
        return self.car.needs_service()