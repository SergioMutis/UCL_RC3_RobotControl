"""DXL OSC MAIN
# This script is part of the Dynamixel Framework adapted for UCL Bartlett RC3's robotics module.
# Within the scope of the robotics module, this file should never be edited."""

import dxl_control_osc
import my_osc_server
from osc_command_patterns import *

my_osc_server.dispatch_callback(START_OSC, dxl_control_osc.start_osc)
my_osc_server.dispatch_callback(READ_POS, dxl_control_osc.read_position)
my_osc_server.dispatch_callback(READ_SPD, dxl_control_osc.read_speed)
my_osc_server.dispatch_callback(READ_LOAD, dxl_control_osc.read_load)
my_osc_server.dispatch_callback(READ_TEMP, dxl_control_osc.read_temperature)
my_osc_server.dispatch_callback(READ_TRQ_LMT, dxl_control_osc.read_torque_limit)
my_osc_server.dispatch_callback(SET_POS, dxl_control_osc.set_position)
my_osc_server.dispatch_callback(SET_SPD, dxl_control_osc.set_speed)
my_osc_server.dispatch_callback(SET_TRQ_LMT, dxl_control_osc.set_torque_limit)
my_osc_server.dispatch_callback(SET_POS_GRP, dxl_control_osc.set_position_group)
my_osc_server.dispatch_callback(SET_SPD_GRP, dxl_control_osc.set_speed_group)
my_osc_server.dispatch_callback(TRQ_TOGGLE, dxl_control_osc.torque_enable_disable)
my_osc_server.server_threading(my_osc_server.address, my_osc_server.dispatcher)
