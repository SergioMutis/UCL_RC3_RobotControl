"""DIFFUSIVE HABITATS FUNCTION LIBRARY
# Developed for the Diffusive Habitats (DH) Project, UCL Bartlett School of Architecture RC3 by Sergio Mutis.
# More info at https://bpro2022.bartlettarchucl.com/rc3-living-architecture-lab-22/diffusive-habitats
# Employs the Dynamixel (DXL) framework (as the robots are actuated by AX-12A Dynamixel servos).
# This script storages DH-specific movement functions and sequences developed experimentally"""

# Importing Code from External Libraries
from dxl_ax12a import AX12a
import time

# Connecting to Default COM Port (the USB port connected to the robots)
DEVICENAME = 'com3'  # Should be default COM port

# Initializing Motors
motor_controller = AX12a(DEVICENAME)

# Setting a Time Delay
time_delay = 2


# BASELINE FUNCTIONS
def write_pos():
    motor_controller.enable_torque()
    value = int(input("Input a target position (0-1023) : "))
    motor_controller.set_position(value)


def wheel_mode():
    motor_controller.enable_torque()
    value = int(input("Input [0] False, [1] True : "))
    motor_controller.set_wheel_mode(value)


def write_speed():
    motor_controller.enable_torque()
    value = int(input("Input a target speed (CCW > 0-1024,CW > 1024-2047) : "))
    motor_controller.set_moving_speed(value)


def read_position():
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_wheel_mode(1)
    import time

    time.sleep(0.75)  # Delays for .75 seconds.
    for i in range(10):
        motor_controller.get_position()
        time.sleep(0.75)  # Delays for .75 seconds.


def read_load():
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_wheel_mode(1)
    import time

    time.sleep(0.75)  # Delays for .75 seconds.
    for i in range(10):
        motor_controller.get_load()
        time.sleep(0.75)  # Delays for .75 seconds.


def rotation_loop():
    # disable wheel mode for all motors
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.set_wheel_mode(0)
    # enable torque for all motors
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.enable_torque()
    # set all motor speeds at 512
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.set_moving_speed(75)
    # set all motor positions at 75
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.set_position(512)

    import time

    time.sleep(2)
    motor_controller.set_id(1)
    motor_controller.set_position(800)

    time.sleep(2)
    motor_controller.set_id(3)
    motor_controller.set_position(225)

    motor_controller.set_id(4)

    time.sleep(1)
    is_running = True
    change = 50
    while is_running:
        position = motor_controller.get_position()
        if position > 800:
            change = -50
        if position < 225:
            change = 50
        print(change)
        motor_controller.set_position(position + change)
        time.sleep(0.5)


# MOVEMENT SEQUENCE FUNCTIONS
# function nomenclature often uses:
# 'r#' to indicate the robot #
# 'm#' to indicate the motor # attached to a surface (m1,m5,m9,m13 are yellow & m4,m8,m12,m16 are green)
# 'x/y _ plus/minus_ #' indicates how the sequence modifies the XY coordinates of the robot in a plane
# 'hanging' functions were optimized for hanging scenarios
# READY MODES
def robot1_ready_mode():
    # wheel-mode off for all motors
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.set_wheel_mode(0)
    # enable torque for all motors
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.enable_torque()
    # set all motor speeds at 75
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.set_moving_speed(75)
    # set all motor positions at 512
    for x in range(1, 5):
        motor_controller.set_id(x)
        motor_controller.set_position(512)


def robot2_ready_mode():
    # wheel-mode off for all motors
    for x in range(5, 9):
        motor_controller.set_id(x)
        motor_controller.set_wheel_mode(0)
    # enable torque for all motors
    for x in range(5, 9):
        motor_controller.set_id(x)
        motor_controller.enable_torque()
    # set all motor speeds at 75
    for x in range(5, 9):
        motor_controller.set_id(x)
        motor_controller.set_moving_speed(75)
    # set all motor positions at 512
    for x in range(5, 9):
        motor_controller.set_id(x)
        motor_controller.set_position(512)


def robot3_ready_mode():
    # wheel-mode off for all motors
    for x in range(9, 13):
        motor_controller.set_id(x)
        motor_controller.set_wheel_mode(0)
    # enable torque for all motors
    for x in range(9, 13):
        motor_controller.set_id(x)
        motor_controller.enable_torque()
    # set all motor speeds at 75
    for x in range(9, 13):
        motor_controller.set_id(x)
        motor_controller.set_moving_speed(75)
    # set all motor positions at 512
    for x in range(9, 13):
        motor_controller.set_id(x)
        motor_controller.set_position(512)


# R1 MOVEMENT
def r1m1_y_plus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)


def r1m1_hanging_y_plus_1():
    robot1_ready_mode()
    time.sleep(2)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(210)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(190)
    time.sleep(2)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)
    time.sleep(2)


def r1m1_y_minus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)


def r1m1_hanging_y_minus_1():
    robot1_ready_mode()
    time.sleep(2)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(832)
    time.sleep(2)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)
    time.sleep(2)


def r1m1_x_plus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(205)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)


def r1m1_hanging_x_plus_1():
    robot1_ready_mode()
    time.sleep(2)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(204)
    time.sleep(2)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(204)
    time.sleep(2)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(190)
    time.sleep(2)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)
    time.sleep(2)


def r1m1_x_minus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(820)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)


def r1m1_hanging_x_minus_1():
    robot1_ready_mode()
    time.sleep(2)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(820)
    time.sleep(2)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(190)
    time.sleep(2)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)
    time.sleep(2)


def r1m4_y_plus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)


def r1m4_hanging_y_plus_1():
    robot1_ready_mode()
    time.sleep(time_delay)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(832)
    time.sleep(time_delay)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)
    time.sleep(time_delay)


def r1m4_y_minus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(197)

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)


def r1m4_hanging_y_minus_1():
    robot1_ready_mode()
    time.sleep(time_delay)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(204)
    time.sleep(time_delay)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(190)
    time.sleep(time_delay)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)
    time.sleep(time_delay)


def r1m4_x_plus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)


def r1m4_hanging_x_plus_1():
    robot1_ready_mode()
    time.sleep(2)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(204)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(204)
    time.sleep(2)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(820)
    time.sleep(2)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)
    time.sleep(2)


def r1m4_x_minus_1():
    robot1_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)


def r1m4_hanging_x_minus_1():
    robot1_ready_mode()
    time.sleep(2)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(204)
    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(204)
    time.sleep(2)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(190)
    time.sleep(2)

    motor_controller.set_id(4)  # green
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(2)  # blue
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(3)  # red
    motor_controller.set_position(512)
    time.sleep(1)

    motor_controller.set_id(1)  # yellow
    motor_controller.set_position(512)
    time.sleep(time_delay)


# R2 MOVEMENT
def r2m5_y_plus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)


def r2m5_y_minus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)


def r2m5_x_plus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(205)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)


def r2m5_x_minus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(820)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)


def r2m8_y_plus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)


def r2m8_y_minus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)


def r2m8_x_plus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)


def r2m8_x_minus_1():
    robot2_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)


# R3 MOVEMENT
def r3m9_y_minus_1():
    robot3_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(512)


def r3m12_x_minus_1():
    robot3_ready_mode()

    time.sleep(time_delay)
    motor_controller.set_id(12)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(12)  # green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(512)


# R4 MOVEMENT
def r4m13_y_minus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(2)

    time.sleep(time_delay)
    motor_controller.set_id(15)  # red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(14)  # blue
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(512)


def r4m16_x_minus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(2)

    time.sleep(time_delay)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(205)

    time.sleep(time_delay)
    motor_controller.set_id(14)  # blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(15)  # red
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(512)


def r4m13_x_minus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(2)

    time.sleep(time_delay)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(820)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(820)

    time.sleep(time_delay)
    motor_controller.set_id(15)  # red
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(14)  # blue
    motor_controller.set_position(210)

    time.sleep(time_delay)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(512)


def r4m16_y_minus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(197)
    time.sleep(2)

    motor_controller.set_id(16)  # green
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(512)


def r4m16_y_plus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(815)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(815)
    time.sleep(2)

    motor_controller.set_id(16)  # green
    motor_controller.set_position(815)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(512)
    time.sleep(2)


def r4m13_x_plus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(205)
    motor_controller.set_id(16)  # green
    motor_controller.set_position(205)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(16)  # green
    motor_controller.set_position(512)
    time.sleep(2)


def r4m13_y_plus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(210)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(512)
    time.sleep(2)


def r4m16_x_plus_1():
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(16)  # green
    motor_controller.set_position(815)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(815)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(205)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(205)
    time.sleep(2)

    motor_controller.set_id(16)  # green
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(14)  # blue
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(15)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(13)  # yellow
    motor_controller.set_position(512)
    time.sleep(2)


# UTILITY METHODS
# Rotating an array
def rotate(basegrid):
    n = len(basegrid)
    m = len(basegrid[0])
    return [[basegrid[j][m-1-i] for j in range(n)] for i in range(m)]


# OPEN NAVIGATION METHOD
# Iteration 1 (Just BOB)
def open_navigation_robot1():
    # 0 Title
    print("\nDIFFUSIVE HABITATS: OPEN NAVIGATION it.2")
    print("This iteration allows to move 1 robot around a base grid\n")

    # 1 Grid
    print("#1 Grid Initialization")
    prompt = "How many columns does the base grid have (x)? "
    basegrid_x = int(input(prompt))

    prompt = "How many does the base grid have (y)? "
    basegrid_y = int(input(prompt))

    basegrid = [[0 for i in range(basegrid_y)] for j in range(basegrid_x)]

    print("\nThe current state of the playground is:")
    print("(0 represents and empty location, 1 represents an occupied location)")
    for i in basegrid:
        for j in i:
            print(j, end="  ")
        print()

    print("")

    # 2 Initial Robot Position
    print("#2 BOB's Initial Position")
    print("(*Yeah, the robot is named BOB)")
    prompt = "Enter BOB's x position (0-indexed): "
    robot_1_x_position = int(input(prompt))

    prompt = "Enter BOB's y position (0-indexed): "
    robot_1_y_position = int(input(prompt))

    print("BOB is standing either on his yellow or green end")
    prompt = "Enter 'y' if its the yellow or 'g' if its the green: "
    standinghead = (input(prompt))

    basegrid[robot_1_x_position][robot_1_y_position] = 1

    def printplayground():
        print("\nThe current state of the playground is:")
        print("(0 represents and empty location, 1 represents BOB's location)")
        rotated = rotate(basegrid)
        for i in rotated:
            for j in i:
                print(j, end="  ")
            print()
        if standinghead == "g":
            print("BOB is standing on his GREEN end")
        else:
            print("BOB is standing on his YELLOW end")
        print("")

    printplayground()

    # 3 BOB's Journey
    print("#3 BOB's Journey")
    forward = 1
    while forward == 1:

        # 3.1 Desired Position
        prompt = "Enter BOB's new x position (0-indexed): "
        new_robot_1_x_position = int(input(prompt))
        prompt = "Enter BOB's new y position? (0-indexed): "
        new_robot_1_y_position = int(input(prompt))
        print("")

        # 3.1 BOB's X-movement
        print("Please wait while BOB makes it there")
        while robot_1_x_position != new_robot_1_x_position:
            if robot_1_x_position < new_robot_1_x_position:
                print("BOB, do a x+1")
                if standinghead == "y":
                    r1m1_x_plus_1()
                    standinghead = "g"
                else:
                    r1m4_x_plus_1()
                    standinghead = "y"
                robot_1_x_position = robot_1_x_position + 1
                basegrid = [[0 for i in range(basegrid_y)] for j in range(basegrid_x)]
                basegrid[robot_1_x_position][robot_1_y_position] = 1
                print("")
            elif robot_1_x_position > new_robot_1_x_position:
                print("BOB, do a x-1")
                if standinghead == "y":
                    r1m1_x_minus_1()
                    standinghead = "g"
                else:
                    r1m4_x_minus_1()
                    standinghead = "y"
                robot_1_x_position = robot_1_x_position - 1
                basegrid = [[0 for i in range(basegrid_y)] for j in range(basegrid_x)]
                basegrid[robot_1_x_position][robot_1_y_position] = 1
                print("")
            elif robot_1_x_position == new_robot_1_x_position:
                pass

        # 3.2 BOB's Y-movement
        while robot_1_y_position != new_robot_1_y_position:
            if robot_1_y_position < new_robot_1_y_position:
                print("BOB, do a y+1")
                if standinghead == "y":
                    r1m1_y_plus_1()
                    standinghead = "g"
                else:
                    r1m4_y_plus_1()
                    standinghead = "y"
                robot_1_y_position = robot_1_y_position + 1
                basegrid = [[0 for i in range(basegrid_y)] for j in range(basegrid_x)]
                basegrid[robot_1_x_position][robot_1_y_position] = 1
                print("")
            elif robot_1_y_position > new_robot_1_y_position:
                print("BOB, do a y-1")
                if standinghead == "y":
                    r1m1_y_minus_1()
                    standinghead = "g"
                else:
                    r1m4_y_minus_1()
                    standinghead = "y"
                robot_1_y_position = robot_1_y_position - 1
                basegrid = [[0 for i in range(basegrid_y)] for j in range(basegrid_x)]
                basegrid[robot_1_x_position][robot_1_y_position] = 1
                print("")
            elif robot_1_y_position == new_robot_1_y_position:
                pass

        # 3.3 Print Final Position
        printplayground()

        # 3.4 Continue?
        prompt = "Enter '1' to continue or press any other # to finish : "
        forward = int(input(prompt))
        print("")


