# root-2021

Programming Language: Python 3.9

## Environment Setup

0. Install Python 3 if you have not done so.
1. Inside the project folder, create a virtual environment
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

You can exit the virtual environment later with _deactivate_

## Run the App

You can configure what input file(s) to process by modifying line 6 in main.py. <br/>
All input files are expected to be in the same directory as main.py.<br/>
<br/>Execute main.py:

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
  The former is my current forte. However, Python seems to be the right tool for the task. If this was a real-world project at Root, I would approach it with Python. Hopefully, this also demonstrated that I can adapt and learn on the go.
  This becomes especially apparent when it comes to testing with Pytest which is considerably different from Jest/Enzyme/Jasmine/Sinon in terms of syntax and approaches but the general testing concept did transfer well.

- How should the program accept file names from my users?<br/>
  I could receive a list of file names from the command line, stdin, or have my program prompts for the file names, or even requiring users to open up main.py and write the file names into the code. <br/>I might be overthinking but I believe it would be of tremendous help for my users if they can provide multiple file names to be processed in a single run! That's why I decided to create a global variable at the top of main.py which is an array of file names.<br/>
  Although now, after a couple of days, I think the best user interface would be to accept file names from the command line with wildcard-character functionalities but what I have done (using an array of file names) is already a step up from the requirement. Plus, the tests have already been written. So I will keep this old implementation for evaluation. Hopefully, this decision wouldn't affect much on the evaluation.

- Arranging the solutions into modular classes and functions makes the code more organized and easier to be tested. That is why I have isolated the solution logic mainly into two big classes: ProcessDrives (the solution class) and Driver.
  Inside ProcessDrives, I have also factored out some helper functions, again, for readability and testing purposes.
  And in main.py, I simply instantiate and execute on the solution class.

- Should I check for mph <5 and >100 outside or inside of Driver class?
  I decided to do the check inside Driver class itself because this is a piece of logic concerning how we handle the Trip command (add_trip() in the Driver class) which should be abstracted out to the class consumer. And later, if we want to change the two boundary numbers, we can easily change them inside the Driver class without affecting the consumer of the class.

- Use a virtual environment or not?<br/>
  Since it is generally a good practice to run and set up a Python program in a virtual environment. I decided to follow so and included a guide to help users to do the same.

- Initially, there were more methods in Driver class, they were mainly getter methods that expose class attributes. However, since my solution doesn't utilize them, I have decided to remove these interfaces to avoid confusion.

- I am only rounding up the miles and hours at the point of presentation. In the "Driver" class itself, the attributes are stored as a float data type to preserve accuracy.

- In Driver class, should I keep track of the time traveled by a driver in hours or minutes unit?<br/>
  Since the Driver class will have to calculate mph, I have decided to go with the hours unit.

## How I Tested the App

Using both automated testing and mock input files.

## Assumptions

1. Assume users may want to process multiple files at a time.
2. Assume there can be empty line(s) between valid commands in an input file.
3. Assume no two drivers have the same name.
4. Assume the two commands will always appear with correct formats and values.
5. Assume the "Driver" command will precede "Trip" commands for a particular driver.
6. Assume the "Driver" command for the same driver name will only appear once in a .txt file.
