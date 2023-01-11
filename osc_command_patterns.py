"""OSC COMMAND PATTERNS
# This script is part of the Dynamixel Framework adapted for UCL Bartlett RC3's robotics module.
# Within the scope of the robotics module, this file should never be edited."""

START_OSC= "/start_osc"

# READ FEEDBACKS
READ_POS = "/read_position"
READ_SPD = "/read_speed"
READ_LOAD = "/read_load"
READ_TEMP = "/read_temperature"
READ_TRQ_LMT = "/read_torque_limit"
READ_MOV = "/read_is_moving"


#ENABLE TORQUE
TRQ_TOGGLE= "/toggle_torque"

#SET PARAMETERS

SET_POS = "/set_position"
SET_SPD = "/set_speed"
SET_TRQ_LMT="/set_torque_limit"

SET_POS_GRP = "/set_position_group"
SET_SPD_GRP = "/set_speed_group"
SET_TRQ_LMT_GRP = "/set_torque_limit_group"

SET_POS_SYNC = "/set_position_sync"
SET_SPD_SYNC = "/set_speed_sync"
SET_TRQ_LMT_SYNC = "/set_torque_limit_sync"

SRV_STRATED="/serveo_started"
