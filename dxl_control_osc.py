"""DXL CONTROL OSC
# This script is part of the Dynamixel Framework adapted for UCL Bartlett RC3's robotics module.
# Within the scope of the robotics module, this file should never be edited."""


from dxl_ax12a import AX12a
from ax12a_control_table import *
from my_osc_client import OSC_CLIENT
from osc_command_patterns import *


# integrate dxl controller with osc client with the ip address that it sends the feedbacks towards
class DXL_OSC:
    motor_controller = None
    client = None
    started = False


    def start_client_controller(self, ip, port, devicename):
        self.client = OSC_CLIENT(ip, int(port))
        self.motor_controller = AX12a(devicename)


    def start_osc(self, ip, port, devicename, dxl_ids, moving_speed, initial_positions):
        self.start_client_controller(ip, port, devicename)
        self.motor_controller.set_initial_state(dxl_ids, moving_speed, initial_positions)
        self.started = True

    def is_started(self):
        return self.started
dxl_osc_ctrl = DXL_OSC()
started = 0


# functional methods
def split_msg(msg, splitter="#"):
    msg_split = msg.split(splitter)
    return msg_split


def start_osc(pattern, start_infos):
    network_info, dxl_ids, moving_speeds, initial_positions = split_msg(start_infos, "#")
    ip, port, devicename = split_msg(network_info, "$")
    m_dxl_ids = split_msg(dxl_ids, "$")
    m_moving_speeds=split_msg(moving_speeds,"$")
    m_initial_positions = split_msg(initial_positions, "$")
    dxl_osc_ctrl.start_osc(ip, port, devicename, m_dxl_ids, m_moving_speeds, m_initial_positions)
    dxl_osc_ctrl.client.send_osc(SRV_STRATED,1)


def client_started():
    return dxl_osc_ctrl.is_started()


# read feedbacks
def read_position(pattern, _id):
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    position = dxl_osc_ctrl.motor_controller.get_position()
    value = "{}#{}".format(_id, position)
    dxl_osc_ctrl.client.send_osc(READ_POS, value)
    return position


def read_speed(pattern, _id):
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    speed = dxl_osc_ctrl.motor_controller.get_present_speed()
    value = "{}#{}".format(_id, speed)
    dxl_osc_ctrl.client.send_osc(READ_SPD, value)
    return speed


def read_temperature(pattern, _id):
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    temp = dxl_osc_ctrl.motor_controller.get_temperature()
    value = "{}#{}".format(_id, temp)
    dxl_osc_ctrl.client.send_osc(READ_TEMP, value)
    return temp


def read_torque_limit(pattern, _id):
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    torque_limit = dxl_osc_ctrl.motor_controller.get_torque_limit()
    value = "{}#{}".format(_id, torque_limit)
    dxl_osc_ctrl.client.send_osc(READ_TRQ_LMT, value)
    return torque_limit


def read_load(pattern, _id):
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    load = dxl_osc_ctrl.motor_controller.get_load()
    value = "{}#{}".format(_id, load)
    dxl_osc_ctrl.client.send_osc(READ_LOAD, value)
    return load


def read_is_moving(pattern, _id):
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    isMoving = dxl_osc_ctrl.motor_controller.is_moving()
    value = "{}#{}".format(_id, isMoving)
    dxl_osc_ctrl.client.send_osc(READ_MOV, value)
    return isMoving


# enable torque
def torque_enable_disable(pattern, id_value):
    _id, value = split_msg(id_value)
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    if value == TORQUE_ENABLE:
        dxl_osc_ctrl.motor_controller.enable_torque()
    elif value == TORQUE_DISABLE:
        dxl_osc_ctrl.motor_controller.disable_torque()


# set parameters
def set_speed(pattern, id_value):
    _id, value = split_msg(id_value)
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    dxl_osc_ctrl.motor_controller.set_moving_speed(int(value))


def set_position(pattern, id_value):
    _id, value = split_msg(id_value)
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    dxl_osc_ctrl.motor_controller.set_position(int(value))


def set_torque_limit(pattern, id_value):
    _id, value = split_msg(id_value)
    dxl_osc_ctrl.motor_controller.set_id(int(_id))
    dxl_osc_ctrl.motor_controller.set_torque_limit(int(value))


def set_position_group(pattern, positions_group):
    positions = split_msg(positions_group, "$")
    dxl_osc_ctrl.motor_controller.set_position_group(positions,10)


def set_speed_group(pattern, speeds_group):
    speeds = split_msg(speeds_group,"$")
    dxl_osc_ctrl.motor_controller.set_speed_group(speeds)
