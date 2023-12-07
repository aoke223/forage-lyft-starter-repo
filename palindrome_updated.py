from datetime import datetime
from sternman_updated import SternmanEngine
from spindler_battery import SpindlerBattery
from updated_car import Car

class Palindrome:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = SternmanEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, datetime.today().date())
        self.car = Car(self.engine, self.battery)
    
    def needs_service(self):
        return self.car.needs_service()