# root-2021

Programming Language: Python 3.9

## Environment Setup

0. Clone the repo and cd into the project folder
1. Create a virtual environment
   ```
   python -m venv myvenv
   ```
2. Activate the virtual environment<br/>
   Windows: _./myvenv/Scripts/activate_<br/>
   MacOS or Linux: _source myvenv/bin/activate_
3. Install the project dependencies
   ```
   pip install -r requirements.txt
   ```

You can exit the virtual environment later with

```
deactivate
```

## Run the App

Execute main.py:

```
python main.py
```

## Test and Test Coverage

To execute all unit tests, run at the root directory:

```
pytest
```

To check the test coverage for each test file:

```
pytest --cov=main
```

```
pytest --cov=models
```

## Engineering Considerations

- JavaScript/TypeScript or Python?<br/>
  The former is my current forte. However, Python seems to be the right tool for the task. If this was a real-world project at Root, I would approach it with Python. Hopefully this also demonstrated that I can adapt and learn on the go.
  This becomes especially apparent when it comes to testing with Pytest which is considerably different from Jest/Enzyme/Jasmine/Sinon in terms of syntax and approaches but the general testing concept did transfer well.

- Arranging the solutions into modular classes and functions makes the code more organized and easier to be tested.

- Since folder structure is not mentioned to be part of the evaluation criteria, I have left the test files in the root directory instead of keeping them in a "tests" folder for example because it requires a little more work to make relative imports work.

- Use a virtual environment or not?<br/>
  Since it is generally a good practice to run and setup Python program in a virtual environment. I decided to follow so and included a guide to help users to do the same.

- Initially there were more methods in the class "ProcessDrives", they were mainly getter methods that expose class attributes. However, since my solution doesn't utilize them, I have decided to remove these interfaces to avoid confusions.

- I am only rounding up the miles and hours at the point of presentation. In the "Driver" class itself, the attributes are stored as float data type to preserve accuracy.

- Should I keep track of the time traveled by a driver in hours or minutes unit?<br/>
  Since the "Driver" class will have to calculate mph, I have decided to go with hours unit.

## Assumptions

1. Assume no two drivers have the same name.
2. Assume only two possible commands as mentioned in the problem statement and that these commands will always appear with correct formats and values.
3. Assume "Driver" command will precede "Trip" commands for a particular driver.
4. Assume "Driver" command for the same driver name will only appear once in a .txt file.
