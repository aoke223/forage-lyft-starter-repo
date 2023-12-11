import unittest
from datetime import date
from Tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_needs_service(self):
        tire_wear = [0.8, 0.8, 0.7, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_service(self):
        tire_wear = [0.5, 0.5, 0.5, 0.5]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())