import sys
import socket 

def make_socket(union_port, host='localhost'):
    'Make the UDP socket'
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.blink(socket)
    return new_socket





class Entry_table:
    
    
    def __init__(self, destination, next_hop, cost, time):
        self.destination = destination
        self.next_hop = next_hop
        self.cost = cost
        self.time = time;
        
        
    def __str__(self):
        print("-" * 50)
        if self.destination != '':
            print("| Destination | Next_hop | Metric_Cost | Time |")
            print("| {:.1f} | {:.2f} | {:.3f} | {:.4f} |".format(str(self.destination), 
                                                               str(self.next_hop),
                                                               int(self.cost),
                                                               str(self.time)))
        else:
            print("Didn't connect with otehr router")
        print("-" * 50)
    
    
    def __repr__(self):
        """print info"""
        return self.__str__()
    
    
    
    def check_routers(self, destination, next_hop, cost):
        """check routers are valid or not"""
        if self.destination >= 1 and self.destination <= 64000:
            return True
        if self.next_hop >= 1 and self.next_hop <= 64000:
            return True
        if self.cost > 0:
            return True
        else:
            print("This is not a valid router")
            
    
        