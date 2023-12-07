# Abstract classes for Engine and Battery
from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

# Concrete Battery Subclasses
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return (self.current_date - self.last_service_date).days / 365 > 2

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        return (self.current_date - self.last_service_date).days / 365 > 4
