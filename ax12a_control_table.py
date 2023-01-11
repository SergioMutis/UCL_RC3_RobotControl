"""AX12A CONTROL TABLE
# This table is part of the Dynamixel Framework for their AX-12A servo motors.
# It provides each function with an address (represented by a number) within each motor.
# Within the scope of UCL RC3's robotics module, this file should never be edited."""

# BASELINE ADDRESSES
ADDR_AX_MODEL_NUMBER_L = 0
ADDR_AX_MODEL_NUMBER_H = 1
ADDR_AX_VERSION = 2
ADDR_AX_ID = 3
ADDR_AX_BAUD_RATE = 4
ADDR_AX_RETURN_DELAY_TIME = 5
ADDR_AX_CW_ANGLE_LIMIT_L = 6
ADDR_AX_CW_ANGLE_LIMIT_H = 7
ADDR_AX_CCW_ANGLE_LIMIT_L = 8
ADDR_AX_CCW_ANGLE_LIMIT_H = 9
ADDR_AX_SYSTEM_DATA2 = 10
ADDR_AX_LIMIT_TEMPERATURE = 11
ADDR_AX_DOWN_LIMIT_VOLTAGE = 12
ADDR_AX_UP_LIMIT_VOLTAGE = 13
ADDR_AX_MAX_TORQUE_L = 14
ADDR_AX_MAX_TORQUE_H = 15
ADDR_AX_RETURN_LEVEL = 16
ADDR_AX_ALARM_LED = 17
ADDR_AX_ALARM_SHUTDOWN = 18
ADDR_AX_OPERATING_MODE = 19
ADDR_AX_DOWN_CALIBRATION_L = 20
ADDR_AX_DOWN_CALIBRATION_H = 21
ADDR_AX_UP_CALIBRATION_L = 22
ADDR_AX_UP_CALIBRATION_H = 23

# RAM REGISTER ADDRESSES (they reset after shut down)
ADDR_AX_TORQUE_ENABLE = 24
ADDR_AX_LED = 25
ADDR_AX_CW_COMPLIANCE_MARGIN = 26
ADDR_AX_CCW_COMPLIANCE_MARGIN = 27
ADDR_AX_CW_COMPLIANCE_SLOPE = 28
ADDR_AX_CCW_COMPLIANCE_SLOPE = 29
ADDR_AX_GOAL_POSITION_L = 30
ADDR_AX_GOAL_POSITION_H = 31
ADDR_AX_GOAL_SPEED_L = 32
ADDR_AX_GOAL_SPEED_H = 33
ADDR_AX_TORQUE_LIMIT_L = 34
ADDR_AX_TORQUE_LIMIT_H = 35
ADDR_AX_PRESENT_POSITION_L = 36
ADDR_AX_PRESENT_POSITION_H = 37
ADDR_AX_PRESENT_SPEED_L = 38
ADDR_AX_PRESENT_SPEED_H = 39
ADDR_AX_PRESENT_LOAD_L = 40
ADDR_AX_PRESENT_LOAD_H = 41
ADDR_AX_PRESENT_VOLTAGE = 42
ADDR_AX_PRESENT_TEMPERATURE = 43
ADDR_AX_REGISTERED_INSTRUCTION = 44
ADDR_AX_PAUSE_TIME = 45
ADDR_AX_MOVING = 46
ADDR_AX_LOCK = 47
ADDR_AX_PUNCH_L = 48
ADDR_AX_PUNCH_H = 49

# USER DEFINED
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0