# COLLAB PICKUPS 2 ROBOTS
def collab_pickup_a():  # X-aligned Yellow-standing (M1 & M5) X+2 Up-Doted
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(815)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(215)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)


def collab_pickup_b():  # X-aligned Yellow-standing (M1 & M5) X+1 Z+1 Up-Doted
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(815)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(215)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(215)
    time.sleep(time_delay)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(815)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(512)


def collab_pickup_c():  # X-aligned Yellow-standing (M1 & M5) X+1 Z+1 Up-Doted
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(815)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(215)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(512)


def collab_pickup_z():  # Help to single PickUp
    time.sleep(time_delay)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(675)

    time.sleep(time_delay)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(300)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(385)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(900)

    time.sleep(time_delay)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)


def r1_pickup_type_a():
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)


def r1_pickup_type_b():
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(815)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(215)

    time.sleep(time_delay)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(815)

    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)


# DEMONSTRATION SERIES ITERATION 01
# Demos at GC, no Unit Movement
def demo1():
    # R1 Rotate
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)

    # R1 Step // R2 Step
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)

    motor_controller.set_id(5)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R1 green
    motor_controller.set_position(512)

    # R1 Disconnect // R2 Step Disconnect
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # R1 yellow
    motor_controller.set_position(820)

    # R1 Rise // R2 Rise
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)

    motor_controller.set_id(5)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R1 green
    motor_controller.set_position(512)

    # R1 Step into R2
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)

    # R1 Disconnect
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(820)

    # R1 Prep Half Step Away
    time.sleep(time_delay)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)

    # R1 Half Step Away
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(820)

    # R1 Half Step Away
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(204)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(820)

    # R1 Disconnect + R2 Disconnect
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(400)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(204)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(820)

    motor_controller.set_id(5)  # R1 yellow
    motor_controller.set_position(400)
    motor_controller.set_id(6)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R1 green
    motor_controller.set_position(512)

    # R1 Up
    time.sleep(1)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)

    # R1 Catch Material
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(820)

    motor_controller.set_id(5)  # R1 yellow
    motor_controller.set_position(512)

    # R1 Lift Material
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)

    # R1 Lift Material
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(490)

    # R1 Low Material
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(485)

    # R1 Low Material
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(502)

    # R1 Disconnect
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(820)

    # R1 Up
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)


def demo2_initial_positions():
    # 00 INITIAL POSITIONS
    time.sleep(time_delay)
    # R1
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    # R2
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(204)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)


def demo2():
    demo2_initial_positions()

    # STEP 01 LET THE PARTY START
    time.sleep(time_delay)
    # R1 Pre-Attach to Wall
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(775)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    # R2 Hold
    # R3 Hold

    # STEP 02
    time.sleep(time_delay)
    # R1 Attach to Wall
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(820)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    # R2 Hold
    # R3 Hold

    # STEP 03
    time.sleep(time_delay)
    # R1 Detach Yellow
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(800)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    # R2 Pre-Position
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(550)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(180)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Hold

    # STEP 04
    time.sleep(time_delay)
    # R1 Step
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    # R2 Hold
    # R3 Hold

    # STEP 05
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    # R2 Position
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(650)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(140)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Hold

    # STEP 06
    time.sleep(time_delay)
    # R1 Hold
    # R2 Connect
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(150)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Hold

    # STEP 07
    time.sleep(time_delay)
    # R1 Detach
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R2 Hold
    # R3 Hold

    # STEP 08
    time.sleep(time_delay)
    # R1 Rotate
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R2 Hold
    # R3 Hold

    # STEP 09
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R2 Position
    # R3 Hold

    # STEP 10
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(700)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    time.sleep(time_delay)
    # R2 Position
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(400)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(204)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(100)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)

    # STEP 11
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(700)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R2 Position
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(400)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(204)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(100)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)

    # STEP 12
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R2 Position
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(204)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(204)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)

    # STEP 13
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R2 Hold
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(314)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(352)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)

    # STEP 14 Land
    time.sleep(time_delay)
    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(365)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(352)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)
    time.sleep(time_delay)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(314)

    # STEP 14 Detach
    time.sleep(time_delay)

    # R1 Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(350)
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(365)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(352)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(650)

    # STEP 15 Leave Alone
    time.sleep(time_delay)
    # R1 Hold
    # R2 Hold
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(352)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(650)

    # STEP 15 Leave Alone
    time.sleep(time_delay)
    # R1 Hold
    # R2 Position
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)
    # R3 Position
    motor_controller.set_id(9)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R1 blue
    motor_controller.set_position(820)
    motor_controller.set_id(11)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R1 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    r1m1_y_plus_1()
    r1m4_x_plus_1()


def wall_walk_initial_positions():  # R3 Hanging

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 Green
    motor_controller.set_position(512)


def wall_walk_a():  # R3 Hanging

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 Green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(400)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(230)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(400)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(245)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(185)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(204)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(245)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(185)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(204)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(185)

    # Connects

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(204)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(270)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(185)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(270)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(204)

    time.sleep(time_delay)
    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(185)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(205)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(204)

    # Connects

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(205)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(235)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(204)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(205)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(235)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(90)

    time.sleep(time_delay)
    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(235)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(90)

    for x in range(4):
        time.sleep(time_delay)
        motor_controller.set_id(9)  # R3 M1 yellow
        motor_controller.set_position(820)

        time.sleep(time_delay)
        motor_controller.set_id(9)  # R3 M1 yellow
        motor_controller.set_position(204)


def wall_walk_b():  # R3 Hanging

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    time.sleep(time_delay)
    time.sleep(time_delay)
    time.sleep(time_delay)
    time.sleep(time_delay)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(400)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(230)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(400)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(245)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(185)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(204)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(245)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(185)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(204)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(185)

    # Connects

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(204)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(270)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(512)

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(790)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(270)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(204)

    time.sleep(time_delay)
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(792)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(205)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(204)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(204)

    # Connects

    time.sleep(time_delay)
    motor_controller.set_id(1)  # R1 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 M2 blue
    motor_controller.set_position(205)
    motor_controller.set_id(3)  # R3 M3 red
    motor_controller.set_position(220)
    motor_controller.set_id(4)  # R1 M4 green
    motor_controller.set_position(204)


# DANCE STUDIES
# Before Paris Starting Position R2 & R3 (the bed is shifted 90 degrees)
def dance_before_paris_start():
    # Starting Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)


# Before Paris Starting Position R2 & R3 (the bed is shifted 90 degrees)
def dance_before_paris_a():
    # R2 Raise (Spot Light A)
    time.sleep(time_delay)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R3 Raise (Spot Light B)
    time.sleep(15)  # Just to turn lights on
    time.sleep(3)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 Face
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R3 Face
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(15)  # Just to turn lights on
    time.sleep(15)  # Just to turn lights on
    # Coordinated Dance (Front Lights)
    time.sleep(3.5)
    for x in range(1, 5):
        motor_controller.set_id(5)  # R2 M1 yellow
        motor_controller.set_position(512)
        motor_controller.set_id(6)  # R2 M2 blue
        motor_controller.set_position(666)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(358)
        motor_controller.set_id(8)  # R2 M4 Green
        motor_controller.set_position(820)
        motor_controller.set_id(9)  # R3 M1 yellow
        motor_controller.set_position(512)
        motor_controller.set_id(10)  # R3 M2 blue
        motor_controller.set_position(666)
        motor_controller.set_id(11)  # R3 M3 red
        motor_controller.set_position(358)
        motor_controller.set_id(12)  # R3 M4 green
        motor_controller.set_position(820)
        time.sleep(0.75)
        motor_controller.set_id(5)  # R2 M1 yellow
        motor_controller.set_position(820)
        motor_controller.set_id(6)  # R2 M2 blue
        motor_controller.set_position(358)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(666)
        motor_controller.set_id(8)  # R2 M4 Green
        motor_controller.set_position(512)
        motor_controller.set_id(9)  # R3 M1 yellow
        motor_controller.set_position(820)
        motor_controller.set_id(10)  # R3 M2 blue
        motor_controller.set_position(358)
        motor_controller.set_id(11)  # R3 M3 red
        motor_controller.set_position(666)
        motor_controller.set_id(12)  # R3 M4 green
        motor_controller.set_position(512)
        time.sleep(0.75)

    time.sleep(2)
    for x in range(1, 13):
        motor_controller.set_id(x)
        motor_controller.set_position(512)

    # R2M5_Yminus1 + R3M9_Yminus1
    robot2_ready_mode()
    robot3_ready_mode()
    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(815)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(815)
    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(815)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(815)
    time.sleep(time_delay)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(815)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(815)
    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(512)
    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(512)

    # R2M9_Xplus1() + R3M12_Xminus1
    robot2_ready_mode()
    robot3_ready_mode()
    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(205)
    motor_controller.set_id(12)  # green
    motor_controller.set_position(205)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(205)
    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(815)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(215)
    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(815)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(215)
    time.sleep(time_delay)
    motor_controller.set_id(8)  # green
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # green
    motor_controller.set_position(512)
    time.sleep(time_delay)
    motor_controller.set_id(6)  # blue
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # blue
    motor_controller.set_position(512)
    time.sleep(time_delay)
    motor_controller.set_id(7)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # yellow
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # red
    motor_controller.set_position(512)
    motor_controller.set_id(9)  # yellow
    motor_controller.set_position(512)

    # R2 R3 Face Each Other
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 R3 Angle towards R2
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(666)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 R3 Angle towards R3
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(666)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 R3 Switch Bases
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(666)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 R3 Ready
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(666)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(4)
    for x in range(1, 13):
        motor_controller.set_id(x)
        motor_controller.set_position(512)

    # R2 R3 Bow
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(800)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(800)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(4)
    for x in range(1, 13):
        motor_controller.set_id(x)
        motor_controller.set_position(512)

    # R2 R3 Face Each Other
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 R3 Pre-Kiss
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    time.sleep(15)  # Just to turn lights on
    time.sleep(15)  # Just to turn lights on
    # R2 R3 Kiss (Lights change)
    time.sleep(4)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # R2 Free
    time.sleep(8)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # UP Prep
    time.sleep(8)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(612)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(745)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(412)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(895)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # UP
    time.sleep(8)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(745)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(895)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)

    # UP 2
    time.sleep(8)
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(745)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(204)

    motor_controller.set_id(9)  # R3 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(10)  # R3 M2 blue
    motor_controller.set_position(335)
    motor_controller.set_id(11)  # R3 M3 red
    motor_controller.set_position(895)
    motor_controller.set_id(12)  # R3 M4 green
    motor_controller.set_position(512)


