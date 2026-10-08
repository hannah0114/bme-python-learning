#csv_demo.py
def calc_bmi(h:float,w:float) -> float:
    return w / (h**2)

in_path = "day5/data.csv"
out_path = "day5/result.csv"

try:
    with open(in_path, "r", encoding="utf-8") as f_in, \
         open(out_path, "w", encoding="utf-8") as f_out:

        #写输出表头
        f_out.write("姓名,身高,体重,BMI\n")

        lines = f_in.readlines()
        for idx,line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            if idx == 0:
                continue #跳过表头
            parts = line.split(",")
            name = parts[0]
            h = float(parts[1])
            w = float(parts[2])
            bmi_val = calc_bmi(h,w)
            #写入一行
            f_out.write(f"{name},{h},{w},{bmi_val:.2f}\n")

    print("完成，已生成result.csv")

except FileNotFoundError:
    print(f"错误：找不到文件 {in_path}")
except ValueError as e:
    print(f"数值转换出错：{e}")