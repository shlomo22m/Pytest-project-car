import unittest
import pytest
import Vehicle
import service
from dotenv import load_dotenv
from Vehicle import vehicle
import os


class MyTestCase(unittest.TestCase):
    load_dotenv()
    car=Vehicle.vehicle()
    log=service.Service()
    exception_pass = os.getenv('EXCEPTION_PASS')
    exception_fail = os.getenv('EXCEPTION_FAIL')
    test_pass = os.getenv('TEST_PASS')
    test_fail = os.getenv('TEST_FAIL')


    def setUp(self):
      self.car

    def test_monney_to_fill(self):
        """shlono 23.1.22 test of feul fill in car"""
        self.car.monney_to_fill(20)
        self.car.money = 501
        try:
            assert self.car.money > 10 and self.car.money <= 500
            self.log.testwriteToFile(f'{self.test_pass}')
        except:
                self.log.testwriteToFile(f'{self.car.money} need to be between 10 to 500')
                self.car.feul = 71
        try:
                assert self.car.feul <= 70
                self.log.testwriteToFile(f'feul level {self.test_pass}')
        except:
                self.log.testwriteToFile(f'feul level at max {self.test_fail}')

        car = vehicle()
        try:
            with pytest.raises(Exception):
                car.monney_to_fill(70)
            self.log.testwriteToFile(self.exception_pass)
        except:
            self.log.testwriteToFile(self.exception_fail)

    def test_car_stop(self):
        """"shlomo mhadker 23.1.23 test that check when the car stops gear back to 0"""
        self.car.car_stop()
        try:
                 assert self.car.gear == 0
                 self.log.testwriteToFile(f'car stop and gear at 0 {self.test_pass}')
        except:
                 self.log.testwriteToFile(f'car stop and gear at 0 {self.test_fail}')

    def test_gear(self):
        try:
            self.car.gear_shift(121)
            self.log.testwriteToFile(f'gear {self.test_pass}')

        except:
            self.log.testwriteToFile(f'gear {self.test_fail}')
        try:
            with pytest.raises(IndexError):
                self.car.gear_shift(121)
            self.log.testwriteToFile(f'IndexError of gear {self.test_pass}')
        except:
            self.log.testwriteToFile(f'IndexError of gear {self.test_fail}')



    def test_car_start(self):
        self.car.car_start()
        try:
            assert self.car.gear == 0
            self.log.testwriteToFile(f'car gear at 0 {self.test_pass}')
        except:
            self.log.testwriteToFile(f'car gear not 0 {self.test_fail}')



    def test_gear_shift(self):
        try:
            self.car.gear_shift(122)
            self.log.testwriteToFile(f'gear {self.test_pass}')

        except:
            self.log.testwriteToFile(f'gear {self.test_fail}')
        try:
            with pytest.raises(IndexError):
                self.car.gear_shift(121)
            self.log.testwriteToFile(f'IndexError of gear {self.test_pass}')
        except:
            self.log.testwriteToFile('IndexError of gear fail')

    def test_km_to_drive(self):
        """shlono 23.1.22 test of km to drive"""
        self.car.feul = 30
        try:
            self.car.km_to_drive(500)
            self.log.testwriteToFile(f'km to drive {self.test_pass}')
        except:
            self.log.testwriteToFile(f'km to drive {self.test_fail}')

        try:
            with pytest.raises(Exception):
                self.car.km_to_drive(500)
            self.log.testwriteToFile(self.exception_pass)
        except:
            print(self.exception_fail)


    def test_write_to_file(self):
        try:
            self.log.writeToFile(f'write to log file {self.test_pass} ')
        except:
            self.log.writeToFile(f'write to log file {self.test_fail}')



    def test_write_to_lggtest(self):
        try:
            self.log.testwriteToFile(f'write to log test file {self.test_pass}')
        except:
            self.log.testwriteToFile('fail to write')

if __name__ == '__main__':
    unittest.main()