"""USB ROBOT CONTROL SCRIPT | DH
# Developed for the Diffusive Habitats (DH) Project, UCL Bartlett School of Architecture RC3 by Sergio Mutis.
# More info at https://bpro2022.bartlettarchucl.com/rc3-living-architecture-lab-22/diffusive-habitats
# Employs the Dynamixel (DXL) framework (as the robots are actuated by AX-12A Dynamixel servos).
# This script is used to control the DH robots when directly connected via USB to a computer."""


# Importing Code from External Libraries
from dxl_ax12a import AX12a
import DH_project_specific_methods
# from dynamixel_sdk import *
# import multiprocessing
# import time

# Connecting to Default COM Port (the USB port connected to the robots)
DEVICENAME = 'com3'

# Initializing Motors
motor_count = 4
connected_motors = [i for i in range(motor_count)]
motor_controller = AX12a(DEVICENAME)


def main():
    # 0 TITLE
    print("\nDIFFUSIVE HABITATS: PROTOTYPE TESTING\n")

    # 1 STARTING POSITION
    # enable torque and set starting speed for all motors
    for x in range(1, motor_count):
        motor_controller.set_id(x)
        motor_controller.set_wheel_mode(2)
        motor_controller.enable_torque()
        motor_controller.set_moving_speed(75)

    # 2 ACTION
    DH_project_specific_methods.robot1_ready_mode()
    DH_project_specific_methods.open_navigation_robot1()


main()

print("\nBye\n")
AX12a.close_port()
