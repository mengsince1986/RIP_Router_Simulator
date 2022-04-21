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
from datetime import datetime
from network_interface import Interface
from forwarding_route import Route
from rip_packet import RipPacket, RipEntry
from IO_formatter import routing_table_formatter
###############################################################################
#                                 Router Class                                #
###############################################################################

class Router:
    """
    Create a new router object
    """
    INFINITY = 16
    TIMER_OFFSET = 1.0

    def __init__(self, router_id,
                 inputs, outputs,
                 period, timeout):
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
        self.__split_horizon_poison_reverse = True
        self.__input_ports = inputs
        self.__output_ports = outputs
        self.__advertise_timer = time.time()
        self.__default_period = period
        self.__period = period
        self.__timeout_check_timer = time.time()
        self.__timeout = timeout
        self.__garbage_collection_time = period * 4
        self.__interface = None
        self.__routing_table = {}
        # Initialisation
        self.init_interface(inputs)
        self.init_routing_table()
        self.random_offset_period()

    def get_router_id(self):
        """
        router_id getter
        """
        return self.__router_id

#    def set_router_id(self, new_id):
#        self.__router_id = new_id

    def get_input_ports(self):
        return self.__input_ports

#    def set_input_ports(self, new_inputs):
#        self.__input_ports = new_inputs
#        self.init_interface(new_inputs)

    def get_output_ports(self):
        return self.__output_ports

#    def set_output_ports(self, new_outputs):
#        self.__output_ports = new_outputs

    def get_period(self):
        return self.__period

#    def set_period(self, new_period):
#        self.__period = new_period

    def get_timeout(self):
        return self.__timeout

#    def set_timeout(self, new_timeout):
#        self.__timeout = new_timeout

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


    def random_offset_period(self):
        """
        randomize self.__period +- TIMER_OFFSET, and convert to 2 decimal places
        """
        self.__period = self.__default_period +\
            random.uniform(-self.TIMER_OFFSET, +self.TIMER_OFFSET)
        print(f"Set Router update period to {self.__period:.2f}")


    def init_interface(self, ports):
        self.__interface = Interface(ports)


    def init_routing_table(self):
        """
        Initialise the __routing_table attribute

        Route object format:
        route.next_hop: 2,
        route.metric: 1,
        route.timeout: 1234,
        route.garbage_collect_time: None(default)
        state: 'active'(default)
        """
        # Create a new Route object to router itself
        self_route = Route('-', 0, None)
        self.__routing_table[self.__router_id] = self_route


    def advertise_all_routes_periodically(self):
        """
        Call advertise_all_routes() periodcally by self.__period

        Use random.random() to calculate offset for self.__period
        in order to avoid synchronized update messages which can lead
        to unnecessary collisions on broadcast networks.
        """
        """
        while True:
            self.advertise_all_routes()
            self.print_routing_table()
            offset = random.random() * self.__period
            time.sleep(self.__period + offset)
        """
        now = time.time()
        if now - self.__advertise_timer >= self.__period:
            self.advertise_all_routes()
            self.print_routing_table()
            self.__advertise_timer = now
            self.random_offset_period()


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
            if ports_num < 1:
                raise ValueError("No output port/socket available")
            for dest_port, metric_id in self.__output_ports.items():
                packet = self.update_packet(metric_id['router_id'])
                self.__interface.send(packet, dest_port)
                current_time = datetime.now().strftime('%H:%M:%S.%f')[:-4]
                print("sends update packet to Router " +
                     f"{metric_id['router_id']} " +
                     f"[{dest_port}] at {current_time}")
        except ValueError as error:
            print(error)


    def update_packet(self, receiver_id):
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
            metric = route.metric
            if self.__split_horizon_poison_reverse and\
               route.next_hop == receiver_id:
                metric = self.INFINITY
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
        """
        while True:
            # The __interface only listen to the input ports
            packets_list = self.__interface.receive()
            for raw_packet in packets_list:
                self.process_received_packet(raw_packet)
        """
        # The __interface only listen to the input ports
        # print(f"Listening to ports at {time.ctime()}")
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
            # update routing_table if incoming packet is valid
            print(f'Received update from Router {rip_packet.router_id}')
            self.update_routing_table(rip_packet)
        else:
            # drop the packet if incoming packet is invalid
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
        # get metric from sender
        sender_id = rip_packet.router_id
        metric_to_sender = None
        for neighbour in self.__output_ports.values():
            if neighbour['router_id'] == sender_id:
                metric_to_sender = neighbour['metric']
        for entry in rip_packet.entries:
            # update the metric for each entry
            # by adding the metric to sender
            # metric = min(metric + metric_to_sender, 16(infinity))
            updated_metric = min(entry.metric + metric_to_sender,
                                 self.INFINITY)
            #if route to dest is unavailable in __routing_table
            if updated_metric != self.INFINITY and\
               not entry.dest in self.__routing_table.keys():
                self.__routing_table[entry.dest] = \
                    Route(sender_id, updated_metric, time.time())
            elif entry.dest in self.__routing_table:
                self.update_availabe_route(entry,
                                           updated_metric,
                                           sender_id)


    def update_availabe_route(self, entry, updated_metric, sender_id):
        """
        Parameters:
        entry: a RipEntry object
        sender_id: the router id from which the entry is sent
        """
        # TODO: triggered update by Meng
        # if route to dest is available in __routing_table

        # 1. if packet is from the same router as
        # existing router, reinitialize the timeout anyway
        from_same_router = sender_id == \
            self.__routing_table[entry.dest].next_hop
        if from_same_router:
            self.__routing_table[entry.dest].timeout = time.time()

        # 2. compare metrics
        new_metric = updated_metric
        old_metric = self.__routing_table[entry.dest].metric
        have_differnt_metrics = new_metric != old_metric
        is_lower_new_metric = new_metric < old_metric
        is_almost_timeout = \
            not self.__routing_table[entry.dest].timeout is None and\
            (time.time() - self.__routing_table[entry.dest].timeout)\
            >= self.__timeout / 2
