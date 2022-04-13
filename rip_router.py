"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: rip_router.py
"""

###############################################################################
#                                Import Modules                               #
###############################################################################
from network_interface import Interface

###############################################################################
#                                 Router Class                                #
###############################################################################

class Router:
    """
    Create a new router object
    """
    def __init__(self, router_id, inputs, outputs, period, timeout):
        self.__router_id = router_id
        self.__input_ports = inputs
        self.__output_ports = outputs
        self.__period = period
        self.__timeout = timeout
        self.__interface = None
        self.init_interface(inputs)
        self.__routing_table = None
        self.init_routing_table()

    def get_router_id(self):
        """
        router_id getter
        """
        return self.__router_id

    def set_router_id(self, new_id):
        self.__router_id = new_id

    def get_input_ports(self):
        return self.__input_ports

    def set_input_ports(self, new_inputs):
        self.__input_ports = new_inputs
        self.init_interface(new_inputs)

    def get_output_ports(self):
        return self.__output_ports

    def set_output_ports(self, new_outputs):
        self.__output_ports = new_outputs

    def get_period(self):
        return self.__period

    def set_period(self, new_period):
        self.__period = new_period

    def get_timeout(self):
        return self.__timeout

    def set_timeout(self, new_timeout):
        self.__timeout = new_timeout

    def init_interface(self, ports):
        self.__interface = Interface(ports)

    def get_interface(self):
        return self.__interface

    def init_routing_table(self):
        print("init_routing_table starts...")
        self.__routing_table = {self.__router_id: ["Next Hop", 0, "timer", "Notes"]}
        return True

    def update_routing_table(self):
        print("update_routing_table starts...")
        return "====================Update Router {}====================".format(self.get_router_id())

    def get_routing_table(self):
        return self.__routing_table

    def print_routing_table(self):
        print(self.get_routing_table())

    def __str__(self):
        return ("Router: {0}\n"
                "Input Ports: {1}\n"
                "Output Ports: {2}\n"
                "Period: {3}\n"
                "Timeout: {4}").format(self.__router_id,
                                       self.__input_ports,
                                       self.__output_ports,
                                       self.__period,
                                       self.__timeout)


if __name__ == '__main__':
    new_router = Router(0, [5001], [[5002, 10, 2]], 3, 18)
    print("Router ID: {0}".format(new_router.get_router_id()))
    print("Input Ports: {0}".format(new_router.get_input_ports()))
    print("Output Ports: {0}".format(new_router.get_output_ports()))
    print("Period: {0}".format(new_router.get_period()))
    print("Timeout: {0}".format(new_router.get_timeout()))
    print("Routing_table: {0}".format(new_router.get_routing_table()))
    print()
    print(new_router)
    print()
    print(new_router.get_interface())
