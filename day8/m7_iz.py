# m7_iz.py
import numpy as np

# 生成1~200数组
nums = np.arange(1,201)
print("原始nums：",nums)

# ①布尔索引筛选偶数
even_nums = nums[nums % 2 == 0]
print("筛选出来所有偶数：", even_nums)

# ②np.where定位大于100的元素下标
idx_gt100 = np.where(nums > 100)
print("大于100元素的索引位置：", idx_gt100)
print("大于100的元素值：", nums[idx_gt100])
