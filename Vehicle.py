import service
from dotenv import load_dotenv
import os
class vehicle:
    load_dotenv()
    log=service.Service()
    #gear=os.getenv('GEAR')
    #feul = int(os.getenv('FEUL'))
    #money=int(os.getenv('MONEY'))
    #feulcapcity=int(os.getenv('FEULCAPCITY'))
    #car_max_speed=int(os.getenv('CAR_MAX_SPEED'))
    new_feul_level=os.getenv('NEW_FEUL_LEVEL')
    new_money_amount = os.getenv('NEW_MONEY_AMOUNT')
    gear_moved_to=os.getenv('GEAR_MOVED_TO')
    shift_7=os.getenv('SHIFT_7')
    max_gear=int(os.getenv('MAX_GEAR'))
    not_enough_feul_for_drive=os.getenv('NOT_ENOUGH_FEUL')
    car_gears=os.getenv('CAR_GEARS')

    def __init__(self):
        self.car_mode=os.getenv('CAR_MODE')
        self.gear = os.getenv('GEAR')
        self.feul = int(os.getenv('FEUL'))
        self.money = int(os.getenv('MONEY'))
        self.feulcapcity = int(os.getenv('FEULCAPCITY'))
        self.car_max_speed = int(os.getenv('CAR_MAX_SPEED'))


    def km_to_drive(self,km):
        """name:shlomo
        date:23.1.23
        describtion:function that tell how much km to drive ,km"""
        self.log.writeToFile('car in drive')
        if self.feul*10 <km:
            self.monney_to_fill(20)
        if self.feul * 10 < km:
            self.log.writeToFile(f'{self.not_enough_feul_for_drive}')
            raise Exception('not enough feul')

        else:
            self.feul=self.feul-(km/10) #substract the feul level
            self.log.writeToFile(f'new feul level after drive {self.feul}')


    def fuelco(self,km):
        remainfuel=0


    def gear_shift(self,speed):
       """shlomo 23.1.23 function that gets the wanted speed and move the shift to its position"""
       gear_change=self.car_gears # set the gear number
       if speed>self.car_max_speed: #check if the speed is not over the car speed
           self.log.writeToFile(f'{self.shift_7}')
           raise IndexError('you in max speed')
       if speed==self.car_max_speed: #check if the speed is at the car speed
           self.gear=self.max_gear
           self.log.writeToFile(f'{self.gear_moved_to} {self.gear}')
           return
       self.gear=gear_change[int(speed/20+1)]#change the car gear
       self.log.writeToFile(f'{self.gear_moved_to} {self.gear}')



    def car_start(self):
        """shlono 23.1.23 function when runing set the gear to 0"""
        self.log.writeToFile('engine start')
        self.gear=0 #set the gear at 0

    def car_stop(self):
        """shlono 23.1.23 function when runing set the gear to 0"""
        self.log.writeToFile('engine stop')
        self.gear = 0 #set the gear at 0



    def monney_to_fill(self,feul):
        """shlomo 23.1.23 function that get the amount of feul we want to fill"""
        self.log.writeToFile('fuling car')
        if self.money>(feul*10) and self.feul+feul<=self.feulcapcity: #check if we have enough money and feul level under 70
                self.money=self.money-(feul*10) #substract the money amount
                self.feul=self.feul+feul #add the feul
                self.log.writeToFile(f'{self.new_feul_level} {self.feul}')
                self.log.writeToFile(f'{self.new_money_amount} {self.money}')
                return
        else:
            self.log.writeToFile('not enogh money filling nax liter fo amount')
            while self.money>10 and self.feul<=self.feulcapcity: #fill the feul until not enough money
                raise Exception('fail to write to log file')
                self.feul=self.feul+1
                self.money=self.money-10
            self.log.writeToFile(f'{self.new_feul_level} {self.feul}')
            self.log.writeToFile(f'{self.new_money_amount} {self.money}')

