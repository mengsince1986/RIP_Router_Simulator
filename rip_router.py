"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: rip_router.py
"""

###############################################################################
#                                Import Modules                               #
###############################################################################
from network_interface import Interface
from IO_format import *
###############################################################################
#                                 Router Class                                #
###############################################################################

class Router:
    """
    Create a new router object
    """
    def __init__(self, router_id, inputs, outputs, period, timeout):
        """
        the __* attributes are private attributes which can only be
        accessed by getter outside of class.
        """
        self.__router_id = router_id
        # inputs format: [5001, 5002, 5003]
        self.__input_ports = inputs
        # outputs format: [6010(port), 2(metric), 3(router_id)]
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

    def advertise_routes_periodically(self):
        """
        call advertise_routes() periodcally based on period (timer)
        """

    def advertise_routes(self):
        """
        # TODO: Meng
        get the latest advertising rip packet from
        update_packet() & triggered_packet() methods and
        advertise the packet to all the neighbours (ouput ports)

        need to add a parameter for updata_packet/triggered_packet
        """
        try:
            ports_num = len(self.__output_ports)
            if (ports_num < 1):
                raise ValueError("There's no output port/socket available")
            for i in range(ports_num):
                dest_port = self.__output_ports[i][0]
                # message id for test
                message = bytes(f'update from router {self.__router_id}, port {self.__input_ports[0]}', 'utf-8')
                self.__interface.send(message, dest_port)
                print(f"sent message to {dest_port}")
        except ValueError as error:
            print(error)

    def update_packet(self):
        """
        # TODO: Meng
        Process the current routing table data and convert it into
        a rip format packet for advertise_routes() method
        """

    def triggered_packet(self, updated_routes):
        """
        # TODO: Scott
        Process the data of changed routes and convert it into a rip
        format packet for advertise_routes() method
        """

    def process_received_update(self):
        """
        # TODO: Meng
        Process the received update and update_routing_table() and
        advertise triggered_packet if necessary
        """

    def receive_routes(self):
        """
        # TODO: Meng
        receive the routes update from neighbours (input ports)
        """
        input_sockets = []
        for input_port in self.__input_ports:
            input_sockets.append(self.__interface.ports_sockets[input_port])
        packet_list = self.__interface.receive(input_sockets)
        print("receiving message")
        return packet_list

    def init_routing_table(self):
        print("init_routing_table starts...")
        self.__routing_table = {self.__router_id: ["Next Hop", 0, "timer", "Notes"]}
        return True

    def update_routing_table(self):
        """
        # TODO: Meng
        """
        print("update_routing_table starts...")
        return "====================Update Router {}====================".format(self.get_router_id())

    def get_routing_table(self):
        return self.__routing_table

    def print_routing_table(self):
        """
        # TODO: Scott
        Get the self.__routing_table and print it out

        need IO_format module
        """
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
