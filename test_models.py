from models import Driver
import pytest


def test_driver_class():
    # create a new driver
    driver = Driver("Root")
    assert driver.get_total_miles() == 0
    with pytest.raises(ZeroDivisionError):
        driver.get_mph()

    # add a trip
    miles = 13.2
    hours = 0.166667
    driver.add_trip(miles, hours)
    assert driver.get_total_miles() == miles
    assert driver.get_mph() == (miles/hours)
