def hash_function_1(data):
    # 使用Python内置哈希函数将数据转换为哈希值
    hash_value = hash(data)
    # 将哈希值映射到范围为0到127的数值
    index = hash_value % 128
    return index

def hash_function_2(data):
    # 通过将数据的字符值相加得到哈希值
    hash_value = sum(ord(c) for c in data)
    # 将哈希值映射到范围为0到127的数值
    index = hash_value % 128
    return index

def hash_function_3(data):
    # 使用字符串长度作为哈希值
    hash_value = len(data)
    # 将哈希值映射到范围为0到127的数值
    index = hash_value % 128
    return index

def hash_function_4(data):
    # 哈希值为数据中所有字符的 Unicode 码点的乘积
    hash_value = 1
    for c in data:
        hash_value *= ord(c)
    # 将哈希值映射到范围为0到127的数值
    index = hash_value % 128
    return index

# 将数据分配到哈希表中
def put_data_in_hash_table(hash_tables, data):
    # 使用哈希函数将数据映射到四个不同的哈希值
    indexes = [f(data) for f in hash_functions]
    # 获取每个哈希表上的桶的大小，选择桶最小的哈希表
    sizes = [len(hash_tables[i][index]) for i, index in enumerate(indexes)]
    index = sizes.index(min(sizes))
    hash_tables[index][indexes[index]].append(data)

# 计算每个哈希单元中的元素数量
def count_elements_in_hash_table(hash_tables):
    counts = [[len(hash_tables[i][j]) for j in range(128)] for i in range(4)]
    return counts

# 测试数据
data = ['hello', 'world', 'this', 'is', 'a', 'test', 'of', 'hash', 'functions']

network_tuples = [("10.0.1.1", "10.0.2.2"),
                  ("10.0.1.1", "10.0.3.3"),
                  ("10.0.1.1", "10.0.4.4"),
                  ("10.0.1.1", "10.0.5.5"),
                  ("10.0.1.1", "10.0.6.6"),
                  ("10.0.1.1", "10.0.1.11"),
                  ("10.0.1.1", "10.0.2.22"),
                  ("10.0.1.1", "10.0.4.44"),
                  ("10.0.2.2", "10.0.1.1"),
                  ("10.0.2.2", "10.0.3.3"),
                  ("10.0.2.2", "10.0.4.4"),
                  ("10.0.2.2", "10.0.5.5"),
                  ("10.0.2.2", "10.0.6.6"),
                  ("10.0.2.2", "10.0.1.11"),
                  ("10.0.2.2", "10.0.2.22"),
                  ("10.0.2.2", "10.0.4.44"),
                  ("10.0.3.3", "10.0.1.1"),
                  ("10.0.3.3", "10.0.2.2"),
                  ("10.0.3.3", "10.0.4.4"),
                  ("10.0.3.3", "10.0.5.5"),
                  ("10.0.3.3", "10.0.6.6"),
                  ("10.0.3.3", "10.0.1.11"),
                  ("10.0.3.3", "10.0.2.22"),
                  ("10.0.3.3", "10.0.4.44"),
                  ("10.0.4.4", "10.0.1.1"),
                  ("10.0.4.4", "10.0.3.3"),
                  ("10.0.4.4", "10.0.2.2"),
                  ("10.0.4.4", "10.0.5.5"),
                  ("10.0.4.4", "10.0.6.6"),
                  ("10.0.4.4", "10.0.1.11"),
                  ("10.0.4.4", "10.0.2.22"),
                  ("10.0.4.4", "10.0.4.44"),
                  ("10.0.5.5", "10.0.1.1"),
                  ("10.0.5.5", "10.0.3.3"),
                  ("10.0.5.5", "10.0.4.4"),
                  ("10.0.5.5", "10.0.2.2"),
                  ("10.0.5.5", "10.0.6.6"),
                  ("10.0.5.5", "10.0.1.11"),
                  ("10.0.5.5", "10.0.2.22"),
                  ("10.0.5.5", "10.0.4.44"),
                  ("10.0.6.6", "10.0.1.1"),
                  ("10.0.6.6", "10.0.3.3"),
                  ("10.0.6.6", "10.0.4.4"),
                  ("10.0.6.6", "10.0.5.5"),
                  ("10.0.6.6", "10.0.2.2"),
                  ("10.0.6.6", "10.0.1.11"),
                  ("10.0.6.6", "10.0.2.22"),
                  ("10.0.6.6", "10.0.4.44"),
                  ("10.0.1.11", "10.0.1.1"),
                  ("10.0.1.11", "10.0.3.3"),
                  ("10.0.1.11", "10.0.4.4"),
                  ("10.0.1.11", "10.0.5.5"),
                  ("10.0.1.11", "10.0.6.6"),
                  ("10.0.1.11", "10.0.2.2"),
                  ("10.0.1.11", "10.0.2.22"),
                  ("10.0.1.11", "10.0.4.44"),
                  ("10.0.2.22", "10.0.1.1"),
                  ("10.0.2.22", "10.0.3.3"),
                  ("10.0.2.22", "10.0.4.4"),
                  ("10.0.2.22", "10.0.5.5"),
                  ("10.0.2.22", "10.0.6.6"),
                  ("10.0.2.22", "10.0.1.11"),
                  ("10.0.2.22", "10.0.2.2"),
                  ("10.0.2.22", "10.0.4.44"),
                  ("10.0.4.44", "10.0.1.1"),
                  ("10.0.4.44", "10.0.3.3"),
                  ("10.0.4.44", "10.0.4.4"),
                  ("10.0.4.44", "10.0.5.5"),
                  ("10.0.4.44", "10.0.6.6"),
                  ("10.0.4.44", "10.0.1.11"),
                  ("10.0.4.44", "10.0.2.22"),
                  ("10.0.4.44", "10.0.2.2")                
]

# 创建四个哈希表
hash_tables = [[[] for _ in range(128)] for _ in range(4)]

# 使用四个不同哈希函数将数据添加到哈希表中
hash_functions = [hash_function_1, hash_function_2, hash_function_3, hash_function_4]
for network_tuple in network_tuples:
    put_data_in_hash_table(hash_tables, network_tuple)

# 计算每个哈希表中每个单元格中的元素数量的统计数据
counts = count_elements_in_hash_table(hash_tables)
min_counts = [min(counts[i][j] for i in range(4)) for j in range(128)]

# 输出最小统计结果
for i in range(128):
    # if min_counts[i] > 0:
    print(f"The minimum count for index {i} is {min_counts[i]}.")
