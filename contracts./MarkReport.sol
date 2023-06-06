// pragma solidity >=0.7.0;

// import "./BokkyPooBahsDateTimeContract.sol";
// import "./BokkyPooBahsDateTimeLibrary.sol";

// // switch 
// contract MarkReport {
    
//     using BokkyPooBahsDateTimeLibrary for uint256;
    
//     struct MarkInfo {
//         address[] reporters; // ethereum address
//         string[] locations; //  ip address 

//         mapping(address => string) Markdata;  
//         mapping(address => uint) MarkLedger;

//         uint timestamp;
//         uint frequency;
//     }
    
//     mapping(address => MarkInfo) MarkHistory;

//     event LogReport(address controller, address reporter,
//      string location, uint value, string _swTrace);

//     //function isLedgerMember(address _controller) public view returns (bool isLedgerMember) {
//     //    if (MarkHistory)[_controller].MarkLedger[msg.sender] == 0 {
//     //        return ture;
//     //    }
//     //    return false;
//     //}

//     //function insertMarkInfo(address _controller, string memory _location) public payable {
//     //    if(isLedgerMember) {
//     //        MarkHistory[_controller].reporters.push(msg.sender);
//     //        MarkHistory[_controller].locations.push(_location);
//     //    }
//     //}

//     //funtion limitTransfer(address payable _controller) public payable {
//     //    require(msg.value > 0);
//     //    _controller.transfer(msg.value);
//     //}

//     function report(address payable _controller, string memory _location,
//      string memory _swTrace) public payable {
//         require(msg.value > 0); // 有成本的发送
//         _controller.transfer(msg.value);

//         uint time = 2000000;
//         uint timestamp = block.timestamp - time;

//         if(MarkHistory[_controller].MarkLedger[msg.sender] == 0) {
//             MarkHistory[_controller].reporters.push(msg.sender);
//             MarkHistory[_controller].locations.push(_location);
//         }

//         MarkHistory[_controller].MarkLedger[msg.sender] += msg.value;
//         MarkHistory[_controller].Markdata[msg.sender] = _swTrace;

//         uint lastTimestamp = MarkHistory[_controller].timestamp;

//         MarkHistory[_controller].timestamp = timestamp;
//         MarkHistory[_controller].frequency = timestamp - lastTimestamp;

//         emit LogReport(_controller, msg.sender, _location, msg.value, _swTrace);
//     }

//     //sw Info
//     function getReportList() public view returns (address[] memory, uint timestamp, uint interval) {
//         return (MarkHistory[msg.sender].reporters, MarkHistory[msg.sender].timestamp, MarkHistory[msg.sender].frequency);
//     }
//     //location Info
//     function getLocationList() public view returns (string[] memory, uint timestamp, uint interval) {
//         return (MarkHistory[msg.sender].locations, MarkHistory[msg.sender].timestamp, MarkHistory[msg.sender].frequency);
//     }

//     //transaction info
//     event LogTxInfo(address controller, address reporter, uint value);
//     function getTxInfo() public {
//         for(uint i = 0; i < MarkHistory[msg.sender].reporters.length; i++) {
//             address reporter = MarkHistory[msg.sender].reporters[i];
//             emit LogTxInfo(msg.sender, reporter, MarkHistory[msg.sender].MarkLedger[reporter]); 
//         }
//     }

//     //markTrace info
//     event LogMarkInfo(address controller, address reporter, string swTrace);
//     function getMarkInfo() public returns (address[] memory reporter, string[] memory markInfo) {
//         // for(uint i = 0; i < MarkHistory[msg.sender].reporters.length; i++) {
//         //     address reporterss = MarkHistory[msg.sender].reporters[i];
//         //     emit LogMarkInfo(msg.sender, reporterss, MarkHistory[msg.sender].Markdata[reporterss]);
//         // }
//         return (MarkHistory[msg.sender].reporters,MarkHistory[msg.sender].locations);
//     }
// }

// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;
import "./BokkyPooBahsDateTimeContract.sol";
import "./BokkyPooBahsDateTimeLibrary.sol";

// switch 
contract MarkReport {
    using BokkyPooBahsDateTimeLibrary for uint256;
    struct MarkInfo {
        address[] reporters; // ethereum address
        string[] locations; //  ip address 

        mapping(address => string) Markdata;  
        mapping(address => uint) MarkLedger;

        uint timestamp;
        uint frequency;
    }
    
    mapping(address => MarkInfo) MarkHistory;

    event LogReport(address controller, address reporter,
     string location, uint value, string _swTrace, uint time);

    //function isLedgerMember(address _controller) public view returns (bool isLedgerMember) {
    //    if (MarkHistory)[_controller].MarkLedger[msg.sender] == 0 {
    //        return ture;
    //    }
    //    return false;
    //}

    //function insertMarkInfo(address _controller, string memory _location) public payable {
    //    if(isLedgerMember) {
    //        MarkHistory[_controller].reporters.push(msg.sender);
    //        MarkHistory[_controller].locations.push(_location);
    //    }
    //}

    //funtion limitTransfer(address payable _controller) public payable {
    //    require(msg.value > 0);
    //    _controller.transfer(msg.value);
    //}

    function report(address payable _controller, string memory _location,
     string memory _swTrace) public payable {
        require(msg.value > 0); // 有成本的发送
        _controller.transfer(msg.value);

        if(MarkHistory[_controller].MarkLedger[msg.sender] == 0) {
            MarkHistory[_controller].reporters.push(msg.sender);
            MarkHistory[_controller].locations.push(_location);
        }

        MarkHistory[_controller].MarkLedger[msg.sender] += msg.value;
        MarkHistory[_controller].Markdata[msg.sender] = _swTrace;
        //
        uint lastTimestamp = MarkHistory[_controller].timestamp;

        MarkHistory[_controller].timestamp = timestamp;
        MarkHistory[_controller].frequency = timestamp - lastTimestamp;

        emit LogReport(_controller, msg.sender, _location, msg.value, _swTrace, timestamp);
    }
    //sw Info
    function getReportList() public view returns (address[] memory, uint timestamp, uint interval) {
        return (MarkHistory[msg.sender].reporters, 
        MarkHistory[msg.sender].timestamp, MarkHistory[msg.sender].frequency);
    }
    //location Info
    function getLocationList() public view returns (string[] memory, uint timestamp, uint interval) {
        return (MarkHistory[msg.sender].locations, MarkHistory[msg.sender].timestamp, MarkHistory[msg.sender].frequency);
    }

    //transaction info
    event LogTxInfo(address controller, address reporter, uint value);
    function getTxInfo() public {
        for(uint i = 0; i < MarkHistory[msg.sender].reporters.length; i++) {
            address reporter = MarkHistory[msg.sender].reporters[i];
            emit LogTxInfo(msg.sender, reporter, MarkHistory[msg.sender].MarkLedger[reporter]); 
        }
    }

    //markTrace info
    // event LogMarkInfo(address controller, address reporter, string swTrace);
    function getMarkInfo() public view returns (address[] memory reporter, string[] memory markInfo) {
        // for(uint i = 0; i < MarkHistory[msg.sender].reporters.length; i++) {
        //     address reporter = MarkHistory[msg.sender].reporters[i];
        //     emit LogMarkInfo(msg.sender, reporter, MarkHistory[msg.sender].Markdata[reporter]);
        // }
        return (MarkHistory[msg.sender].reporters,MarkHistory[msg.sender].locations);
    }
}
