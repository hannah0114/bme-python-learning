# import_demo.py
# 三种导入写法示范
import numpy as np
import pandas
from datetime import datetime

# 打印版本，确认库正常导入
print("numpy版本:", np.__version__)
print("pandas版本:", pandas.__version__)
now = datetime.now()
print("当前时间:", now)