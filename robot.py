from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

# Declaring ports
hub = PrimeHub()
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)  # Red
right_wheel = Motor(Port.E)  # Cyan
left_arm = Motor(Port.F)  # Yellow
right_arm = Motor(Port.B)  # Purple
chassis = DriveBase(left_wheel, right_wheel, 62.4, 81)
front_color = ColorSensor(Port.D)  # Green
back_color = ColorSensor(Port.C)  # Blue
chassis.use_gyro(True)
DriveBase.settings(chassis, 200)

# Setting detectebale colors for back light sensor
Color.BLACK = Color(180, 9, 24)
Color.RED = Color(352, 90, 96)
Color.MAGENTA = Color(340, 84, 87)
Color.YELLOW = Color(90, 29, 100)
Color.BLUE = Color(213, 92, 85)
Color.GREEN = Color(154, 78, 65)
run_colors = (
    Color.RED,
    Color.BLUE,
    Color.GREEN,
    Color.BLACK,
    Color.YELLOW,
    Color.MAGENTA,
    Color.WHITE,
)
# chassis.straight(200)
# right_arm.run_time(1000, 1750)
# right_arm.run_time(-1000, 1750)
# chassis.straight(-200)


def PID_straight(target_distance, target_percentage, kp=0.0):
    while chassis.distance() < target_distance:
        error = hub.imu.heading()

        correction = kp * error * -1

        powerA = target_percentage + correction
        powerB = target_percentage - correction

        right_wheel.dc(powerA)
        left_wheel.dc(powerB)
        print(
            "error "
            + str(error)
            + "; correction "
            + str(correction)
            + "; powerA "
            + str(powerA)
            + "; powerB "
            + str(powerB)
        )
        wait(10)
    chassis.stop()


def turn_to(angle):
    print(hub.imu.heading())
    start_angle = (hub.imu.heading() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)

    if deg_to_turn >= 180:
        chassis.turn(deg_to_turn - 360)
    else:
        chassis.turn(deg_to_turn)


# while "1+1 = 3" == False:  # change to true for testing colors
#     print(back_color.hsv())
# print(hub.battery.voltage())



# runs
def blue():
    hub.imu.reset_heading(0)
    right_arm.run_angle(200,-100, wait=False)
    chassis.straight(295)
    chassis.turn(45)
    right_arm.run_angle(200,-200, wait=False)
    chassis.straight(-100)
    chassis.straight(130)
    right_arm.run_angle(500,300)  # boat done
    chassis.straight(-225)
    right_arm.run_angle(450, -125, wait=False)
    chassis.curve(200, 70)
    chassis.straight(-250) #cril
    chassis.turn(65) 
    chassis.straight(-280) #cril
    chassis.curve(100,50)
    # chassis.turn(86)
    chassis.straight(-200)#plankton
    # right_arm.run_angle(200,-100, wait=False)
    # chassis.straight(100)
    # chassis.turn(30)
    chassis.curve(125,42)
    # wait(10000)
    chassis.straight(-100)
    chassis.straight(150)
    # chassis.curve(100, 90, then=Stop.NONE)
    # turn_to(-135)
    turn_to(0)
    chassis.straight(-300, then=Stop.NONE)
    chassis.curve(-300, 45, then=Stop.NONE)
    chassis.straight(-500)
    

def black():
    hub.imu.reset_heading(0)
    right_arm.run_time(-300, 1800, wait=False)
    chassis.curve(500, 30, then=Stop.NONE)
    chassis.straight(260)
    chassis.settings(turn_rate=100)
    turn_to(-85)
    wait(300)
    chassis.settings(straight_speed=100)
    chassis.straight(125)
    chassis.settings(straight_speed=200)
    # Picks up the guy
    right_arm.run_time(300, 1000)
    chassis.straight(-100)
    turn_to(-45)
    # Dolphin
    chassis.settings(straight_speed=310)
    chassis.straight(280)
    chassis.settings(straight_speed=200)
    right_arm.run_angle(-100, 110, wait=False)
    chassis.straight(-180)
    # PUT THE GUY WHERE HE BELONGS!
    turn_to(21)
    chassis.straight(110)
    chassis.straight(-30)
    chassis.turn(-10)
    right_arm.run_time(200, 500)
    chassis.straight(30)
    right_arm.run_time(-300, 1500)
    chassis.straight(-80)
    turn_to(-90)
    turn_to(-90)
    chassis.straight(-710, then=Stop.NONE)
    chassis.curve(-900, -15, then=Stop.NONE)
    chassis.straight(-200)
    turn_to(-87)
    wait(200)
    chassis.straight(-120)
    turn_to(-135)
    chassis.straight(-270)
    chassis.straight(105)
    chassis.curve(200, -45, then=Stop.NONE)
    chassis.straight(250, then=Stop.NONE)
    right_arm.run_time(300, 3000, wait=False)
    chassis.curve(200, -45, then=Stop.NONE)
    chassis.straight(500)


