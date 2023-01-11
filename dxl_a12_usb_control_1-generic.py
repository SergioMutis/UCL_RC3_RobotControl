"""USB ROBOT CONTROL SCRIPT | Generic
# Developed by UCL Bartlett School of Architecture RC3 by Ziming He and Sergio Mutis.
# Each RC3 team should take this script, edit it, and expand it to serve their project
# This script controls AX-12A Dynamixel servos motors when directly connected via USB to a computer."""


# Importing Code from External Libraries
from dxl_ax12a import AX12a

# Connecting to Default COM Port (the USB port connected to the robots)
DEVICENAME = 'com3'  # Default COM Port

# Initializing Motors
motor_count = 9
connected_motors = [i for i in range(motor_count)]
motor_controller = AX12a(DEVICENAME)
time_delay = 2

# Function Mode Names
modes_pattern = ("none", "write_pos", "wheel_mode", "write_speed", "read_position", "read_load", "rotation_loop\n")


# Check to see if user wants to continue
def user_input():
    ans = input('Continue? : y/n ')
    if ans == 'n':
        return False
    else:
        return True


# Execute a function depending on mode id selection
def execute(mode, _id):
    motor_controller.set_id(_id)

    # 0 none
    if mode == modes_pattern[0]:
        return

    # BASELINE METHODS
    # 1 write_pos
    elif mode == modes_pattern[1]:
        motor_controller.enable_torque()
        value = int(input("Input a target position (0-1023) : "))
        motor_controller.set_position(value)

    # 2 wheel_mode
    elif mode == modes_pattern[2]:
        motor_controller.enable_torque()
        value = int(input("Input [0] False, [1] True : "))
        motor_controller.set_wheel_mode(value)

    # 3 write_speed
    elif mode == modes_pattern[3]:
        motor_controller.enable_torque()
        value = int(input("Input a target speed (CCW > 0-1024,CW > 1024-2047) : "))
        motor_controller.set_moving_speed(value)

    # 4 read_position
    elif mode == modes_pattern[4]:
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()
        motor_controller.set_wheel_mode(1)
        import time
        time.sleep(0.75)  # Delays for .75 seconds.
        for i in range(10):
            motor_controller.get_position()
            time.sleep(0.75)  # Delays for .75 seconds.

    # 5 read_load
    elif mode == modes_pattern[5]:
        motor_controller.set_moving_speed(0)
        motor_controller.enable_torque()
        motor_controller.set_wheel_mode(1)
        import time
        time.sleep(0.75)  # Delays for .75 seconds.
        for i in range(10):
            motor_controller.get_load()
            time.sleep(0.75)  # Delays for .75 seconds.

    # 6 rotation_loop
    elif mode == modes_pattern[6]:
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


# ORIGINAL MAIN FUNCTION
def listening():
    is_listening = True
    while is_listening:

        prompt = "[0]%s [1]%s [2]%s [3]%s [4]%s [5]%s [6]%s:" % modes_pattern
        ptn_id = int(input(prompt))
        m_cmd = modes_pattern[ptn_id]

        import time
        time.sleep(time_delay)

        if ptn_id < 7:
            input_string = ""
            for _id in connected_motors:
                input_string += "[{}] servo_ID_{} ".format(_id, _id)

            input_string += ":"
            m_id = int(input(input_string))
            execute(m_cmd, m_id)
            is_listening = user_input()

        else:
            m_id = 0
            execute(m_cmd, m_id)

    else:
        quit()


# Detect obstacles with current load parameters
def listen_load_change(motor_object):
    motor_object.set_wheel_mode(1)
    motor_object.set_moving_speed(50)

    is_listening = True
    while is_listening:
        load = motor_object.get_load()
        print("current load is %s" % load)
        if 200 > load > 100:
            motor_object.set_moving_speed(load)
        elif 1500 > load > 1300:
            motor_object.set_moving_speed(load)


listening()

AX12a.close_port()
