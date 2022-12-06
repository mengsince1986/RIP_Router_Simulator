"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO (21671773)
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
    # Get header
    header = table_header_formatter(router_id)
    # Get content
    content = table_content_formatter(table)
    return header + content


def talbe_border_formatter(length):
    """
    return two formatted routing table borders
    """
    border = length * '-'
    double_border = length * '='
    return border, double_border


def table_header_formatter(router_id):
    """
    return a formatted routing table header
    """
    border, double_border = talbe_border_formatter(72)
    title = f'Router {router_id:02} RIP ROUTING TABLE'
    padded_title = '|' + 21 * ' ' + title + 22 * ' ' + '|'
    labels = "|   Dest   |   Next   |   Metric   |  Timeout  |  Garbage  |   State   |"
    header = '\n' + double_border + '\n' +\
        padded_title + '\n' +\
        double_border + '\n' +\
        labels + '\n' +\
        border + '\n'
    return header


def table_content_formatter(table):
    """
    retrun formatted routing table content
    """
    border = talbe_border_formatter(72)[0]
    content = ""
    for dest, rip_route in table.items():
        next_hop = rip_route.next_hop
        metric = rip_route.metric

        timeout = rip_route.timeout
        if not timeout is None:
            timeout = round(time.time() - rip_route.timeout, 2)
            timeout_str = f'{timeout:^11.1f}'
        else:
            timeout_str = 5 * ' ' +  '-' + 5 * ' '

        garbage_collect_time = rip_route.garbage_collect_time
        if not garbage_collect_time is None:
            garbage_collect_time = int(time.time() - garbage_collect_time)
            gc_str = f'{garbage_collect_time:^11.0f}'
        else:
            gc_str = 5 * ' ' +  '-' + 5 * ' '
        state = rip_route.state
        content += f'|{dest:^10}|{next_hop:^10}|{metric:^12}|'+\
            f'{timeout_str}|{gc_str}|{state:^11}|' + '\n' +\
            border + '\n'
    return content