# DIFFICULT TERRAIN STUDIES | 1R
def r1_a_walk_until_edge():
    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 02 Prep Step
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 02 Step
    time.sleep(1)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(215)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 03 Disconnect
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(215)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 04 Forward Prep
    time.sleep(time_delay)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(810)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 05 Forward
    time.sleep(1)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(810)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(810)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 06 Disconnect
    time.sleep(3)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(810)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(810)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(204)

    # 06 New Terrains
    time.sleep(2)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(333)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    time.sleep(1)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 06 Nope
    time.sleep(3)
    robot1_ready_mode()

    # 06 New Terrains
    time.sleep(2)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(333)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 06 Nope
    time.sleep(2.5)
    robot1_ready_mode()


def r1_b_walk_4():
    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 02 Prep Step
    time.sleep(3)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 02 Step
    time.sleep(1)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(215)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 03 Disconnect
    time.sleep(2)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(215)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 04 Forward Prep
    time.sleep(2)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(810)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 05 Forward
    time.sleep(1)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(810)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(810)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 06 Disconnect
    time.sleep(3)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(810)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(810)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(204)

    # 06 Forward Prep
    time.sleep(2)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(204)

    # 06 Forward
    time.sleep(1)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(215)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 06 Disconnect
    time.sleep(3)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(204)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(215)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(215)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # 06 UP
    time.sleep(2)
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    time.sleep(2)


def r2_crawl_test_01():  # facing down (unsuccessful) 0

    for x in range(1, 8):
        time.sleep(2)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(820)
        time.sleep(2)
        motor_controller.set_id(6)  # R2 M2 blue
        motor_controller.set_position(820)
        time.sleep(2)
        motor_controller.set_id(6)  # R2 M2 blue
        motor_controller.set_position(512)
        time.sleep(2)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(512)


def r2_crawl_test_02():  # facing down (succesful) 6

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(140)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(875)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    time.sleep(2)

    for x in range(1, 16):
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(820)
        motor_controller.set_id(6)  # R2 blue
        motor_controller.set_position(140)
        time.sleep(.5)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(875)
        motor_controller.set_id(6)  # R2 blue
        motor_controller.set_position(50)
        time.sleep(.5)


def r2_crawl_test_03():  # facing down (unsuccesful) 0

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    time.sleep(2)

    for x in range(1, 16):
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(875)
        motor_controller.set_id(6)  # R2 blue
        motor_controller.set_position(875)
        time.sleep(.5)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(820)
        motor_controller.set_id(6)  # R2 blue
        motor_controller.set_position(820)
        time.sleep(.5)


def r2_crawl_test_04():  # facing down

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(630)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    time.sleep(2)

    for x in range(1, 16):
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(875)
        motor_controller.set_id(6)  # R2 M2 blue
        motor_controller.set_position(400)
        time.sleep(.5)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_position(820)
        motor_controller.set_id(6)  # R2 M2 blue
        motor_controller.set_position(630)
        time.sleep(.5)


def r2_crawl_test_05():  # facing down

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(512)

    time.sleep(4)

    for x in range(1, 9):
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_moving_speed(500)
        motor_controller.set_position(600)

        time.sleep(2)
        motor_controller.set_id(6)  # R2 M3 red
        motor_controller.set_moving_speed(75)
        motor_controller.set_position(600)

        time.sleep(2)
        motor_controller.set_id(7)  # R2 M3 red
        motor_controller.set_moving_speed(75)
        motor_controller.set_position(820)
        motor_controller.set_id(6)  # R2 M3 red
        motor_controller.set_moving_speed(75)
        motor_controller.set_position(820)
        time.sleep(2)


def r2_crawl_test_06():  # facing down

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    for x in range(1, 5):
        time.sleep(4)
        motor_controller.set_id(8)  # R2 M3 red
        motor_controller.set_position(204)

        time.sleep(4)
        motor_controller.set_id(5)  # R2 M3 red
        motor_controller.set_position(204)

        time.sleep(4)
        motor_controller.set_id(8)  # R2 M3 red
        motor_controller.set_position(820)

        time.sleep(4)
        motor_controller.set_id(5)  # R2 M3 red
        motor_controller.set_position(820)


def r2_crawl_test_07():  # facing down (succesful on wood) 7

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    for x in range(1, 17):
        time.sleep(.5)
        motor_controller.set_id(8)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(200)
        time.sleep(4)
        motor_controller.set_moving_speed(0)
        motor_controller.set_wheel_mode(2)

        time.sleep(.5)
        motor_controller.set_id(5)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(200)
        time.sleep(4)
        motor_controller.set_moving_speed(0)
        motor_controller.set_wheel_mode(2)

    motor_controller.set_id(8)
    motor_controller.set_wheel_mode(2)
    motor_controller.set_id(5)
    motor_controller.set_wheel_mode(2)


def r2_crawl_test_08():  # facing down (wierd)

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    for x in range(1, 9):
        time.sleep(.5)
        motor_controller.set_id(8)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(500)
        time.sleep(2)
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()

        time.sleep(.5)
        motor_controller.set_id(5)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(500)
        time.sleep(2)
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()

    motor_controller.set_id(8)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_id(5)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()


def r2_crawl_test_09():  # facing down (wierd)

    # 01 Initial Position
    motor_controller.set_id(5)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(6)  # R2 M2 blue
    motor_controller.set_position(820)
    motor_controller.set_id(7)  # R2 M3 red
    motor_controller.set_position(820)
    motor_controller.set_id(8)  # R2 M4 Green
    motor_controller.set_position(820)

    time.sleep(4)
    motor_controller.set_id(8)  # R2 M3 red
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(250)
    motor_controller.set_id(5)  # R2 M3 red
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(250)
    time.sleep(12)

    motor_controller.set_id(8)
    motor_controller.set_wheel_mode(0)
    motor_controller.set_id(5)
    motor_controller.set_wheel_mode(0)


# crawl 10 - wheel - turns - speed 250 (success)
def r1_crawl_test_10():  # facing down () Success 9

    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(790)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(700)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(820)

    time.sleep(4)

    for x in range(1, 9):
        time.sleep(1)
        motor_controller.set_id(2)  # R2 M2 blue
        motor_controller.set_position(700)
        motor_controller.set_id(3)  # R2 M3 red
        motor_controller.set_position(790)
        time.sleep(1)
        motor_controller.set_id(1)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(250)
        time.sleep(2)
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()

        time.sleep(1)
        motor_controller.set_id(2)  # R2 M2 blue
        motor_controller.set_position(790)
        motor_controller.set_id(3)  # R2 M3 red
        motor_controller.set_position(700)
        time.sleep(1)
        motor_controller.set_id(4)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(1274)
        time.sleep(2)
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()


# crawl 11 - wheel - double - speed 250 (success)
def r1_crawl_test_11():  # facing down () Success 9

    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(820)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(790)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(700)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(820)

    time.sleep(4)

    for x in range(1, 9):
        time.sleep(1)
        motor_controller.set_id(2)  # R2 M2 blue
        motor_controller.set_position(700)
        motor_controller.set_id(3)  # R2 M3 red
        motor_controller.set_position(790)
        time.sleep(1)
        motor_controller.set_id(1)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(500)
        time.sleep(2)
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()

        time.sleep(1)
        motor_controller.set_id(2)  # R2 M2 blue
        motor_controller.set_position(790)
        motor_controller.set_id(3)  # R2 M3 red
        motor_controller.set_position(700)
        time.sleep(1)
        motor_controller.set_id(4)  # R2 M3 red
        motor_controller.set_wheel_mode(1)
        motor_controller.set_moving_speed(1524)
        time.sleep(2)
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()


# crawl 12 - wheel - double - speed 500 (success)
def r1_crawl_test_12():  # facing down () Success 10

    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # Rotate
    motor_controller.set_id(1)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(250)
    motor_controller.set_id(4)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(1274)

    # Stop
    time.sleep(9.2)
    motor_controller.set_id(1)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_id(4)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()

    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)


def r1r2_crawl_test_13():  # facing down () Success 10

    # 01 Initial Position
    motor_controller.set_id(1)  # R2 M1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R2 M2 blue
    motor_controller.set_position(535)
    motor_controller.set_id(3)  # R2 M3 red
    motor_controller.set_position(535)
    motor_controller.set_id(4)  # R2 M4 Green
    motor_controller.set_position(512)

    # Rotate
    motor_controller.set_id(1)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(500)
    motor_controller.set_id(4)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(1274)

    # Stop
    time.sleep(6)
    motor_controller.set_id(1)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_id(4)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()


# DIFFICULT TERRAIN STUDIES | 2R
# 01 Pull
def r1r2_crawl_test_01():  # facing down () Success 10

    # 00 Separated Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(600)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(666)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(190)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 Initial Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(600)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(450)  # CHANGE
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(190)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Crawl
    for x in range(0, 16):
        # Pull Position
        motor_controller.set_id(2)  # R1 blue
        motor_controller.set_position(190)  # CHANGE
        motor_controller.set_id(3)  # R1 red
        motor_controller.set_position(600)
        time.sleep(2)

        # Rise Position
        motor_controller.set_id(2)  # R1 blue
        motor_controller.set_position(190)
        motor_controller.set_id(3)  # R1 red
        motor_controller.set_position(700)  # CHANGE
        time.sleep(1)

        # Extend Position
        motor_controller.set_id(2)  # R1 blue
        motor_controller.set_position(512)  # CHANGE
        motor_controller.set_id(3)  # R1 red
        motor_controller.set_position(700)
        time.sleep(1)

        # Down Position
        motor_controller.set_id(2)  # R1 blue
        motor_controller.set_position(512)
        motor_controller.set_id(3)  # R1 red
        motor_controller.set_position(600)  # CHANGE
        time.sleep(1)


# 02 Push
def r1r2_crawl_test_02():  # facing down () Success 10

    # 00 Separated Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(600)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(666)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(214)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 Initial Position
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(600)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(204)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(450)  # CHANGE
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(214)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Crawl
    for x in range(0, 16):
        # Rise
        motor_controller.set_id(3)  # R1 red
        motor_controller.set_position(700)  # CHANGE
        time.sleep(1)

        # Contract
        motor_controller.set_id(2)  # R1 blue
        motor_controller.set_position(155)  # CHANGE
        time.sleep(2)

        # Down
        motor_controller.set_id(3)  # R1 red
        motor_controller.set_position(600)  # CHANGE
        time.sleep(1)

        # Push
        motor_controller.set_id(2)  # R1 blue
        motor_controller.set_position(512)  # CHANGE
        time.sleep(2)


# 03 Wheel Mode | Floor Cleaning
def r1r2_crawl_wheel_test_03():  # facing down () Success 10

    # 01 Initial Position
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(3)
    motor_controller.set_position(475)
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(475)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(8)
    motor_controller.set_position(512)

    # Rotate
    motor_controller.set_id(1)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(250)
    motor_controller.set_id(8)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(1274)

    # Stop
    time.sleep(16)
    motor_controller.set_id(1)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_id(8)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()

    # 01 Initial Position
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(3)
    motor_controller.set_position(475)
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(475)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(8)
    motor_controller.set_position(512)


# 03 Wheel Mode | Segway
def r1r2_crawl_wheel_test_04():  # facing down () Success 10

    # 01 Initial Position
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)

    # Rotate
    motor_controller.set_id(1)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(250)
    motor_controller.set_id(4)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(1274)
    motor_controller.set_id(5)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(1274)
    motor_controller.set_id(8)
    motor_controller.set_wheel_mode(1)
    motor_controller.set_moving_speed(1274)

    # Stop
    time.sleep(16)
    motor_controller.set_id(1)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()
    motor_controller.set_id(8)
    motor_controller.set_moving_speed(0)
    motor_controller.enable_torque()

    # 01 Initial Position
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)


