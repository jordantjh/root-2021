from enum import Enum
from datetime import datetime
from models.Driver import Driver


class Command(Enum):
    Driver = 1
    Trip = 2


class ProcessDrives():
    def __init__(self, file_names):
        self.file_names = file_names

    def execute(self):
        """ Generate a report for each file """
        for file_name in self.file_names:
            # Print report header for the current file
            print()
            print("-" * 25)
            print(f"Report: {file_name}")
            print("-" * 25)

            try:
                file = open(file_name, "r")
            except FileNotFoundError:
                print(f"Error: {file_name} not found.\nSkipping the file.\n")
                continue

            data = {}  # driver_name to driver_object map

            for line_index, line in enumerate(file, start=1):
                line_array = line.split()
                try:
                    command = line_array[0]
                except IndexError:
                    # skip empty line
                    continue

                if command == Command.Driver.name:
                    """ Register a new driver """
                    driver_name = line_array[1]  # assume Driver command is always valid
                    data[driver_name] = Driver(driver_name)
                elif command == Command.Trip.name:
                    """ Add a trip to an existing driver """
                    _, driver_name, start_time, end_time, miles_driven = line_array
                    driver = data[driver_name]
                    traveled_hours = self.__get_traveled_hours(
                        start_time, end_time)

                    # ignore trips that has mph <5 or >100
                    mph = float(miles_driven) / traveled_hours
                    driver.add_trip(float(miles_driven), traveled_hours)
                else:
                    print(
                        f"Warning: unknown command in {file_name} at line {line_index}. Line ignored.")

            self.__generate_report(data)
            file.close()

    def __generate_report(self, data):
        """ 
        Description
        -----------
        A helper method to execute().

        Inputs
        ---------
        data: a driver_name to driver_object map

        Output
        ------
        Print to the console,
        the total miles driven and average speed for each driver,
        sorted by most miles driven to least.
        Miles and mph are rounded to the nearest integer.
        """
        sorted_drivers = dict(sorted(data.items(),
                                     key=lambda kv: kv[1].get_total_miles(), reverse=True))
        prev_miles = None
        for name, obj in sorted_drivers.items():
            miles = obj.get_total_miles()

            if miles > 0:
                rounded_miles = round(miles)
                rounded_mph = round(obj.get_mph())
                print(f"{name}: {rounded_miles} miles @ {rounded_mph} mph")
            else:
                print(f"{name}: 0 miles")
        print()

    def __get_traveled_hours(self, start_time, end_time):
        """ Calculate hours traveled """
        time_format = "%H:%M"
        time_delta = datetime.strptime(
            end_time, time_format) - datetime.strptime(start_time, time_format)
        return time_delta.seconds / 3600  # convert from seconds to hours
