### 彻底搞懂基于LOAM框架的3D激光SLAM

- UBUNTU 20.04 LTS 安装DOCKER：https://www.cnblogs.com/songxi/p/12788249.html
- 《视觉SLAM十四讲》
- 两种常见的点云配准方法ICP&NDT https://zhuanlan.zhihu.com/p/96908474
- LOAM细节分析 https://zhuanlan.zhihu.com/p/57351961
- LOAM源码注解版： https://github.com/cuitaixiang/LOAM_NOTED
- Gtsam gtsam 是基于因子图的C++库
	- https://gtsam.org/tutorials/intro.html
	- https://github.com/borglab/gtsam
- (11条消息) 微鉴道长的博客_zkk9527_CSDN博客-SLAM学习笔记 https://blog.csdn.net/zkk9527?t=1
- 


#### 01 激光SLAM概述 & 第一个3D激光SLAM

- https://github.com/laboshinl/loam_velodyne
- Dokcer运行环境映射本地目录
- sudo docker pull osrf/ros:kinetic-desktop-full
- UBUNTU 20.04 LTS 安装DOCKER：https://www.cnblogs.com/songxi/p/12788249.html
- 矢量地图，定位地位，高精地图（基于图像，基于激光）。
- 车道线提取（三维重建，创建索引，路面提取，强度过滤，车道线模版搜索）


#### 02 里程计介绍
- 轮速里程计
- IMU（惯性测量单元）
- 视觉里程计
- 激光里程计
- 激光+IMU+GPS
- 激光+轮速计
- 激光+视觉
- 激光里程计（R，t）
	- 点云运动畸变 & 矫正
	- ICP & NDT
	- PL-ICP
	- 非线性最小二乘
	- 梯度下降法
	- 高斯牛顿法
	- L-M方法
	- Ceres, g2o, gtsam

- LOAM: https://github.com/laboshinl/loam_velodyne
	- LOAM，即Lidar Odometry and Mapping in Real Time,是卡耐基梅隆大学（CMU）的 Ji Zhang 等于2014
	年提出的使用激光雷达完成定位与三维建图的算法。
	- 在 Lidar Odometry 部分，通过提取每帧点云的角点和平面点(基于曲率)，并以点到线的距离和点到
	平面的距离作为优化函数，采用L-M方法求取最优解，得到两帧点云的位姿变换关系。
- LEGO-LOAM
	- 分割模块：将每一帧点云重投影到扇区内，进行地面分割，同时对非地面进行分割聚类;
	- 特征提取模块：和LOAM一致，提取角点和平面点；
	- Lidar Odometry 模块：和LOAM一致构建约束关系，采用两次L-M方法优化，得到位姿变换矩阵；
	- Lidar Mapping 模块：采用图优化的方式构建scan-to-map的约束关系，并加入回环检测；
- 前端里程计改进思路：
	- （1）滤除噪点，考虑去除掉远距离的激光点；
	- （2）考虑使用轮速计或GPS作为初始值，约束激光里程计；

 #### 03 后端优化
 - 基于滤波的方法
 - 图优化方法

 #### 04 回环检测
- 回环检测方法：
	- 1 特征匹配的方法激光：点云配准 scan to scan， scan to map
	- 2 基于里程计的方法，可以基于里程计判断是否回到相同位置，加载对应位置的关键帧进行匹配优化；（LEGO-LOAM
	- 3 深度学习方法，采用深度学习的方法判断是否回到相同场景；（SC-LEGO-LOAM）





