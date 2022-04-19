"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: rip_router.py
"""

###############################################################################
#                                Import Modules                               #
###############################################################################
import time
import random
from network_interface import Interface
from forwarding_route import Route
from rip_packet import RipPacket, RipEntry
from IO_formatter import *
###############################################################################
#                                 Router Class                                #
###############################################################################

class Router:
    """
    Create a new router object
    """
    def __init__(self, router_id,
                 inputs, outputs,
                 period, timeout, garbage_collection_time=12):
        """
        the __* attributes are private attributes which can only be
        accessed by getter outside of class.

        inputs: [5001, 5002, 5003]
        outputs format: [[6010(port), 2(metric), 3(router_id)], [...], ...]
        output ports format: {6010(port): {'metric': 1, 'router_id': 1},
                              6030(port): {'metric': 2, 'router_id': 3},
                              ... : {...}
                             }
        """
        # Instance attributes
        self.__router_id = router_id
        self.__input_ports = inputs
        self.__output_ports = outputs
        self.__period = period
        self.__timeout = timeout
        self.__garbage_collection_time = garbage_collection_time
        self.__interface = None
        self.__routing_table = {}
        # Initialisation
        self.init_interface(inputs)
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

    def get_interface(self):
        return self.__interface

    def get_routing_table(self):
        return self.__routing_table


    def print_routing_table(self):
        """
        # Done: Scott
        Print the current self.__routing_table
        """
        print(routing_table_formatter(self.__router_id,
                                      self.__routing_table))


    def init_interface(self, ports):
        self.__interface = Interface(ports)


    def init_routing_table(self):
        """
        Initialise the __routing_table attribute

        Route object format:
        route.next_hop: 2,
        route.metric: 1,
        route.timer: 1234,
        state(default): 'active'
        """
        # Create a new Route object to router itself
        self_route = Route('-', 0, time.time())
        self.__routing_table[self.__router_id] = self_route


    def advertise_all_routes_periodically(self):
        """
        Call advertise_all_routes() periodcally by self.__period

        Use random.random() to calculate offset for self.__period
        in order to avoid synchronized update messages which can lead
        to unnecessary collisions on broadcast networks.
        """
        offset = random.random() * self.__period
        while True:
            self.advertise_all_routes()
            self.print_routing_table()
            time.sleep(self.__period + offset)


    def advertise_all_routes(self):
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
                raise ValueError("No output port/socket available")
            for dest_port, metric_id in self.__output_ports.items():
                # message = bytes(f'update from router {self.__router_id}, port {self.__input_ports[0]}', 'utf-8')
                packet = self.update_packet(dest_port)
                self.__interface.send(packet, dest_port)
                print(f"sends update packet to Router {metric_id['router_id']} [{dest_port}] at {time.ctime()}")
        except ValueError as error:
            print(error)


    def update_packet(self, receiver_port):
        """
        # Done: Meng
        parameter:
        receiver_port

        Process the current routing table data and convert it into
        a rip format packet for advertise_all_routes() method
        """
        # Create RipEntries for all the routes
        entries = []
        for dest, route in self.__routing_table.items():
            metric = None
            if dest == self.__router_id:
                # if the destination is myself,
                # get the metric from the __outputs_ports by receiver_port
                # instead of the route.metric which is always 0
                for output_port, metric_id in self.__output_ports.items():
                    # output format: {6010(port): {'metric': 2, 'router_id': 3}}
                    if output_port == receiver_port:
                        metric = metric_id['metric']
            else:
                metric = route.metric
            entry = RipEntry(dest, metric)
            entries.append(entry)

        # Create RipPacket
        packet = RipPacket(entries, self.__router_id)
        packet_bytes = packet.packet_bytes()
        return packet_bytes

    def triggered_packet(self, updated_routes):
        """
        # TODO: Scott
        Process the data of changed routes and convert it into a rip
        format packet for advertise_routes() method
        """
        pass


    def receive_routes(self):
        """
        Receive the routes update from neighbours (input ports)

        The implementation is in a while loop and should be called with
        a separate thread from the main thread
        """
        while True:
            # The __interface only listen to the input ports
            packets_list = self.__interface.receive()
            for raw_packet in packets_list:
                self.process_received_packet(raw_packet)


    def process_received_packet(self, raw_packet):
        """
        # TODO: Meng
        Process the received packet and call update_routing_table()
        if necessary

        Parameter: packet
        an array of bytes
        """
        # Check if raw_packet valid in RipPacket and RipEntry classes
        # Process the raw_packet if valid,
        # and return (True, RipPacket object)
        # otherwise, return (False, router_id)
        is_valid, rip_packet = RipPacket.decode_packet(raw_packet)
        if is_valid:
            # check and update routing_table
            print(f'Received update from Router {rip_packet.router_id}')
            self.update_routing_table(rip_packet)
        else:
            # drop the packet
            print(f'Drop invalid packet from Router {rip_packet}')


    def update_routing_table(self, rip_packet):
        """
        # TODO: Meng
        check all the entries in rip_packet object, and update current
        routing table if necessary

        Parameter:
        rip_packet: a valid rip_packet object

        Reture: boolean
        return True if new route added, otherwise False
        """
        has_updated = False
        sender_id = rip_packet.router_id
        metric_to_sender = None
        for neighbour in self.__output_ports.values():
            if neighbour['router_id'] == sender_id:
                metric_to_sender = neighbour['metric']
        for entry in rip_packet.entries:
            #if route to dest is unavailable
            if not entry.dest in self.__routing_table.keys():
                self.__routing_table[entry.dest] = \
                    self.new_route(entry, sender_id, metric_to_sender)
                has_updated = True
            else:
                # if route to dest is available
                pass
        return has_updated


    def new_route(self, entry, sender_id,  metric_to_sender):
        """
        add a new route to the routing table

        parameters:
        entry: the RipEntry object which contains the new route
        metric_to_sender: the int metric to the sender

        Return: router
        new new Route object
        """
        # the metric to the new dest is equal to
        # the metric from neighbour to dest +
        # the metric to neighbour
        metric = entry.metric + metric_to_sender
        for neighbour in self.__output_ports.values():
            # check if the destination is one of the neighbours
            if neighbour['router_id'] == entry.dest:
                # if the dest is our neighbor, no need to add
                # additional metric
                metric = entry.metric
        route = Route(sender_id,
                          metric,
                          time.time())
        return route





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
