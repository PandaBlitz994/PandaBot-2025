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


def till_black(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while back_color.reflection() > 20:
        print(back_color.color())
        pass

    chassis.stop()


# def turn_to(target, base_speed, kp=0.05, then: Stop = Stop.HOLD):
#     STOP_RANGE = 1
#     base_speed *= 4
#     while not (
#         hub.imu.heading() - STOP_RANGE < target < hub.imu.heading() + STOP_RANGE
#     ):
#         print(hub.imu.heading())
#         error = (target - (hub.imu.heading() % 360)) % 360
#         speed = base_speed + (error * kp)
#         direction = "left" if error > 180 else "right"
#         if direction == "left":
#             left_wheel.dc(-speed)
#             right_wheel.dc(speed)
#         else:
#             left_wheel.dc(speed)
#             right_wheel.dc(-speed)

#     if then == Stop.HOLD:
#         left_wheel.hold()
#         right_wheel.hold()
#     else:
#         chassis.brake()


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


# runs
def blue():
    chassis.settings(turn_rate=100, straight_speed=350)
    hub.imu.reset_heading(0)
    right_arm.run_angle(200, -170, wait=False)
    chassis.straight(310)
    chassis.turn(45)
    right_arm.run_angle(200, -150, wait=False)
    chassis.straight(-100)
    chassis.straight(130)
    right_arm.run_angle(500, 300)  # boat done
    chassis.straight(-235)
    turn_to(135)
    straight_time(-200, 2000)  # imposter dropped
    right_arm.run_angle(200, -150, wait=False)
    chassis.straight(75)
    chassis.curve(120, 90)
    chassis.straight(-60)
    turn_to(180)
    chassis.straight(-575, then=Stop.NONE)  # crils picked up
    right_arm.run_time(-500, 1000, wait=False)
    chassis.curve(300, 45)
    right_arm.run_time(500, 1000, wait=False)
    chassis.straight(-270)  # picked up cril
    chassis.curve(250, 70, then=Stop.NONE)
    chassis.straight(30)
    turn_to(-80)
    right_arm.run_time(-200, 1000, wait=False)
    straight_time(-130, 2500)  # plankton stolen
    chassis.straight(100)
    right_arm.run_angle(500, 300, wait=False)
    turn_to(0)
    chassis.settings(500)
    chassis.straight(-400, then=Stop.NONE)
    chassis.curve(-300, 45, then=Stop.NONE)
    chassis.straight(-500)
    # home. run 1.


def black():
    straight_time(-500, 500)
    chassis.settings(300)
    hub.imu.reset_heading(0)
    right_arm.run_time(-300, 1800, wait=False)
    chassis.curve(500, 30, then=Stop.NONE)
    chassis.straight(275)
    chassis.settings(turn_rate=100)
    turn_to(-85)
    wait(150)
    chassis.settings(straight_speed=100)
    straight_time(150, 1000)
    chassis.settings(straight_speed=250)
    # Picks up the guy
    right_arm.run_time(300, 1000)
    chassis.straight(-80)
    turn_to(-55)
    # Zorek the guy because we dont do the thing you have to put it in his place
    # right_arm.run_time(300, 3000, wait=False)
    # Dolphin
    chassis.settings(straight_speed=300)
    chassis.straight(260)
    chassis.settings(straight_speed=250)
    right_arm.run_angle(-100, 110, wait=False)
    chassis.straight(-145)
    # PUT THE GUY WHERE HE BELONGS!
    turn_to(-90)
    chassis.settings(turn_rate=25, straight_speed=320, straight_acceleration=400)
    chassis.straight(-1350)
    chassis.settings(straight_acceleration=750)
    turn_to(-135)
    straight_time(-200, 2500)
    chassis.settings(500, turn_rate=400)
    chassis.curve(200, -20, then=Stop.NONE)
    chassis.straight(250, then=Stop.NONE)
    chassis.curve(400, -45, then=Stop.NONE)
    chassis.straight(1000)
    chassis.settings(100, turn_rate=100)


def red():
    ## Add code that make it so if pressed Button.LEFT itll go to the second part of the run please.
    chassis.settings(600)
    hub.imu.reset_heading(0)
    chassis.curve(500, 35, then=Stop.NONE)
    chassis.straight(200)
    left_arm.run_time(1000, 2000)
    chassis.curve(-500, 15, then=Stop.NONE)
    chassis.straight(-1000)
    # chassis.use_gyro(False)


def red_2():
    chassis.settings(350)
    chassis.straight(520)
    left_arm.run_time(-1000, 1200)
    # left_arm.run_angle(300, 150)
    chassis.settings(550)
    chassis.straight(-1000, then=Stop.NONE)


def yellow():
    straight_time(-500, 500)
    chassis.settings(350)
    chassis.straight(30, then=Stop.NONE)
    chassis.curve(300, -45, then=Stop.NONE)
    chassis.straight(500, then=Stop.NONE)
    chassis.curve(850, -20)
    turn_to(-45)
    straight_time(300, 1500)
    right_arm.run_time(-1000, 2500)
    chassis.straight(-320)
    turn_to(-90)
    chassis.straight(400)
    chassis.straight(-250)


def green():
    chassis.settings(300)
    right_arm.run_time(1000, 5000, wait=False)
    hub.imu.reset_heading(0)
    straight_time(-400, 500)  ### just reseting so itll be straigther
    hub.imu.reset_heading(0)
    chassis.settings(300)
    chassis.straight(50, then=Stop.NONE)
    chassis.curve(320, 60)
    turn_to(0)
    chassis.straight(350, then=Stop.NONE)
    chassis.curve(390, -31, then=Stop.NONE)
    chassis.curve(150, 31)
    turn_to(0)
    chassis.settings(150)
    chassis.straight(-100)
    turn_to(0)
    till_black(-70, 0)
    chassis.straight(-165)
    chassis.settings(75)
    chassis.straight(200)
    chassis.settings(300)
    chassis.straight(150, then=Stop.NONE)
    chassis.curve(425, 40)
    turn_to(160)
    chassis.straight(195)
    turn_to(135)
    right_arm.run_angle(-300, 500, wait=False)
    wait(0)
    straight_time(200, 2500)
    chassis.straight(-40)
    right_arm.run_time(-330, 3000, wait=False)
    wait(1000)
    chassis.settings(140)
    chassis.straight(200)
    right_arm.run_angle(200, 270, wait=False)
    wait(500)
    chassis.settings(200)
    chassis.straight(-200)
    chassis.settings(300)
    turn_to(0)
    chassis.curve(440, 45)
    turn_to(0)
    chassis.settings(80)
    chassis.straight(-320)
    chassis.straight(200, then=Stop.NONE)
    chassis.settings(500)
    chassis.curve(200, -45, then=Stop.NONE)
    chassis.straight(500, then=Stop.NONE)


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
