import sys
from ProcessDrives import ProcessDrives

# configure your input files here
INPUT_FILES = ["input1.txt", "unknown.txt", "input2.txt"]


def main():
    pd = ProcessDrives(INPUT_FILES)
    pd.execute()


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
