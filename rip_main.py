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

    while True:
        ROUTER.advertise_routes()
        messages = ROUTER.receive_routes()
        for m in messages:
            print(m)
        time.sleep(5)
