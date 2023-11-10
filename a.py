import pandas as pd
import os

# 读取CSV文件
df = pd.read_csv('file.csv')

# 遍历每一行
for index, row in df.iterrows():
    # 获取姓名，学号和文件名
    name = row[1]
    student_id = row[2]
    filename = row[3]
    
    # 获取文件扩展名
    _, file_extension = os.path.splitext(filename)

    # 构建新的文件名
    new_filename = f"{student_id} {name}{file_extension}"

    # 重命名文件
    if os.path.exists(filename):
        os.rename(filename, new_filename)