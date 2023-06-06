// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <=0.9.0;

import "./BokkyPooBahsDateTimeContract.sol";
import "./BokkyPooBahsDateTimeLibrary.sol";
// import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// controller 
// contract spoofingRecord{
        
//     string location;
//     string swTrace;
//     uint public dos_counter; // 公开遭遇攻击次数
//     address recorder;

//     event LogUpdate(string indexed swTrace, string indexed location);

//     constructor() {
//     // 初始化最初状态
//     location = "unknown";
//     recorder = msg.sender;
//     dos_counter = 0;
//     }

//     // 对写入者recorder进行限制
//     modifier checkOwner(address _addr) {
//         //require(condition, <String> 不符合条件返回提示);
//         require(_addr == recorder, "Permission denied");
//         dos_counter += 1;
//         _;
//     }

//         /*
//     {[recorder: "192.168.10.3"? or "S3"];
//         [switchtrace: "1/5/2/"];
//         [attacker: "192.168.10.2"? or "s2"];
//     }
//     enum attackType {black, gray}
//     struct cell{
//         address recorder; //switch log
//         string  swTrace;// attack path
//         string  location;// location
        
//     }
//     */

//     function setRecord(string memory _switchtrace, string memory _location
//     /*string memory _attackType*/) public checkOwner(msg.sender) returns (string memory) {
//         recorder = msg.sender;
//         swTrace = _switchtrace;
//         location = _location;
//         //attackType = _attackType;
//         emit LogUpdate(swTrace, location);
//         return location;
//     }
    
//     function getReocrd() public view returns(string memory) {
//         return swTrace ;
//     }
// }

contract SpoofRecord {
    // using SafeMath for uint256; // 使用safemath库
    using BokkyPooBahsDateTimeLibrary for uint256;
    // using BokkyPooBahsDateTimeContract for uint256;

    // 可疑数据统计摘要：受害者信息和目的端口
    struct VictimAlliance{
        string srcIPAddress;
        string dstPort;
        uint timestamp;
        uint cnt;
        uint  frequency; // 暂时未使用
    }

    // map(node, victimSet)
    mapping(string=>VictimAlliance) victimAlliances;
    address[] public peers;
    address public owner;
    constructor() {
        owner = msg.sender;
    }

    event RecordSet(address indexed sender, string indexed srcIP, string  srcIPAddress, string dstPort);

    function addPeer(address _peer) public {
        require(msg.sender == owner, "Only contract owner can add peers");
        peers.push(_peer);
    }

    function setRecord(string memory srcIPAddress, string memory dstPort) public {
        require(isPeer(msg.sender), "Only authorized peers can set record");
        uint time = 2000000;
        uint timestamp = block.timestamp - time;
        if(victimAlliances[srcIPAddress].timestamp == 0) {
            victimAlliances[srcIPAddress] = VictimAlliance({
                srcIPAddress : srcIPAddress,
                dstPort : dstPort,
                timestamp : timestamp,
                cnt : 1,
                frequency : 0
            });
        } else {
            victimAlliances[srcIPAddress].cnt += 1;
            // victimAlliances[srcIPAddress].timestamp = timestamp;
            uint lastTimestamp = victimAlliances[srcIPAddress].timestamp;
            uint lastCnt = victimAlliances[srcIPAddress].cnt;
            uint currentFrequency = timestamp;
            if (lastCnt > 1) {
                // currentFrequency = (timestamp - lastTimestamp) / (lastCnt - 1);
                currentFrequency = (timestamp - lastTimestamp);
            }
            victimAlliances[srcIPAddress].frequency = currentFrequency;
            victimAlliances[srcIPAddress].timestamp = timestamp;
        }
        emit RecordSet(msg.sender, srcIPAddress, srcIPAddress, dstPort);
    }

    function getRecord(string memory srcIPAddress) public view returns(string memory srcIP, string memory dstPort, uint timestamp, uint count, uint interval) {
        
        
        VictimAlliance storage victimAlliance = victimAlliances[srcIPAddress];

        return (victimAlliance.srcIPAddress, victimAlliance.dstPort, victimAlliance.timestamp, victimAlliance.cnt, victimAlliance.frequency);
    }

    function getDate(uint256 timestamp) public pure returns (uint year, uint month, uint day, uint hour, uint minute, uint second) {
        return timestamp.timestampToDateTime();
    }

    function isPeer(address _address) private view returns (bool) {
        for(uint i = 0; i < peers.length; i++) {
            if(peers[i] == _address) {
                return true;
            }
        }
        return false;
    }
}
