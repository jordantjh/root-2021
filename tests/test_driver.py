from models.Driver import Driver
import pytest


def test_driver_class():
    # create a new driver
    driver = Driver("Root")
    assert driver.get_total_miles() == 0
    with pytest.raises(ZeroDivisionError):
        driver.get_mph()

    # add a valid trip
    miles_1 = 13.2
    hours_1 = 0.166667
    driver.add_trip(miles_1, hours_1)
    assert driver.get_total_miles() == miles_1
    assert driver.get_mph() == (miles_1/hours_1)

    # add a second valid trip
    miles_2 = 18.1
    hours_2 = 0.5
    driver.add_trip(miles_2, hours_2)
    total_miles = miles_1 + miles_2
    total_hours = hours_1 + hours_2
    assert driver.get_total_miles() == total_miles
    assert driver.get_mph() == (total_miles/total_hours)

    # add an invalid trip (<5 mph)
    miles_2 = 2
    hours_2 = 1
    driver.add_trip(miles_2, hours_2)
    assert driver.get_total_miles() == total_miles
    assert driver.get_mph() == (total_miles/total_hours)

    # add an invalid trip (>100 mph)
    miles_2 = 300
    hours_2 = 1
    driver.add_trip(miles_2, hours_2)
    assert driver.get_total_miles() == total_miles
    assert driver.get_mph() == (total_miles/total_hours)
