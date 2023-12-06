#!/usr/bin/env python
#coding = utf-8
import sys
import struct

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr,ls
from scapy.all import Packet, IPOption
from scapy.all import PacketListField, ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, UDP, Raw
from scapy.layers.inet import _IPOption_HDR




def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print ("Cannot find eth0 interface")
        exit(1)
    return iface

class SwitchTrace(Packet):
    name = "sw"
    # fields_desc = [IntField("swid", 0), IntField("eport", 0), IntField("pktCount", 0)]
    fields_desc = [IntField("swid", 0), IntField("eport", 0)]

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
                    PacketListField("switchRecode",[], SwitchTrace, count_from=lambda pkt:(pkt.count*1)) ]

def handle_pkt(pkt):
    print('===================================================')
    print ("\033[0;31m Received a packet \033[0m")
    print('===================================================')
    pkt.show()
    # pkt = IP(dst="8.8.8.8", options=IPOption_MRI(count=2, switchRecode=[SwitchTrace(swid=1, qdepth=10, eport=2), SwitchTrace(swid=2, qdepth=6, eport=1)]))
    switchstack_option = pkt[2]
    switchtrace_str = ""
    switch_recode = switchstack_option.switchRecode
    for switchtrace in switchstack_option.switchRecode:
        # switchtrace_str += "switch{}:port{}({})-> ".format(switchtrace.swid, switchtrace.eport, switchtrace.qdepth)
        switchtrace_str += "switch{}:port{}<-".format(switchtrace.swid, switchtrace.eport)

    switchtrace_str = switchtrace_str[:-2]

    # print('-----------------------------------------------------')
    print ("The Telemetry Result:\033[0;32m swid:port(qdepth)->swid:port(qdepth) \033[0m")
    
    print('----------------------------------------------------')

    
    swid_list = []
    eport_list = []
    # pktCount_list = []

    for switchtrace in switchstack_option.switchRecode:
        swid_str = str(switchtrace.swid) 
        eport_str = str(switchtrace.eport)
        # pktCount_str = str(switchtrace.pktCount)

        swid_list.append(swid_str)
        eport_list.append(eport_str)
        # pktCount_list.append(pktCount_str)

        space_num = len(swid_str) - len(eport_str)
        if space_num > 0:
            eport_str = " " * space_num + eport_str
        else:
            swid_str = " " * (-space_num) + swid_str

        # space_num = len(swid_str) - len(pktCount_str)
        # if space_num > 0:
        #     pktCount_str = " " * space_num + pktCount_str
        # else:
        #     swid_str = " " * (-space_num) + swid_str

        # print(swid_str, eport_str)


    # print("-" * (len(swid_list[0]) + len(eport_list[0])))

    # for swid, eport in zip(swid_list, eport_list):
    #     print(swid, eport)
    


    # table_header = "swid".center(10) + "|" + "pktCount".center(10)+ "|" + "SwitchTrace".center(30)
    table_header = "swid".center(10) + "|" + "eport".center(10)+ "|" + "SwitchTrace".center(30)
    # table_header = "SwitchTrace".center(30) + "|" + "swid".center(10) + "|" + "qdepth".center(10) + "|" + "eport".center(10)
    print(table_header)
    print("-" * len(table_header))
    switch_string = ""

    table_format = "{:<10}|{:<10}|{:<30}"
    for switch in switch_recode:
        swid = switch.swid
        # qdepth = switch.qdepth
        eport = switch.eport
        # pktCount = switch.pktCount
        # switch_string = f"{swid}q{qdepth}e{eport}"  >python3.6 
        switch_string = switchtrace_str
        # switch_string += "%s%s" % (swid, eport)
        # print(table_format.format(swid, pktCount, switch_string))
        print(table_format.format(swid, eport, switch_string))
        # print(table_format.format(swid, eport, pktCount, switch_string))



    # print('\033[0;32m {}\033[0m'.format(switchtrace_str))


    
    # f=file("/home/p4/tutorials/exercises/mri/result","a+")
    # #f=file("/home/p4/tutorials/exercises/mri/result","r+")
    # f.write(p+'\n')
    # f.close()
    
    #pkt.pdfdump(layer_shift=1)
    #pkt.pdfdump("/home/p4/tutorials/exercises/mri/test.eps",layer_shift=1)
    sys.stdout.flush()


def main():
    iface = 'eth0'
    print "sniffing on %s" % iface
    sys.stdout.flush()
    sniff(filter="udp and port 4321", iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