# DIFFICULT TERRAIN STUDIES | 2R Mat
def r1r2mat_walk_test_01():
    # 00 Straight
    motor_controller.set_id(1)  # R1 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(2)  # R1 blue
    motor_controller.set_position(512)
    motor_controller.set_id(3)  # R1 red
    motor_controller.set_position(512)
    motor_controller.set_id(4)  # R1 green
    motor_controller.set_position(512)
    motor_controller.set_id(5)  # R2 yellow
    motor_controller.set_position(512)
    motor_controller.set_id(6)  # R2 blue
    motor_controller.set_position(512)
    motor_controller.set_id(7)  # R2 red
    motor_controller.set_position(512)
    motor_controller.set_id(8)  # R2 green
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Walk
    for x in range(0, 16):
        # Extend
        motor_controller.set_id(3)
        motor_controller.set_position(400)  # CHANGE
        motor_controller.set_id(6)
        motor_controller.set_position(550)  # CHANGE
        time.sleep(3)

        # Step
        motor_controller.set_id(3)
        motor_controller.set_position(512)  # CHANGE
        motor_controller.set_id(6)
        motor_controller.set_position(512)  # CHANGE
        time.sleep(3)


# DIFFICULT TERRAIN STUDIES | 3R Mat
def r1r2r3mat_walk_test_01():
    # 00 Straight
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(545)
    motor_controller.set_id(3)
    motor_controller.set_position(630)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(545)
    motor_controller.set_id(7)
    motor_controller.set_position(630)
    motor_controller.set_id(8)
    motor_controller.set_position(204)

    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(545)
    motor_controller.set_id(11)
    motor_controller.set_position(630)
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    time.sleep(4)

    # 02 Leg Push
    for x in range(0, 16):
        motor_controller.set_id(10)
        motor_controller.set_position(512)
        motor_controller.set_id(11)
        motor_controller.set_position(512)
        time.sleep(2)

        motor_controller.set_id(10)
        motor_controller.set_position(545)
        motor_controller.set_id(11)
        motor_controller.set_position(630)
        time.sleep(2)


# DIFFICULT TERRAIN STUDIES | Drag / Push Mat
def r1mat_pull_test_01():
    # 00 Start
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(375)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Drag
    for x in range(0, 8):
        # Pull
        motor_controller.set_id(3)
        motor_controller.set_position(860)
        time.sleep(2)

        # Raise Arm
        motor_controller.set_id(2)
        motor_controller.set_position(300)
        time.sleep(1)

        # Extend
        motor_controller.set_id(3)
        motor_controller.set_position(512)
        time.sleep(2)

        # Lower Arm
        motor_controller.set_id(2)
        motor_controller.set_position(375)
        time.sleep(1)


def r1mat_push_test_02():
    # 00 Start
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(375)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Drag
    for x in range(0, 8):
        # Raise Arm
        motor_controller.set_id(2)
        motor_controller.set_position(300)
        time.sleep(1)

        # Contract
        motor_controller.set_id(3)
        motor_controller.set_position(860)
        time.sleep(2)

        # Lower Arm
        motor_controller.set_id(2)
        motor_controller.set_position(375)
        time.sleep(1)

        # Extend
        motor_controller.set_id(3)
        motor_controller.set_position(512)
        time.sleep(2)


def r1r2mat_pull_test_03():
    # 00 Start
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(375)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(375)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Drag
    for x in range(0, 8):
        # Pull
        motor_controller.set_id(3)
        motor_controller.set_position(860)
        motor_controller.set_id(7)
        motor_controller.set_position(860)
        time.sleep(2)

        # Raise Arm
        motor_controller.set_id(2)
        motor_controller.set_position(300)
        motor_controller.set_id(6)
        motor_controller.set_position(300)
        time.sleep(1)

        # Extend
        motor_controller.set_id(3)
        motor_controller.set_position(512)
        motor_controller.set_id(7)
        motor_controller.set_position(512)
        time.sleep(2)

        # Lower Arm
        motor_controller.set_id(2)
        motor_controller.set_position(375)
        motor_controller.set_id(6)
        motor_controller.set_position(375)
        time.sleep(1)


def r1r2mat_push_test_02():
    # 00 Start
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(375)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(375)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)

    time.sleep(4)

    # 02 Drag
    for x in range(0, 8):
        # Raise Arm
        motor_controller.set_id(2)
        motor_controller.set_position(300)
        motor_controller.set_id(6)
        motor_controller.set_position(300)
        time.sleep(0.5)

        # Contract
        motor_controller.set_id(3)
        motor_controller.set_position(900)
        motor_controller.set_id(7)
        motor_controller.set_position(900)
        time.sleep(1)

        # Lower Arm
        motor_controller.set_id(2)
        motor_controller.set_position(375)
        motor_controller.set_id(6)
        motor_controller.set_position(375)
        time.sleep(0.5)

        # Extend
        motor_controller.set_id(3)
        motor_controller.set_position(512)
        motor_controller.set_id(7)
        motor_controller.set_position(512)
        time.sleep(1)


# CLIMBING STUDIES
# 01 Straight Climb (flip)
def r3_climbing_test_01():  # starts in X2 Y2, on yellow, looking towards the camera

    # 00 Starting Position
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 Turn & Prep
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(204)
    motor_controller.set_id(12)
    motor_controller.set_position(820)

    time.sleep(2)

    # 02 Down & Connect
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(2)

    # 03 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(2)

    # 04 Up
    motor_controller.set_id(11)
    motor_controller.set_position(512)

    time.sleep(2)

    # 05 Turn
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(2)

    # 06 Down & Connect
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(2)

    # 07 Disconnect
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    time.sleep(2)

    # 08 Up
    motor_controller.set_id(10)
    motor_controller.set_position(450)

    time.sleep(2)

    # 09 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(4)

    # 10 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(512)

    time.sleep(2)

    # 11 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(204)

    time.sleep(2)

    # 12 Hang
    motor_controller.set_id(11)
    motor_controller.set_position(666)

    time.sleep(2)

    # 13 Prep
    motor_controller.set_id(10)
    motor_controller.set_position(820)

    time.sleep(2)

    # 14 Up
    motor_controller.set_id(11)
    motor_controller.set_position(300)

    time.sleep(3)

    # 15 Prep
    motor_controller.set_id(10)
    motor_controller.set_position(204)
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(3)

    # 16 Connect
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(2)

    # 17 Disconnect
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    time.sleep(2)

    # 18 Hang & Flip
    motor_controller.set_id(10)
    motor_controller.set_position(750)

    time.sleep(4)

    # 19 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(3)

    # 20 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(820)

    time.sleep(2)


# 03 Horizontal Climb
def r3_climbing_test_03():  # starts in X2 Y2, on yellow, looking towards the camera

    # 00 Starting Position
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 Forward Prep
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(1.5)

    # 02 Forward Connect
    motor_controller.set_id(10)
    motor_controller.set_position(204)

    time.sleep(2)

    # 03 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(204)

    time.sleep(2)

    # 04 Prep1
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    motor_controller.set_id(11)
    motor_controller.set_position(450)

    time.sleep(2)

    # 05 Prep2
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(2)

    # 06 Connect with Wall
    motor_controller.set_id(11)
    motor_controller.set_position(512)

    time.sleep(2)

    # 07 Disconnect
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    time.sleep(2)

    # 08 Prep
    motor_controller.set_id(10)
    motor_controller.set_position(700)
    motor_controller.set_id(11)
    motor_controller.set_position(666)

    time.sleep(2)

    # 08.5 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(512)

    time.sleep(2)

    # 09 Rotate
    motor_controller.set_id(9)
    motor_controller.set_position(838)

    time.sleep(2)

    # 10 Connect Pre
    motor_controller.set_id(11)
    motor_controller.set_position(820)

    time.sleep(2)

    # 11 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(820)

    time.sleep(2)

    # 12 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(2)

    # 13 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(250)
    motor_controller.set_id(12)
    motor_controller.set_position(230)

    time.sleep(4)

    # 13 Prep
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(204)

    time.sleep(4)

    # 14 Connect
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(1.5)

    # 15 Disconnect
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(2)

    # 16 Prep
    motor_controller.set_id(10)
    motor_controller.set_position(266)

    time.sleep(2)

    # 17 Rotate
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(2)

    # 18 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(204)

    time.sleep(2)

    # 19 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(204)

    time.sleep(2)

    # 20 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(266)

    time.sleep(2)

    # 21 Turn
    motor_controller.set_id(12)
    motor_controller.set_position(185)

    time.sleep(2)

    # 22 Connect
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(2)

    # 22 Disconnect
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(2)

    # 23 Prep
    motor_controller.set_id(10)
    motor_controller.set_position(266)

    time.sleep(2)

    # 24 Turn
    motor_controller.set_id(9)
    motor_controller.set_position(800)
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    time.sleep(4)

    # 23 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(204)

    time.sleep(2)

    # 24 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(2)

    # 25 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(266)

    time.sleep(2)

    # 26 Rotate
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(2)

    # 27 Connect
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(2)

    # 29 Disconnect
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    time.sleep(2)

    # 30 Prep
    motor_controller.set_id(10)
    motor_controller.set_position(266)

    time.sleep(2)

    # 31 Turn
    motor_controller.set_id(9)
    motor_controller.set_position(835)

    time.sleep(2)

    # 32 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(204)

    time.sleep(2)

    # 33 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(512)

    time.sleep(2)

    # 33 Pre
    motor_controller.set_id(11)
    motor_controller.set_position(266)

    time.sleep(2)

    # 33 Turn
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(12)
    motor_controller.set_position(840)

    time.sleep(4)

    # 33 Pre
    motor_controller.set_id(11)
    motor_controller.set_position(204)

    time.sleep(2)


# XX Around the World
def r1_around_the_world():
    # 00 Starting Position
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 Prep
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    time.sleep(2)

    # 02 Connect
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    time.sleep(2)

    # 03 Disconnect
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    time.sleep(2)

    # 04 Up Prep
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(3)
    motor_controller.set_position(450)
    time.sleep(2)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    time.sleep(2)

    # 05 Connect Wall - Yellow
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    time.sleep(1.3)

    # 06 Disconnect - Green
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    time.sleep(2)

    # 07 Prep
    motor_controller.set_id(2)
    motor_controller.set_position(730)
    motor_controller.set_id(3)
    motor_controller.set_position(666)
    time.sleep(1)
    motor_controller.set_id(2)
    motor_controller.set_position(700)
    time.sleep(2)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(333)
    time.sleep(2)
    motor_controller.set_id(3)
    motor_controller.set_position(333)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(275)
    time.sleep(1)
    motor_controller.set_id(3)
    motor_controller.set_position(425)
    time.sleep(1)
    motor_controller.set_id(2)
    motor_controller.set_position(215)
    time.sleep(1)
    motor_controller.set_id(3)
    motor_controller.set_position(475)
    time.sleep(1)

    # 08 Connect - Green
    motor_controller.set_id(2)
    motor_controller.set_position(208)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    time.sleep(.5)
    motor_controller.set_id(2)
    motor_controller.set_position(190)

    # 09 Disconnect - Yellow
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    time.sleep(2)

    # 10 Step & Connect Yellow
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    time.sleep(2)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(2)

    # 11 Disconnect - Green
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    time.sleep(2)

    # 12 Prep & Connect
    motor_controller.set_id(2)
    motor_controller.set_position(333)
    time.sleep(3)
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    time.sleep(3)

    # 13 Connect - Green (to last hanging point)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    time.sleep(1.5)

    # 14 Disconnect - Yellow
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    time.sleep(2)

    # 15 Prep
    motor_controller.set_id(3)
    motor_controller.set_position(333)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    time.sleep(3)

    # 16 Connect - Yellow
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    time.sleep(2)

    # 17 Disconnect - Green (from last hanging point)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    time.sleep(2)

    # Prep
    motor_controller.set_id(2)
    motor_controller.set_position(750)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(350)
    time.sleep(3)
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    time.sleep(2)

    # 17 Disconnect - Yellow (from last wall point)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    time.sleep(2)

    # 17 Prep & Connect - Yellow
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    time.sleep(2)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(2)

    # 17 Disconnect - Green
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    time.sleep(2)

    # 00 Starting Position
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    time.sleep(1)
    motor_controller.set_id(3)
    motor_controller.set_position(500)
    motor_controller.set_id(4)
    motor_controller.set_position(512)


