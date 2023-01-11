"""MY OSC CLIENT
# This script is part of the Dynamixel Framework adapted for UCL Bartlett RC3's robotics module.
# Within the scope of the robotics module, this file should never be edited."""

from pythonosc import udp_client


class OSC_CLIENT:
    out_ip = "0,0,0,0"
    out_port = 8888

    client = None


    @classmethod
    def init(cls, ip, port):
        cls.out_ip = ip
        cls.out_port = port
        cls.setup_client()

    @classmethod
    def setup_client(cls):
        cls.client = udp_client.SimpleUDPClient(cls.out_ip, cls.out_port)
        print("connected to {} on port {}".format(cls.out_ip,cls.out_port))

    def send_osc(self, pattern, value):
        self.client.send_message(pattern, value)
        print("send value: {} pattern : {} to {}".format(value, pattern, self.out_ip))

    def __init__(self,ip,port):
        OSC_CLIENT.init(ip,port)



