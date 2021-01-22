class Driver:
    def __init__(self, name):
        self.__name = name
        self.__total_miles = 0
        self.__total_hours = 0

    def add_trip(self, miles, hours):
        mph = miles / hours

        # ignore trips with mph < 5 and > 100
        if not (mph < 5 or mph > 100):
            self.__total_miles += miles
            self.__total_hours += hours

    def get_total_miles(self):
        return self.__total_miles

    def get_mph(self):
        return self.__total_miles / self.__total_hours
