"""SERVO CONTROL PIPELINE PROTOCOL
# Unity >> Raspberry Pi >> Dynamixel servo control pipeline via udp protocol extended and refactored based on
principals of code developed by Justin Moon with Valentina Soana and Research Cluster 3 Bartlett UCL (
https://unitylist.com/p/spm/DXL-AX-12-A ) """

from dynamixel_sdk import *
from ax12a_control_table import *

from dynamixel_sdk import GroupSyncRead
from dynamixel_sdk import GroupSyncWrite


# basic class for ax12a control
class AX12a:
    PROTOCOL_VERSION = 1.0
    BAUDRATE = 1000000  # Dynamixel default baudrate
    DEVICENAME = 'com3'  # Default COM Port

    portHandler = None
    packetHandler = None

    DXL_IDS = []

    INITIAL_POSITIONS = []
    INITIAL_SPEEDS = []

    PRESENT_POSITIONS = []
    PREV_GOAL_POSITIONS = []
    MIN_POS_VAL = 0
    MAX_POS_VAL = 1023

    MOVING_SPEED = 200

    bulk_position_read = None
    group_torque_enable_write = None
    group_speed_write = None
    group_position_write = None
    group_cw_compliance_slope_write = None
    group_ccw_compliance_slope_write = None

    @classmethod
    def init(cls, devicename, baudrate=1000000):
        cls.portHandler = PortHandler(devicename)
        cls.packetHandler = PacketHandler(cls.PROTOCOL_VERSION)
        cls.open_port()
        cls.baudrate = baudrate
        cls.set_baudrate()

    @classmethod
    def open_port(cls):
        if cls.portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            quit()

    @classmethod
    def set_baudrate(cls):
        if cls.portHandler.setBaudRate(cls.BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            quit()

    @classmethod
    def close_port(cls):
        cls.portHandler.closePort()
        print('Successfully closed port')

    def __init__(self, devicename):
        # Initialize porthandler, packethandler
        AX12a.init(devicename)

    def set_initial_state(self, dxl_ids, moving_speeds, initial_positions):

        # Initialize group control instances
        self.group_torque_enable_write = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_AX_TORQUE_ENABLE, 1)
        self.group_speed_write = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_AX_GOAL_SPEED_L, 2)
        self.group_position_write = GroupSyncWrite(self.portHandler, self.packetHandler, ADDR_AX_GOAL_POSITION_L, 2)
        self.group_cw_compliance_slope_write = GroupSyncWrite(self.portHandler, self.packetHandler,
                                                              ADDR_AX_CW_COMPLIANCE_SLOPE, 1)
        self.group_ccw_compliance_slope_write = GroupSyncWrite(self.portHandler, self.packetHandler,
                                                               ADDR_AX_CCW_COMPLIANCE_SLOPE, 1)

        # Set motors to initial state

        self.INITIAL_POSITIONS = initial_positions
        self.PRESENT_POSITIONS = [int(str_pos) for str_pos in initial_positions]
        self.update_present_positions()
        self.PREV_GOAL_POSITIONS = [int(str_pos) for str_pos in initial_positions]
        self.DXL_IDS = [int(str_id) for str_id in dxl_ids]
        self.initial_enable_torque_group()
        self.INITIAL_SPEEDS = [int(speed) for speed in moving_speeds]
        self.initial_speed_group(self.INITIAL_SPEEDS)
        positions = [int(pos) for pos in initial_positions]
        self.initial_position_group(positions)
        self.initial_compliance_slope_group(64)

    def set_id(self, motor_id):
        self.id = motor_id

    def set_register1(self, reg_num, reg_value):
        dxl_comm_result, dxl_error = AX12a.packetHandler.write1ByteTxRx(
            AX12a.portHandler, self.id, reg_num, reg_value)
        AX12a.check_error(dxl_comm_result, dxl_error)

    def set_register2(self, reg_num, reg_value):
        dxl_comm_result, dxl_error = AX12a.packetHandler.write2ByteTxRx(
            AX12a.portHandler, self.id, reg_num, reg_value)
        AX12a.check_error(dxl_comm_result, dxl_error)

    def get_register1(self, reg_num):
        reg_data, dxl_comm_result, dxl_error = AX12a.packetHandler.read1ByteTxRx(
            AX12a.portHandler, self.id, reg_num)
        AX12a.check_error(dxl_comm_result, dxl_error)
        return reg_data

    def get_register2(self, reg_num_low):
        reg_data, dxl_comm_result, dxl_error = AX12a.packetHandler.read2ByteTxRx(
            AX12a.portHandler, self.id, reg_num_low)
        AX12a.check_error(dxl_comm_result, dxl_error)
        return reg_data

    def get_register2_ID(self, reg_num_low, index):
        reg_data, dxl_comm_result, dxl_error = AX12a.packetHandler.read2ByteTxRx(
            AX12a.portHandler, index, reg_num_low)
        AX12a.check_error(dxl_comm_result, dxl_error)
        return reg_data

    def set_wheel_mode(self, enabled):

        limit_cw = self.MIN_POS_VAL
        limit_ccw = self.MAX_POS_VAL

        if enabled == 1:
            limit_cw = 0
            limit_ccw = 0
        self.set_register2(ADDR_AX_CW_ANGLE_LIMIT_L, limit_cw)
        self.set_register2(ADDR_AX_CCW_ANGLE_LIMIT_L, limit_ccw)

    def enable_torque(self):
        """Enable torque for motor."""
        self.set_register1(ADDR_AX_TORQUE_ENABLE, TORQUE_ENABLE)
        print(self.get_register1(ADDR_AX_TORQUE_ENABLE))
        # print("Torque has been successfully enabled for dxl ID: %d" % self.id)

    def initial_compliance_slope_group(self, data_value):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            self.group_cw_compliance_slope_write.addParam(dxl_id, [data_value])
            self.group_ccw_compliance_slope_write.addParam(dxl_id, [data_value])

        COMM_RESULT_CW = self.group_cw_compliance_slope_write.txPacket()
        COMM_RESULT_CCW = self.group_ccw_compliance_slope_write.txPacket()
        print(self.packetHandler.getTxRxResult(COMM_RESULT_CW))
        print(self.packetHandler.getTxRxResult(COMM_RESULT_CCW))

    def set_compliance_slope_group(self, data_value):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            self.group_cw_compliance_slope_write.changeParam(dxl_id, [data_value])
            self.group_ccw_compliance_slope_write.changeParam(dxl_id, [data_value])

        COMM_RESULT_CW = self.group_cw_compliance_slope_write.txPacket()
        COMM_RESULT_CCW = self.group_cw_compliance_slope_write.txPacket()
        print(self.packetHandler.getTxRxResult(COMM_RESULT_CW))
        print(self.packetHandler.getTxRxResult(COMM_RESULT_CCW))

    def initial_enable_torque_group(self):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            self.group_torque_enable_write.addParam(dxl_id, [TORQUE_ENABLE])

        COM_RESULT = self.group_torque_enable_write.txPacket()
        print(self.packetHandler.getTxRxResult(COM_RESULT))

    def enable_torque_group(self):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            self.group_torque_enable_write.changeParam(dxl_id, [TORQUE_ENABLE])

        COM_RESULT = self.group_torque_enable_write.txPacket()
        print(self.packetHandler.getTxRxResult(COM_RESULT))

    def disable_torque_group(self):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            self.group_torque_enable_write.changeParam(dxl_id, [TORQUE_DISABLE])

        COM_RESULT = self.group_torque_enable_write.txPacket()
        print(self.packetHandler.getTxRxResult(COM_RESULT))

    def disable_torque(self):
        """Disable torque."""
        self.set_register1(ADDR_AX_TORQUE_ENABLE, TORQUE_DISABLE)
        print(self.get_register1(ADDR_AX_TORQUE_ENABLE))
        # print("Torque has been successfully disabled for dxl ID: %d" % self.id)

    def set_position(self, dxl_goal_position):
        """Write goal position."""
        self.set_register2(ADDR_AX_GOAL_POSITION_L, dxl_goal_position)
        print("Position of dxl ID: %d set to %d " %
              (self.id, dxl_goal_position))

    def initial_position_group(self, positions):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            position = int(positions[i])
            self.group_position_write.addParam(dxl_id, [DXL_LOBYTE(position), DXL_HIBYTE(position)])
        self.set_position_group(positions, 10)

    def position_close_enough(self, pos_a, pos_b, threshold=2):
        return abs(pos_a - pos_b) <= threshold

    def update_present_positions(self):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            self.PRESENT_POSITIONS[i] = self.get_position_ID(dxl_id)

    def set_position_group(self, positions, iterations=1.0):
        self.update_present_positions()
        delta_positions = [int(positions[IDX]) - self.PRESENT_POSITIONS[IDX] for IDX in range(len(self.DXL_IDS))]
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            position = int(positions[i])
            speed = int(abs(delta_positions[i]))+1
            self.group_position_write.changeParam(dxl_id, [DXL_LOBYTE(position), DXL_HIBYTE(position)])
            self.group_speed_write.changeParam(dxl_id, [DXL_LOBYTE(speed), DXL_HIBYTE(speed)])
            self.PREV_GOAL_POSITIONS[i] = position
            print("SPEED OF ID %3d IS %3d"%(dxl_id,speed))

        COMM_RESULT_POS = self.group_position_write.txPacket()
        COMM_RESULT_SPD = self.group_speed_write.txPacket()

        print("POSITION SET RESULT :" + self.packetHandler.getTxRxResult(COMM_RESULT_POS))
        print("SPEED SET RESULT :" + self.packetHandler.getTxRxResult(COMM_RESULT_SPD))

    def set_moving_speed(self, dxl_goal_speed):
        """Set the moving speed to goal position [0-1023]."""
        self.set_register2(ADDR_AX_GOAL_SPEED_L, dxl_goal_speed)
        print("Moving speed of dxl ID: %d set to %d " %
              (self.id, dxl_goal_speed))

    def set_speed_group(self, speeds):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            speed = int(speeds[i])
            self.group_speed_write.changeParam(dxl_id, [DXL_LOBYTE(speed), DXL_HIBYTE(speed)])

        COM_RESULT = self.group_speed_write.txPacket()
        print(self.packetHandler.getTxRxResult(COM_RESULT))

    def initial_speed_group(self, speeds):
        for i in range(len(self.DXL_IDS)):
            dxl_id = self.DXL_IDS[i]
            speed = int(speeds[i])
            self.group_speed_write.addParam(dxl_id, [DXL_LOBYTE(speed), DXL_HIBYTE(speed)])

        COMM_RESULT = self.group_speed_write.txPacket()
        print(self.packetHandler.getTxRxResult(COMM_RESULT))

    def get_position(self):
        """Read present position."""
        dxl_present_position = self.get_register2(ADDR_AX_PRESENT_POSITION_L)
        print("ID:%03d  PresPos:%03d" % (self.id, dxl_present_position))
        return dxl_present_position

    def get_position_ID(self, index):
        """Read present position."""
        dxl_present_position = self.get_register2_ID(ADDR_AX_PRESENT_POSITION_L, index)
        print("ID:%03d  PresPos:%03d" % (index, dxl_present_position))
        return dxl_present_position

    def get_present_speed(self):
        """Returns the current speed of the motor."""
        present_speed = self.get_register2(ADDR_AX_PRESENT_SPEED_L)
        return present_speed

    def get_moving_speed(self):
        """Returns moving speed to goal position [0-1023]."""
        moving_speed = self.get_register2(ADDR_AX_GOAL_SPEED_L)
        return moving_speed

    def led_on(self):
        """Turn on Motor Led."""
        self.set_register1(ADDR_AX_LED, True)

    def led_off(self):
        """Turn off Motor Led."""
        self.set_register1(ADDR_AX_LED, False)

    def get_load(self):
        """Returns current load on motor."""
        dxl_load = self.get_register2(ADDR_AX_PRESENT_LOAD_L)
        # CCW 0-1023 # CW 1024-2047
        print("ID:%03d  PresLoad:%03d" % (self.id, dxl_load))
        return dxl_load

    def get_temperature(self):
        """Returns internal temperature in units of Celsius."""
        dxl_temperature = self.get_register2(ADDR_AX_PRESENT_TEMPERATURE)
        return dxl_temperature

    def get_voltage(self):
        """Returns current voltage supplied to Motor in units of Volts."""
        dxl_voltage = (self.get_register1(ADDR_AX_PRESENT_VOLTAGE)) / 10
        return dxl_voltage

    def set_torque_limit(self, torque_limit):
        """Sets Torque Limit of Motor."""
        self.set_register2(ADDR_AX_TORQUE_LIMIT_L, torque_limit)

    def get_torque_limit(self):
        """Returns current Torque Limit of Motor."""
        dxl_torque_limit = self.get_register2(ADDR_AX_TORQUE_LIMIT_L)
        return dxl_torque_limit

    def is_moving(self):
        """Checks to see if motor is still moving to goal position."""
        dxl_motion = self.get_register1(ADDR_AX_MOVING)
        return dxl_motion

    @staticmethod
    def check_error(comm_result, dxl_err):
        if comm_result != COMM_SUCCESS:
            print("%s" % AX12a.packetHandler.getTxRxResult(comm_result))
        elif dxl_err != 0:
            print("%s" % AX12a.packetHandler.getRxPacketError(dxl_err))


def lerp(a, b, t):
    return a + (b - a) * t


def smooth_inout(a, t, N):
    return (N / 2 - (abs(a - N / 2) ** 2) / (N / 2) * t) / (N / 2)
