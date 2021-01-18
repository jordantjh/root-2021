import sys
from datetime import datetime
from models import Command, Driver


def generate_report(data):
    """
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
    print()
    print("-" * 20)
    print("Report".center(20))
    print("-" * 20)
    sorted_drivers = dict(sorted(data.items(),
                                 key=lambda kv: kv[1].get_total_miles(), reverse=True))
    for name, obj in sorted_drivers.items():
        miles = obj.get_total_miles()
        if miles > 0:
            rounded_miles = round(miles)
            rounded_mph = round(obj.get_mph())
            print(f"{name}: {rounded_miles} miles @ {rounded_mph} mph")
        else:
            print(f"{name}: 0 miles")


def main():
    try:
        file = open("input2.txt", "r")
    except FileNotFoundError:
        sys.exit("Error: Input file not found.\nStopping execution.")
    except:
        sys.exit("Unknown error while reading file.")

    data = {}  # driver_name to driver_object map
    time_format = "%H:%M"

    for line_index, line in enumerate(file):
        line_array = line.split()
        try:
            command = line_array[0]
        except IndexError:
            # skip empty line
            continue
        except:
            sys.exit("Unknown error processing a line.")

        if command == Command.Driver.name:
            """ Register a new driver """
            try:
                driver_name = line_array[1]
            except:
                sys.exit("Unknown error processing a Driver command.")
            data[driver_name] = Driver(driver_name)
        elif command == Command.Trip.name:
            """ Add a trip to an existing driver """
            _, driver_name, start_time, end_time, miles_driven = line_array
            driver = data[driver_name]
            time_delta = datetime.strptime(
                end_time, time_format) - datetime.strptime(start_time, time_format)
            traveled_hours = time_delta.seconds / 3600  # convert from seconds to hours
            driver.add_trip(float(miles_driven), traveled_hours)
        else:
            print(
                f"Warning: unknown command at line {line_index + 1}. Line ignored.")

    generate_report(data)
    file.close()


if __name__ == "__main__":
    main()
