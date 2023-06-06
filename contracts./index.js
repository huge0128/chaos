var express = require('express');
var router = express.Router();

var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));

// const contractAddr =  '0xE5D63B33f2f89c4b52BAf6755AE2b53B759760a2';
const contractAddr =  '0x9695430FF314d102b9C60BdD03495c55c2961480';
const controller = '0x9054D3779a16fdA9C4deEf97f0fBDd620126581F';
//import abi from './abi.json'

console.log("==========================================================");
console.log('\033[0;36m','Event-driven information integration for blockchain is deploying...','\033[0m');
console.log("==========================================================");

var myContract = new web3.eth.Contract(
	// [
	// 	{
	// 		"anonymous": false,
	// 		"inputs": [
	// 			{
	// 				"indexed": false,
	// 				"internalType": "address",
	// 				"name": "controller",
	// 				"type": "address"
	// 			},
	// 			{
	// 				"indexed": false,
	// 				"internalType": "address",
	// 				"name": "reporter",
	// 				"type": "address"
	// 			},
	// 			{
	// 				"indexed": false,
	// 				"internalType": "string",
	// 				"name": "location",
	// 				"type": "string"
	// 			},
	// 			{
	// 				"indexed": false,
	// 				"internalType": "uint256",
	// 				"name": "value",
	// 				"type": "uint256"
	// 			},
	// 			{
	// 				"indexed": false,
	// 				"internalType": "string",
	// 				"name": "_swTrace",
	// 				"type": "string"
	// 			}
	// 		],
	// 		"name": "LogReport",
	// 		"type": "event"
	// 	},
	// 	{
	// 		"anonymous": false,
	// 		"inputs": [
	// 			{
	// 				"indexed": false,
	// 				"internalType": "address",
	// 				"name": "controller",
	// 				"type": "address"
	// 			},
	// 			{
	// 				"indexed": false,
	// 				"internalType": "address",
	// 				"name": "reporter",
	// 				"type": "address"
	// 			},
	// 			{
	// 				"indexed": false,
	// 				"internalType": "uint256",
	// 				"name": "value",
	// 				"type": "uint256"
	// 			}
	// 		],
	// 		"name": "LogTxInfo",
	// 		"type": "event"
	// 	},
	// 	{
	// 		"inputs": [],
	// 		"name": "getTxInfo",
	// 		"outputs": [],
	// 		"stateMutability": "nonpayable",
	// 		"type": "function"
	// 	},
	// 	{
	// 		"inputs": [
	// 			{
	// 				"internalType": "address payable",
	// 				"name": "_controller",
	// 				"type": "address"
	// 			},
	// 			{
	// 				"internalType": "string",
	// 				"name": "_location",
	// 				"type": "string"
	// 			},
	// 			{
	// 				"internalType": "string",
	// 				"name": "_swTrace",
	// 				"type": "string"
	// 			}
	// 		],
	// 		"name": "report",
	// 		"outputs": [],
	// 		"stateMutability": "payable",
	// 		"type": "function"
	// 	},
	// 	{
	// 		"inputs": [],
	// 		"name": "getLocationList",
	// 		"outputs": [
	// 			{
	// 				"internalType": "string[]",
	// 				"name": "",
	// 				"type": "string[]"
	// 			},
	// 			{
	// 				"internalType": "uint256",
	// 				"name": "timestamp",
	// 				"type": "uint256"
	// 			},
	// 			{
	// 				"internalType": "uint256",
	// 				"name": "interval",
	// 				"type": "uint256"
	// 			}
	// 		],
	// 		"stateMutability": "view",
	// 		"type": "function"
	// 	},
	// 	{
	// 		"inputs": [],
	// 		"name": "getMarkInfo",
	// 		"outputs": [
	// 			{
	// 				"internalType": "address[]",
	// 				"name": "reporter",
	// 				"type": "address[]"
	// 			},
	// 			{
	// 				"internalType": "string[]",
	// 				"name": "markInfo",
	// 				"type": "string[]"
	// 			}
	// 		],
	// 		"stateMutability": "view",
	// 		"type": "function"
	// 	},
	// 	{
	// 		"inputs": [],
	// 		"name": "getReportList",
	// 		"outputs": [
	// 			{
	// 				"internalType": "address[]",
	// 				"name": "",
	// 				"type": "address[]"
	// 			},
	// 			{
	// 				"internalType": "uint256",
	// 				"name": "timestamp",
	// 				"type": "uint256"
	// 			},
	// 			{
	// 				"internalType": "uint256",
	// 				"name": "interval",
	// 				"type": "uint256"
	// 			}
	// 		],
	// 		"stateMutability": "view",
	// 		"type": "function"
	// 	}
	// ]
	[
		{
			"anonymous": false,
			"inputs": [
				{
					"indexed": false,
					"internalType": "address",
					"name": "controller",
					"type": "address"
				},
				{
					"indexed": false,
					"internalType": "address",
					"name": "reporter",
					"type": "address"
				},
				{
					"indexed": false,
					"internalType": "string",
					"name": "location",
					"type": "string"
				},
				{
					"indexed": false,
					"internalType": "uint256",
					"name": "value",
					"type": "uint256"
				},
				{
					"indexed": false,
					"internalType": "string",
					"name": "_swTrace",
					"type": "string"
				},
				{
					"indexed": false,
					"internalType": "uint256",
					"name": "time",
					"type": "uint256"
				}
			],
			"name": "LogReport",
			"type": "event"
		},
		{
			"anonymous": false,
			"inputs": [
				{
					"indexed": false,
					"internalType": "address",
					"name": "controller",
					"type": "address"
				},
				{
					"indexed": false,
					"internalType": "address",
					"name": "reporter",
					"type": "address"
				},
				{
					"indexed": false,
					"internalType": "uint256",
					"name": "value",
					"type": "uint256"
				}
			],
			"name": "LogTxInfo",
			"type": "event"
		},
		{
			"inputs": [],
			"name": "getTxInfo",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [
				{
					"internalType": "address payable",
					"name": "_controller",
					"type": "address"
				},
				{
					"internalType": "string",
					"name": "_location",
					"type": "string"
				},
				{
					"internalType": "string",
					"name": "_swTrace",
					"type": "string"
				}
			],
			"name": "report",
			"outputs": [],
			"stateMutability": "payable",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "getLocationList",
			"outputs": [
				{
					"internalType": "string[]",
					"name": "",
					"type": "string[]"
				},
				{
					"internalType": "uint256",
					"name": "timestamp",
					"type": "uint256"
				},
				{
					"internalType": "uint256",
					"name": "interval",
					"type": "uint256"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "getMarkInfo",
			"outputs": [
				{
					"internalType": "address[]",
					"name": "reporter",
					"type": "address[]"
				},
				{
					"internalType": "string[]",
					"name": "markInfo",
					"type": "string[]"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "getReportList",
			"outputs": [
				{
					"internalType": "address[]",
					"name": "",
					"type": "address[]"
				},
				{
					"internalType": "uint256",
					"name": "timestamp",
					"type": "uint256"
				},
				{
					"internalType": "uint256",
					"name": "interval",
					"type": "uint256"
				}
			],
			"stateMutability": "view",
			"type": "function"
		}
	], contractAddr);

myContract.methods.getReportList().call({from: controller}, function(error, result){
//   console.log("Reporter nodeList: ", result);
//   console.log("Keys: ", Object.keys(result));
  const timestamp = result.timestamp;
  const date = new Date(timestamp * 1000);
  const formattedDate = date.toLocaleString('zh-CN', {year: 'numeric', month:'2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit'}).replace(/\/|\s|,/g, '-');
  console.log("TimeStamp: ", '\033[0;36m',formattedDate,'\033[0m');
});

// myContract.methods.getLocationList().call({from: controller}, function(error, result){
// //   console.log("Detected Attackers' LocationList: ", result);
//   console.log("Keys: ", Object.keys(result));
// });

// myContract.methods.getLocationList().call({from: controller}).then(function(result){
// 	console.log("Detected Attackers' LocationList: ", result);
// 	console.log("Keys: ", Object.keys(result));
//   });

myContract.methods.getMarkInfo().call({from: controller}, function(error, result){
	// console.log("MarkInfo: ", Object.values(result));
	// console.log("MarkInfo: ", Object.keys(result));
	console.log("Reporter nodeList: ");
	console.log(result.reporter);
	console.log("Detected Attackers' LocationList: ");
	console.log(result.markInfo);
});

// myContract.methods.getSwTraceList().call({from: controller}, function(error, result){
//   console.log("Detected Attackers' SwitchTraceList: ", result);
// });

// =======================================================================================
// event LogMarkInfo(address controller, address reporter, string swTrace);
// myContract.events.LogMarkInfo({
//   filter: {}, // Using an array means OR: e.g. 20 or 23
//   fromBlock: 0
// }, function(error, event){ console.log(event); })
// .on("connected", function(subscriptionId){
//   console.log(subscriptionId);
// })
// .on('data', function(event){
//   console.log(event); // same results as the optional callback above
// })
// .on('changed', function(event){
//   // remove event from local database
// })
// .on('error', function(error, receipt) { // If the transaction was rejected by the network with a receipt, the second parameter will be the receipt.
//   //...
// })
// ;

const logs = [];



myContract.getPastEvents('LogReport', {
	fromBlock: 0,
	toBlock:'latest' 
  }, function(error, events){ 
	if(!error) {
		logs.push(...events);
		console.log(`共获取到 ${events.length} 条LogReport事件数据`);
	} else {
		console.error(error);
	}
  }).then(function(){
	// console.log(Object.keys(events[0]))
	// console.log(Object.entries(events[1].returnValues)) // parse the keys of the events subobject
	logs.forEach(function(log) { // 遍历logs数组

		const blockNumber = log.blockNumber; // 获取区块号
		const data = log.returnValues; // 获取事件数据
		console.log("==========================================================");
		// console.log('\033[0;31m',"Catching events......",'\033[0m'); 
		console.log('\033[0;31m',`区块号: ${blockNumber}, 数据: `,'\033[0m'); // 打印数据
		// console.log("==========================================================");

		// console.log(Object.keys(data))
		// console.log(" Block Number:", data)
		// console.log('\033[;31m', "Collected Mark reportes as follow: ",'\033[0m')
		console.log("Center controller Address:", '\033[;32m ', data.controller,'\033[0m')
		console.log("Local switch Address:     ", '\033[;32m ', data.reporter,'\033[0m')
		console.log("Spoof Traceback SwIdPath: ", '\033[;32m ', data._swTrace,'\033[0m')
		console.log("Transfer Ether(per ether):", '\033[;32m ', web3.utils.fromWei(data.value, + 'ether'),'\033[0m')
		const timestamp = data.time;
		const date = new Date(timestamp * 1000);
		const formattedDate = date.toLocaleString('zh-CN', {year: 'numeric', month:'2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit'}).replace(/\/|\s|,/g, '-');
		console.log("TimeStamp: ", '\033[32m',formattedDate,'\033[0m');
	  });

	
  });

// 事件监听...
// myContract.getPastEvents('LogReport', {
// 	fromBlock: 0,
// 	toBlock:'latest' 
//   }, function(error, events){ 
// 	console.log("==========================================================");
// 	console.log('\033[0;36m',"Catching events......",'\033[0m'); 
// 	console.log("==========================================================");})
//   .then(function(events){
// 	// console.log(Object.keys(events[0]))
// 	// console.log(Object.entries(events[1].returnValues)) // parse the keys of the events subobject

// 	console.log(" Block Number:", events[0].blockNumber)
// 	console.log("\033[;31m Collected Mark reportes as follow: ")
// 	console.log("\033[;0m Center controller Address:", '\033[;32m ', events[0].returnValues.controller)
// 	console.log("\033[;0m Local switch Address:     ", '\033[;32m ', events[0].returnValues.reporter)
// 	console.log("\033[;0m Spoof Traceback SwIdPath: ", '\033[;32m ', events[0].returnValues._swTrace)
// 	console.log("\033[;0m Transfer Ether(per ether):", '\033[;32m ', web3.utils.fromWei(events[0].returnValues.value, + 'ether'))
//   });

 

//   myContract.getPastEvents('LogReport', {
// 	filter: {controller:'0x75c47A47694ceF5981ae160C86239127db5C322B'}, // Using an array means OR: e.g. 20 or 23
// 	fromBlock: 6,
// 	toBlock: 'latest'
//   }, function(error, events){ 
// 	console.log("\033[;36m==========================================================");
// 	console.log("Catching events......"); 
// 	console.log("==========================================================");})
//   .then(function(events){
// 	// console.log(Object.keys(events[0]))
// 	// console.log(Object.keys(events[0]))
// 	// console.log(Object.entries(events[1].returnValues)) // parse the keys of the events subobject
// 	console.log(" Block Number:", events[1].blockNumber)
// 	console.log("\033[;31m Collected Mark reportes as follow: " )
// 	console.log("\033[;0m Center controller Address:", '\033[;32m ', events[1].returnValues.controller)
// 	console.log("\033[;0m Local switch Address:     ", '\033[;32m ', events[1].returnValues.reporter)
// 	console.log("\033[;0m Spoof Traceback SwIdPath: ", '\033[;32m ', events[1].returnValues._swTrace)
// 	console.log("\033[;0m Transfer Ether(per ether):", '\033[;32m ', web3.utils.fromWei(events[1].returnValues.value, 'ether'))
//   });

//   myContract.getPastEvents('LogReport', {
// 	filter: {reporter:'0x3c1e6c97db29cbC026966e0E75129F2d8785D7C5'}, // Using an array means OR: e.g. 20 or 23
// 	fromBlock: 0
// 	// toBlock: 
//   }, function(error, events){ 
// 	console.log("\033[;36m==========================================================");
// 	console.log("Catching events......"); 
// 	console.log("==========================================================");})
//   .then(function(events){
// 	// console.log(Object.keys(events[1]))
// 	// console.log(Object.entries(events[1].returnValues)) // parse the keys of the events subobject
// 	console.log(" Block Number:", events[0].blockNumber + 1)
// 	console.log("\033[;31m Collected Mark reportes as follow: ")
// 	console.log("\033[;0m Center controller Address:", '\033[;32m ', events[1].returnValues.controller)
// 	console.log("\033[;0m Local switch Address:     ", '\033[;32m ', events[1].returnValues.reporter)
// 	console.log("\033[;0m Spoof Traceback SwIdPath: ", '\033[;32m ', events[1].returnValues._swTrace)
// 	console.log("\033[;0m Transfer Ether(per ether):", '\033[;32m ', web3.utils.fromWei(events[1].returnValues.value, 'ether'))
//   });


// event LogMarkInfo(address controller, address reporter, string swTrace);
// TODO : extract the returnValues from event
// myContract.getPastEvents('LogMarkInfo', {
//   filter: {}, // Using an array means OR: e.g. 20 or 23
//   fromBlock: 0,
//   toBlock: 'latest'
// }, function(error, events){ 
//   //console.log(events)
//   console.log("\033[;36m==========================================================");
//   console.log("Catching events......");
//   console.log("=========================================================="); })
// .then(function(events){
// //   console.log(Object.keys(events[0])) // parse the keys of the events
//   console.log("Block Number:", events[0].blockNumber)
//   console.log("Collected Mark reportes as follow:")
//   console.log("\033[;31m Center controller Address:", '\033[;32m ', events[0].returnValues.controller)
//   console.log("\033[;31m Local switch Address:     ", '\033[;32m ', events[0].returnValues.reporter)
//   console.log("\033[;31m Spoof Traceback SwIdPath: ", '\033[;32m ', events[0].returnValues.swTrace)
// });




// 监听事件
// myContract.events.LogReport({}, (error, event) => {
//   if (error) {
//     console.error(error);
//     return;
//   }

//   console.log(`LogReport event: ${JSON.stringify(event.returnValues)}`);
// });

// myContract.events.LogTxInfo({}, (error, event) => {
//   if (error) {
//     console.error(error);
//     return;
//   }

//   console.log(`LogTxInfo event: ${JSON.stringify(event.returnValues)}`);
// });




// ===========================================================================================

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
