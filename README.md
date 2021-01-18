# root-2021

- python 3

consideration notes:
- removed get_name and get_total_hours interfaces from the class because unused for our use case
- rounding up miles and hours to nearest integer only at the presentation end (not inside the driver class)
    to keep the driver class data accurate so that it can be used in other code in the future.
- driver object, track total travel time in hours or mins?
- use dict to store name->driver_obj
    assumption: no two drivers with the same name
- assumption: 
    - only two possible commands 
      and assume no variation input patterns for those two commands



# Run the application
cd root-2021
python3 main.py

