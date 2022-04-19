"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: IO_formatter.py
"""
import time

def routing_table_formatter(router_id, table):
    """
    Parameters:
    table: a dictionary of routes
    {id1: Route object, id2: Route object, ...}

    Return:
    table: a formatted string which contains data of the table
    """
    # Border Top and Bottom: 49 chars
    border = 60 * '-'
    double_border = 60 * '='
    # Title: 49 chars =  27 chars + 22 paddding spaces
    title = f'Router {router_id:02} RIP ROUTING TABLE'
    padded_title = '|' + 15 * ' ' + title + 16 * ' ' + '|'
    # Lables: 49 chars
    labels = "|   Dest   |   Next   |   Metric   |   Timer   |   State   |"
    # Table header
    header = '\n' + double_border + '\n' +\
        padded_title + '\n' +\
        double_border + '\n' +\
        labels + '\n' +\
        border + '\n'
    # Table content
    content = ""
    for dest, rip_route in table.items():
        next_hop = rip_route.next_hop
        metric = rip_route.metric
        timer = int(time.time() - rip_route.timer)
        state = rip_route.state
        content += f"|{dest:^10}|{next_hop:^10}|{metric:^12}|{timer:^11.0f}|{state:^11}|" + '\n' +\
            border + '\n'

    return header + content
