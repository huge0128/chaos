# # from datasketch import CountMinSketch
# # {
# # # 初始化Count-Min Sketch
# # width = 1000
# # depth = 10
# # sketch = CountMinSketch(width, depth)

# # # 模拟五元组数据流
# # data_stream = [("192.168.0.1", "192.168.0.2", 80, "TCP", 100),
# #                ("192.168.0.1", "192.168.0.3", 443, "TCP", 200),
# #                ("192.168.0.1", "192.168.0.2", 80, "TCP", 150),
# #                ("192.168.0.1", "192.168.0.3", 80, "TCP", 300)]

# # # 使用sketch计算五元组计数
# # for data in data_stream:
# #     sketch.update(str(data))

# # # 输出五元组计数信息
# # for data in data_stream:
# #     count = sketch.query(str(data))
# #     print("五元组信息：{0}, 出现次数：{1}".format(data, count))
# # }|

# import mmh3
# import numpy as np

# # 创建一个名为Sketch的类
# class Sketch:
#     def __init__(self, width, depth):
#         self.width = width
#         self.depth = depth
#         self.table = np.zeros((depth, width))
#         self.hash_funcs = [mmh3.hash]

#     def increment(self, key):
#         for i in range(self.depth):
#             print(self.hash_funcs[i](key),self.width)
#             index = self.hash_funcs[i](key) % self.width
#             self.table[i, index] += 1
    
#     def get_freq(self, key):
#         return min([self.table[i][self.hash_funcs[i](key) % self.width] for i in range(self.depth)])

# # 初始化Sketch
# width = 1000
# depth = 10
# sketch = Sketch(width, depth)

# # 模拟五元组数据流
# # data_stream = [("192.168.0.1", "192.168.0.2", 80, "UDP", 100),
# #                ("192.168.0.1", "192.168.0.3", 443, "UDP", 200),
# #                ("192.168.0.1", "192.168.0.2", 80, "UDP", 150),
# #                ("192.168.0.1", "192.168.0.3", 80, "UDP", 300)]

# data_stream = [("76"),
#                ("76"),
#                ("76")]

# # 使用sketch计算五元组计数
# for data in data_stream:
#     sketch.increment(str(data))

# # 输出五元组计数信息
# for data in data_stream:
#     count = sketch.get_freq(str(data))
#     print("五元组信息：{0}, 出现次数：{1}".format(data, count))

# import socket
# import zlib

# # 定义Count-Min Sketch算法的参数
# num_rows = 1000
# num_cols = 100
# sketch_table = [[0] * num_cols for i in range(num_rows)]
# eps = 0.001
# delta = 0.0001

# # 定义哈希函数
# def hash_func(data, seed):
#     return zlib.crc32(data, seed) & (num_cols - 1)

# # 添加随机生成的五元组数据
# five_tuples = [
#     ("192.168.1.1", "10.0.0.1", 12345, 80, "TCP"),
#     ("192.168.1.2", "10.0.0.2", 23456, 8080, "UDP"),
#     ("192.168.1.3", "10.0.0.3", 34567, 443, "TCP"),
#     ("192.168.1.4", "10.0.0.4", 45678, 3389, "TCP"),
#     ("192.168.1.5", "10.0.0.5", 56789, 53, "UDP"),
#     ("192.168.1.6", "10.0.0.6", 67890, 3306, "TCP"),
#     ("192.168.1.7", "10.0.0.7", 78901, 1194, "UDP"), 
#     ("192.168.1.8", "10.0.0.8", 89012, 69, "UDP"),
#     ("192.168.1.9", "10.0.0.9", 90123, 22, "TCP"),
#     ("192.168.1.10", "10.0.0.10", 3456, 161, "UDP")
# ]

# # 对所有五元组进行计数
# for five_tuple in five_tuples:
#     # 将五元组转换成二进制表示
#     data = bytes(five_tuple)
    
#     # 对五元组进行计数
#     for i in range(num_rows):
#         seed = i
#         col_index = hash_func(data, seed)
#         row_index = i
#         sketch_table[row_index][col_index] += 1

# # 统计源地址的计数结果
# source_address_counter = {}
# for i in range(num_rows):
#     min_counter = float('Inf')
#     for j in range(num_cols):
#         min_counter = min(min_counter, sketch_table[i][j])
#     source_address_counter[hash(i)] = min_counter

# # 打印源地址的计数结果
# for src_addr, counter in source_address_counter.items():
#     print("源地址为：", src_addr, "，计数器值为：", counter)

import random


def hash_function(data):
    # 使用Python内置哈希函数将数据转换为哈希值
    hash_value = hash(data)
    # 将哈希值映射到范围为0到127的数值
    index = hash_value % 128
    return index

# def hash_function_2(data):
#     # 通过将数据的字符值相加得到哈希值
#     hash_value = sum(ord(c) for c in data)
#     # 将哈希值映射到范围为0到127的数值
#     index = hash_value % 128
#     return index

