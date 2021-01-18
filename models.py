from enum import Enum


class Command(Enum):
    Driver = 1
    Trip = 2


class Driver:
    def __init__(self, name):
        self.__name = name
        self.__total_miles = 0
        self.__total_hours = 0

    def add_trip(self, miles, hours):
        self.__total_miles += miles
        self.__total_hours += hours

    def get_total_miles(self):
        return self.__total_miles

    def get_mph(self):
        return self.__total_miles / self.__total_hours
