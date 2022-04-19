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
    # Border Top and Bottom: 72 chars
    border = 72 * '-'
    double_border = 72 * '='
    # Title: 49 chars =  27 chars + 21 + 22 paddding spaces
    title = f'Router {router_id:02} RIP ROUTING TABLE'
    padded_title = '|' + 21 * ' ' + title + 22 * ' ' + '|'
    # Lables: 49 chars
    labels = "|   Dest   |   Next   |   Metric   |  Timeout  |  Garbage  |   State   |"
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
        timeout = int(time.time() - rip_route.timeout)

        garbage_collect_time = rip_route.garbage_collect_time
        if not (garbage_collect_time is None):
            garbage_collect_time = int(time.time() - garbage_collect_time)
            gc_str = f'{garbage_collect_time:^11.0f}'
        else:
            gc_str = 5 * ' ' +  '-' + 5 * ' '
        state = rip_route.state
        content += f'|{dest:^10}|{next_hop:^10}|{metric:^12}|{timeout:^11.0f}|' +\
            f'{gc_str}|{state:^11}|' + '\n' +\
            border + '\n'
    return header + content
