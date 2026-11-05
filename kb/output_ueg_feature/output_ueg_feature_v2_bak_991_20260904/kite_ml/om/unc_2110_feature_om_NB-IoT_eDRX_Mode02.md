# 激活NB-IoT eDRX模式（SGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活NB-IoT eDRX模式特性的操作过程。

**说明** 

适用于SGW-C

## 必备事项

前提条件

- 请仔细阅读GWFD-026104 NB-IoT eDRX模式特性概述（SGW-C）。
- 完成加载License。

数据

| 类别                  | 参数名称                           | 取值样例        | 获取方法   | 说明                                        |
|:--------------------|:-------------------------------|:------------|:-------|:------------------------------------------|
| SET SMFGLBDLBUFTIME | NB-IoT用户下行数据缓存时长（NBIOTUSER）    | 200         | 本端规划   | 全局的NB-IoT用户下行报文缓存时长。                      |
| ADD SMFAPNDLBUFTIME | APN名称（APN）                     | test        | 本端规划   | 指定APN下的NB-IoT用户下行报文缓存时长。                  |
| ADD SMFAPNDLBUFTIME | NB-IoT用户下行报文缓存时长(秒)（NBIOTUSER） | 200         | 本端规划   | 指定APN下的NB-IoT用户下行报文缓存时长。                  |
| SET PFCPCMPT        | 是否支持BAR信元（BAR）                 | SUPPORT（支持） | 全网规划   | 控制PFCP接口是否支持BAR（Buffering Action Rule）信元。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. **可选：**配置下行数据到达S-GW时，全局的NB-IoT用户下行报文缓存时长。

   **SET SMFGLBDLBUFTIME**
4. 配置下行数据到达S-GW时，指定APN下的NB-IoT用户下行报文缓存时长。

   **ADD SMFAPNDLBUFTIME**
5. 配置下行数据到达S-GW时，PFCP接口支持BAR（Buffering Action Rule）信元。

   ****SET PFCPCMPT****

## 任务示例

任务描述

在UEG上配置NB-IoT eDRX模式功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WNBDRX11",SWITCH=ENABLE;
```

//配置下行数据到达S-GW时，S-GW缓存报文的缓存时长。

```
SET SMFGLBDLBUFTIME: NBIOTUSER=200;
ADD SMFAPNDLBUFTIME: APN="test", NBIOTUSER=200;
```

//配置下行数据到达S-GW时，PFCP接口支持BAR（Buffering Action Rule）信元。

```
SET PFCPCMPT:BAR = SUPPORT;
```