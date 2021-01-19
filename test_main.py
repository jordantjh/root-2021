from main import ProcessDrives
from models import Driver
import re

MOCK_INPUT_FILES = ["1.txt"]
PD = ProcessDrives(MOCK_INPUT_FILES)


def test_get_traveled_hours():
    """ Test that the hours traveled are calculated correctly given start and end time """
    start_time = "08:00"
    end_time = "10:00"
    traveled_hours = PD._ProcessDrives__get_traveled_hours(
        start_time, end_time)
    assert traveled_hours == 2


def test_generate_report(capfd):
    """ Test that the drivers are sorted from most miles driven to least """
    driver1_name = "driver1"
    driver2_name = "driver2"
    driver3_name = "driver3"
    driver1 = Driver(driver1_name)
    driver2 = Driver(driver2_name)
    driver3 = Driver(driver3_name)
    driver1.add_trip(50, 1.5)
    driver2.add_trip(1, 0.03)
    driver3.add_trip(100, 3)

    mock_data = {
        driver1_name: driver1,
        driver2_name: driver2,
        driver3_name: driver3
    }

    PD._ProcessDrives__generate_report(mock_data)
    captured = capfd.readouterr()

    # capture all printed miles in an array
    # eg: ['100 miles', '50 miles', '1 miles']
    miles = matches = re.findall(r"\d+ miles", captured.out)

    prev_miles = None
    for m in miles:
        cur_miles = float(m.split()[0])
        if prev_miles is None:
            prev_miles = cur_miles
        else:
            assert prev_miles >= cur_miles
            prev_miles = cur_miles
