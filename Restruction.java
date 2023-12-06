import jdk.jfr.Description;
import java.util.*;

public class Restruction {
    public static void main(String[] args) {
        int cnt = 0; // 计数器
        int fragment = 4; // 1-4 分片数
        int hopCount = 4; // 1-30 hop转发距离
        int probability = 10; // 5% 标记概率
        int testCount = 100; // 测试次数

        int[] nrmData = new int[testCount];
        int[] ppmData = new int[testCount];
        int[] oppmData = new int[testCount];

        // 运行 PPM 场景
        System.out.println("\nPPM Scenario:");
        ppmData = packetWithRemark("192.168.0.1", hopCount, probability, testCount);
        System.out.println("PPM Data: " + Arrays.toString(sortAndCopy(ppmData)));
        // 运行 NRM 场景
        System.out.println("NRM Scenario:");
        nrmData = packetVoidRemark("192.168.0.1", probability,  testCount);
        System.out.println("NRM Data: " + Arrays.toString(sortAndCopy(nrmData)));
        // 运行 OPPM 场景
//        System.out.println("\nOPPM Scenario:");
//        oppmData = packetdynamicRemark("192.168.0.1", hopCount, testCount);
//        System.out.println("OPPM Data: " + Arrays.toString(sortAndCopy(oppmData)));

        String[] dataset1 = {
//                "version;userID;timestamp;src;dst;method;stop;ttl;hopaddr;rtt",
                "scamper.20211212a;0;1643414357;157.92.44.100;38.1.133.94;icmp-echo-paris;GAPLIMIT;1;157.92.44.97;0.324",
                "scamper.20211212a;0;1643414357;157.92.44.100;38.1.133.94;icmp-echo-paris;GAPLIMIT;2;10.169.242.225;0.994",
                "scamper.20211212a;0;1643414357;157.92.44.100;38.1.133.94;icmp-echo-paris;GAPLIMIT;4;170.51.254.174;2.831",
                "scamper.20211212a;0;1643414357;157.92.44.100;38.1.133.94;icmp-echo-paris;GAPLIMIT;5;170.51.254.180;5.399",
                "scamper.20211212a;0;1643414357;157.92.44.100;38.1.133.94;icmp-echo-paris;GAPLIMIT;7;154.54.47.229;153.446",
                "scamper.20211212a;0;1643414357;157.92.44.100;38.1.133.94;icmp-echo-paris;GAPLIMIT;8;154.54.24.145;166.225",
                // ... 其他测试数据
        };

        // 提取 src 和 dst 字段，组成二维数组
        String[][] testData1 = extractSrcDst1(dataset1);
        System.out.println("\nTest Data 1: " + Arrays.deepToString(testData1));

        int testCount1 = testData1.length;
        // 收集数据的数组
        int[] nrmData1 = new int[testCount1];
        int[] ppmData1 = new int[testCount1];
        int[] oppmData1 = new int[testCount1];

        for (int i = 0; i < testCount1; i++) {
            // 提取 src
            String src = testData1[i][0];
            // PPM 场景
            ppmData1[i] = packetWithRemark1(src, hopCount, probability);

            // NRM 场景
            nrmData1[i] = packetVoidRemark1(src, probability);

            // OPPM 场景
//            oppmData1[i] = packetdynamicRemark1(src, hopCount, i);
        }

        // 输出收集到的数据
        System.out.println("\nData Collection:");
        System.out.println("NRM Data1: " + Arrays.toString(sortAndCopy(nrmData1)));
        System.out.println("PPM Data1: " + Arrays.toString(sortAndCopy(ppmData1)));
        System.out.println("OPPM Data1: " + Arrays.toString(sortAndCopy(oppmData1)));

        /** NRM*/
//        System.out.println(packetVoidRemark1("192.168.0.1", probability));
        /** PPM*/
//        System.out.println(packetWithRemark1("192.168.0.1", distance, probability));
        /** OPPM*/
//        System.out.println(packetdynamicRemark1("192.168.0.1", distance));

    }
    @Description("模拟覆盖标记的网络数据包多次传输")
    public static int[] packetWithRemark(String IPAddr, int distance, int probability, int testCount) {
        int[] ppmData = new int[testCount];

        // 执行 testCount 次过程
        for (int test = 0; test < testCount; test++) {
            int cnt = 0;
            Set<String> received = new HashSet<>();
            String tmp;

            // 模拟数据包传输
            for (int time = 1; time <= distance; time++) {
                for (int i = 0; i <= time;) {
                    while (received.size() < 4) {  // 假设 IPv4 地址有 4 分片
                        // 通过概率标记数据包，存在重复标记
                        tmp = splitPacket(IPAddr, probability);
                        if (!received.contains(tmp) && !tmp.equals("101")) {
                            received.add(tmp);
                        }
                        cnt += 1;
                    }
                    received.clear();
                    i++;
                }
            }
            ppmData[test] = cnt;
//            System.out.println("Test " + (test + 1) + ": " + cnt);
        }

        return ppmData;
    }
    @Description("模拟覆盖标记的网络数据包传输")
    public static int packetWithRemark1(String IPAddr, int hopCount, int probability) {
        int cnt = 0;
        Set<String> received = new HashSet<>();
        String tmp;
        for (int time = 1; time <= hopCount; time++) {
            while (received.size() < 4) {  // 假设 IPv4 地址有 4 分片
                // 通过概率标记数据包，存在重复标记
                tmp = splitPacket(IPAddr, probability);
                if (!received.contains(tmp) && !tmp.equals("-1")) {
                    received.add(tmp);
                }
                cnt += 1;
                }
            received.clear();
        }
        return cnt;
    }
    // 修改 packetdynamicRemark1 方法，接受测试次数作为参数，并返回数组形式的结果

