import os
from datetime import datetime
import sys

class Service:
    # function that write to log file
    def writeToFile(self, string):
        """"date:18.1.23 name:shlomo function: write all the logs to a file"""
        os.chdir(os.getcwd())
        try:
            self.file = open("logfile.txt", "a")
            string += datetime.now().strftime(" %d/%m/%Y %H:%M:%S\n")
            self.file.write(string)
            self.file.flush()
            self.file.close()
        except Exception as e:
            self.writeToFile("Something went wrong: " + str(e))
            print("Exception: " + str(e))
            sys.exit(1)

    # function that write all the logs of the tests
    def testwriteToFile(self, string):
        """"date:18.1.23 name:shlomo function: write all the test logs to a file"""
        os.chdir(os.getcwd())
        try:
            self.file = open("testlogfile.txt", "a")
            string += datetime.now().strftime(" %d/%m/%Y %H:%M:%S\n")
            self.file.write(string)
            self.file.flush()
            self.file.close()
        except Exception as e:
            self.writeToFile("Something went wrong: " + str(e))
            print("Exception: " + str(e))
            sys.exit(1)