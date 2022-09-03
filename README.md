# Router Demon Simulator with RIP Protocol

## AUTHORS
* Meng Zhang
* Zheng Chao

## Introduction
This project is the assignment of UC-COSC364: Internet Technology and Engineering. The program implements a "routing demon" as a normal userspace program under Linux. Instead of sending its routing packets over real network interfaces, the routing demon communicates with its peer demons (which run in parallel on the same machine) through local sockets. Each instance of the demon runs as a separate process. 
