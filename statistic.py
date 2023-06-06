import math
import random
import numpy as np



# 统计流量数据集中每个源地址出现的次数
def count_src_addresses(data):
    src_addresses = {}
    for d in data:
        if d['src_address'] in src_addresses:
            src_addresses[d['src_address']] += 1
        else:
            src_addresses[d['src_address']] = 1
    return src_addresses

# 计算熵值
def entropy(data):
    total = len(data)
    src_addresses = count_src_addresses(data)
    entropy_value = 0.0
    for count in src_addresses.values():
        p = float(count) / total
        entropy_value -= p * math.log(p, 2)
    return entropy_value

# 测试代码
# 单次统计
# data = [
#     {'src_address': '10.0.0.1'},
#     {'src_address': '10.0.0.2'},
#     {'src_address': '10.0.0.3'},
#     {'src_address': '10.0.0.1'},
#     {'src_address': '10.0.0.2'},
#     {'src_address': '10.0.0.3'},
#     {'src_address': '10.0.0.1'},
#     {'src_address': '10.0.0.2'},
#     {'src_address': '10.0.0.4'},
#     {'src_address': '10.0.0.5'},
# ]
# print(entropy(data))

# 测试代码
# 多次统计
# data_sets = [
#     [
#         {'src_address': '10.0.0.1'},
#         {'src_address': '10.0.0.2'},
#         {'src_address': '10.0.0.3'},
#         {'src_address': '10.0.0.1'},
#         {'src_address': '10.0.0.2'},
#         {'src_address': '10.0.0.3'},
#         {'src_address': '10.0.0.1'},
#         {'src_address': '10.0.0.2'},
#         {'src_address': '10.0.0.4'},
#         {'src_address': '10.0.0.5'},
#     ],
#     [
#         {'src_address': '10.0.0.1'},
#         {'src_address': '10.0.0.2'},
#         {'src_address': '10.0.0.3'},
#         {'src_address': '10.0.0.1'},
#     ],
#     [
#         {'src_address': '10.0.0.1'},
#         {'src_address': '10.0.0.2'},
#         {'src_address': '10.0.0.1'},
#         {'src_address': '10.0.0.3'},
#         {'src_address': '10.0.0.1'},
#     ],
# ]


# 模拟生成一百组随机数据
# data_sets = []
# for i in range(100):
#     data = []
#     for j in range(100):
#         data.append({'src_address': f'10.0.0.{random.randint(1, 10)}'})
#     data_sets.append(data)

# 模拟90组低频流量和10组高频流量
data_sets = []
low_freq_data = []
for i in range(33):
    data = []
    for j in range(100):
        data.append({'src_address': f'10.0.0.{random.randint(1, 100)}'})
        # data.append({'src_address': f'10.0.0.{i+1}'})
    # low_freq_data.extend(data)
    data_sets.append(data)


high_freq_data = []
for i in range(33):
    data = []
    for j in range(100):
        data.append({'src_address': f'10.0.0.{random.randint(1, 10)}'})
        # data.append({'src_address': f'10.0.0.{i+1}'})
    # high_freq_data.extend(data)
    data_sets.append(data)

low_freq_data = []
for i in range(33):
    data = []
    for j in range(100):
        data.append({'src_address': f'10.0.0.{random.randint(1, 100)}'})
        # data.append({'src_address': f'10.0.0.{i+1}'})
    # low_freq_data.extend(data)
    data_sets.append(data)

# 计算所有数据集的熵值，并输出结果
entropies = []
for i, data in enumerate(data_sets):
    entropies.append(entropy(data))
    # print(f"数据集{i+1}的熵值: {entropies[-1]}")
np.savetxt('ddos.csv', entropies, delimiter=',')

# 计算平均熵值
mean_entropy = sum(entropies) / len(entropies)
print(f"所有数据集的平均熵值: {mean_entropy}")

for i, data in enumerate(data_sets):
    # print(f"熵值{str(i+1)}: {entropy(data)}")
    print(f"  {entropy(data)}")