def red():
    ## Add code that make it so if pressed Button.LEFT itll go to the second part of the run please.
    chassis.settings(400)
    hub.imu.reset_heading(0)
    chassis.curve(500, 35, then=Stop.NONE)
    chassis.straight(150)
    left_arm.run_time(1000, 2000)
    chassis.straight(-700)
    chassis.use_gyro(False)


def red_2():
    # hub.imu.reset_heading(0)
    # chassis.settings(300)
    # chassis.straight(1100)
    # chassis.straight(-200)
    # chassis.curve(-75, 90, then=Stop.NONE)
    # chassis.straight(200)
    # turn_to(-90)
    # chassis.curve(-220, 90)
    # chassis.straight(-220)
    # chassis.straight(50, then=Stop.NONE)
    # chassis.settings(400)
    # chassis.curve(170, 180)
    # turn_to(0)
    # chassis.straight(300, then=Stop.NONE)
    # chassis.curve(500, 50, then=Stop.NONE)
    # chassis.straight(400)
    chassis.settings(1000)
    chassis.straight(1000, then=Stop.NONE)
    chassis.curve(1000, 45)


def yellow():
    chassis.settings(50)
    chassis.straight(120)
    chassis.settings(200)
    chassis.straight(-200)


def green():
    chassis.settings(250)
    chassis.straight(50, then=Stop.NONE)
    chassis.curve(300, 60)
    turn_to(0)
    chassis.straight(350, then=Stop.NONE)
    chassis.curve(410, -30)
    chassis.curve(150, 30)
    chassis.settings(200)
    chassis.straight(-450)
    chassis.settings(100)
    chassis.straight(250)
    chassis.straight(-25)
    chassis.straight(230)
    chassis.settings(200)
    turn_to(0)
    chassis.curve(300, 40)
    turn_to(150)
    chassis.straight(120)
    turn_to(135)
    right_arm.run_angle(1000, 350, wait=False)
    chassis.straight(350)
    chassis.straight(-70)
    right_arm.run_time(300, 3000, wait=False)
    wait(700)
    chassis.straight(80)
    right_arm.run_angle(-300, 700, wait=False)
    wait(800)
    chassis.settings(500)
    chassis.straight(-100)
    turn_to(0)
    chassis.straight(200, then=Stop.NONE)
    chassis.curve(700, -50)


    # chassis.curve(200, 180)
    # chassis.settings(50)
    # chassis.straight(-70)
    # chassis.straight(200)
    # chassis.curve(600, -45)
    




print(str((hub.battery.current() / 2000) * 100) + "% Battery")


# Run selection
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
    Color.RED: "R",
    Color.BLUE: "B",
    Color.GREEN: "G",
    Color.BLACK: "K",
    Color.YELLOW: "Y",
    Color.MAGENTA: "M",
    Color.WHITE: "W",
}

while back_color.color() != next(color_cycle):
    pass

menu = [color_map[back_color.color()]]
for i in range(len(run_colors) - 1):
    menu.append(color_map[next(color_cycle)])


selected = hub_menu(*menu)  # pylint: disable=E1111

if selected == "R":
    red()
elif selected == "B":
    blue()
elif selected == "G":
    green()
elif selected == "K":
    black()
elif selected == "Y":
    yellow()
elif selected == "M":
    red_2()
elif selected == "W":
    left_wheel.dc(100)
    right_wheel.dc(100)
    while "1 + 1 = 3":
        pass

print(selected)