# XX Around the World
def r3_around_the_world():
    # 00 Starting Position
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 Prep
    motor_controller.set_id(11)
    motor_controller.set_position(204)
    time.sleep(2)

    # 02 Connect
    motor_controller.set_id(10)
    motor_controller.set_position(204)
    time.sleep(2)

    # 03 Disconnect
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    time.sleep(2)

    # 04 Up Prep
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    motor_controller.set_id(11)
    motor_controller.set_position(450)
    time.sleep(2)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    time.sleep(2)

    # 05 Connect Wall - Yellow
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    time.sleep(1.3)

    # 06 Disconnect - Green
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(2)

    # 06 Prep


# BRIDGING STUDIES
# R1R2R3 Portable Demo Bridging test 1 (Level 2 Pass)
def r1r2r3_bridging_test_01():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(4)

    # 01
    print("")
    print("GO")
    print("# 01 R2 Prep Step")
    motor_controller.set_id(7)
    motor_controller.set_position(820)
    time.sleep(2)

    # 02
    motor_controller.set_id(6)
    motor_controller.set_position(820)
    time.sleep(2)

    # 03
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # 04
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    time.sleep(0.5)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    time.sleep(2)

    # 05 R1 Disconnect R1_M1 from mat | R2 UP | R3 Connects with mat
    print("")
    print("05 R1 Disconnect R1_M1 from mat | R2 UP | R3 Connects with mat")
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    time.sleep(0.2)
    motor_controller.set_id(3)
    motor_controller.set_position(300)
    time.sleep(2)

    # 06
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    time.sleep(1)

    # 07
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    time.sleep(2)

    # 08
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(2)

    # 09 R1&R2 Disconnect R1_M4 & R2_M5
    print("")
    print("09 R1&R2 Disconnect R1_M4 & R2_M5")
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(5)
    motor_controller.set_position(333)
    time.sleep(0.1)
    motor_controller.set_id(2)
    motor_controller.set_position(750)
    time.sleep(1)

    # 10
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(820)
    time.sleep(2)

    # 11
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(7)
    motor_controller.set_position(820)
    time.sleep(2)

    # 12
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)

    # 13 Connect R1_M4 with mat
    print("")
    print("13 R1 Connect R1_M4 with mat")
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    time.sleep(2)

    # 14 Disconnect R1_M1 & R3_M9
    print("")
    print("14 R1&R3 Disconnect R1_M1 & R3_M9")
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(9)
    motor_controller.set_position(333)
    time.sleep(0.1)
    motor_controller.set_id(3)
    motor_controller.set_position(275)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    time.sleep(1)

    # 15 R1 UP
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    time.sleep(2)

    # 16 R3 Connect Back
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    time.sleep(2)

    # 17 R3 Disconnect
    print("")
    print("17 R3 Disconnect R1_M1 & R3_M9")
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(2)

    # 18 R3 UP
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    time.sleep(1)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(2)


# R1R2R3 Portable Demo Bridging test 2 (Level 1 Pass)
def r1r2r3_bridging_test_02():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(6)

    # 01 GO
    print("")
    print("GO")
    print("# 01 R1 Prep Step")
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(1)

    # 02 R1R2 Connect
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    time.sleep(2)

    # 03 R1 Disconnect R1_M1 from mat
    print("")
    print("03 Disconnect R1_M1 from mat")
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(850)
    motor_controller.set_id(11)
    motor_controller.set_position(155)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(2)

    # 04 R1 Step
    print("")
    print("04 R2&R3 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(1)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    time.sleep(3)

    # 05 R1&R2 Disconnect
    print("")
    print("05 R1&R2 Disconnect")
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(7)
    motor_controller.set_position(333)
    motor_controller.set_id(8)
    motor_controller.set_position(333)
    time.sleep(0.2)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    time.sleep(2)

    # 06 R1 Step into mat
    print("")
    print("07 R1 Step into mat")
    motor_controller.set_id(3)
    motor_controller.set_position(155)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    time.sleep(2.5)
    motor_controller.set_id(2)
    motor_controller.set_position(255)
    time.sleep(2)

    # 08 R1&R3 Disconnect
    print("")
    print("08 R1&R3 Disconnect")
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_position(333)
    time.sleep(0.2)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    time.sleep(2)

    # 09 R1 UP
    print("")
    print("09 R1 UP")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)


# R1R2R3 Portable Demo Combined test 2 (Level 1 Pass to Level 2)
def r1r2r3_bridging_elevator_test_01():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(4)

    # 01 GO
    print("")
    print("GO")
    print("# 01 R1 Prep Step")
    motor_controller.set_id(6)
    motor_controller.set_position(800)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(1)

    # 02 R1R2 Connect
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    time.sleep(2)

    # 03 R1 Disconnect R1_M1 from mat
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(180)

    # 03 R1 UP
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(1)
    motor_controller.set_position(255)


# R1R2R3 Portable Demo Combined test 2 (Level 1 Pass to Level 2)
def r1r2r3_bridging_elevator_test_02():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(5)

    # 01 GO
    print("")
    print("GO")
    print("# 01 R1 Prep Step")
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(1)

    # 02 R1R2 Connect
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    time.sleep(2)

    # 03 R1 Disconnect R1_M1 from mat
    print("")
    print("Disconnect R1_M1 from mat")
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(850)
    motor_controller.set_id(11)
    motor_controller.set_position(155)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(2)

    # 03 R1 Step
    print("")
    print("03 R2&R3 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    time.sleep(1.66)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(1)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    time.sleep(3)

    # 04 R2R3 Pre Elevator
    print("")
    print("04 Prep Elevator")
    motor_controller.set_id(7)
    motor_controller.set_position(100)
    motor_controller.set_id(11)
    motor_controller.set_position(100)
    time.sleep(1)

    # 05 R2R3 Elevator UP
    print("")
    print("05 Elevator UP")
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    time.sleep(.2)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    time.sleep(3.5)

    # 05 R1&R2 Disconnect
    print("")
    print("05 R1&R2 Disconnect")
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(7)
    motor_controller.set_position(333)
    motor_controller.set_id(8)
    motor_controller.set_position(333)
    time.sleep(0.2)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    time.sleep(2)

    # 06 R1 Step into mat
    print("")
    print("07 R1 Step into mat")
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    time.sleep(2.5)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    time.sleep(2.5)

    # 08 R1&R3 Disconnect
    print("")
    print("08 R1&R3 Disconnect")
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_position(333)
    time.sleep(0.2)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    time.sleep(2)

    # 09 R1 UP
    print("")
    print("09 R1 UP")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)


# B-Pro DEMO #
def speeds_reset():
    for x in range(1, 17):
        motor_controller.set_id(x)
        motor_controller.set_moving_speed(75)


def r1r2r3r4_optitrack_demo_01_r2():
    # R2 SIDE | Catch & Place Piece
    # R2 SIDE START POS
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    time.sleep(3)

    # R2 SIDE 01
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    time.sleep(0.5)

    # R2 SIDE 02
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    time.sleep(2)

    # R2 SIDE 03
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE 04
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE 05
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE 06
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    time.sleep(2)

    # R2 SIDE 07
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE 08
    motor_controller.set_id(6)
    motor_controller.set_position(550)
    time.sleep(1)

    # R2 SIDE 09
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE START POS
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    time.sleep(2)


def r1r2r3r4_optitrack_demo_01_r4():
    # 00 R4 Starting Position
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(8)

    # 01 R4 Prep Connect 1
    motor_controller.set_id(14)
    motor_controller.set_position(790)
    time.sleep(2)

    # 02 R4 Prep Connect 2
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2)

    # 03 R4 Connects Up (Green)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(2)

    # 04 R4 Disconnects (Yellow)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(2)

    # 05 R4 Prep Turn
    motor_controller.set_id(15)
    motor_controller.set_position(790)
    time.sleep(2)

    # 06 R4 Turn
    motor_controller.set_id(16)
    motor_controller.set_position(850)
    time.sleep(2)

    # 07 R4 Connect Right (Yellow)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2)

    # 08 R4 Disconnect (Green)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2)

    # 09 R4 Prep Turn 1
    motor_controller.set_id(14)
    motor_controller.set_position(750)
    time.sleep(2)

    # 10 R4 Prep Turn 2
    motor_controller.set_id(15)
    motor_controller.set_position(135)
    time.sleep(4)

    # 11 R4 Turn
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(666)
    time.sleep(2)

    # 12 R4 Prep Connect
    motor_controller.set_id(15)
    motor_controller.set_position(750)
    time.sleep(4)

    # 13 R4 Connect (Green Down)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(2)

    # 14 R4 Disconnect (Yellow Up)
    motor_controller.set_id(13)
    motor_controller.set_position(820)
    time.sleep(2)

    # 15 R4 Prep Catch
    motor_controller.set_id(15)
    motor_controller.set_position(450)
    time.sleep(1)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    time.sleep(2)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(2)

    # 16 R4 Catch
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(1)

    # 17 R4 UP
    motor_controller.set_id(14)
    motor_controller.set_position(480)
    time.sleep(2)

    # 18 R4 Half-Turn
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    time.sleep(2)

    # 19 R4 Prep Half Turn
    motor_controller.set_id(14)
    motor_controller.set_position(530)
    time.sleep(2)

    # 20 R4 Half-Turn
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(1)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    time.sleep(2)


def r1r2r3r4_optitrack_demo_01_r1r4():
    # Starting Pos
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    time.sleep(0.5)

    # R1 Prep Catch
    motor_controller.set_id(3)
    motor_controller.set_position(450)
    motor_controller.set_id(3)
    motor_controller.set_position(450)
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    time.sleep(2)

    # R1 Catch
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    time.sleep(1)

    # R4 Detach
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(3)
    motor_controller.set_position(333)
    motor_controller.set_id(3)
    motor_controller.set_position(333)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    time.sleep(2)

    # R1 Prep Turn
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(820)
    time.sleep(2)

    # R1 Turn
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(204)
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    motor_controller.set_id(11)
    motor_controller.set_position(820)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2)

    # R1 Down
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(475)
    motor_controller.set_id(15)
    motor_controller.set_position(475)
    time.sleep(2)

    # R1 Detach
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    time.sleep(2)

    # UP
    motor_controller.set_id(3)
    motor_controller.set_position(333)
    motor_controller.set_id(3)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    time.sleep(1)


