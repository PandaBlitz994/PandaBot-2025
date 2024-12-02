from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

# Declaring ports
hub = PrimeHub()
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE) #Red
right_wheel = Motor(Port.E) #Cyan
left_arm = Motor(Port.F) #Yellow
right_arm = Motor(Port.B) #Purple
chassis = DriveBase(left_wheel, right_wheel, 62.4, 81)
front_color = ColorSensor(Port.D) #Green
back_color = ColorSensor(Port.C)  #Blue
chassis.use_gyro(True) 
DriveBase.settings(chassis, 200)

# Setting detectebale colors for back light sensor
Color.BLACK = Color(180,9,24)
Color.RED = Color(352,90,96)
Color.YELLOW = Color(90,29,100)
Color.BLUE = Color(213,92,85)
Color.GREEN = Color(154,78,65)
run_colors = (Color.BLACK, Color.RED, Color.YELLOW, Color.BLUE, Color.GREEN)

###########################

def cycle(iterable):
    iterator = iter(iterable)  
    while True:
        try:
            yield next(iterator)  
        except StopIteration:  
            iterator = iter(iterable)  

back_color.detectable_colors(run_colors)
color_cycle = cycle(run_colors)
color_map = {
    Color.RED: 'R',
    Color.GREEN: 'G',
    Color.BLUE: 'B',
    Color.YELLOW: 'Y',
    Color.BLACK: 'K',
}

while back_color.color() != next(color_cycle):
    pass

menu = [color_map[back_color.color()]]
for i in range(len(run_colors)-1):
    menu.append(color_map[next(color_cycle)])


selected = hub_menu(*menu) # pylint: disable=E1111

if selected == "R":
    import fly_mission
elif selected == "G":
    import drive_mission
elif selected == "B":
    import zigzag
print(selected)


###########################

# def start(n):
#     while not Button.CENTER in hub.buttons.pressed():
#         if n == 1:
#             chassis.straight(100)
#         if n == 2:
#             chassis.straight(100)
#         if n == 3:
#             chassis.straight(100)
#         if n == 4:
#             chassis.straight(100)
#         if n == 5:
#             chassis.straight(100)
#         elif (Button.LEFT in hub.buttons.pressed()):
#             break
#         elif (Button.RIGHT in hub.buttons.pressed()):
#             break
        

# if back_color.color() == Color.RED:
#     hub.display.number(1)
#     start(1)
# elif back_color.color() == Color.BLUE:
#     hub.display.number(2)
#     start(2)
# elif back_color.color() == Color.GREEN:
#     hub.display.number(3)
#     start(3)
# elif back_color.color() == Color.BLACK:
#     hub.display.number(4)
#     start(4)
# elif back_color.color() == Color.YELLOW:
#     hub.display.number(5)
#     start(5)



wait(5000)
if selected