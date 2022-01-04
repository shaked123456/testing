#!usr/bin/python3

from datetime import datetime

HOUR = datetime.now().hour
MINUTE = datetime.now().minute

if __name__ == '__main__':
    print("The current hour is: {0} and {1} minutes".format(HOUR, MINUTE))
