# evher
## 第一步，安装python3.7
## 第二步，安装依赖包
## 第三步，替换依赖包的文件..\envs\py37\Lib\site-packages\stable_baselines\her\replay_buffer.py替换为本项目下的replay_buffer.py
## 第四步，运行“批量跑实验.py”，前提是改脚本所在目录下创建名字为“output”的文件夹。默认批量跑sac的五个方法['final','episode','random','future','evher']
## 第五步，在"提取日志.py"里设置要提取的日志路径，然后运行该脚本，就可以得到对比分析结果哦。

**注意**
如果要测试TD3和DDPG需要把her_example2.py的算法换成TD3和DDPG
