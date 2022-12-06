# RIP Router Simulator

## Introduction
The program implements a "[RIP](https://en.wikipedia.org/wiki/Routing_Information_Protocol) routing demon" as a normal userspace program under Linux. Instead of sending its routing packets over real network interfaces, the routing demon communicates with its peer demons (which run in parallel on the same machine) through local sockets. Each instance of the demon runs as a separate process.

## How to start a router?

Run `rip_main.py` (in folder *src*) with router config file as argument. There are 7 router configuration files for demostration in folder *router_configs*. For example:

```bash
python rip_main.py ../router_configs/router1_config.txt
```
## How to create a new router configuration file?

There are 5 parameters to be specified for each configuration file.
**router-id**: the unique id of this router.
**input-ports**: this is the set of port numbers (underlying sockets) on which the instance of the routing daemon will listen for incoming routing packets from peer routing daemons. There needs to be a separate input port for each neighbor the router has.
**output-ports**: this is the set of contact information for neightboured routers, to which a direct link shoud exist and with which this router exchanges routing information. The format for the contact information is *input port number*-*cost for the link*-*router id of the peer router*.
**period**: an integer value representing time in seconds, an event method is only invoked when its elapsed time is equal to or greater than its preset period.
**timeout**: an integer value representing time in seconds, the garbage collection timer of the route starts after the timeout timer expires, the route's state flag is labelled “dying”, and the metric to the router is changed to infinity.

For Example, following is the configuration for the defaut router 1:
```bash
router-id 1
input-ports 6010, 6011, 6012
output-ports 6020-1-2, 6061-5-6, 6071-8-7
period 3
timeout 18
```