    @Description("模拟没有重复标记的网络数据包多次传输")
    public static int[] packetVoidRemark(String IPAddr, int probability, int testCount) {
        int[] nrmData = new int[testCount];

        // 执行 testCount 次过程
        for (int test = 0; test < testCount; test++) {
            int cnt = 0;
            Set<String> received = new HashSet<>();
            String tmp;

            // 模拟数据包传输
            for (int time = 0; time < 300; time++) {
                while (received.size() < 4) {  // 假设 IPv4 地址有 4 分片
                    // 通过概率标记数据包，不重复标记
                    tmp = splitPacket(IPAddr, probability);
                    if (!received.contains(tmp) && !tmp.equals("-1")) {
                        received.add(tmp);
                    }
                    cnt += 1;
                }
                received.clear();
                nrmData[test] = cnt;
                cnt = 0;
            }
//            System.out.println("Test " + (test + 1) + ": " + cnt);
        }
        return nrmData;
    }
    @Description("模拟没有重复标记的网络数据包传输")
    public static int packetVoidRemark1(String IPAddr, int probability) {
        int cnt = 0;
        Set<String> received = new HashSet<>();
        String tmp;
        // 模拟数据包传输，假设有testCount次传输
        while (received.size() < 4) {  // 假设 IPv4 地址有 4 分片
            // 通过概率标记数据包，不重复标记
            tmp = splitPacket(IPAddr, probability);
            if (!received.contains(tmp) && !tmp.equals("-1")) {
                received.add(tmp);
            }
            cnt += 1;
        }
        received.clear();
        return cnt;
    }

