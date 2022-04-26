"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO (21671773)
File: rip_init.py
"""


# Import Modules
from IO_parser import router_config
from rip_router import Router


# Initialise router
def rip_router_init(config_file_name):
    """
    Parameter:
    config_file_name: the name of the config file to initialise a new
    router object.

    Return: a new Router object
    """
    config = router_config(config_file_name)
    router = Router(config['router_id'],
                        config['input_ports'],
                        config['output_ports_metric_id'],
                        config['period'],
                        config['timeout'])
    print(f"Created Router {router.get_router_id()}")
    return router
