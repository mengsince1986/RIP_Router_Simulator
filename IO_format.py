"""
COSC364 2022-S1 Assignment: RIP routing
Authors: MENG ZHANG (71682325), ZHENG CHAO
File: IO_format.py
"""
#import sys




class TablePrinter:
    
    
    def __init__(self, destination, next_hop, cost, state):
        self.destination = destination
        self.next_hop = next_hop
        self.cost = cost
        self.state = state;
        
        
    def __str__(self):
        print("-" * 50)
        if self.destination != '':
            print("| Destination | Next_hop | Metric_Cost | Time |")
            print("| {:.1f} | {:.2f} | {:.3f} | {:.4f} |".format(str(self.destination), 
                                                               str(self.next_hop),
                                                               int(self.cost),
                                                               str(self.state)))
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
            
    

# Test
if __name__ == "__main__":
    print("IO-format Module Test")
    print_message("print_message starts...")
    print_table("====Print_table starts====")
    print()
    
    
    
