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


# default:

chassis.settings(200, 750, 150, 750)
# Setting detectebale colors for back light sensor
Color.BLACK = Color(180, 9, 24)
Color.RED = Color(352, 90, 96)
Color.MAGENTA = Color(340, 84, 87)
Color.YELLOW = Color(90, 29, 100)
Color.BLUE = Color(213, 92, 85)
Color.GREEN = Color(154, 78, 65)
run_colors = (
    Color.MAGENTA,
    Color.BLUE,
    Color.GREEN,
    Color.BLACK,
    Color.RED,
    Color.YELLOW,
    Color.WHITE,
)

def turn_to(angle, then=Stop.HOLD):
    print(hub.imu.heading())
    start_angle = (hub.imu.heading() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)
    if then == Stop.NONE:
        if deg_to_turn >= 180:
            chassis.turn(deg_to_turn - 360)
        else:
            chassis.turn(deg_to_turn)
        return
    if deg_to_turn >= 180:
        chassis.turn(deg_to_turn - 360)
    else:
        chassis.turn(deg_to_turn)


# while "1+1 = 3" == False:  # change to true for testing colors
#     print(back_color.hsv())
# print(hub.battery.voltage())


def straight_time(speed, time):
    timer = StopWatch()
    last = chassis.settings()[0]
    chassis.settings(speed)

    while timer.time() < time:
        if speed > 0:
            chassis.straight(1000, wait=False)
        else:
            chassis.straight(-1000, wait=False)
    chassis.stop()

    chassis.settings(last)


def red():
    ## Add code that make it so if pressed Button.LEFT itll go to the second part of the run please.
    # chassis.settings(600)
    # hub.imu.reset_heading(0)
    # chassis.curve(500, 35, then=Stop.NONE)
    # chassis.straight(200)
    # left_arm.run_time(1000, 1000)
    # chassis.curve(-500, 35, then=Stop.NONE)
    # chassis.straight(-1000)
    chassis.settings(400)
    left_arm.run_time(-1000, 1500, wait=False)
    chassis.straight(200, then=Stop.NONE)
    chassis.curve(200, -35)
    chassis.settings(straight_acceleration=350)
    chassis.straight(350, wait=False)
    wait(1500)
    left_arm.run_time(1000, 2000)
    left_arm.run_time(-1000, 700, wait=False)
    chassis.straight(400)
    chassis.settings(700, 1200)
    chassis.straight(-350, then=Stop.NONE)
    chassis.curve(-300, -50, then=Stop.NONE)
    chassis.straight(-1000)

    # chassis.use_gyro(False)


def black():
    hub.imu.reset_heading(0)
    chassis.settings(400, 630)
    chassis.straight(220, then=Stop.NONE)
    chassis.curve(330, -55, then=Stop.NONE)
    chassis.straight(220)
    turn_to(-140)
    left_arm.run_time(-800, 1200)
    chassis.settings(straight_acceleration=300)
    chassis.straight(340, wait=False)
    wait(2000)
    chassis.settings(straight_acceleration=630)
    left_arm.run_time(350, 3000, wait=False)
    right_arm.run_time(1000, 3000)
    wait(500)
    chassis.straight(-250)
    turn_to(155)
    chassis.settings(1000, straight_acceleration=900)
    chassis.straight(1500)


def green():
    # chassis.settings(300)
    # right_arm.run_time(1000, 5000, wait=False)
    # straight_time(-400, 500)  ### just reseting so itll be straigther
    # hub.imu.reset_heading(0)
    # chassis.settings(300)
    # chassis.straight(50, then=Stop.NONE)
    # chassis.curve(330, 60)
    # turn_to(0)
    # chassis.straight(350, then=Stop.NONE)
    # chassis.curve(390, -31, then=Stop.NONE)
    # chassis.curve(150, 31)
    # turn_to(0)
    # chassis.settings(150)
    # chassis.straight(-100)
    # turn_to(0)
    # till_black(-70, 0)
    # chassis.straight(-165)
    # turn_to(0)
    # chassis.settings(75)
    # chassis.straight(200)
    # chassis.settings(300)
    # chassis.straight(150, then=Stop.NONE)
    # chassis.curve(425, 40)
    # turn_to(160)
    # chassis.straight(195)
    # turn_to(135)
    # right_arm.run_angle(-300, 500, wait=False)
    # wait(0)
    # straight_time(200, 2500)
    # chassis.straight(-40)
    # right_arm.run_time(-330, 3000, wait=False)
    # wait(1000)
    # chassis.settings(140)
    # straight_time(140, 3000)
    # right_arm.run_angle(200, 270, wait=False)
    # wait(500)
    # chassis.settings(200)
    # chassis.straight(-200)
    # chassis.settings(300)
    # turn_to(0)
    # chassis.curve(500, 45)
    # turn_to(0)
    # chassis.settings(200)
    # chassis.straight(-150)
    # chassis.settings(80)
    # chassis.straight(-230)
    # chassis.settings(300, 500)
    # chassis.straight(200, then=Stop.NONE)
    # chassis.settings(500, 750)
    # chassis.curve(200, -45, then=Stop.NONE)
    # chassis.straight(500, then=Stop.NONE)
    hub.imu.reset_heading(0)
    chassis.settings(250)
    chassis.straight(100, then=Stop.NONE)
    chassis.curve(200, 90, then=Stop.NONE)
    # turn_to(90)
    chassis.settings(80)
    chassis.straight(300, then=Stop.NONE)
    chassis.curve(100, 20)
    turn_to(45)
    chassis.settings(200)
    right_arm.run_angle(-640, 300, wait=False)
    wait(0)
    straight_time(200, 2500)
    chassis.straight(-40)
    right_arm.run_time(-720, 2000, wait=False)
    wait(1000)
    chassis.settings(140)
    straight_time(100, 3000)
    right_arm.run_angle(240, 1000, wait=False)
    wait(400)
    chassis.settings(140, 300)
    chassis.straight(-275)
    chassis.settings(turn_rate=80)
    turn_to(90)
    chassis.settings(300, 400)
    chassis.straight(350)
    till_black(80, 0)
    chassis.straight(20)
    chassis.settings(150, 300)
    chassis.straight(-300)
    turn_to(60)
    chassis.settings(700)
    chassis.curve(600, 30, then=Stop.NONE)
    chassis.settings(400)
    chassis.straight(350, then=Stop.NONE)
    chassis.curve(400, 45, then=Stop.NONE)
    chassis.straight(300)
    # till_black(80, 0)
    # chassis.settings(200, 900)
    # chassis.settings(200, 300)
    # chassis.settings(100)
    # chassis.straight(-300)
    # turn_to(60)
    # chassis.settings(300)
    # chassis.curve(600, 30, then=Stop.NONE)
    # turn_to(90)
    # chassis.settings(400)
    # chassis.straight(350, then=Stop.NONE)
    # chassis.curve(400, 45, then=Stop.NONE)
    # chassis.straight(300)


