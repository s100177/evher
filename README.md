# evher
## 第一步，安装python3.7
## 第二步，安装依赖包
## 第三步，替换依赖包的文件..\envs\py37\Lib\site-packages\stable_baselines\her\replay_buffer.py替换为本项目下的replay_buffer.py
## 第四步，运行“批量跑实验.py”，默认是对比sac的五个方法['final','episode','random','future','evher']
## 第五步，运行

如果要测试TD3和DDPG需要把her_example2.py的算法换成TD3和DDPG
