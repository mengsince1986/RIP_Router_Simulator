"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: rip_router.py
"""

class Router:
    """
    Create a new router object
    """
    def __init__(self, router_id, inputs, outputs, period, timeout):
        self.router_id = router_id
        self.input_ports = inputs
        self.output_ports = outputs
        self.period = period
        self.timeout = timeout
        self.routing_table = None
        self.init_routing_table()

    def get_router_id(self):
        return self.router_id

    def set_router_id(self, new_id):
        self.router_id = new_id

    def get_input_ports(self):
        return self.input_ports

    def set_input_ports(self, new_inputs):
        self.input_ports = new_inputs

    def get_output_ports(self):
        return self.output_ports

    def set_input_ports(self, new_outputs):
        self.output_ports = new_outputs

    def get_period(self):
        return self.period

    def set_period(self, new_period):
        self.period = new_period

    def get_timeout(self):
        return self.timeout

    def set_timeout(self, new_timeout):
        self.timeout = new_timeout

    def init_routing_table(self):
        print("init_routing_table starts...")

    def update_routing_table(self):
        print("update_routing_table starts...")

    def get_routing_table(self):
        return self.routing_table

    def __str__(self):
        return ("Router: {0}\n"
                "Input Ports: {1}\n"
                "Output Ports: {2}\n"
                "Period: {3}\n"
                "Timeout: {4}").format(self.router_id,
                                       self.input_ports,
                                       self.output_ports,
                                       self.period,
                                       self.timeout)


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
