"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO (21671773)
File: rip_main.py
"""


# Import Modules
import sys
import time
import threading
from rip_init import rip_router_init


# Program Entry Point
if __name__ == "__main__":
    print("Starts RIP Daemon...")
    # get config file name
    try:
        if len(sys.argv) != 2:
            raise ValueError("Invalid argument for rip_main\n" +
                             "Rip router requires ONE config file")
        config_file_name = sys.argv[1]
    except ValueError as error:
        print(error)

    # Initialise a new Router object
    ROUTER = rip_router_init(config_file_name)

    # First advertise ROUTER itself immediately
    ROUTER.advertise_routes('all')
    ROUTER.print_routing_table()
    ROUTER.random_offset_period()

    # Start loop
    while True:
        ROUTER.receive_routes()
        ROUTER.advertise_all_routes_periodically()
        ROUTER.check_timeout_entries_periodically()
