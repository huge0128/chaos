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
