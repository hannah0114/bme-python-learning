import pandas as pd

# 1 读取csv数据
df = pd.read_csv(r"C:\Users\Beverly\Desktop\bme-python\day9\data.csv")
print("====打印全部列名====")
print(df.columns)

# 2 计算BMI
df["BMI"] = df["体重"] / (df["身高"] ** 2)
print("\n====新增BMI之后的数据====")
print(df)

# 3 添加是否超标标记
df.loc[df["BMI"]>24, "是否超标"] = "超标"
df.loc[df["BMI"]<=24, "是否超标"] = "正常"
print("\n====增加超标标记列====")
print(df)

# 4 新增组别 + groupby分组聚合练习
df.loc[0,"组别"] = "A"
df.loc[1,"组别"] = "A"
df.loc[2,"组别"] = "B"
df.loc[3,"组别"] = "B"
print("\n====新增组别列====")
print(df)

res = df.groupby("组别")["BMI"].agg(["mean","std","count"])
print("\n====分组聚合结果====")
print(res)

# 5 loc、iloc练习
print("\n====loc取第0行====")
print(df.loc[0])
print("\n====iloc取第0行====")
print(df.iloc[0])

# 6 筛选练习
df_filter = df[df["BMI"] >24]
print("\n====BMI大于24筛选结果====")
print(df_filter)

df_filter2 = df[(df["BMI"]>24) & (df["体重"]>65)]
print("\n====多条件筛选结果====")
print(df_filter2)
# ==========7. Day9综合练习（重点任务）==========
# 1.读取data.csv原始数据
df = pd.read_csv(r"C:\Users\Beverly\Desktop\bme-python\day9\data.csv")

# 2.划分体重区间，我们四个人体重：51、62、66、75，设置区间
bins = [40, 55, 65, 80, 200]
labels = ["40~55kg","55~65kg","65~80kg","80kg以上"]

# 3.根据体重划分区间，新增体重区间列
df["体重区间"] = pd.cut(df["体重"], bins=bins, labels=labels, right=False)

# 4.先计算BMI
df["BMI"] = df["体重"] / (df["身高"] ** 2)

# 5.按照体重区间分组，求每组BMI平均值
group_result = df.groupby("体重区间")["BMI"].agg(["mean"]).reset_index()
group_result.columns = ["体重区间","BMI平均值"]

print("\n=====体重区间分组统计结果=====")
print(group_result)

# 6.导出结果文件 group_result.csv
group_result.to_csv("group_result.csv", index=False, encoding="utf-8-sig")
print("\n====文件导出完成，生成 group_result.csv====")