def r1r2r3r4_optitrack_demo_01():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)

    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(8)

    # 01 GO
    print("")
    print("GO")
    print("# 01 R1 Prep Step")
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(1)

    # 02 R1R2 Connect | #01 R4 Prep Connect 1
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    motor_controller.set_id(14)
    motor_controller.set_position(790)
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    motor_controller.set_id(14)
    motor_controller.set_position(790)
    time.sleep(2)

    # 03 R1 Disconnect R1_M1 from mat  | #02 R4 Prep Connect 2
    print("")
    print("Disconnect R1_M1 from mat")
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(850)
    motor_controller.set_id(11)
    motor_controller.set_position(155)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(850)
    motor_controller.set_id(11)
    motor_controller.set_position(155)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2)

    # 03 R1 Step | # 03 R4 Connects Up (Green)
    print("")
    print("03 R2&R3 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    time.sleep(1.66)

    motor_controller.set_id(3)
    motor_controller.set_position(820)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(3)

    # 04 R2R3 Pre Elevator | # 04 R4 Disconnects (Yellow)
    print("")
    print("04 Prep Elevator")
    motor_controller.set_id(7)
    motor_controller.set_position(100)
    motor_controller.set_id(11)
    motor_controller.set_position(100)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    motor_controller.set_id(7)
    motor_controller.set_position(100)
    motor_controller.set_id(11)
    motor_controller.set_position(100)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(2)

    # 05 R2R3 Elevator UP | # 05 R4 Prep Turn
    print("")
    print("05 Elevator UP")
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    time.sleep(.2)

    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(790)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(790)
    time.sleep(3.5)

    # 05 R1&R2 Disconnect | # 06 R4 Turn
    print("")
    print("05 R1&R2 Disconnect")
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(7)
    motor_controller.set_position(666)
    motor_controller.set_id(8)
    motor_controller.set_position(333)
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(7)
    motor_controller.set_position(666)
    motor_controller.set_id(8)
    motor_controller.set_position(333)
    time.sleep(0.2)

    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(850)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(850)
    time.sleep(2)

    # 06 R1 Step into mat | # 07 R4 Connect Right (Yellow) | # 08 R4 Disconnect (Green)
    print("")
    print("07 R1 Step into mat")
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2.5)

    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2.5)

    # 08 R1&R3 Disconnect | # R2 SIDE START POS | # 09 R4 Prep Turn 1
    print("")
    print("08 R1&R3 Disconnect")
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_position(333)
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_position(333)
    time.sleep(0.2)

    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(750)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(750)
    time.sleep(2)

    # 09 R1 UP | # R2 SIDE 01 | # 10 R4 Prep Turn 2
    print("")
    print("09 R1 UP")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(15)
    motor_controller.set_position(135)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(15)
    motor_controller.set_position(135)
    time.sleep(4)

    # R2 SIDE 02 | # 11 R4 Turn
    print("")
    print("")
    print("09 R2 & R4 Lead")
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(666)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(666)
    time.sleep(2)

    # R2 SIDE 03 | # 12 R4 Prep Connect
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(750)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(750)
    time.sleep(4)

    # R2 SIDE 04 | # 13 R4 Connect (Green Down)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE 05 | # 14 R4 Disconnect (Yellow Up)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(820)
    time.sleep(2)

    # R2 SIDE 06 | # R2 SIDE 07 | # 15 R4 Prep Catch
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(450)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(450)
    time.sleep(1)

    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    time.sleep(2)

    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(2)

    # R2 SIDE 08 | # 16 R4 Catch
    motor_controller.set_id(6)
    motor_controller.set_position(550)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(550)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(1)

    # R2 SIDE 09 | # 17 R4 UP
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(480)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(480)
    time.sleep(2)

    # 18 R4 Half-Turn
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    time.sleep(2)

    # 19 R4 Prep Half Turn
    motor_controller.set_id(14)
    motor_controller.set_position(530)
    motor_controller.set_id(14)
    motor_controller.set_position(530)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    time.sleep(2)

    # 20 R4 Half-Turn | # R2 SIDE START POS
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    time.sleep(1.5)

    # R1 LEAD
    print("")
    print("")
    print("R1 LEAD")

    r1r2r3r4_optitrack_demo_01_r1r4()


def r1r2r3r4_optitrack_demo_01_slow():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)

    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)

    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(5)

    # 01 GO
    print("")
    print("GO")
    print("# 01 R1 Prep Step")
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(1)
    motor_controller.set_id(6)
    motor_controller.set_position(850)
    motor_controller.set_id(7)
    motor_controller.set_position(155)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(1)

    # 02 R1R2 Connect | #01 R4 Prep Connect 1
    print("")
    print("02 R1&R2 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    motor_controller.set_id(14)
    motor_controller.set_position(790)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(180)
    motor_controller.set_id(3)
    motor_controller.set_position(255)
    motor_controller.set_id(14)
    motor_controller.set_position(790)
    time.sleep(2)

    # 03 R1 Disconnect R1_M1 from mat  | #02 R4 Prep Connect 2
    print("")
    print("Disconnect R1_M1 from mat")
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(850)
    motor_controller.set_id(11)
    motor_controller.set_position(155)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2)
    motor_controller.set_id(1)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(850)
    motor_controller.set_id(11)
    motor_controller.set_position(155)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2)

    # 03 R1 Step | # 03 R4 Connects Up (Green)
    print("")
    print("03 R2&R3 Connect")
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    time.sleep(1.66)
    motor_controller.set_id(2)
    motor_controller.set_position(820)
    time.sleep(1.66)

    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(1)
    motor_controller.set_id(3)
    motor_controller.set_position(820)
    time.sleep(1)

    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(3)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(3)

    # 04 R2R3 Pre Elevator | # 04 R4 Disconnects (Yellow)
    print("")
    print("04 Prep Elevator")
    motor_controller.set_id(7)
    motor_controller.set_position(100)
    motor_controller.set_id(11)
    motor_controller.set_position(100)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(2)
    motor_controller.set_id(7)
    motor_controller.set_position(100)
    motor_controller.set_id(11)
    motor_controller.set_position(100)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(2)

    # 05 R2R3 Elevator UP | # 05 R4 Prep Turn
    print("")
    print("05 Elevator UP")
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    time.sleep(.2)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    time.sleep(.2)

    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(790)
    time.sleep(3.5)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(790)
    time.sleep(3.5)

    # 05 R1&R2 Disconnect | # 06 R4 Turn
    print("")
    print("05 R1&R2 Disconnect")
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(7)
    motor_controller.set_position(666)
    motor_controller.set_id(8)
    motor_controller.set_position(333)
    time.sleep(0.2)
    motor_controller.set_id(4)
    motor_controller.set_position(333)
    motor_controller.set_id(7)
    motor_controller.set_position(666)
    motor_controller.set_id(8)
    motor_controller.set_position(333)
    time.sleep(0.2)

    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(850)
    time.sleep(2)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(850)
    time.sleep(2)

    # 06 R1 Step into mat | # 07 R4 Connect Right (Yellow) | # 08 R4 Disconnect (Green)
    print("")
    print("07 R1 Step into mat")
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2.5)
    motor_controller.set_id(3)
    motor_controller.set_position(204)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(820)
    time.sleep(2.5)

    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2.5)
    motor_controller.set_id(2)
    motor_controller.set_position(204)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    time.sleep(2.5)

    # 08 R1&R3 Disconnect | # R2 SIDE START POS | # 09 R4 Prep Turn 1
    print("")
    print("08 R1&R3 Disconnect")
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_position(333)
    time.sleep(0.2)
    motor_controller.set_id(1)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_position(333)
    time.sleep(0.2)

    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(750)
    time.sleep(2)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(14)
    motor_controller.set_position(750)
    time.sleep(2)

    # 09 R1 UP | # R2 SIDE 01 | # 10 R4 Prep Turn 2
    print("")
    print("09 R1 UP")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(15)
    motor_controller.set_position(135)
    time.sleep(2)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(204)
    motor_controller.set_id(10)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(15)
    motor_controller.set_position(135)
    time.sleep(2)

    # R2 SIDE 02 | # 11 R4 Turn
    print("")
    print("")
    print("09 R2 & R4 Lead")
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(666)
    time.sleep(2)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(666)
    time.sleep(2)

    # R2 SIDE 03 | # 12 R4 Prep Connect
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(750)
    time.sleep(4)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(750)
    time.sleep(4)

    # R2 SIDE 04 | # 13 R4 Connect (Green Down)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(2)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(2)

    # R2 SIDE 05 | # 14 R4 Disconnect (Yellow Up)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(820)
    time.sleep(2)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(820)
    time.sleep(2)

    # R2 SIDE 06 | # R2 SIDE 07 | # 15 R4 Prep Catch
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(450)
    time.sleep(1)
    motor_controller.set_id(7)
    motor_controller.set_position(204)
    motor_controller.set_id(15)
    motor_controller.set_position(450)
    time.sleep(1)

    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    time.sleep(2)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(204)
    time.sleep(2)

    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(2)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(820)
    time.sleep(2)

    # R2 SIDE 08 | # 16 R4 Catch
    motor_controller.set_id(6)
    motor_controller.set_position(550)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(1)
    motor_controller.set_id(6)
    motor_controller.set_position(550)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    time.sleep(1)

    # R2 SIDE 09 | # 17 R4 UP
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(480)
    time.sleep(2)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(480)
    time.sleep(2)

    # 18 R4 Half-Turn
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    time.sleep(2)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    time.sleep(2)

    # 19 R4 Prep Half Turn
    motor_controller.set_id(14)
    motor_controller.set_position(530)
    time.sleep(2)
    motor_controller.set_id(14)
    motor_controller.set_position(530)
    time.sleep(2)

    # 20 R4 Half-Turn | # R2 SIDE START POS
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(1)
    motor_controller.set_id(5)
    motor_controller.set_position(204)
    motor_controller.set_id(6)
    motor_controller.set_position(512)
    motor_controller.set_id(7)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(204)
    motor_controller.set_id(13)
    motor_controller.set_position(204)
    time.sleep(1)

    motor_controller.set_id(14)
    motor_controller.set_position(512)
    time.sleep(2)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    time.sleep(2)

    # R1 LEAD
    print("")
    print("")
    print("R1 LEAD")

    r1r2r3r4_optitrack_demo_01_r1r4()


def r3m12_upright():
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(2)

    # Disconnect MA
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    time.sleep(1)

    # Tilt
    motor_controller.set_id(11)
    motor_controller.set_position(266)
    motor_controller.set_id(11)
    motor_controller.set_position(266)
    motor_controller.set_id(11)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate Up
    motor_controller.set_id(12)
    motor_controller.set_position(840)
    motor_controller.set_id(12)
    motor_controller.set_position(840)
    motor_controller.set_id(12)
    motor_controller.set_position(840)
    time.sleep(2)

    # Down
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    time.sleep(2)


def r3m9_up():
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(820)
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(820)
    time.sleep(2)

    # Disconnect MD
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(1)

    # Tilt
    motor_controller.set_id(10)
    motor_controller.set_position(266)
    motor_controller.set_id(10)
    motor_controller.set_position(266)
    motor_controller.set_id(10)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate Up
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    time.sleep(2)


def r3m12_up_left():
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(2)

    # Disconnect MA
    motor_controller.set_id(9)
    motor_controller.set_position(205)
    motor_controller.set_id(9)
    motor_controller.set_position(205)
    motor_controller.set_id(9)
    motor_controller.set_position(205)
    time.sleep(1)

    # Tilt
    motor_controller.set_id(11)
    motor_controller.set_position(266)
    motor_controller.set_id(11)
    motor_controller.set_position(266)
    motor_controller.set_id(11)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate Up
    motor_controller.set_id(12)
    motor_controller.set_position(190)
    motor_controller.set_id(12)
    motor_controller.set_position(190)
    motor_controller.set_id(12)
    motor_controller.set_position(190)
    time.sleep(2)

    # Down
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    time.sleep(2)


def r3m9_up_left():
    motor_controller.set_id(9)
    motor_controller.set_position(205)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(205)
    time.sleep(2)

    # Disconnect MD
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Tilt
    motor_controller.set_id(10)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate Up
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    time.sleep(2)


