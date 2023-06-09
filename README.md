# chaos//Research on Address Spoofing Attack Traceability and Defense Mechanism in Programmable Network
Some programs of thesis uesd for flow traceback

## 1 flow statistic 
run the flow.p4 to collect the flow info 
```
P4@P4: cd/flow
P4@P4: make
```
run the flowtest.py
```
./holt.py
```
## 2 traceback
terminal 1
```
P4@P4: cd/traceroute
P4@P4: make
mininet> xterm h4 h2
```
xterm 
```
root@P4: ./receive.py
```
```
root@P4: ./send.py 10.0.2.2 "come from h4" n
```

terminal 2
```
P4@P4: cd/fragment
P4@P4: make
mininet> xterm h4 h2
```
xterm 
```
root@P4: ./receive.py
```
```
root@P4: ./test.py 10.0.2.2 "come from h4" n
```

the packet format
```
got a packet
###[ Ethernet ]###
  dst       = 00:04:00:02:00:02
  src       = f2:ed:e6:df:4e:fa
  type      = 0x800
###[ IP ]###
     version   = 4L
     ihl       = 10L
     tos       = 0x0
     len       = 42
     id        = 1
     flags     =
     frag      = 0L
     ttl       = 62
     proto     = udp
     chksum    = 0x60c0
     src       = 10.0.1.1
     dst       = 10.0.2.2
     \options   \
      |###[ MetadataStack ]###
      |  copy_flag = 0L
      |  optclass  = control
      |  option    = 31L
      |  length    = 20
      |  count     = 2
      |  \swtraces  \
      |   |###[ SwitchTrace ]###
      |   |  swid      = 4
      |   |  eport    = 2
      |   |###[ SwitchTrace ]###
      |   |  swid      = 3
      |   |  eport    = 2
      |   |###[ SwitchTrace ]###
      |   |  swid      = 2
      |   |  eport    = 1
###[ UDP ]###
        sport     = 1234
        dport     = 4321
        len       = 18
        chksum    = 0x1c7b
###[ Raw ]###
           load      = 'come from h4'
```


## 3 Smart Contract
generate the testnet of blockcahin in cache
```
P4@P4:ganache-cli -q
```

terminal 1 deploy the contracts 
```
P4@P4: node deploy.js
```
terminal 2 call the contracts 
```
P4@P4: node call.js
```
terminal 3 get the event based logs 
```
P4@P4: cd/eth/dapptest/ddostest/ddosdapp
P4@P4: ~/eth/dapptest/ddostest/ddosdapp$ npm start
```
