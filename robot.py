from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu


hub = PrimeHub()
left_wheel = Motor(Port.F, Direction.COUNTERCLOCKWISE) #Red
right_wheel = Motor(Port.B) #Cyan
left_arm = Motor(Port.D) #Yellow
right_arm = Motor(Port.A) #Purple
chassis = DriveBase(left_wheel, right_wheel, 62.4, 81) #black
front_color = ColorSensor(Port.C) #Green
back_color = ColorSensor(Port.E)  #Blue
chassis.use_gyro(True) 
DriveBase.settings(chassis, 200)

black = Color(180,9,24)
red = Color(352,90,96)
yellow = Color(90,29,100)
blue = Color(213,92,85)
green = Color(154,78,65)

back_color.detectable_colors(
    [
        black, red, yellow, blue, green
    ]
)

# print(back_color.color(True))
chassis.straight(1000)
# print(front_color.hsv())
# left_arm.run_time(300,5000)
# for port in [Port.A, Port.B... ]:
#     try: 
#         m = Motor(port)
#         m.run()
#         break
#     except OSError:
#         print("incorrect port")