def r3m9_down_left():
    motor_controller.set_id(9)
    motor_controller.set_position(820)
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    motor_controller.set_id(11)
    motor_controller.set_position(205)
    motor_controller.set_id(12)
    motor_controller.set_position(205)
    time.sleep(2)

    # Disconnect MD
    motor_controller.set_id(12)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Tilt
    motor_controller.set_id(10)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate Up
    motor_controller.set_id(9)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(10)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m8_down_right():
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)

    # Disconnect MA
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # Rotate Up
    motor_controller.set_id(8)
    motor_controller.set_position(840)
    motor_controller.set_id(8)
    motor_controller.set_position(840)
    motor_controller.set_id(8)
    motor_controller.set_position(840)
    time.sleep(2)

    # Down
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m5_left_up():
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    time.sleep(0.5)

    # Disconnect MD
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # Rotate Up
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m8_down_left():
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Disconnect MA
    motor_controller.set_id(5)
    motor_controller.set_position(245)
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # Rotate Up
    motor_controller.set_id(8)
    motor_controller.set_position(190)
    motor_controller.set_id(8)
    motor_controller.set_position(190)
    motor_controller.set_id(8)
    motor_controller.set_position(190)
    time.sleep(2)

    # Down
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m5_right_up():
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    time.sleep(0.5)

    # Disconnect MD
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # Rotate Up
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m8_fun1():
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Disconnect MA
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(225)
    motor_controller.set_id(7)
    motor_controller.set_position(225)
    motor_controller.set_id(7)
    motor_controller.set_position(225)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # Rotate Up
    motor_controller.set_id(8)
    motor_controller.set_position(50)
    motor_controller.set_id(8)
    motor_controller.set_position(50)
    motor_controller.set_id(8)
    motor_controller.set_position(50)
    time.sleep(1)

    # Move
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    time.sleep(1)

    # Move
    motor_controller.set_id(5)
    motor_controller.set_position(888)
    motor_controller.set_id(5)
    motor_controller.set_position(888)
    motor_controller.set_id(5)
    motor_controller.set_position(888)
    time.sleep(2)

    # Move
    motor_controller.set_id(5)
    motor_controller.set_position(200)
    motor_controller.set_id(5)
    motor_controller.set_position(200)
    motor_controller.set_id(5)
    motor_controller.set_position(200)
    motor_controller.set_id(6)
    motor_controller.set_position(600)
    motor_controller.set_id(6)
    motor_controller.set_position(600)
    motor_controller.set_id(6)
    motor_controller.set_position(600)
    time.sleep(2)

    # Undo Move 1
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    time.sleep(2)

    # Undo Move 2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # Undo Rotate Up
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(4)

    # Undo Tilt (Down)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m5_up_right():
    # Starting Position
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Disconnect MD
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    time.sleep(0.5)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate
    motor_controller.set_id(5)
    motor_controller.set_position(220)
    motor_controller.set_id(5)
    motor_controller.set_position(220)
    motor_controller.set_id(5)
    motor_controller.set_position(220)
    time.sleep(2)

    # Down
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m8_left_down():
    # Starting Position
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    time.sleep(0.5)

    # Disconnect MA
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(215)
    motor_controller.set_id(7)
    motor_controller.set_position(215)
    motor_controller.set_id(7)
    motor_controller.set_position(215)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m8_fun2():
    # Starting Position
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Disconnect MA
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # Rotate Up
    motor_controller.set_id(8)
    motor_controller.set_position(1000)
    motor_controller.set_id(8)
    motor_controller.set_position(1000)
    motor_controller.set_id(6)
    motor_controller.set_position(700)
    motor_controller.set_id(8)
    motor_controller.set_position(1000)
    time.sleep(2.5)

    # Play
    motor_controller.set_id(6)
    motor_controller.set_position(300)
    time.sleep(1)
    motor_controller.set_id(6)
    motor_controller.set_position(400)
    motor_controller.set_id(5)
    motor_controller.set_position(100)
    motor_controller.set_id(8)
    motor_controller.set_position(800)
    time.sleep(0.5)
    motor_controller.set_id(6)
    motor_controller.set_position(300)
    motor_controller.set_id(8)
    motor_controller.set_position(1000)
    time.sleep(0.5)

    motor_controller.set_id(6)
    motor_controller.set_position(205)
    time.sleep(2)

    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(3)

    # Down
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)

    # Starting Position
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)


def r2m5_up_left():
    # Starting Position
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # Disconnect MD
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    time.sleep(0.5)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate
    motor_controller.set_id(5)
    motor_controller.set_position(805)
    motor_controller.set_id(5)
    motor_controller.set_position(805)
    motor_controller.set_id(5)
    motor_controller.set_position(805)
    time.sleep(2)

    # Down
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m8_right_down():
    # Starting Position
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    time.sleep(0.5)

    # Disconnect MA
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(220)
    motor_controller.set_id(7)
    motor_controller.set_position(220)
    motor_controller.set_id(7)
    motor_controller.set_position(220)
    time.sleep(2)

    # Tilt
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(2)

    # Rotate
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)

    # Down
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)


# R2R3R4 Combined Sequences for B-Pro DEMO
def r2m8_down_right_combined():
    # STARTING POSITION
    # R2
    motor_controller.set_id(5)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    # R3
    # R4
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    time.sleep(1)

    # DISCONNECT MA 1
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    # R3
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(700)
    time.sleep(0.5)
    # DISCONNECT MA 2
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    # R3
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(200)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(900)
    # R4
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(120)
    motor_controller.set_position(900)
    time.sleep(0.5)

    # ROTATE UP
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(840)
    motor_controller.set_id(8)
    motor_controller.set_position(840)
    motor_controller.set_id(8)
    motor_controller.set_position(840)
    # R3
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(366)
    # R4
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(100)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(100)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    time.sleep(2)


def r2m5_left_up_combined():
    # STARTING POS
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(820)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(200)
    motor_controller.set_position(100)
    time.sleep(0.5)

    # DISCONNECT MD
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(777)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(777)
    time.sleep(0.5)
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(120)
    motor_controller.set_position(800)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(120)
    motor_controller.set_position(100)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(295)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(295)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # ROTATE UP
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(800)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(900)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(150)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(100)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(1000)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(1000)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(2)


def r2m8_down_left_combined():
    # STARTING POS
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(0.5)

    # DISCONNECT MA
    # R2
    motor_controller.set_id(5)
    motor_controller.set_moving_speed(200)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_moving_speed(200)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_moving_speed(200)
    motor_controller.set_position(205)
    motor_controller.set_moving_speed(75)
    motor_controller.set_moving_speed(75)
    motor_controller.set_moving_speed(75)
    # R4
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(0.5)
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    motor_controller.set_id(7)
    motor_controller.set_position(235)
    # R3
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(850)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    # R4
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(900)
    time.sleep(0.5)

    # ROTATE UP
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(190)
    motor_controller.set_id(8)
    motor_controller.set_position(190)
    motor_controller.set_id(8)
    motor_controller.set_position(190)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(800)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    time.sleep(2)


def r2m5_right_up_combined():
    # STARTING POS
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    time.sleep(0.5)

    # DISCONNECT MD
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(0.5)
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    motor_controller.set_id(6)
    motor_controller.set_position(225)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(800)
    # R4
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(0.5)

    # ROTATE UP
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    # R4
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(900)
    time.sleep(2)


def r2m5_up_right_combined():
    # STARTING POSITION
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # DISCONNECT MD
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    time.sleep(0.5)
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(850)
    # R4
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(700)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    # R3
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    # ROTATE
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(220)
    motor_controller.set_id(5)
    motor_controller.set_position(220)
    motor_controller.set_id(5)
    motor_controller.set_position(220)
    # R3
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(900)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(100)
    time.sleep(2)


def r2m8_left_down_combined():
    # STARTING POSITION
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(205)
    time.sleep(0.5)

    # DISCONNECT MA
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(215)
    motor_controller.set_id(7)
    motor_controller.set_position(215)
    motor_controller.set_id(7)
    motor_controller.set_position(215)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(850)
    # R4
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    time.sleep(2)

    # ROTATE
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    # R4
    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    time.sleep(2)


def r2m8_fun1_combined():
    # START POSITION
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(0.5)

    # DISCONNECT MA
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    motor_controller.set_id(5)
    motor_controller.set_position(205)
    time.sleep(0.5)
    motor_controller.set_id(7)
    motor_controller.set_position(225)
    motor_controller.set_id(7)
    motor_controller.set_position(225)
    motor_controller.set_id(7)
    motor_controller.set_position(225)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    # TILT
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    motor_controller.set_id(7)
    motor_controller.set_position(266)
    time.sleep(0.5)

    # ROTATE UP
    motor_controller.set_id(8)
    motor_controller.set_position(50)
    motor_controller.set_id(8)
    motor_controller.set_position(50)
    motor_controller.set_id(8)
    motor_controller.set_position(50)
    time.sleep(1)

    # MOVE
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    motor_controller.set_id(6)
    motor_controller.set_position(666)
    # R3
    motor_controller.set_id(10)
    motor_controller.set_position(666)
    motor_controller.set_id(11)
    motor_controller.set_position(300)
    motor_controller.set_id(12)
    motor_controller.set_position(666)
    # R4
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(900)
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(900)
    time.sleep(1)

    # MOVE
    motor_controller.set_id(5)
    motor_controller.set_position(888)
    motor_controller.set_id(5)
    motor_controller.set_position(888)
    motor_controller.set_id(5)
    motor_controller.set_position(888)
    time.sleep(2)

    # MOVE
    motor_controller.set_id(5)
    motor_controller.set_position(200)
    motor_controller.set_id(5)
    motor_controller.set_position(200)
    motor_controller.set_id(5)
    motor_controller.set_position(200)
    motor_controller.set_id(6)
    motor_controller.set_position(600)
    motor_controller.set_id(6)
    motor_controller.set_position(600)
    motor_controller.set_id(6)
    motor_controller.set_position(600)
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(800)
    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(800)
    time.sleep(2)

    # UNDO MOVE 1
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(11)
    motor_controller.set_position(350)
    motor_controller.set_id(12)
    motor_controller.set_position(600)
    time.sleep(2)

    # UNDO MOVE 2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    time.sleep(2)

    # UNDO ROTATE UP
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    time.sleep(2)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    time.sleep(2)

    # UNDO TILT (DOWN)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    time.sleep(2)


def r2m5_up_left_combined():
    # STARTING POS
    # R2
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    time.sleep(0.5)

    # DISCONNECT MD
    # R2
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    motor_controller.set_id(8)
    motor_controller.set_position(820)
    time.sleep(0.5)
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    motor_controller.set_id(6)
    motor_controller.set_position(215)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(2)

    # TILT
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    motor_controller.set_id(6)
    motor_controller.set_position(266)
    # R3
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(528)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(614)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    # R4
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(2)

    # ROTATE
    motor_controller.set_id(5)
    motor_controller.set_position(805)
    motor_controller.set_id(5)
    motor_controller.set_position(805)
    motor_controller.set_id(5)
    motor_controller.set_position(805)
    time.sleep(2)

    # DOWN
    # R2
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    # R3
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(2)


def b_pro_arch_sequence_r2():
    # 00 STARTING POSITION
    print("")
    print("00 Starting Position")
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)

    time.sleep(8)

    # 01 STEP - DOWN RIGHT
    r2m8_down_right()

    # 02 STEP - LEFT UP
    r2m5_left_up()

    # 03 STEP - DOWN LEFT
    r2m8_down_left()

    # 04 STEP - RIGHT UP
    r2m5_right_up()

    # 05 STEP - DOWN LEFT
    r2m8_down_left()

    # 06 STEP - RIGHT UP
    r2m5_right_up()

    # 07 FUN 1
    r2m8_fun1()

    # 08 STEP - UP RIGHT
    r2m5_up_right()

    # 09 STEP - LEFT DOWN
    r2m8_left_down()

    # 10 STEP - UP RIGHT
    r2m5_up_right()

    # 11 STEP - LEFT DOWN
    r2m8_left_down()

    # 12 FUN 2
    r2m8_fun2()

    # 13 STEP - UP LEFT
    r2m5_up_left()

    # 14 STEP - RIGHT DOWN
    r2m8_right_down()


