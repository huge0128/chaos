import numpy as np
import matplotlib.pyplot as plt



# 参数设置
s0 = 0
b0 = 0
c0 = 1
# 初始化
# α是数据平滑因子
# β是趋势平滑因子
# γ是季节改变平滑因子
alpha = 0.9
beta = 0.1
gama = 0.8
# 预测长度 预测第t+m时刻
m = 5
# 季节周期长度
L = 5
# TSD数据集构造
t = np.linspace(0, 10, 100)
data = np.genfromtxt('D:\code\P4\ddos.csv', delimiter = ',')
y =data
# y = 2 * t + np.random.rand(len(t))
# 原始时序数据
plt.figure(figsize=(16, 7))
plt.plot(y)
plt.title("origin")
plt.show()


# exp smooth order 1
def ExpSmooth(y, s0, alpha, order=1, b0=0, beta=0.5,c0=1,gama=0.1):
    if order == 1:
        s = [s0]
        for i in range(1, len(y)):
            s.append(alpha * y[i] + (1 - alpha) * s[-1])
        return s
    if order == 2:
        s = [s0]
        b = [b0]
        for i in range(1, len(y)):
            s.append(alpha * y[i] + (1 - alpha) * (s[-1] + b[-1]))
            b.append(beta * (s[i] - s[i - 1]) + (1 - beta) * b[-1])
        return s, b
    if order == 3:
        if b0 is None:
            # 初始化趋势估计b0
            sum = 0
            for i in range(L):
                sum+=(y[L+i+1]-y[i+1])
            b0 = sum/(L**2)
        s = [s0]
        b = [b0]
        c = np.ones(L)*c0#c是季节量 固定长度L
        for i in range(1, len(y)):
            c[i % L] = c[i%L] if c[i%L]!=0 else c[i%L]+1e-5
            s.append(alpha * y[i]/(c[i%L]) + (1 - alpha) * (s[-1] + b[-1]))
            b.append(beta * (s[i] - s[i - 1]) + (1 - beta) * b[-1])
            c[i%L] = gama*y[i]/s[i]+(1-gama)*c[i%L]
        return s, b,c
    return None


# for epoch in range(epochs):#暂未找到自动搜索alpha的方法
# print("Epoch:",epoch+1)
predict = ExpSmooth(y, s0, alpha)
# np.savetxt('order1.csv', predict, delimiter=',')
loss = np.mean((predict - y) ** 2)
print("Order=1 loss:", loss, "alpha:", alpha)
# print(predict)
plt.plot(predict, label='Pred tsd')
plt.plot(y, label='True tsd')
plt.legend(loc=1)
plt.title("order 1")
plt.show()


# b:时间趋势统计量
predict, b = ExpSmooth(y, s0, alpha, order=2, b0=b0, beta=beta)
# np.savetxt('order2.csv', predict, delimiter=',')
loss = np.mean((predict - y) ** 2)
print("Order=2 loss:", loss, "alpha:", alpha, "beta:", beta)
plt.plot(predict, label='Pred tsd')
plt.plot(y, label='True tsd')
plt.legend(loc=1)
# plt.title("tsd Predictions Order=2")
plt.title("order 2")
plt.show()

# 二阶指数平滑可以预测t+m时刻的结果
# y[t+m]=predict[t]+mb[t]
predict_m = [predict[t_] + m * b[t_] for t_ in range(len(y) - m)]
# np.savetxt('order3.csv', predict, delimiter=',')
loss = np.mean((predict_m - y[m:]) ** 2)
print("Order=2 loss:", loss, "alpha:", alpha, "beta:", beta, "m:", m)
plt.plot(predict, label='Pred tsd')
plt.plot(y, label='True tsd')
plt.legend(loc=1)
plt.title("order 2 m=%d" % m)
# plt.title("tsd Predictions Order=2 m=%d" % m)
plt.show()

# Order=3
# 季节性被定义为时间序列数据的周期性。
# “季节”表示行为每隔时间段L就开始重复。
# 季节性“累加性”(additive)和“累乘性“(multiplicative)

predict, b,c = ExpSmooth(y, s0, alpha, order=3, b0=b0, beta=beta,c0=c0,gama=gama)
loss = np.mean((predict - y) ** 2)
# print("Order=3 loss:", loss, "alpha:", alpha, "beta:", beta)
plt.plot(predict, label='Pred tsd')
plt.plot(y, label='True tsd')
plt.legend(loc=1)
plt.title("tsd Predictions Order=3")
plt.show()

# 三阶指数平滑可以预测t+m时刻的结果
# y[t+m]=(predict[t]+mb[t])c[(t-L+m)%L]
predict_m = [(predict[t_] + m * b[t_])*c[(t_-L+m)%L] for t_ in range(len(y) - m)]
# np.savetxt('order4.csv', predict, delimiter=',')
loss = np.mean((predict_m - y[m:]) ** 2)
print("Order=3 loss:", loss, "alpha:", alpha, "beta:", beta, "m:", m)
plt.plot(predict, label='Pred tsd')
plt.plot(y, label='True tsd')
plt.legend(loc=1)
plt.title("tsd Predictions Order=3 m=%d L=%d" % (m,L))
plt.show()
