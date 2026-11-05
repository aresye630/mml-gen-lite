# 激活AMF Pool 用户迁移特性

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活AMF Pool用户迁移特性的操作过程。

AMF Pool用户迁移特性是指根据AMF Pool内各AMF的负载情况，操作人员通过下发启动迁移命令，将负载过高或需要升级的AMF上的用户迁移到AMF Pool中的其他AMF上，从而实现实时、动态地调整AMF Pool内的负荷分布。

适用于AMF。

## 必备事项

前提条件

* 请仔细阅读WSFD-104302 AMF Pool用户迁移特性概述。
* 完成加载License。
* 完成激活AMF Pool特性。
* 需要对端网元gNodeB支持AMF Pool用户迁移特性。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****MOD AMFINFO**** | 相对容量（CAPACITY） | 0 | 全网规划 | 用户迁移信息 |
| ****MOD NFPROFILE**** | NF实例名称（NFINSTANCENAME） | AMF\_Instance\_0 | 全网规划 |  |
|  | 容量（CAPACITY） | 0 | 全网规划 |  |
| ****STR OFFLOADAMF**** | 迁移类型（TYPE） | ALL | 本端规划 |  |

## 操作步骤

配置特性开关以及迁移配置参数。

1. 进入“MML命令行-UNC”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**

配置迁移任务

3. 启动用户迁移任务。

   + 迁移全部用户

     ****STR OFFLOADAMF****
   + 迁移部分用户

     ****STR OFFLOADAMF****
   + 迁移百分比用户

     ****STR OFFLOADAMF****
   + 按IMSI迁移单个用户

     ****STR OFFLOADAMF****

配置按指定IMSI的单个用户至指定目标AMF的迁移类型

4. 查询目标AMF名称。

   ****LST AMFINFO****
5. 在原AMF上配置指定IMSI的单个用户至指定目标AMF的迁移参数，迁移单个用户。

   ****STR OFFLOADAMF****

## 任务示例

任务描述

* 任务1：

  将该AMF上全部的用户同时启动迁移任务。
* 任务2：

  对该AMF启动用户迁移任务，迁移类型为迁移百分比用户，迁移比率设为10%。
* 任务3：

  将注册在AMF1上的IMSI为"123037301000001"的用户迁移至AMF2。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2SMAP01", SWITCH=ENABLE;
```

* 任务1的脚本。

  //对需要迁移的AMF下发启动迁移命令，迁移所有用户。

  ```
  STR OFFLOADAMF: TYPE=ALL;
  ```
* 任务2的脚本。

  //对需要迁移的AMF下发启动迁移命令，迁移比率为10%。

  ```
  STR OFFLOADAMF: TYPE=RATE, OFFLOADRATE=10;
  ```
* 任务3的脚本。

  //查询目标AMF名称。

  ```
  LST AMFINFO:;
  ```

  //配置按IMSI迁移单个用户至指定目标AMF的迁移参数。

  ```
  STR OFFLOADAMF: TYPE=IMSI, IMSI="123037301000001", TAMF="AMF2";
  ```

版权所有 © 华为技术有限公司
