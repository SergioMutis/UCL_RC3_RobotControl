"""DXL OSC SERVER
# This script is part of the Dynamixel Framework adapted for UCL Bartlett RC3's robotics module.
# Within the scope of the robotics module, this file should never be edited."""

from pythonosc import dispatcher
from pythonosc import osc_server

from my_osc_client import OSC_CLIENT

address=("0.0.0.0",8888)

dispatcher=dispatcher.Dispatcher()

def dispatch_callback(pattern,function):
    dispatcher.map(pattern,function)


def server_threading(args,_dispatcher):
    server=osc_server.ThreadingOSCUDPServer((args[0],args[1]),_dispatcher)
    print("servering on {}".format(server.server_address))
    server.serve_forever()