# def hash_function_3(data):
#     # 使用字符串长度作为哈希值
#     hash_value = len(data)
#     # 将哈希值映射到范围为0到127的数值
#     index = hash_value % 128
#     return index

# def hash_function_4(data):
#     # 哈希值为数据中所有字符的 Unicode 码点的乘积
#     hash_value = 1
#     for c in data:
#         hash_value *= ord(c)
#     # 将哈希值映射到范围为0到127的数值
#     index = hash_value % 128
#     return index



# 将数据分配到哈希表中
def put_data_in_hash_table(hash_table, data):
    index = hash_function(data)
    hash_table[index].append(data)

# 计算每个哈希单元中的元素数量
def count_elements_in_hash_table(hash_table):
    counts = [len(hash_table[i]) for i in range(128)]
    return counts

# 生成100条网络五元组的测试数据
network_tuples = [("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
                  ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
                  ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
                  ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
                  ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
                  ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
                  ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
                  ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
                  ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
                  ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established")] + \
                 [("10.0.0."+str(i), "192.168.0."+str(i%2+1), i%1000, "TCP" if i%2==0 else "UDP", "established" if i%3==0 else "closed") for i in range(10, 100)]

# network_tuples = [("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),  
#                   ("10.0.0.2", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),
#                   ("10.0.0.1", "192.168.0.1", 80, "TCP", "established"),               
# ]

# 生成100条网络五元组的测试数据
# network_tuples = [("10.0.1.1", "10.0.2.2"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established"),
#                   ("10.0.1.1", "10.0.3.3", 80, "UDP", "established"),
#                   ("192.168.0.1", "10.0.0.1", 80, "TCP", "established"),
#                   ("10.0.0.2", "192.168.0.2", 443, "HTTPS", "established"),
#                   ("192.168.0.2", "10.0.0.2", 443, "HTTPS", "established"),
#                   ("10.0.0.3", "192.168.0.1", 22, "SSH", "established"),
#                   ("192.168.0.1", "10.0.0.3", 22, "SSH", "established"),
#                   ("10.0.0.4", "192.168.0.2", 53, "UDP", "open"),
#                   ("192.168.0.2", "10.0.0.4", 53, "UDP", "open"),
#                   ("10.0.0.5", "192.168.0.1", 443, "HTTPS", "established"),
#                   ("192.168.0.1", "10.0.0.5", 443, "HTTPS", "established")
# ]


# network_tuples = [("10.0.1.1", "10.0.2.2"),
#                   ("10.0.1.1", "10.0.3.3"),
#                   ("10.0.1.1", "10.0.4.4"),
#                   ("10.0.1.1", "10.0.5.5"),
#                   ("10.0.1.1", "10.0.6.6"),
#                   ("10.0.1.1", "10.0.1.11"),
#                   ("10.0.1.1", "10.0.2.22"),
#                   ("10.0.1.1", "10.0.4.44"),
#                   ("10.0.2.2", "10.0.1.1"),
#                   ("10.0.2.2", "10.0.3.3"),
#                   ("10.0.2.2", "10.0.4.4"),
#                   ("10.0.2.2", "10.0.5.5"),
#                   ("10.0.2.2", "10.0.6.6"),
#                   ("10.0.2.2", "10.0.1.11"),
#                   ("10.0.2.2", "10.0.2.22"),
#                   ("10.0.2.2", "10.0.4.44"),
#                   ("10.0.3.3", "10.0.1.1"),
#                   ("10.0.3.3", "10.0.2.2"),
#                   ("10.0.3.3", "10.0.4.4"),
#                   ("10.0.3.3", "10.0.5.5"),
#                   ("10.0.3.3", "10.0.6.6"),
#                   ("10.0.3.3", "10.0.1.11"),
#                   ("10.0.3.3", "10.0.2.22"),
#                   ("10.0.3.3", "10.0.4.44"),
#                   ("10.0.4.4", "10.0.1.1"),
#                   ("10.0.4.4", "10.0.3.3"),
#                   ("10.0.4.4", "10.0.2.2"),
#                   ("10.0.4.4", "10.0.5.5"),
#                   ("10.0.4.4", "10.0.6.6"),
#                   ("10.0.4.4", "10.0.1.11"),
#                   ("10.0.4.4", "10.0.2.22"),
#                   ("10.0.4.4", "10.0.4.44"),
#                   ("10.0.5.5", "10.0.1.1"),
#                   ("10.0.5.5", "10.0.3.3"),
#                   ("10.0.5.5", "10.0.4.4"),
#                   ("10.0.5.5", "10.0.2.2"),
#                   ("10.0.5.5", "10.0.6.6"),
#                   ("10.0.5.5", "10.0.1.11"),
#                   ("10.0.5.5", "10.0.2.22"),
#                   ("10.0.5.5", "10.0.4.44"),
#                   ("10.0.6.6", "10.0.1.1"),
#                   ("10.0.6.6", "10.0.3.3"),
#                   ("10.0.6.6", "10.0.4.4"),
#                   ("10.0.6.6", "10.0.5.5"),
#                   ("10.0.6.6", "10.0.2.2"),
#                   ("10.0.6.6", "10.0.1.11"),
#                   ("10.0.6.6", "10.0.2.22"),
#                   ("10.0.6.6", "10.0.4.44"),
#                   ("10.0.1.11", "10.0.1.1"),
#                   ("10.0.1.11", "10.0.3.3"),
#                   ("10.0.1.11", "10.0.4.4"),
#                   ("10.0.1.11", "10.0.5.5"),
#                   ("10.0.1.11", "10.0.6.6"),
#                   ("10.0.1.11", "10.0.2.2"),
#                   ("10.0.1.11", "10.0.2.22"),
#                   ("10.0.1.11", "10.0.4.44"),
#                   ("10.0.2.22", "10.0.1.1"),
#                   ("10.0.2.22", "10.0.3.3"),
#                   ("10.0.2.22", "10.0.4.4"),
#                   ("10.0.2.22", "10.0.5.5"),
#                   ("10.0.2.22", "10.0.6.6"),
#                   ("10.0.2.22", "10.0.1.11"),
#                   ("10.0.2.22", "10.0.2.2"),
#                   ("10.0.2.22", "10.0.4.44"),
#                   ("10.0.4.44", "10.0.1.1"),
#                   ("10.0.4.44", "10.0.3.3"),
#                   ("10.0.4.44", "10.0.4.4"),
#                   ("10.0.4.44", "10.0.5.5"),
#                   ("10.0.4.44", "10.0.6.6"),
#                   ("10.0.4.44", "10.0.1.11"),
#                   ("10.0.4.44", "10.0.2.22"),
#                   ("10.0.4.44", "10.0.2.22"),
#                   ("10.0.4.44", "10.0.2.2")                
# ]

# for i in range(90):
#     # 随机生成源 IP 地址和目标 IP 地址
#     src_ip = "10.0.0." + str(random.randint(1, 254))
#     dst_ip = "192.168.0." + str(random.randint(1, 254))

#     # 随机生成源端口和目标端口
#     src_port = random.randint(1, 65535)
#     dst_port = random.randint(1, 65535)

#     # 随机选择协议
#     protocol = random.choice(["TCP", "UDP"])

#     # 随机确定连接状态
#     status = random.choice(["established", "closed", "open"])

#     # 加入生成的五元组数据到队列
#     network_tuples.append((src_ip, dst_ip, src_port, protocol, status))

# flows = []
# for flow_id in range(9):
#     # 生成当前流的五元组数据
#     src_ip = "10.0." + str(flow_id+1) + ".1"
#     dst_ip = "192.168." + str(flow_id+1) + ".1"
#     src_port = random.randint(10000, 65535)
#     dst_port = random.randint(10000, 65535)
#     protocol = random.choice(["TCP", "UDP"])
#     status = "established"
#     flow = []
#     for i in range(10):
#         # 生成当前流的五元组信息并添加到流列表中
#         src_ip_in_flow = "10.0." + str(flow_id+1) + "." + str(random.randint(1, 254))
#         dst_ip_in_flow = "192.168." + str(flow_id+1) + "." + str(random.randint(1, 254))
#         src_port_in_flow = src_port
#         dst_port_in_flow = dst_port
#         protocol_in_flow = protocol
#         status_in_flow = status
#         network_tuple_in_flow = (src_ip_in_flow, dst_ip_in_flow, src_port_in_flow, protocol_in_flow, status_in_flow)
#         flow.append(network_tuple_in_flow)
#     # 将当前流添加到流列表中
#     flows.append(flow)

# # 打印生成的流的五元组数据
# for flow in flows:
#     for network_tuple in flow:
#         print(network_tuple)



# 创建一个包含128个空列表的哈希表
hash_table = [[] for _ in range(128)]

# 将数据添加到哈希表
# put_data_in_hash_table(hash_table, "hello")
# put_data_in_hash_table(hash_table, "world")
# put_data_in_hash_table(hash_table, "this")
# put_data_in_hash_table(hash_table, "is")
# put_data_in_hash_table(hash_table, "a")
# put_data_in_hash_table(hash_table, "test")

for network_tuple in network_tuples:
    put_data_in_hash_table(hash_table, network_tuple)

# for network_tuple in network_tuples:
#     put_data_in_hash_table(hash_table, network_tuple)




# 计算哈希表中每个单元格中的元素数量
counts = count_elements_in_hash_table(hash_table)

# # 统计五元组信息的出现次数
# count_results = {}
# for network_tuple in network_tuples:
#     count = cms.check_count(str(network_tuple))
#     count_results[str(network_tuple)] = count

# 输出结果以显示每个哈希单元中有多少元素
for i in range(128):
    # print("Hash index", i, "contains", counts[i], "elements")
    print(counts[i])

# 统计准确率
accuracy = 0
for network_tuple in network_tuples:
    if count_results[str(network_tuple)] == network_tuples.count(network_tuple):
        accuracy += 1
accuracy /= len(network_tuples)
print(f"准确率为：{accuracy:.2%}")
