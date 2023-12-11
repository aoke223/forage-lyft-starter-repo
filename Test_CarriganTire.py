import unittest
from datetime import date
from Tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_needs_service(self):
        tire_wear = [0.0, 0.9, 0.5, 0.2]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_service(self):
        tire_wear = [0.0, 0.8, 0.5, 0.2]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())