    @Description("模拟标记概率随跳数变化的网络数据包多次传输")
    public static int[] packetdynamicRemark(String IPAddr, int hopCount, int testCount) {
        int[] oppmData = new int[testCount];

        // 执行 testCount 次过程
        for (int test = 0; test < testCount; test++) {
            int cnt = 0;
            int fragment = 4;  // 假设 IPv4 地址有 4 部分
            Map<String, Integer> recv = new HashMap<>();
            String tmp;

            // 模拟数据包传输
            for (int time = 1; time <= 30; time++) {
                while (recv.size() < fragment) {
                    int dynamicProbability = setDynamicProbability1(hopCount, time);
                    tmp = splitPacket(IPAddr, dynamicProbability);
                    if (!recv.containsKey(tmp) && !tmp.equals("101")) {
                        recv.put(tmp, 1);  // 使用 Map 存储已收到的数据包
                    }
                    cnt += 1;
                }
                recv.clear();
            }
            oppmData[test] = cnt;
            System.out.println("Test " + (test + 1) + ": " + cnt);
        }

        return oppmData;
    }
    @Description("模拟标记概率随跳数变化的网络数据包传输")
    public static int packetdynamicRemark1(String IPAddr, int hopCount, int count) {
        int cnt = 0;
        int fragment = 4;  // 假设 IPv4 地址有 4 部分
        Map<String, Integer> recv = new HashMap<>();
        String tmp;

        while (recv.size() < fragment) {
            int dynamicProbability = setDynamicProbability1(hopCount, count);
            tmp = splitPacket(IPAddr, dynamicProbability);
            if (!recv.containsKey(tmp) && !tmp.equals("-1")) {
                recv.put(tmp, 1);  // 使用 Map 存储已收到的数据包
            }
            cnt += 1;
        }
//        System.out.println(cnt);
        recv.clear();
        return cnt;
    }
    @Description("模拟数据包分片传输，通过概率标记数据包，每次返回一个 IPv4 地址的一分片")
    public static String splitPacket(String IPAddr, int probability) {
        String[] ipParts = IPAddr.split("\\.");
        int random = (int)(Math.random()*100);
        if (random < probability) {
            // 随机返回IPv4 地址的一部分,默认分成4部分
            int randomPartIndex = (int) (Math.random() * 4);
            return ipParts[randomPartIndex];
        } else {
            return "-1";
        }
    }
    @Description("模拟分片标记概率随 hop 跳数变化")
    private static int setDynamicProbability1(int hopCount, int i) {
        int basep = 1;
        float tmp ;
        if (i < 5) {
            tmp = (float) 1 / (5 + 1 - i);
            return (int)(tmp * 100);
        } else if (hopCount >= 5 && hopCount < 10) {
            tmp = 1 / (10 + 1 - i);
            return (int)(tmp * 100);
        } else if (hopCount >= 10 && hopCount < 15) {
            tmp = 1 / (15 + 1 - i);
            return (int)(tmp * 100);
        } else if (hopCount >= 15 && hopCount < 20) {
            tmp = 1 / (20 + 1 - i);
            return (int)(tmp * 100);
        } else if (hopCount >= 20 && hopCount < 25) {
            tmp = 1 / (25 + 1 - i);
            return (int)(tmp * 100);
        } else if (hopCount >= 25 && hopCount < 30) {
            tmp = 1 / (30 + 1 - i);
            return (int)(tmp * 100);
        }
        return basep * 100;
    }

    @Description("对数组进行排序并返回副本")
    public static int[] sortAndCopy(int[] array) {
        int[] sortedArray = Arrays.copyOf(array, array.length);
        Arrays.sort(sortedArray);
        return sortedArray;
    }

    @Description("提取 src 和 dst 字段，组成二维数组")
    public static String[][] extractSrcDst(String[] dataset) {
        String[][] testData = new String[dataset.length][2];

        for (int i = 0; i < dataset.length; i++) {
            String[] fields = dataset[i].split(";");
            testData[i][0] = fields[3].trim(); // src 字段
            testData[i][1] = fields[4].trim(); // dst 字段
        }

        return testData;
    }
    @Description("提取 src 和 dst 字段，组成二维数组")
    public static String[][] extractSrcDst1(String[] dataset) {
        int startIndex = 0;
        int endIndex = dataset.length;
        int rowCount = endIndex - startIndex;
        String[][] result = new String[rowCount][2];  // 2 表示 src 和 dst 两个字段

        // 动态检测标题栏的位置
        for (int i = 0; i < dataset.length; i++) {
            if (dataset[i].contains("version;userID;timestamp;src;dst;method;stop;ttl;hopaddr;rtt")) {
                startIndex = i + 1;
                break;
            }
        }

        for (int i = startIndex; i < endIndex; i++) {
            String[] fields = dataset[i].split(";");
            if (fields.length >= 10) {
                result[i - startIndex][0] = fields[3];  // src 字段
                result[i - startIndex][1] = fields[4];  // dst 字段
            }
        }
        return result;
    }
}
