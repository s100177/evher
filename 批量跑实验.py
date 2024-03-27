import subprocess

# # 运行命令
#     for i in range(1,20):
#         process = subprocess.Popen(f'd:/Apps/anaconda3/envs/py37/python.exe her_example2.py > output_{name}{i}.txt', shell=True,
#                                    stdout=subprocess.PIPE)
#         process.communicate()

# 运行命令
method = ['final','episode','random','future','evher']
# method = ['final']
for name in method:
    for i in range(1, 20):
        process = subprocess.Popen(f'd:/Apps/anaconda3/envs/py37/python.exe her_example2.py --sample_method {name}> ./output/output_{name}{i}.txt', shell=True,
                                   stdout=subprocess.PIPE)
        process.communicate()