def b_pro_arch_sequence_r3():
    # 00 Starting Pos # Combined-1
    print("")
    print("00 Starting Position")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(795)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(278)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(880)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(213)
    time.sleep(4)

    # XX Next Move # Combined-123
    print("")
    print("XX Next Move")
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(700)
    time.sleep(0.5)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(200)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(900)
    time.sleep(0.5)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(120)
    motor_controller.set_position(900)
    time.sleep(2)

    # XX Next Move - Combined-123
    print("")
    print("XX Next Move")
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(366)
    time.sleep(0.5)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    time.sleep(0.5)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(200)
    motor_controller.set_position(100)
    time.sleep(2)

    # XX Next Move - Combined-1234
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(120)
    motor_controller.set_position(800)
    time.sleep(2)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(120)
    motor_controller.set_position(100)
    time.sleep(2)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(800)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(900)
    time.sleep(2)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(150)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(100)
    time.sleep(2)

    # XX Next Move - Combined-12
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(2)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(850)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(800)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(800)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(850)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(850)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(4)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    time.sleep(4)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(4)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(4)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(850)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(2)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(528)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(614)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(4)

    # XX Next Move - Combined-1
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(1)

    # XX Next Move
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(515)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(850)
    time.sleep(2)

    # XX Next Move
    print("")
    print("XX Next Move")
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(400)
    time.sleep(3)

    # XX Next Move
    print("")
    print("XX Next Move")
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(528)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    time.sleep(1)


def b_pro_arch_sequence_r4():
    # 00 Starting Pos - Combined 1
    print("")
    print("00 Starting Position")
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined 1
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(0)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(0)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(3)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(777)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(333)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(777)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(295)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(295)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(1000)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(1000)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(666)
    time.sleep(3)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(1000)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    time.sleep(2)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(900)
    time.sleep(2)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(700)
    time.sleep(6)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(100)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(1000)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(000)
    time.sleep(3)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(342)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(490)
    time.sleep(2)

    motor_controller.set_id(20)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(600)
    time.sleep(2)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(500)
    time.sleep(0.5)

    motor_controller.set_id(18)
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(1000)
    time.sleep(2)

    motor_controller.set_id(18)  # Combined
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(900)
    time.sleep(0.5)

    motor_controller.set_id(18)
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(1000)
    time.sleep(0.5)

    motor_controller.set_id(18)
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(900)
    time.sleep(0.5)

    motor_controller.set_id(18)
    motor_controller.set_moving_speed(150)
    motor_controller.set_position(1000)
    time.sleep(0.5)

    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    motor_controller.set_id(20)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(512)
    motor_controller.set_id(18)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(820)
    time.sleep(2)


# Full B-Pro Arch Sequence
def b_pro_arch_sequence():
    # 00 STARTING POSITION
    print("")
    print("00 Starting Position")
    motor_controller.set_id(5)
    motor_controller.set_position(512)
    motor_controller.set_id(6)
    motor_controller.set_position(205)
    motor_controller.set_id(7)
    motor_controller.set_position(205)
    motor_controller.set_id(8)
    motor_controller.set_position(512)
    motor_controller.set_id(9)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(795)
    motor_controller.set_id(10)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(278)
    motor_controller.set_id(11)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(880)
    motor_controller.set_id(12)
    motor_controller.set_moving_speed(75)
    motor_controller.set_position(213)

    time.sleep(8)

    # 01 R2 STEP - DOWN RIGHT
    r2m8_down_right_combined()

    # 02 R2 STEP - LEFT UP
    r2m5_left_up_combined()

    # 03 R2 STEP - DOWN LEFT
    r2m8_down_left_combined()

    # 04 R2 STEP - RIGHT UP
    r2m5_right_up_combined()

    # 05 R2 STEP - DOWN LEFT
    r2m8_down_left_combined()

    # 06 R2 STEP - RIGHT UP
    r2m5_right_up_combined()

    # 07 R2 FUN 1
    r2m8_fun1_combined()

    # 08 R2 STEP - UP RIGHT
    r2m5_up_right_combined()

    # 09 R2 STEP - LEFT DOWN
    r2m8_left_down_combined()

    # 10 R2 STEP - UP RIGHT
    r2m5_up_right_combined()

    # 11 R2 STEP - LEFT DOWN
    r2m8_left_down_combined()

    # 12 R2 FUN 2
    r2m8_fun2()

    # 13 R2STEP - UP LEFT
    r2m5_up_left_combined()

    # 14 R2 STEP - RIGHT DOWN
    r2m8_right_down()


# Correct Table Sequence
def b_pro_table_sequence():
    # 00 Starting Position
    print("")
    print("00 Starting Position")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(4)

    # 01 R1 Step
    print("")
    print("01 R1 Step")
    r1m4_y_plus_1()

    # xx R2 Prep Place
    print("")
    print("xx R2 Place Position")
    motor_controller.set_id(16)
    motor_controller.set_position(821)
    motor_controller.set_id(16)
    motor_controller.set_position(821)
    motor_controller.set_id(16)
    motor_controller.set_position(821)

    time.sleep(2)

    # xx R2 Place Position
    print("")
    print("xx R2 Place Position")
    motor_controller.set_id(13)
    motor_controller.set_position(504)
    motor_controller.set_id(14)
    motor_controller.set_position(492)
    motor_controller.set_id(15)
    motor_controller.set_position(825)
    motor_controller.set_id(16)
    motor_controller.set_position(821)
    motor_controller.set_id(13)
    motor_controller.set_position(504)
    motor_controller.set_id(14)
    motor_controller.set_position(492)
    motor_controller.set_id(15)
    motor_controller.set_position(825)
    motor_controller.set_id(16)
    motor_controller.set_position(821)

    time.sleep(4)

    # xx R2 Prep Up
    print("")
    print("xx R2 Place Position")
    motor_controller.set_id(13)
    motor_controller.set_position(504)
    motor_controller.set_id(14)
    motor_controller.set_position(400)
    motor_controller.set_id(15)
    motor_controller.set_position(825)
    motor_controller.set_id(16)
    motor_controller.set_position(821)
    motor_controller.set_id(13)
    motor_controller.set_position(504)
    motor_controller.set_id(14)
    motor_controller.set_position(400)
    motor_controller.set_id(15)
    motor_controller.set_position(825)
    motor_controller.set_id(16)
    motor_controller.set_position(821)

    time.sleep(1)

    # xx R2 Up
    print("")
    print("xx R2 Place Position")
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(400)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)
    motor_controller.set_id(13)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(400)
    motor_controller.set_id(15)
    motor_controller.set_position(512)
    motor_controller.set_id(16)
    motor_controller.set_position(512)

    time.sleep(2)

    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)
    motor_controller.set_id(14)
    motor_controller.set_position(512)

    time.sleep(2)

    # 02 R1 & R2 Prep Pass
    print("")
    print("02 R1 & R2 Prep Pass")
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(700)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(700)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)
    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)

    time.sleep(4)

    # 03 R1 & R2 Pass
    print("")
    print("03 R1 & R2 Pass")
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(516)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(516)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)
    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)
    time.sleep(2)

    # 04 R2 Separate
    print("")
    print("04 R2 Separate")
    motor_controller.set_id(16)
    motor_controller.set_position(820)
    motor_controller.set_id(16)
    motor_controller.set_position(820)
    motor_controller.set_id(16)
    motor_controller.set_position(820)
    time.sleep(1)
    motor_controller.set_id(14)
    motor_controller.set_position(600)
    motor_controller.set_id(14)
    motor_controller.set_position(600)
    motor_controller.set_id(14)
    motor_controller.set_position(600)
    time.sleep(1)

    # 05 R1 Rest
    print("")
    print("05 R1 Rest")
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    # 08 R4 Step in X
    print("")
    print("08 R4 Step in X")
    r4m13_x_minus_1()

    # 07 R1 Why not Move
    print("")
    print("07 R1 Why Not Move")
    motor_controller.set_id(1)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)
    motor_controller.set_id(1)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(512)
    motor_controller.set_id(3)
    motor_controller.set_position(512)
    motor_controller.set_id(4)
    motor_controller.set_position(512)

    # 06 R4 Step in Y
    print("")
    print("06 R4 Step in Y")
    r4m16_y_minus_1()

    # 09 R1 Why not Move 2
    print("")
    print("09 R1 Why Not Move 2")
    motor_controller.set_id(1)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    # 10 R1R4 Why not Move 3
    print("")
    print("R1R4 Why not Move 3")
    motor_controller.set_id(1)
    motor_controller.set_position(512)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    motor_controller.set_id(13)
    motor_controller.set_position(612)
    motor_controller.set_id(14)
    motor_controller.set_position(612)
    motor_controller.set_id(15)
    motor_controller.set_position(412)
    motor_controller.set_id(16)
    motor_controller.set_position(412)

    time.sleep(1)

    motor_controller.set_id(13)
    motor_controller.set_position(412)
    motor_controller.set_id(14)
    motor_controller.set_position(412)
    motor_controller.set_id(15)
    motor_controller.set_position(612)
    motor_controller.set_id(16)
    motor_controller.set_position(612)

    time.sleep(2)

    # xx R4 Back in Y
    print("")
    print("xx R4 Back in Y")
    r4m13_y_plus_1()

    # 09 R1 Why not Move 2
    print("")
    print("09 R1 Why Not Move 2")
    motor_controller.set_id(1)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(820)
    motor_controller.set_id(2)
    motor_controller.set_position(560)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    # xx R4 Back in X
    print("")
    print("xx R4 Back in Y")
    r4m16_x_plus_1()

    # 02 R1 & R2 Prep Pass
    print("")
    print("02 R1 & R2 Prep Pass")
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(700)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(700)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)
    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)

    time.sleep(4)

    # 03 R1 & R2 Pass
    print("")
    print("03 R1 & R2 Pass")
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(516)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)
    motor_controller.set_id(1)
    motor_controller.set_position(382)
    motor_controller.set_id(2)
    motor_controller.set_position(516)
    motor_controller.set_id(3)
    motor_controller.set_position(295)
    motor_controller.set_id(4)
    motor_controller.set_position(502)

    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)
    motor_controller.set_id(13)
    motor_controller.set_position(362)
    motor_controller.set_id(14)
    motor_controller.set_position(520)
    motor_controller.set_id(15)
    motor_controller.set_position(252)
    motor_controller.set_id(16)
    motor_controller.set_position(530)
    time.sleep(2)

    # 02 Prep Out
    print("")
    print("02 R1 & R2 Prep Pass")
    motor_controller.set_id(1)
    motor_controller.set_position(353)
    motor_controller.set_id(2)
    motor_controller.set_position(363)
    motor_controller.set_id(3)
    motor_controller.set_position(444)
    motor_controller.set_id(4)
    motor_controller.set_position(509)

    motor_controller.set_id(13)
    motor_controller.set_position(326)
    motor_controller.set_id(14)
    motor_controller.set_position(642)
    motor_controller.set_id(15)
    motor_controller.set_position(107)
    motor_controller.set_id(16)
    motor_controller.set_position(522)

    time.sleep(4)

    # 02 Prep Out 2
    print("")
    print("02 R1 & R2 Prep Pass")
    motor_controller.set_id(1)
    motor_controller.set_position(385)
    motor_controller.set_id(2)
    motor_controller.set_position(371)
    motor_controller.set_id(3)
    motor_controller.set_position(422)
    motor_controller.set_id(4)
    motor_controller.set_position(377)

    motor_controller.set_id(13)
    motor_controller.set_position(308)
    motor_controller.set_id(14)
    motor_controller.set_position(632)
    motor_controller.set_id(15)
    motor_controller.set_position(114)
    motor_controller.set_id(16)
    motor_controller.set_position(623)

    time.sleep(4)

    # 03 Separate
    print("")
    print("03 R1 & R2 Pass")
    motor_controller.set_id(4)
    motor_controller.set_position(205)
    motor_controller.set_id(4)
    motor_controller.set_position(205)
    motor_controller.set_id(4)
    motor_controller.set_position(205)
    time.sleep(0.5)
    motor_controller.set_id(2)
    motor_controller.set_position(666)
    motor_controller.set_id(2)
    motor_controller.set_position(666)
    motor_controller.set_id(2)
    motor_controller.set_position(666)
    time.sleep(2)

    # XX R1 Step
    print("")
    print("03 R1 & R2 Pass")
    r1m1_y_minus_1()
