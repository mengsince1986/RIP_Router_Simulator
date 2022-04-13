"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: rip_main.py
"""

###############################################################################
#                                Import Modules                               #
###############################################################################

import sys
from rip_init import rip_router_init, rip_sockets_init

###############################################################################
#                               Global Variables                              #
###############################################################################


###############################################################################
#                             Program Entry Point                             #
###############################################################################

if __name__ == "__main__":
    print("rip_main starts...")
    # get config file name
    try:
        if len(sys.argv) != 2:
            raise ValueError("Invalid argument for rip_main\n" +
                             "Rip router requires ONE config file")
        config_file_name = sys.argv[1]
    except ValueError as error:
        print(error)

    # Initialise router
    ROUTER = rip_router_init(config_file_name)
    
    print(ROUTER)
    print()
    print(ROUTER.update_routing_table())
    ROUTER.print_routing_table()

    # TODO: Initialise sockets