#        is_available_route = entry.dest in self.__routing_table

        if from_same_router and have_differnt_metrics:
            self.__routing_table[entry.dest].metric = new_metric
            if new_metric == self.INFINITY:
                self.__routing_table[entry.dest].garbage_collect_time \
                    = time.time()
                self.__routing_table[entry.dest].state = 'updated'
        elif is_lower_new_metric:
            self.__routing_table[entry.dest].metric = new_metric
            self.__routing_table[entry.dest].next_hop = sender_id
            self.__routing_table[entry.dest].timeout = time.time()
        elif not have_differnt_metrics and is_almost_timeout:
            self.__routing_table[entry.dest].next_hop = sender_id
            self.__routing_table[entry.dest].timeout = time.time()


    def check_timeout_entries_periodically(self):
        """
        call check_timeout_entries() every default_period
        """
        now = time.time()
        if now - self.__timeout_check_timer >= self.__default_period:
            self.check_timeout_entries()
            self.__timeout_check_timer = now


    def check_timeout_entries(self):
        """
        Check the timeout of each entry in __routing_table

        if an entry is timeout, start its garbage_collect_time
        """
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-4]
        print(f"Checking timeout entries at {current_time}")

        entries_to_remove = []
        for dest_id, entry in self.__routing_table.items():
            if not entry.timeout is None and \
               entry.garbage_collect_time is None and \
               time.time() - entry.timeout >= self.__timeout:
                entry.garbage_collect_time = time.time()
                entry.state = 'dying'
                self.print_routing_table()
            elif not entry.garbage_collect_time is None and \
                 (time.time() - entry.garbage_collect_time) \
                 >= self.__garbage_collection_time:
                entries_to_remove.append(dest_id)

        for dest_id in entries_to_remove:
            self.__routing_table.pop(dest_id)
            print(f"Removed timeout route to {dest_id}")
            self.print_routing_table()


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
