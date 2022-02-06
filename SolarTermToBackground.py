import os
import sys
import ctypes
import random
import datetime
import re

class Main:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        date_now = datetime.datetime.now()
        month = date_now.month
        day = date_now.day
#        month = 2
#        day = 10

        solarterm=[
            [2,4,'BeginningofSpring',0], #0
            [2,19,'RainWater',1], #1
            [3,6,'AwakeningofInsects',2], #2
            [3,21,'SpringEquinox',3], #3
            [4,5,'PureBrightness',4], #4
            [4,20,'GrainRain',5], #5 
            [5,6,'BeginningofSummer',6], #6
            [5,21,'GrainBuds',7], #7
            [6,6,'GrainInEar',8], #8
            [6,21,'SummerSolstice',9], #9
            [7,7,'MinorHeat',10], #10
            [7,23,'MajorHeat',11], #11
            [8,8,'BeginningofAutumn',12], #12
            [8,23,'EndofHeat',13], #13
            [9,8,'WhiteDew',14], #14
            [9,23,'AutumnEquinox',15], #15
            [10,8,'ColdDew',16], #16
            [10,23,'FrostsDescent',17], #17
            [11,7,'BeginningofWinter',18], #18
            [11,22,'MinorSnow',19], #19
            [12,7,'MajorSnow',20], #20
            [12,22,'WinterSolstice',21], #21
            [1,6,'MinorCold',22], #22
            [1,20,'MajorCold',23] #23
        ]

        #find current solar term
        for i,j in enumerate(solarterm):
            if month == solarterm[i][0]:
                if day < solarterm[i][1]:
                    solarterm_now = solarterm[i-1] 
                    break
                elif solarterm[i][1] <= day < solarterm[i+1][1]:
                    solarterm_now = solarterm[i]
                    break
                else:
                    solarterm_now = solarterm[i+1]
                    break
        print(solarterm_now)

        for root, directories, files in os.walk(os.path.join(self.path, 'backgrounds')):
            self.backgrounds = [file.lower() for file in files if int(re.findall(r'\d+', file)[0]) == solarterm_now[3]]
        print(self.backgrounds)
#            self.backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]
#        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'backgrounds', random.choice(self.backgrounds)) , 0)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'backgrounds', self.backgrounds[0]), 0)

application = Main()