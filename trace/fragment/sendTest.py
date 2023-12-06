#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct
import os 
import time 
import hashlib
from scapy.all import sendp, send, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import Ether, IP, UDP
from scapy.all import IntField, FieldListField, FieldLenField, ShortField, PacketListField
from scapy.layers.inet import _IPOption_HDR

from time import sleep

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print ("Cannot find eth0 interface")
        exit(1)
    return iface
        

class SwitchTrace(Packet):
    fields_desc = [ 
        IntField("swid", 0),
        # IntField("qdepth", 0),
        IntField("eport", 0),
        # IntField("pktCount", 0)
        ]
    def extract_padding(self, p):
                return "", p

class IPOption_MRI(IPOption):
    name = "SWITCHSTACK"
    option = 31
    fields_desc = [ _IPOption_HDR,
                    FieldLenField("length", None, fmt="B",
                                  length_of="swtraces",
                                  adjust=lambda pkt,l:l*2+4),
                    ShortField("count", 0),
                    PacketListField("swtraces",
                                   [],
                                   SwitchTrace,
                                   count_from=lambda pkt:(pkt.count*1)) ]


def main():

    if len(sys.argv)<3:
        print ('pass 2 arguments: <destination> "<message>"')
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    pkt = Ether(src=get_if_hwaddr(iface), dst="ff:ff:ff:ff:ff:ff") / IP(
        src="10.0.1.1",dst="10.0.2.2", options = IPOption_MRI(count=3,swtraces=[])) / UDP(
            dport=4321, sport=1234) / sys.argv[2]

    ip_byte = bytes(pkt[IP].src)
    # print(ip_byte)

    # 1. Insert DSCP Type 00001100
    dscp_byte = 18
    pkt[IP].tos = dscp_byte
    print("DCSP :\033[0;32m{}\033[0m".format(pkt[IP].tos))

    # 2. Generate 15 bit hash_value: hash_val_bin
    md5_obj = hashlib.md5(ip_byte)

    hash_val = md5_obj.hexdigest()[:15]
    hash_val_int = int(hash_val, 16)  
    hash_val_bin = bin(hash_val_int)[2:]  
    hash_val_bin = hash_val_bin.zfill(60)[:15]  
    
    # 3. Genetrate 4 ip address fragments[n]
    fragments = []

    src_val = pkt[IP].src
    for i in range(4):
        byte = (int(src_val.split('.')[i])) >> (i*8) & 0xff
        bin_str = bin(byte)[2:].zfill(8)

        fragments.append(bin_str)


    for i in range(4):
        print("offset \033[0;32m{}\033[0m :fragment\033[0;32m{}\033[0m".format(i, fragments[i]))

    # 32 bit ip address
    # bin_str = ''.join(fragments)
    # print(bin_str)

    # 4. Select random IP fragment with index frag_idx
    frag_idx= random.randint(0, 3)
    # frag_set = set()
    # frag_set.add((frag_idx, fragments[frag_idx]))
    
    offset = frag_idx
    # print(offset)
    fragment = fragments[offset]
    offset  = bin(offset)[2:].zfill(2)
    # print(offset)
    highbit = offset[0]
    lowbit  = offset[1]
    print("highbit \033[0;32m{}\033[0m :lowbit\033[0;32m{}\033[0m".format(highbit, lowbit))
    
    # 4. Insert four fileds into ipv4 header
    # 4.1 Insert hash&highbit into id
    bin_str = '{:0>15b}{}'.format(int(hash_val_bin, 2), highbit)
    result = int(bin_str, 2)
    print(bin(result)[2:])

    pkt[IP].id = bin(result)[2:].zfill(16)
    print("Overwrite Identification: \033[0;32m{}\033[0m".format(pkt[IP].id))
    
    # 4.2 Insert lowbit into flag
    print(pkt[IP].flags)
    pkt[IP].flags = bool(lowbit)
    print(pkt[IP].flags)
    
    # print(pkt[1])

    # 4.3 Insert distance&fragment into ip frag
    distance = 0
    distance_str = bin(distance)[2:].zfill(5)

    bin_str = '{:0>8b}{}'.format(int(fragment, 2), distance_str)
    result = int(bin_str, 2)
    frag = bin(result)[2:].zfill(13)
    pkt[IP].frag = frag

    print('===================================================')
    print ("\033[0;31m Depart a SrcIP address into 4 fragments\033[0m")
    print('===================================================')

    table_header = "SrcIP Hash".center(20) + "|" + "Offset".center(10)+ "|"+ "Fragment".center(10)+ "|" + "Hopcount".center(10)
    print(table_header)
    print("-" * len(table_header))
    table_format = "\033[0;32m{:<20}\033[0m|\033[0;32m{:<10}\033[0m|\033[0;32m{:<10}\033[0m|\033[0;32m{:<10}\033[0m"
    print(table_format.format(hash_val_bin, offset, fragment, distance_str))

    pkt.show()
    switchstack = pkt[2]
    # print(switchstack)
    
    #hexdump(pkt)
    try:
      for i in range(int(sys.argv[3])):
        sendp(pkt, iface=iface)
        sleep(1)
    except KeyboardInterrupt:
        print("The TIME:%s"%time.ctime())
        os.system("su - p4")
        raise


if __name__ == '__main__':
    main()
