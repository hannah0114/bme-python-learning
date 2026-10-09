# numpy_basic.py
import numpy as np   # ✅ 必写，忘记就NameError（易错点3）

# 1. 手动创建数组
a = np.array([1, 2, 3, 4])
print("a = ",a)

# 2. arange：起点、终点、步长（左闭右开）
arr1 = np.arange(0, 10, 2)
print("arange(0,10,2) = ", arr1)

# 3. linspace：在0~1之间生成5个等间隔数字
arr2 = np.linspace(0, 1, 5)
print("linspace(0,1,5) = ", arr2)

# 4. zeros / ones / eye
arr_zeros = np.zeros((3,3))   # 3行3列全0矩阵
arr_ones = np.ones((2,4))     # 2行4列全1矩阵
arr_eye = np.eye(3)           # 3阶单位矩阵
print("zeros:\n",arr_zeros)
print("ones:\n",arr_ones)
print("eye:\n",arr_eye)

# 查看数组属性 shape维度 / dtype数据类型 / size总元素个数
print("a.shape = ", a.shape)
print("a.dtype = ", a.dtype)
print("a.size = ", a.size)
import sys
print(sys.executable)
# ----------------索引切片练习----------------
# 一维数组
b = np.array([10,20,30,40,50])
print("b[0] 第一个元素：", b[0])
print("b[-1] 最后一个元素：", b[-1])
print("b[1:4] 切片：", b[1:4])

# ✅ 演示视图问题！！非常重要
b_slice = b[1:4]
b_slice[0] = 999
print("修改切片后原数组b：",b) # 原数组被改动了！！

# 如果想要独立副本，使用 .copy()
b2 = np.array([10,20,30,40,50])
b_slice_copy = b2[1:4].copy()
b_slice_copy[0] = 999
print("使用copy，原数组不受影响b2：",b2)


# 二维数组练习
c = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print("c[0,1] 第0行第1列元素：", c[0,1])
print("c[:,0] 取第0整列：", c[:,0])
print("c[0:2, 1:3] 取子矩阵（前2行，1~3列）：\n", c[0:2, 1:3])
# ----------------广播与逐元素运算----------------
arr_x = np.array([1,2,3])
# 数组 + 标量
print("arr_x + 10 = ", arr_x + 10)
print("arr_x * 2 = ", arr_x * 2)

# 两个数组逐元素加减乘除
arr_y = np.array([10,20,30])
print("arr_x + arr_y = ", arr_x + arr_y)
print("arr_x * arr_y = ", arr_x * arr_y)

# ✅广播例子！！（重点笔记案例）
# (3,1)数组 和 (1,4)数组自动广播成(3,4)
br1 = np.array([[1],[2],[3]]) # shape (3,1)
br2 = np.array([[10,20,30,40]]) # shape (1,4)
br_result = br1 + br2
print("广播例子 br1+br2 =\n",br_result)