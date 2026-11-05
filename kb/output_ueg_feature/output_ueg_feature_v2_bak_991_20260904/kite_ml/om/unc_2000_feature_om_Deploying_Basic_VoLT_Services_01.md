# 激活VoLTE基础语音业务（适用于SGW-C/PGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程。

## 必备事项

前提条件

- 请仔细阅读GWFD-025401 VoLTE基础语音业务特性概述
- 本特性受License控制，请先完成加载License。

数据

| 类别               | 参数名称                          | 取值样例                | 获取方法   | 说明                                                                                                                                                               |
|:-----------------|:------------------------------|:--------------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET CPAPNIMSATTR | IMS开关（IMSSWITCH）              | ENABLE              | 全网规划   | 开启IMS功能开关。 业务处理过程中优先应用APN下的设置，只有当APN下配置为“INHERIT”时才应用全局下的设置。                                                                                                     |
| SET CPAPNIMSATTR | 信令空口增强开关（SIGNALRADIOPRE）      | ENABLE              | 全网规划   | 用于开启IMS信令空口增强功能。                                                                                                                                                 |
| SET DDNATTR      | 携带EBI（EBI）                    | Enable(使能)          | 与对端协商  | 配置支持在Downlink Data Notification消息中携带EBI信元。 协议中Downlink Data Notification消息中的Bearer ID为可选信元，为确保MME能够通过Downlink Data Notification消息中的Bearer ID识别VoLTE语音被叫，需要配置此功能。 |
| SET DDNATTR      | EBI值（EBIVALUE）                | DEFAULTBEARER(缺省承载) | 与对端协商  | 配置支持在Downlink Data Notification消息中携带EBI信元。 协议中Downlink Data Notification消息中的Bearer ID为可选信元，为确保MME能够通过Downlink Data Notification消息中的Bearer ID识别VoLTE语音被叫，需要配置此功能。 |
| SET CONFCTRL     | EPS消息缓存重发的次数（EPSRETRYTIMES）   | 3                   | 本端规划   | 配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数。次数达到设置值时，消息将被丢弃。  说明： EPSRETRYTIMES建议默认值为3。                                         |
| SET CONFCTRL     | EPS消息缓存重发的时间间隔(s)（EPSTIMEOUT） | 2                   | 本端规划   | 配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。    |

## 操作步骤

打开License配置开关。

1. 进入“MML命令行-UEG”窗口。
2. 打开License配置开关。

   **SET LICENSESWITCH**

3. 开启全局缺省PCC开关。

   **SET PCCFUNC**
4. 开启APN下的PCC开关。

   **SET APNPCCFUNC**
5. 将指定的PCRF分组及号段信息绑定到指定APN。

   **ADD PCRFGRPBNDAPN**

配置基于APN的IMS业务

6. 配置IMS使能开关和IMS信令空口增强开关，绑定到指定APN实例下。
7. 配置支持在Downlink Data Notification消息中携带EBI信元。

   **SET DDNATTR**
8. 配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数；配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。

   **SET CONFCTRL**

## 任务示例

任务描述

部署VoLTE基础语音业务。

脚本

**打开License开关**

//进入“MML命令行-UEG”窗口。

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3W9IMSA12", SWITCH=ENABLE;
```

//开启全局缺省PCC开关。

```
SET PCCFUNC: HOMEPCCSWITCH=ENABLE;
```

//开启APN下的PCC开关。

```
SET APNPCCFUNC: APN="ims", HOMEPCCSWITCH=ENABLE;
```

//将指定的PCRF分组及号段信息绑定到指定APN。参数PCRFGRPNAME使用**ADD PCRFGROUP**命令配置生成。执行该命令前请先通过**LST PCRFGROUP**查询当前是否已添加该PCRF Group。根据查询结果，选择是否配置该参数。

```
ADD PCRFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, PCRFGRPNAME="aaa";
```

**配置基于APN的IMS业务**

//配置IMS使能开关和IMS信令空口增强开关，绑定到指定APN实例下。

```
SET CPAPNIMSATTR: APN="ims", IMSSWITCH=ENABLE, SIGNALRADIOPRE=ENABLE;
```

//配置支持在Downlink Data Notification消息中携带EBI信元。

```
SET DDNATTR: EBI=Enable, EBIVALUE=DefaultBearer;
```

//配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数；配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。

```
SET CONFCTRL: EPSRETRYTIMES=3, EPSTIMEOUT=2;
```