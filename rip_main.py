"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: rip_main.py
"""

###############################################################################
#                                Import Modules                               #
###############################################################################

import sys
import time
import threading
from rip_init import rip_router_init

###############################################################################
#                               Global Variables                              #
###############################################################################


###############################################################################
#                             Program Entry Point                             #
###############################################################################

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

    # Initialise router with interface (sockets binding)
    ROUTER = rip_router_init(config_file_name)
    # Receive from input ports in a new thread
    receiver_thread = threading.Thread(target=ROUTER.receive_routes)
    receiver_thread.start()
    # Advertise to ouput ports in a new thread
    advertiser_thread = threading.Thread(target=ROUTER.advertise_all_routes_periodically)
    advertiser_thread.start()

    # Join threads
    #    receiver_thread.join()
    #    advertiser_thread.join()
