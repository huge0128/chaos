const { error } = require('console');
const e = require('cors');
const Web3 = require('web3');
const web3 = new Web3('http://localhost:8545'); // 这里使用本地的以太坊节点

const contractAddress = '0xE5D63B33f2f89c4b52BAf6755AE2b53B759760a2'; // 合约地址
const contractABI = [
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
]; // 合约ABI

const contract = new web3.eth.Contract(contractABI, contractAddress);// 创建合约实例

const srcIPAddress = '10.0.1.1'; // 假设这是源IP地址
const dstPort = '123'; // 假设这是目的端口

const controller = '0x9054D3779a16fdA9C4deEf97f0fBDd620126581F';
const location = "10.0.4.4";
const swTrace = "s2-eth2<-s3-eth3<-s4-eth2";
const value = web3.utils.toWei('1', 'ether');

const account = '0x9054D3779a16fdA9C4deEf97f0fBDd620126581F'; // 使用的账户地址
const privateKey = '0x8c30affb3dcd104628f500581259f4b6e2d28f2abe3836cad6f22356f81d399f'; // 账户对应的私钥
// account = web3.eth.accounts.privateKeyToAccount(privateKey);

// 调用setRecord函数
// const setRecordData = contract.methods.setRecord(controller, location, swTrace).encodeABI();
// const setRecordTx = {
//   from: account,
//   to: contractAddress,
//   gas: 2000000,
//   gasPrice: 1000000000,
//   data: setRecordData,
// };


contract.methods.report(controller, location, swTrace).send({
    from:account,
    to: contractAddress,
    value: value,
    gas: 3000000,
    gasPrice: 10000000000
}).then(receipt => {
    console.log(receipt);
}).catch(error => {
    console.error(error);
});

// web3.eth.accounts.signTransaction(setRecordTx, privateKey).then(signed => {
//   web3.eth.sendSignedTransaction(signed.rawTransaction).on('receipt', receipt => {
//     console.log('setRecord receipt:', receipt);
//   });
// });
    // // 调用getRecord函数
    // const getRecordData = contract.methods.getRecord(srcIPAddress).encodeABI();
    // const getRecordTx = {
    //   from: account,
    //   to: contractAddress,
    //   gas: 2000000,
    //   gasPrice: 1000000000,
    //   data: getRecordData,
    // };

    // web3.eth.call(getRecordTx).then(result => {
    //   const [srcIP, dstPort, timestamp, count, interval] = web3.eth.abi.decodeParameters(['string', 'string', 'uint', 'uint', 'uint'], result);
    //   console.log(`getRecord result - srcIP: ${srcIP}`);
    //   console.log(`getRecord result - dstPort: ${dstPort}`);
    //   console.log(`getRecord result - timestamp: ${timestamp}`);
    //   console.log(`getRecord result - count: ${count}`);
    //   console.log(`getRecord result - interval: ${interval}`);
    // })
    // .catch(error =>{
    //     console.error('getRecord error:', error);
    // });

    // 调用getDate函数
    // const timestamp = 1624825476; // 假设这是一个时间戳
//     const getDateData = contract.methods.getDate(timestamp).encodeABI();
//     const getDateTx = {
//       from: account,
//       to: contractAddress,
//       gas: 2000000,
//       gasPrice: 1000000000,
//       data: getDateData,
//     };

//     web3.eth.call(getDateTx).then(result => {
//       const [year, month, day, hour, minute, second] = web3.eth.abi.decodeParameters(['uint', 'uint', 'uint', 'uint', 'uint', 'uint'], result);
//       console.log(`getDate result - year: ${year}`);
//       console.log(`getDate result - month: ${month}`);
//       console.log(`getDate result - day: ${day}`);
//       console.log(`getDate result - hour: ${hour}`);
//       console.log(`getDate result - minute: ${minute}`);
//       console.log(`getDate result - second: ${second}`);
//     })
//     .catch(error => {
//         console.error('getdate error:', error);
//     });
//   });
