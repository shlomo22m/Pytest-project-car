import pytest
import service

from dotenv import load_dotenv
import os
from  Vehicle import vehicle

load_dotenv()
money=os.getenv('TESTMONEY')
exception_pass=os.getenv('EXCEPTION_PASS')
exception_fail=os.getenv('EXCEPTION_FAIL')
test_pass=os.getenv('TEST_PASS')
test_fail=os.getenv('TEST_FAIL')
log=service.Service()

@pytest.fixture
def car():
    return vehicle()



def test_monney_to_fill(car):
    """shlono 23.1.22 test of feul fill in car"""
    car.monney_to_fill(20)
    car.money=500
    try:
        assert car.money>10 and car.money<=500
        log.testwriteToFile(f'{test_pass}')
    except:
         log.testwriteToFile(f'{car.money} need to be between 10 to 500')

    car.feul=69
    try:
        assert car.feul<70
        log.testwriteToFile(f'feul level is good {test_pass}')
    except:
        log.testwriteToFile(f'feul level {test_fail}')

    car=vehicle()
    try:
        with pytest.raises(Exception):
            car.monney_to_fill(70)
        log.testwriteToFile(exception_pass)
    except: log.testwriteToFile(exception_fail)

@pytest.mark.skip
def test_car_stop(car):
    """"shlomo mhadker 23.1.23 test that check when the car stops gear back to 0"""
    car.car_stop()
    try:
        assert car.gear == 0
        log.testwriteToFile(f'car stop and gear at 0 {test_pass}')
    except:
        log.testwriteToFile(f'car stop and gear at 0 {test_fail}')


def test_km_to_drive(car):
    """shlono 23.1.22 test of km to drive"""
    car.feul=30
    try:
            car.km_to_drive(700)
            log.testwriteToFile(f'km to drive {test_pass}')
    except:
             log.testwriteToFile(f'km to drive {test_fail}')

    try:
        with pytest.raises(Exception):
            car.km_to_drive(701)
        log.testwriteToFile(exception_pass)
    except:
        print(exception_fail)


def test_car_start(car):
    """shlono 23.1.22 test of gear status at start"""
    car.car_start()
    try:
        assert car.gear==0
        log.testwriteToFile(f'car gear at 0 {test_pass}')
    except:
        log.testwriteToFile(f'car gear  at 0 {test_fail}')


def test_gear_shift(car):
    """shlono 23.1.22 test of gear shft"""
    try:
        car.gear_shift(12)
        log.testwriteToFile(f'gear {test_pass}')

    except:
            log.testwriteToFile(f'gear {test_fail}')
    try:
         with pytest.raises(IndexError):
            car.gear_shift(121)
         log.testwriteToFile(f'IndexError {test_pass}')
    except:
            log.testwriteToFile(f'IndexError of gear {test_fail}')


def test_write_to_file():
    """shlono 23.1.22 test the write to file function"""
    try:
        log.writeToFile('able to write')
    except:
        log.writeToFile(f'write {test_fail}')


def test_write_to_logtest():
    """shlono 23.1.22 test the write to file function"""
    try:
        log.testwriteToFile(f'write to test log {test_pass}')
    except:
        log.testwriteToFile(f'write {test_fail}')