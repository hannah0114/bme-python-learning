# pandas_csv_demo.py
import pandas as pd

# 读取day5的data.csv
df = pd.read_csv("day5/data.csv", encoding="utf-8")
print("原始数据：")
print(df.head())

# 增加BMI列，这里改成中文列名！
df["BMI"] = df["体重"] / (df["身高"] ** 2)
df["BMI"] = df["BMI"].round(2)

print("\n增加BMI之后：")
print(df)

# 输出新csv，Excel打开不乱码用 utf‑8‑sig
df.to_csv("day6/pandas_result.csv", index=False, encoding="utf-8-sig")
print("\n已输出 pandas_result.csv 到day6文件夹")