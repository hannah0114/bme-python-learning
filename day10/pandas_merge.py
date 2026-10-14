import pandas as pd

# 表1：沿用day9的4个人：姓名、身高、体重、BMI、组别
df_bmi = pd.DataFrame({
    "姓名":["小明","小红","小李","小张"],
    "身高":[1.70,1.62,1.78,1.65],
    "体重":[62,51,75,66],
    "BMI":[21.45,19.43,23.67,24.24],
    "组别":["A","A","B","B"]
})

# 表2：新增体检项目表（部分人有额外数据，用来练习连接）
df_check = pd.DataFrame({
    "姓名":["小明","小红","小张","小王"],
    "血压":["120/80","115/75","132/84","128/78"],
    "心率":[72,68,80,74]
})

print("=====BMI主表=====")
print(df_bmi)
print("\n=====体检附表=====")
print(df_check)
# 1. inner内连接：只保留两张表【姓名同时存在】的人（小明、小红、小张）
#df_inner = pd.merge(df_bmi, df_check, on="姓名", how="inner")
#print("\n=====inner 内连接（交集）=====")
#print(df_inner)
# 2. left左连接：以左边df_bmi全部4个人为主，匹配附表，匹配不到的填NaN
df_left = pd.merge(df_bmi, df_check, on="姓名", how="left")
print("\n=====left 左连接（保留左边全部）=====")
print(df_left)
# 3. right右连接：以右边体检表为主（小明小红小张小王）
# df_right = pd.merge(df_bmi, df_check, on="姓名", how="right")
# print("\n=====right 右连接=====")
# print(df_right)
# 4. outer全外连接：两张表所有人全部保留
# df_outer = pd.merge(df_bmi, df_check, on="姓名", how="outer")
# print("\n=====outer 全外连接（并集）=====")
# print(df_outer)
# 新增第二批人员数据
df_new = pd.DataFrame({
    "姓名":["小周","小陈"],
    "身高":[1.68,1.72],
    "体重":[59,68],
    "BMI":[20.86,23.05],
    "组别":["A","B"]
})
# 纵向拼接，把df_new拼到df_bmi下面
df_concat = pd.concat([df_bmi, df_new], ignore_index=True)
print("\n=====concat纵向拼接后=====")
print(df_concat)
ignore_index=True
pivot_res = pd.pivot_table(
    df_concat,
    index="组别",       # 行：分组依据组别A/B
    values="BMI",       # 需要统计的值
    aggfunc=["mean","max","count"] # 同时求均值、最大值、计数
)
print("\n=====pivot_table透视表结果=====")
print(pivot_res)

# 导出透视结果
pivot_res.to_csv("pivot_result.csv", encoding="utf-8-sig")
print("\n====导出透视表 pivot_result.csv====")
# 拿左连接的表，把NaN（缺失血压心率）填充为“未检测”
df_left_fill = df_left.fillna("未检测")
print("\n====缺失值填充完成=====")
print(df_left_fill)

# 导出合并完成的总表
df_left_fill.to_csv("merge_total.csv", index=False, encoding="utf-8-sig")
print("\n====导出合并总表 merge_total.csv，day10全部完成====")