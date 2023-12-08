import unittest
from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car

class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        engine = CapuletEngine(current_mileage=31000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

# Repeat similar tests for SternmanEngine and WilloughbyEngine...

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        battery = SpindlerBattery(last_service_date=datetime.now() - timedelta(days=365*3), current_date=datetime.now())
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        battery = SpindlerBattery(last_service_date=datetime.now() - timedelta(days=365), current_date=datetime.now())
        self.assertFalse(battery.needs_service())

# Repeat similar tests for NubbinBattery...

class TestCar(unittest.TestCase):
    def test_car_needs_service_engine(self):
        engine = CapuletEngine(current_mileage=31000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.now() - timedelta(days=365), current_date=datetime.now())
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_car_needs_service_battery(self):
        engine = CapuletEngine(current_mileage=10000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.now() - timedelta(days=365*3), current_date=datetime.now())
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_car_does_not_need_service(self):
        engine = CapuletEngine(current_mileage=10000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.now() - timedelta(days=365), current_date=datetime.now())
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

# This if statement ensures that the tests only run when this file is executed directly, not when it's imported
if __name__ == '__main__':
    unittest.main()