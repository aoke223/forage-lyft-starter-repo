from abc import ABC, abstractmethod
from __init__ import CapuletEngine
from __init__ import SpindlerBattery

class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

# This refactored structure makes it easy to add new types of engines or batteries.
# Let's create a sample instance to demonstrate how this would work.

from datetime import datetime, timedelta

# Sample instance creation with arbitrary dates and mileage
sample_engine = CapuletEngine(current_mileage=32000, last_service_mileage=1000)
sample_battery = SpindlerBattery(last_service_date=datetime.now() - timedelta(days=800), current_date=datetime.now())
sample_car = Car(engine=sample_engine, battery=sample_battery)

# Check if the sample car needs service
does_sample_car_need_service = sample_car.needs_service()
does_sample_car_need_service