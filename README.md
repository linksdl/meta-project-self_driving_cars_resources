## The Era of Autonomous Driving (自动驾驶时代)
- This repository is using mainly for self-driving cars learning.
- 本项目主要用于自我学习和研究自动驾驶技术，通过收集和整理各种学习资源和内容，方便查阅, 不用于商业用途。其中部分资源来源相关的个人，也会注明出处。

## The Roadmap of Becoming a Self-Driving Cars Engineer 
自动驾驶工程师学习路线

![自动驾驶](自动驾驶学习路线图.png)
The image[1] shows the roadmap of becoming a self-driving cars engineer.

- [如何成为一名自动驾驶工程师 So you want to be a self-driving car engineer?](https://autonomous-driving.org/2018/08/15/so-you-want-to-be-a-self-driving-car-engineer/)[2].
- 如何成为一名合格的自动驾驶工程师？.pdf 

## Table of Content(资源目录)
- [Skills(技能要求)](#tree-skills)
- [Companies(自动驾驶公司)](#companies)
- [Websites(学习网站)](#websites)
- [Blogs, News,Platforms and Articles (博客公众号)](#blogs)
- [Technical Skills (技术学习)](#skills)
- [Books(书籍)](#books)
- [Papers(学术论文)](#papers)
- [Reports(行业报告)](#reports)
- [Notes 学习笔记](#notes)
- [Courses and Videos, 课程和视频](#videos)
- [Projects and Codes 实践项目](#projects)
- [Jobs 工作机会](#jobs)
- [Questions and Challenges 行业问题&挑战](#questions)
- [Future 前沿技术](#future)
- [References（参考文献）](#refers) 

### The Required Technical Skills <a name="tree-skills"></a>
自动驾驶工程师技能栈:
- 自动驾驶感知算法工程师
- 自动驾驶激光雷达算法工程师
- 自动驾驶感知融合算法工程师
- 自动驾驶毫米波算法工程师
- 自动驾驶规划决策算法工程师
- 自动驾驶融合定位算法工程师

#### 计算机基础
- 数据结构与算法
- 计算机组成原理
- 操作系统原理
- 计算机网络
- 通信原理
- 信息论
- 控制理论

#### 数学基础设计
- 高等数学
- 概率论，贝叶斯思维
- 线性代数
- 离散数学
- 矩阵论等
- 科学计算：优化理论，数值优化，非线性优化，凸优化问题

#### 编程开发
-  C/C++：C++基础，C++面向对象编程，内存管理，性能优化，多线程/并发
-  C++的Bazel、Cmake、Protobuf等编译工具
-  Python编程
-  AI -> Deep Learning, Python, Pytorch, Tensorflow
-  ROS,
-  Python库：Pandas, Numpy, Matplotlib等常见库
-  OPenCV, PCL, Open3D, G2O, Gtsam, Eigen, Sofus
-  Matlab & Simulink
-  JavaScript(Node.js, React)
-  操作系统：QNX，Linux, Shell, Vim
-  高性能编程，
-  CUDA编程, JETSON AGX Orin GPU computing

#### 开发工具
- VsCode, Pycharm, Clion, 
- CPU
- GPU(CUDA)
- FPGA
- Simulation: Matlab/Simulink, GameEngine(UE4)
- 云计算平台：HD map, OpenDrive, Data Platform(虚拟化, 异构计算，分布式计算，分布式存储)，Security, OTA, DuerOS
- ROS, Cyber RT 
- Rviz(数据可视化)， Gazebo(物理仿真模型)
- Docker， K8s

#### 优化库
- [各种库的安装](https://blog.csdn.net/HZ490727/article/details/80866894?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-80866894-blog-88374776.pc_relevant_multi_platform_featuressortv2dupreplace&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-80866894-blog-88374776.pc_relevant_multi_platform_featuressortv2dupreplace&utm_relevant_index=1)
- ceres-solver 线性优化，常用优化算法
- g2o 图优化
- gtsam
- eigen 矩阵操作
  - 旋转矩阵 Eigen::Matirix3d
  - 旋转向量 Eigen::AngleAxisd
  - 欧拉角 Eigen::Vector3d
  - 四元数 Eigen::Quaterniond
  - 欧式变换矩阵 Eigen::Isometry3d
  - 仿射变换 Eigen::Affine3d
  - 射影变幻 Eigen::Projective3d
- Sophus，李群， 李代数
- OpenCV 对图像的处理和操作
- PCL 对点云的处理库

#### 车辆工程
- 电子电气
- 运动模型
- 动力模型

#### 车辆系统
- Drive-by-wire Vehicle
- 车辆电子控制系统（Protocol(Can, Lin, FlexRay)）, 动力系统控制，制动系统控制，转向系统控制
- 车载语音交互系统
- 组件架构设计：AUTOSAR
- 车辆底盘, 1转向系统, 油门控制, 2制动系统, 3动力系统, 4控制系统
- 电子电气架构（环境感知, 定位导航, 通信系统，计算平台，供电系统）
- 线控油门，线控转向，线控制动

#### 人工智能
- 机器学习：经典机器学习
- 深度学习：DNN, CNN, 迁移学习，RNN, NLP, 文本挖掘
- 强化学习：Reinforcement Learning
- 图神经网络，图优化
- 深度框架：Pytorch, Tensorflow, Caffe, Keras, PaddlePaddle
- 计算机视觉: 传统计算机视觉知识
- 图形学：Low-Level Vision, 图形学与视觉几何
- 模型部署：CUDA， TensorRT

#### 芯片技术
- CPU，GPU

#### 基础架构
- 自动驾驶基础架构
- 感知层，决策层（车联网，高精地图），执行层
- 云计算
- 车联网
- 地图
- 系统安全（硬件稳定性，系统稳定性，人机切换）
- 处理芯片（处理能力，实时性，成本）
- 人工智能（大数据，深度学习，图像处理）
- 感知系统（激光雷达，毫米波雷达，摄像头）

#### 硬件知识
- Computing Unit(IPC，Intel, Nvidia, 专用自动驾驶计算单元（PX2 TX2...）)
- 感知传感器：Camera(单目/双目，多目), Lidar, Radar, Ultrasonic Radar
- 定位：GPS, GNSS, IMU, INS,Other Perception Sensors
- 摄像机, 惯性导航仪，GPS卫星定位系统
- 网络差分
- CAN card
- HMI Device
- V2X Device（V2Vehicle, V2Infrastructure, V2Pedestrian, V2Road, V2Network, V2Cloud）
- 车联网
- 智能网联
- 智慧交通
- 智慧城市
- 道路协同
- Safety, Black Box
- 传感器知识和技能：搭建方式，配置流程，数据形式，能够通过数据判断传感器是否正常工作
- 无人车知识和技能：
  - 基本的硬件组成
  - 各Sensors流程
  - 通讯信息接口
  - 个人传感器优点，能力与局限
  - 知道本模块对于硬件的需求
  - 算法对于硬件的依赖，瓶颈
  - 硬件的基本参数性能，调参方法
  - 熟悉上车开发调试环境

#### 传感器标定
- 内参外参标定
- 摄像头标定
- 激光雷达标定
- 联合标定

### 环境感知
- 传感器融合
- 激光 & 视觉
- 2D&3D 目标检测
- 2D&3D 语义分割
- 2D&3D 场景分割
- 状态估计与滤波（KF, EKF，IEKF，UKF, PF）


### 定位建图
- 车辆定位
- 路径规划
- 视觉SLAM
- 激光SLAM
- Smoothing Curves
- Vehicle Kinematics
- Station-time 2D Model
- Optimization Algorithms: Dynamic Programming
- Quadratic Programming
- Smoothing Spline
- *A
- Probability Math Models: Bayesian
- Markov Process
- MDP
- Basic Motion Planning Technique
- Sampling Based Motion Planning
- Computer Science: Parallel Programming
- Dynamic Programming 
- Computation Geometry

### 决策规划
- 强化学习
- A*算法

#### 运动控制
- Basic Control Theory
- Linear-Quadratic Regulator(LQR)
- Model Predictive Control(MPC)
- PID Basic Control Theory


#### 智能网联
- 车路协同
- V2X

#### 仿真测试
- 仿真器
- 道路测试
- 城市测试

#### 应用场景
- 矿区
- 园区
- 公园
- 固定道路
- RoboTaxi, RoboBus, RoboTruck
- 末端物流配送
- 室内清扫机器人，室内搬运机器人，室外作业机器人

### 自动驾驶算法与芯片设计
- 3D物体检测
- 车道检测，交通灯检测
- 运动规划与控制
- 定位与建图
- 自动驾驶仿真器
- 自动驾驶芯片
- 深度学习模型优化
- 自动驾驶Soc设计
- 自动驾驶操作系统
- 自动驾驶软件架构
- 5G C-V2X 车联网

#### 具体技术
##### 1. 激光SLAM
- LOAM，Categrahper-3D, A-LOAM，V-LOAM, LeGo-LOAM, LIO-SAM, LVI-SAM, LINS
- IMU内参，零偏；IMU外参，相对于车体坐标系的位置，位姿态等
- 激光内参，外参标定
- IMU和激光的联合标定，平移和旋转参数
- 室内2D激光SLAM
  - hector_slam
  - karto_slam
  - gmapping
  - cartographer2D
- 室外3D激光SLAM
  - LOAM，Categrahper-3D, A-LOAM，V-LOAM, LeGo-LOAM, LIO-SAM, LVI-SAM, LINS
  - fast-LIO 紧耦合

### Companies (自动驾驶公司) <a name="companies"></a>
#### 国外公司
- [Waymo](https://waymo.com/intl/es/), [Tesla](https://www.tesla.com/de_DE/autopilot), Zoox, Voyage, Cruise, Intel-Mobieye, Aptiv-Hyundai
- Yandex, Bosch, May MObility, Ford Auto, Toytota, Voyage Auto, BMW, Volvo
#### 中国公司
- 百度，理想，蔚来汽车，小鹏，小马智行，吉利汽车，长安汽车，上汽集团。

#### L4 自动驾驶公司盘点
- [百度Apollo, 小马智行, 文远知行](https://mp.weixin.qq.com/s/pLbf7HqGVPhrtXxHcisJAw)
- [AutoX, 元戎启行, 轻舟智航](https://mp.weixin.qq.com/s/7bs2fscMGW5BfI_CxzHUlA)
- [Momenta, 领骏科技, 滴滴自动驾驶](https://mp.weixin.qq.com/s/XM8e0fYckWwWBNgUzz3_Ng)
- [智行者, 驭势科技, 中智行](https://mp.weixin.qq.com/s/o_S4wpjXo_zzTtL_rr_J5g)
- [图森未来, 智加科技, 赢彻科技](https://mp.weixin.qq.com/s/ekL_8ai4oZhD2DJexQtzsg)
- [飞步科技, 斯年智驾,主线科技](https://mp.weixin.qq.com/s/NyBFEB44huVfic0FTFmXdg)
- [西井科技, 挚途科技, 擎天智卡](https://mp.weixin.qq.com/s/ecDgioIQ0c3XSiW-IuQ8Qw)
- [希迪智驾, 猩行科技, 畅行智能](https://mp.weixin.qq.com/s/JiYhsaB8RLKA3jafsgD4yg)
- [千挂科技, 踏歌智行, 慧拓智能](https://mp.weixin.qq.com/s/QtuV0bonHmeaLx5eaPtmnw)
- [易控智驾, 伯镭科技, 盟识科技](https://mp.weixin.qq.com/s/dFpws5T-YXKzXGUN_5u35w)
- [路凯智行, 仓擎智能, 九耀智能](https://mp.weixin.qq.com/s/yRw_8zMjOU0tlJEEsN21Fw)
- [美团, 京东, 阿里达摩院](https://mp.weixin.qq.com/s/6OhxKWvQy5XQmaWofuqQRA)
- [行深智能, 白犀牛, 高仙机器人](https://mp.weixin.qq.com/s/WEBGFKRr4pFNMt879-gH5w)
- [酷哇机器人, 新石器, 渡众机器人](https://mp.weixin.qq.com/s/TGa6aKsczdGLfBbvdaO-oQ)
- [仙途智能, 于万智驾, 深兰科技](https://mp.weixin.qq.com/s/oEHBZ3PsFB4kER1g8yEXCA)


#### [智能汽车产业链全景图](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NTcwMDQwMg==&action=getalbum&album_id=1673026835321831424&scene=173&from_msgid=2650811033&from_itemidx=1&count=3&nolastread=1#wechat_redirect)
- [智能汽车产业链全景图（2023年5月版）](https://mp.weixin.qq.com/s/Vi2so3soN9xauj0Hbx-6Rg)
- [智能汽车产业链全景图（2023年4月版)](https://mp.weixin.qq.com/s?__biz=MzA4NTcwMDQwMg==&mid=2650822411&idx=1&sn=0130b78a604dda5c5c4cef3bcc5fbd08&chksm=84270d56b35084406332ea85f109d5f42821221d1f493ed43b5d5ed0f6cfe7629d9ea992c19c&scene=178&cur_album_id=1673026835321831424#rd)
- [智能汽车产业链全景图（2022年4月版）](https://mp.weixin.qq.com/s/955_RMhb6KRo_96HBaLUog)
- [智能汽车产业链全景图（2021年10月版）](https://mp.weixin.qq.com/s/-HccIKWX8kNafs3osAS9qA)
- [智能汽车产业链全景图（2021年9月版）](https://mp.weixin.qq.com/s/cBGwT6GC1kRWL_gSBFcNug)
- [智能汽车产业链全景图（2021年8月版）](https://mp.weixin.qq.com/s/VW3BGpLQFF2oWJh0L4dB7w)
- [智能汽车产业链全景图（2021年7月版）](https://mp.weixin.qq.com/s/9n2ufRSNdFqrYqaOMPGDeA)
- [智能汽车产业链全景图（2021年6月版）](https://mp.weixin.qq.com/s/Syj6O3cAzPLNJor1QglQWg)
- [智能汽车产业链全景图（2021年5月版）](https://mp.weixin.qq.com/s?__biz=MzA4NTcwMDQwMg==&mid=2650795086&idx=1&sn=3a9e0128602301ba0f8d0e5f30225a28&chksm=87d8b613b0af3f057ba6f0142101a1e3f5782e942b18b7eb8a0ce6a2d36d8068791304cc0fc9&scene=178&cur_album_id=1673026835321831424#rd)
- [智能网联汽车产业链全景图（2021年4月版）](https://mp.weixin.qq.com/s/_-WEZrf_th5rtAqcq5YaAA)
- [智能网联汽车产业链全景图（2021年3月版）](https://mp.weixin.qq.com/s/zngNt1EVvu1x0glEFD5VoA)
- [智能网联汽车产业链全景图（2021年1月版）](https://mp.weixin.qq.com/s/MUus8eW-Y2LFj8PwodZmwg)
- [智能网联汽车产业链全景图（2020年12月版）](https://mp.weixin.qq.com/s/twt6K6tBfs_q_7HO5wKf_g)
- [智能网联汽车产业链全景图（2020年11月版）](https://mp.weixin.qq.com/s/3fNS-JiOfF-HcTuiaP-Yjw)
- [智能网联汽车产业链全景图（2020年10月版）](https://mp.weixin.qq.com/s/oTjp4uCSzYI8qcezaWKKfw)
- [智能网联汽车产业链全景图（2020年9月版）](https://mp.weixin.qq.com/s/ND4SbkDxZCLgb6Xt1bvaHw)
- [智能网联汽车产业链全景图（2020年8月版）](https://mp.weixin.qq.com/s/mUS5oDGyPFbug9hoPg-Ubw)
- [座舱产业链全景图（2020年8月版）](https://mp.weixin.qq.com/s/5zqEhNDEPpEQVM6OxUmtJw)
- [智能网联汽车产业链全景图（2020年7月版）](https://mp.weixin.qq.com/s/30OQjOJTPvHnfpralzvVrA)
- [智能网联汽车产业链全景图（2020年6月版）](https://mp.weixin.qq.com/s/grEUnaEhBl4WqCYBlU1tpQ)
- [2019年自动驾驶产业链企业全景图（共300多家）](https://mp.weixin.qq.com/s/Su8LaHFucmi2BUkq1fcjPg)

### Websites (学习网站)<a name="websites"></a>
#### 1，[优达学城 Udacity](https://www.udacity.com/)
The School of Autonomous Systems 
> The field of autonomous vehicles is set to grow by 42% within the next four years, with salaries for top engineers averaging between $300-$500k. Advance your career in this rewarding field by studying 15 hours/week.
**课程 Courses**
- 自动驾驶入门 Introduction to Self-Driving Cars
- 机器人软件工程师 Robotics Software Engineer
- 无人飞行车工程师 Flying Car and Autonomous Flight Engineer
- 自动驾驶工程师 Self-Driving Car Engineer
- 感知融合工程师 Sensor Fusion Engineer
- 数字的自由职业者 Digital Freelancer
- C++编程
- 数据结构与算法 Data Structures and Algorithms
- 计算机视觉 Computer Vision
- AI编程（Python）AI Programming with Python
- 机器学习入门（PyTorch）Intro to Machine Learning with PyTorch
- 机器学习入门（TensorFlow）Intro to Machine Learning with TensorFlow
- 深度强化学习 Deep Reinforcement Learning
- 人工智能 Artificial Intelligence
- 深度学习 Deep Learning

#### 2, [Coursera](https://www.coursera.org/)
Self-Driving Cars Specialization Offered by University of TORONTO
> Launch Your Career in Self-Driving Cars. Be at the forefront of the autonomous driving industry.

**课程 Courses**
- 自动驾驶入门 Introduction to Self-Driving Cars
- 自动驾驶状态估计和定位 State Estimation and Localization for Self-Driving Cars
- 自动驾驶视觉感知 Visual Perception for Self-Driving Cars
- 自动驾驶运动规划 Motion Planning for Self-Driving Cars
- 深度学习专项认证 [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning?#courses)
- 机器学习 [Machine Learning](https://www.coursera.org/learn/machine-learning)


#### 3, [中国大学 MOOC](https://www.icourse163.org/course/BIT-1207432808?tid=1465692443)
> 这是一门面向初学者的无人驾驶车辆慕课，由北京理工大学智能车辆团队倾情打造。理论联系实际，用丰富的案例进行讲解。课程也许不会告诉你无人驾驶全部的“秘密”，但从这门课学到的知识，可以帮助你去探寻无人驾驶的“秘密”。
>来吧，这里有你想要的 ^_^

**课程 Courses**
- [无人驾驶车辆](https://www.icourse163.org/learn/BIT-1207432808?tid=1467141702#/learn/announce)

#### 4, [深蓝学院](https://www.shenlanxueyuan.com/)
当下学术界和企业界应用最广泛的机器人操作系统。
基于摄像头或激光雷达的机器人定位与建图技术，解决“我在哪，我周围是什么”两个问题。
移动机器人导航的核心技术，无人车/无人机等企业的重要技术支撑。
以多种传感器的数据作为输入，经过计算及处理，对机器人的周围环境精确感知的系统。
旋翼无人机被广泛应用于救灾、土地测量、旅游等，自主旋翼无人机作为一项复杂的工程，涉及到感知定位、规划控制等多项核心技术。
- 基础课程
  - 线性代数几何意义
  - 机器学习数学基础
- 算法与数据结构
- 编程与开发
  - C++基础与深度解析
- 机器学习
  - 深度学习理论与实践（视觉方向）
  - 机器学习数学基础
  - 图深度学习：理论与实践（全新版）
  - CUDA入门与深度神经网络加速
- 计算机视觉
  - 深度学习理论与实践（视觉方向）
  - 数字图像处理
  - 计算机视觉应用基础
  - 基于深度学习的物体检测
  - 基于深度学习的人脸识别
- 三维视觉
  - 数字图像处理
  - 三维点云处理
  - 基于图像的三维重建
- 系统与架构
  - ROS理论与实践
- 定位与建图
  - SLAM技术入门，进阶与发展趋势
  - ROS理论与实践
  - 视觉SLAM理论与实践
  - 激光SLAM理论与实践
  - 视觉SLAM基础与VIO进阶
  - 语义SLAM概述
  - VINS-Mono 代码解析
  - 机器人学中的状态估计
  - 视觉SLAM/VIO开源代码解析
  - 视觉SLAM进阶：从零开始手写VIO
  - 多传感器融合定位
- 运动规划
  - ROS理论与实践
  - 自动驾驶控制与规划
  - 移动机器人运动规划
- 环境感知
  - 深度学习理论与实践（视觉方向）
  - 计算机视觉应用基础
  - 自动驾驶环境感知
  - 基于深度学习的物体检测
  - 三维点云处理
  - 多传感器融合感知
- 工业机器人
  - 工业机器人控制
  - ROS机械臂开发：从入门到实战
- 旋翼无人机
  - 自主旋翼无人机导论
  - 从0制作自主空中机器人
  - 智能无人机：从硬件到技术实战

#### 5, 其他平台
- [斯坦福公开课](https://online.stanford.edu/)
- [3D视觉工坊](https://app0s6nfqrg6303.pc.xiaoe-tech.com/page/2733206?navIndex=0)
- [计算机视觉life](https://cvlife.net/)
- [睿慕课](https://www.aiimooc.com/)

### Blogs, News,Platforms and Articles (博客公号) <a name="blogs"></a>
- blogs,[How cities can benefit from automated driving (城市如何从自动驾驶中受益)](https://www.bosch.com/stories/economic-impact-of-self-driving-cars/)
- blogs,[How Google's Self-Driving Car Will Change Everything (谷歌的自动驾驶汽车将如何改变一切)](https://www.investopedia.com/articles/investing/052014/how-googles-selfdriving-car-will-change-everything.asp)
- news, [Introducing the 5th-generation Waymo Driver: Informed by experience, designed for scale, engineered to tackle more environments (引入第 5 代 Waymo 驱动程序：以经验为基础，为规模而设计，旨在应对更多环境)](https://blog.waymo.com/2020/03/introducing-5th-generation-waymo-driver.html)

### Technical Skills (技术学习) <a name="skills"></a>
- Machine Learning 机器学习
  - 混淆矩阵，[Understanding Confusion Matrix(理解混淆矩阵)](https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62) 
  - 交叉验证，[Cross Validation(交叉验证)](https://www.cs.cmu.edu/~schneide/tut5/node42.html) 
- Deep Learning 深度学习
  - 模型设计，[AutoML: Automating the design of machine learning models for autonomous driving(AutoML：自动设计用于自动驾驶的机器学习模型)](https://blog.waymo.com/2019/07/automl-automating-design-of-machine.html)  
  - 模型训练，[A Recipe for Training Neural Networks(训练神经网络的秘诀)](http://karpathy.github.io/2019/04/25/recipe/) 
   
- Computer Vision 计算机视觉
  - 图像形成，[Geometry of Image Formation(图像形成几何)](https://learnopencv.com/geometry-of-image-formation/) 
  - 图像校正，[Understanding Lens Distortion(了解镜头失真)](https://learnopencv.com/understanding-lens-distortion/)
- Object Detection 目标检测
  - 联合交集IoU, [Intersection over Union (IoU) for object detection(用于目标检测的联合交集 (IoU))](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)[3]

### Books(书籍) <a name="books"></a>

#### 自动驾驶入门
- 《自动驾驶技术系列丛书》
- 《第一本无人驾驶书》

#### 自动驾驶必备技术
- 《ROS技术理论与实践》
- 《C++ Prime Plus》
- 《C Prime Plus》
- 《cmake实践》
- 《Effective C++》
- 《More Effective C++》

#### SLAM 系列
- 《视觉SLAM十四讲》
- 《概率机器人》
- 《计算机视觉中的多视图几何》
- 《机器人学中的状态估计》

#### 深度学习
- 《Deep Learning》


### Papers(学术论文) <a name="papers"></a>
  
### Reports（行业报告）<a name="reports"></a>

### Notes 学习笔记 <a name="notes"></a> 
- 无人驾驶入门
- 从零开始一起学习SLAM

### Courses and Videos, 课程和视频 <a name="videos"></a>

### Projects and Codes 实践项目 <a name="projects"></a>
- [projects and codes](https://github.com/linksdl/meta-project-self_driving_cars_projects)

### Jobs 工作机会  <a name="jobs"></a>


### Questions and Challenges 行业问题&挑战 <a name="questions"></a>
- 如何在基于视觉下的交通灯的识别问题，如何判断哪一个红绿灯才是需要作出决策的？
- 如何实现在行驶过程中识别静止车辆突然开门？
- 如何识别大型的拖车（因为形状前小后大）？
- 如何识别公交车（因为中间是个链接体，材质不同导致雷达识别两个同的物体。）
- IMU定位设备的标定问题

### Future 前沿技术 <a name="future"></a>


### 设备厂商
- 激光雷达 Lidar
  - 国产，Robosense
  - 国外, Velodyne

### 技术问题
- 传感器授时，使用GPS
- 多传感器融合定位和建图，紧耦合还是松耦合？ 紧耦合效果会好，紧耦合可能计算量会大一些，所以看应用场景。
- Lidar 与IMU 外参标定，在线标定
- evo 轨迹对比， gps 对比 如果是整形解的rtk，可以作为真值。 ground truth 
- 相机，Lidar, GNSS(GPS+RTK), IMU, 轮速历程计Odometry
- 多传感器融合，以视觉为主还是激光雷达为主
  > 视觉slam方向：常见的方式是一个视觉特征点前端（当然还有基于直接法的前端，如DSO），通过光流
或者描述子建立不同帧特征点之间的关联，后端根据前端特征关联的结果和其他传感器数据进行融合，
根据融合的方式分为基于优化的后端（ORBSLAM2、3, VINS-MONO，VINS-FUSION）以及基于滤波的
后端（MSCKF），视觉通常会提供一个重投影误差作为约束或者更新量 
  > 激光slam方向：目前性能最好使用最广的激光slam方案是基于LOAM的系列方案，LOAM主要是为多线
激光雷达设计的lidar定位和建图的方案，当然，由于现在其他一些lidar硬件的推出，一些LOAM的改进
版本也是适当推出，如（Livox LOAM）。
  > 基于LOAM方案通常前端是对当前帧激光雷达提取特征（通常是面特征和线特征），通常后端结合其他
传感器信息给当前帧到地图中的匹配提供一个良好的初值（激光slam中最重要的事情就是给scan
matching提供一个更准确的init guess）
- 传感器融合方案介绍（LOAM, A-LOAM, LeGO-LOAM, LIO-SAM, LIVOX-LOAM）
- 多传感器融合定位
- 工控机，CANbus, CanNet, Cube
- IMU预积分，IMU不能过长时间作位姿，IMU 
- 组合导航（Novatel, 诺瓦泰17-19W），国产组合导航(3-5W)，IMU自己融合
- 激光雷达，机械的有禾赛、速腾、镭神等，固态的大疆 livox 应用较广


#### 2022技术趋势
![2022技术趋势](./Future(前沿技术)/2022%20top10%20technology%20trends.jpg)

### References 参考文献 <a name="refers"></a>
- [1] Udacity https://www.udacity.com/
- [2] Felix, 2018, So you want to be a self-driving car engineer? 
- [3] Adrian Rosebrock, 2016, Intersection over Union (IoU) for object detection
