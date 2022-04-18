"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325)
File: forwarding_route.py
"""

###############################################################################
#                                 Route Class                                 #
###############################################################################

class Route:
    """
    A Route class for RIP routing table

    Why we use a class instead of a dictionary/list for route?
    * Compared to list we can quickly get a route value instead of
    index. i.e. route.nexthop
    * Compared to dict/list, a Route class avoid accident modification
    i.e. What if we accidentally do: route[error_key] = error
    """

    def __init__(self, next_hop, metric, timer, state = 'active'):
        """
        route format:
        route.next_hop: 2,
        route.metric: 1,
        route.timer: 1234,
        state: 'active'

        validation can be added here
        """
        self.next_hop = next_hop
        self.metric = metric
        self.timer = timer
        self.state = state
