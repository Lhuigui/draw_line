import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 生成一些数据
water_levels = np.linspace(0, 10, 100)

# 面积 (x轴1)
area = water_levels * 10

# 流速 (x轴2)
velocity = np.sqrt(water_levels) * 5

# 流量 (x轴3)
flow_rate = water_levels ** 1.5

# 创建一个大的图框
fig, ax = plt.subplots(figsize=(12, 7), dpi=600)  # 调整大小以适应水平排列
fig.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)

# 取消主轴上的刻度线
ax.set_xticks([])

# 设置统一的x轴刻度间隔
num_ticks = 6  # 刻度数量
flow_ticks = np.linspace(0, 50, num_ticks)  # 流量的刻度
speed_ticks = np.linspace(0, 20, num_ticks)   # 流速的刻度
area_ticks = np.linspace(0, 100, num_ticks)  # 面积的刻度

# 创建三个子图，散列在一行中，并共享 y 轴
ax1 = fig.add_subplot(131, sharey=ax)
ax2 = fig.add_subplot(132, sharey=ax)
ax3 = fig.add_subplot(133, sharey=ax)

# 绘制曲线
ax1.plot(flow_rate, water_levels, color='r')
ax2.plot(velocity, water_levels, color='g')
ax3.plot(area, water_levels, color='b')

ax1.set_xticks(flow_ticks)
ax2.set_xticks(speed_ticks)
ax3.set_xticks(area_ticks)

# 调整子图间距
plt.subplots_adjust(wspace=0)  # wspace 调整子图之间的宽度间隔，数值越大，间隔越宽

ax1.set_xlabel('流量($m^3/s$)')
ax1.set_ylabel('水位($m$)', labelpad=10)
ax2.set_xlabel('流速($m/s$)')
ax3.set_xlabel('面积($m^2$)')

# 设置网格线颜色（使用0-255的RGB值）
def rgb_to_normalized(rgb):
    return tuple(c / 255.0 for c in rgb)

# 设置网格线颜色（使用RGB）
main_grid_color = rgb_to_normalized((245, 222, 179))  # 主网格线颜色，灰色
minor_grid_color = rgb_to_normalized((245, 222, 179))  # 次网格线颜色，浅灰色

# 取消每个子图的边框
for ax in [ax1, ax2, ax3]:
    ax.grid(True, which='both', color=main_grid_color)
    ax.minorticks_on()  # 启用次级刻度线
    ax.grid(True, which='minor', linestyle=':', linewidth=0.5, color=minor_grid_color)  # 设置次网格线样式
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y', which='both', length=0, labelsize=0)  # 隐藏刻度线和刻度标签
ax1.spines['left'].set_visible(True)

# 仅显示第一个子图的y轴，隐藏其余两个子图的y轴
plt.setp(ax2.get_yticklabels(), visible=False)
plt.setp(ax2.get_yticklines(), visible=False)

plt.setp(ax3.get_yticklabels(), visible=False)
plt.setp(ax3.get_yticklines(), visible=False)

# 设置标题
fig.suptitle('二郎矶水位-流量-面积-流速曲线')

plt.show()