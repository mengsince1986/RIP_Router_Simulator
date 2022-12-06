"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO (21671773)
File: forwarding_route.py
"""

# Route Class
class Route:
    """
    A Route class for creating entries of RIP routing table

    Why we use a class instead of a dictionary/list for route?
    * Compared to list we can quickly get a route value by name
    instead of number index. i.e. route.nexthop
    * Compared to dict/list, a Route class avoid accidental
    modification.
    i.e. What if we accidentally do: route[error_key] = error
    """
    def __init__(self, next_hop, metric,
                 timeout, garbage_collect_time=None,
                 state = 'active'):
        """
        parameters:
        next_hop: an integer of router ID, i.e. 2, 3
        metric: an integer, i.e. 1, 5, 7
        timeout: the current time obtained by time.time()
        garbage_collect_time: None or the current time
        state: a string, i.e. 'active', 'dying', 'updated'
        """
        self.next_hop = next_hop
        self.metric = metric
        self.timeout = timeout
        self.garbage_collect_time = garbage_collect_time
        self.state = state
