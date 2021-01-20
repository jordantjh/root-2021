# root-2021

- python 3

consideration notes:

- JavaScript/TypeScript vs Python
  eventually i found that Pytest offers less interfaces than what i'm used to do in Jasmine/Jest and enzyme. But the concepts are the same which i hope i have demonstrate enough via the pytest code
- left the test files out in the root directory and not in a separate "tests" folder because more work needs to be done to make relative imports work and also "folder structure" is not part of the evaluation.
- put the solution into a class: for code organization and testing.
- assert statement to check correct sorting order instead of making the functionality into a separate method and test it using Pytest because the sorting code is pretty much a built-in python function. We just want to make sure the sorting code is not messed with and still correctly sorting the drivers by most miles to least.
- virtual env or not (YES, assume production -> just better to keep things in a venv)
- removed get_name and get_total_hours interfaces from the class because unused for our use case
- rounding up miles and hours to nearest integer only at the presentation end (not inside the driver class)
  to keep the driver class data accurate so that it can be used in other code in the future.
- driver object, track total travel time in hours or mins?
- use dict to store name->driver_obj
  assumption: no two drivers with the same name
- assumption:
  - only two possible commands
    and assume no variation input patterns for those two commands

# Environment Setup

0. Clone the repo and cd into the project folder
1. Create a virtual environment
   python -m venv venv
2. Activate the virtual environment
   Windows: ./venv/Scripts/activate
   MacOS or Linux: source env/bin/activate
3. Install the project dependencies
   pip install -r requirements.txt

# Run the application

cd root-2021
python3 main.py