def blue():
    chassis.settings(500, 800, turn_rate=100)
    hub.imu.reset_heading(0)
    right_arm.run_angle(200, -170, wait=False)
    chassis.straight(280)
    chassis.turn(45)
    right_arm.run_angle(200, -150, wait=False)
    chassis.straight(-100)
    chassis.settings(straight_acceleration=350)
    chassis.straight(150)
    chassis.settings(500, 1000)
    right_arm.run_time(1000, 1800)  # boat done
    chassis.straight(-220, then=Stop.NONE)
    chassis.settings(turn_rate=250)
    turn_to(135, then=Stop.NONE)
    right_arm.run_time(-500, 3000, wait=False)
    straight_time(-550, 800)  # imposter dropped
    chassis.settings(1000)
    chassis.straight(150, then=Stop.NONE)
    chassis.curve(200, -45, then=Stop.NONE)
    chassis.straight(500)


def blue_2():
    chassis.settings(450)
    chassis.straight(300, then=Stop.NONE)
    chassis.curve(80, 55, then=Stop.NONE)
    chassis.settings(600)
    chassis.straight(450)
    chassis.settings(450)
    chassis.straight(-400)
    turn_to(45)
    chassis.settings(600)
    chassis.straight(530, wait=False)
    wait(1500)
    left_arm.run_time(-700, 2500)
    chassis.straight(-150)
    turn_to(135)
    straight_time(240, 1000)
    chassis.straight(-100)
    turn_to(-135)
    chassis.settings(900, 900)
    chassis.straight(220, then=Stop.NONE)
    chassis.curve(500, -50, then=Stop.NONE)
    chassis.straight(400)

    # home.


def red_2():
    chassis.straight(200)
    left_arm.run_time(800, 5000, wait=False)
    right_arm.run_time(700, 3000)
    wait(2000)
    left_arm.run_time(800, 2000)
    left_arm.run_time(500, 2000, wait=False)
    chassis.straight(-240)
    chassis.turn(55)
    chassis.straight(200)
    left_arm.run_time(-7000, 2500)


def yellow():
    hub.imu.reset_heading(0)
    chassis.settings(400, 500)
    chassis.straight(100, then=Stop.NONE)
    chassis.curve(300, -30, then=Stop.NONE)
    chassis.straight(265)
    turn_to(-135)
    straight_time(-170, 3500)
    chassis.straight(150)
    turn_to(-90)
    chassis.straight(220, then=Stop.NONE)
    chassis.curve(300, 45)
    turn_to(-45)
    chassis.settings(400, 900)
    straight_time(300, 1000)
    # chassis.settings(30)
    # chassis.straight(-1)
    right_arm.run_time(-2000, 3000)
    wait(170)
    chassis.settings(400, 500)
    chassis.straight(-100)
    turn_to(-90)
    chassis.curve(270, -60)
    turn_to(-90)
    straight_time(400, 1000)
    chassis.straight(-230)
    # chassis.curve(50, 50)
    # chassis.straight(40)
    # turn_to(80)
    # chassis.straight(10)
    # chassis.curve(220, 90)
    # chassis.straight(250)
    # chassis.straight(-2)
    # right_arm.run_time(-1000, 5000)
    # chassis.straight(-10)
    # chassis.curve(-220, -90)
    # chassis.straight(40)

    # chassis.straight(500, then=Stop.NONE)
    # chassis.curve(850, -20)
    # turn_to(-45)
    # straight_time(300, 1500)
    # right_arm.run_time(-1000, 1300)
    # wait(170)
    # chassis.straight(-290)
    # turn_to(-90)
    # chassis.straight(370)
    # chassis.straight(-250)


# print(str((hub.battery.current() / 2000) * 100) + "% Battery")


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
    Color.BLACK: "K",
    Color.BLUE: "B",
    Color.GREEN: "G",
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
    blue_2()
elif selected == "W":
    chassis.settings(150)
    chassis.straight(150)
    chassis.settings(300)
    chassis.straight(-300)
    # left_wheel.dc(100)
    # right_wheel.dc(100)
    # while "1 + 1 = 3":
    #     pass

print(selected)
