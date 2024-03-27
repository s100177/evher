import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 输入要对比的老方法，老方法有四种：'final','episode','random','future'
old = 'final'

def get_number(file_path):
    # 指定要读取的文件路径
    # file_path = f'output_new{i}.txt'  # 用您的文件路径替换 'your_file.txt'

    # 打开文件并读取内容
    with open(file_path, 'r') as file:
        text = file.read()


    # 使用正则表达式提取数据
    success_rate_pattern = r"\|\s*success rate\s*\|\s*([\d.-]+)\s*\|"
    matches = re.findall(success_rate_pattern, text)

    # 输出结果
    # if matches:
    #     print("Success rates found: ", matches)
    # else:
    #     print("No success rates found.")
    # 训练集上的表现
    result = [float(i) for i in matches]

    # 测试集上的表现
    pattern = r"Success\? (\w+)"
    matches = re.findall(pattern, text)
    test_result = [1 if x.lower() == 'true' else 0 for x in matches]
    # print(test_result)
    return result, test_result


all_result = {}

all_test_result_new = []
all_test_result_old = []

for i in range(15):
    # 指定要读取的文件路径
    file_path = f'output_new{i}.txt'  # 用您的文件路径替换 'your_file.txt'
    try:
        result,rest_result = get_number(file_path)
        all_result[f'new_{i}'] = result[:60]
        all_test_result_new.extend(rest_result)

    except:
        result = None
    # 打开文件并读取内容
    file_path2 = f"output_{old}{i}.txt"
    try:
        result2,test_result2 = get_number(file_path2)
        all_result[f"{old}_{i}"] = result2[:60]
        all_test_result_old.extend(test_result2)

    except:
        result2 = None

df = pd.DataFrame(all_result)


# 绘制曲线图
plt.figure(figsize=(10, 6))
for column in df.columns:
    if 'new' in column:
        plt.plot(df.index, df[column], color='red', label=column)
    else:
        plt.plot(df.index, df[column], color='blue', label=column)

plt.legend()
plt.title('Data from DataFrame')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()





# 绘制曲线和置信区间
plt.figure(figsize=(10, 6))
for column in df.columns:
    if 'new' in column:
        sns.lineplot(data=df[column], label=column, color='red')
    else:
        sns.lineplot(data=df[column], label=column, color='blue')

plt.title(f'new-{old}')
plt.xlabel('Index')
plt.ylabel('Value')

# 显示图例
plt.legend()

# 展示置信区间
# plt.fill_between(df.index, df['new_col1'], color='red', alpha=0.2)
# plt.fill_between(df.index, df['new_col2'], color='red', alpha=0.2)
# plt.fill_between(df.index, df['old_col1'], color='blue', alpha=0.2)
# plt.fill_between(df.index, df['old_col2'], color='blue', alpha=0.2)

plt.show()


# 绘制第一类分位数填充图
plt.figure(figsize=(10, 6))
columns2 = []
columns1 = []
for column in df.columns:
    if 'new' in column:
        columns1.append(column)
    else:
        columns2.append(column)


# 填充第一类的分位数
plt.plot(df.index, df[columns1].quantile(0.5,axis=1), color='red', alpha=1,label='new')
plt.plot(df.index, df[columns2].quantile(0.5,axis=1), color='blue', alpha=1,label=old)

plt.fill_between(df.index, df[columns1].quantile(0.25,axis=1), df[columns1].quantile(0.75,axis=1), color='red', alpha=0.2)
plt.fill_between(df.index, df[columns2].quantile(0.25,axis=1), df[columns2].quantile(0.75,axis=1), color='blue', alpha=0.2)
plt.title(f'new-{old}')
plt.title(f'new-{old}')

plt.xlabel('episodes*10')
plt.ylabel('success rate')
plt.legend()
plt.show()


# 提取测试集成功率数据
# 老方法的成功率
test_success_ratio_old = sum(all_test_result_old)/len(all_test_result_old)
# 新方法的成功率
test_success_ratio_new = sum(all_test_result_new)/len(all_test_result_new)

print("训练集上的训练过程数据:")
print(df.head())
print(f"测试集上，老方法的成功率：{test_success_ratio_old}")
print(f"测试集上，新方法的成功率：{test_success_ratio_new}")

