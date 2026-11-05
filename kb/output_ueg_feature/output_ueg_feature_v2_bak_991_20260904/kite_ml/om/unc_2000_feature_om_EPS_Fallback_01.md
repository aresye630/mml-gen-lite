# 激活EPS Fallback

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

EPS Fallback（Evolved Packet System Fallback）是指在无线网络没有部署VoNR（Voice over NR，NR网络语音业务）的情况下，当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行通话时，会通过切换或者重定向的方式回落到4G网络通过VoLTE进行通话。它是VoLTE向VoNR演进的过渡语音方案。

**说明** 

适用于AMF、SMF。

## 必备事项

前提条件

- 请仔细阅读GWFD-025702 EPS Fallback特性概述。
- 已完成加载License。
- 完成N26接口配置，并完成基于N26接口5GC互操作的新建部署。

数据

| 类别                  | 参数名称                           | 取值样例            | 获取方法   | 说明                                                                                                                                                                     |
|:--------------------|:-------------------------------|:----------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET NGIMSVOPS       | AMF是否支持IMS语音 (AMFHOMO )        | SUPPORT         | 全网规划   | 设置VoPS配置                                                                                                                                                               |
| SET NGIMSVOPS       | Data Centric类型终端支持VoPS（DCVOPS） | SUPPORT         | 全网规划   | 设置允许Data Centric终端使用5G语音功能                                                                                                                                             |
| ADD CPAPN           | APN名称（APN）                     | ims             | 全网规划 - | 配置IMS网络的APN                                                                                                                                                            |
| SET CPAPNIMSATTR    | APN名称                          | ims             | 本端规划   | 配置APN的IMS属性。                                                                                                                                                           |
| SET CPAPNIMSATTR    | IMS开关                          | ENABLE          | 本端规划   | 配置APN的IMS属性。                                                                                                                                                           |
| ADD PCSCFGROUP      | P-CSCF组名                       | vonr            | 本端规划   | 添加P-CSCF组                                                                                                                                                              |
| ADD PCSCFGROUP      | IP地址版本                         | IPV4            | 本端规划   | 添加P-CSCF组                                                                                                                                                              |
| ADD PCSCFGROUP      | P-CSCF获取方式                     | LOCAL           | 本端规划   | 添加P-CSCF组                                                                                                                                                              |
| ADD PCSCFIP         | P-CSCF组名                       | vonr            | 本端规划   | 添加P-CSCF地址                                                                                                                                                             |
| ADD PCSCFIP         | IP地址版本                         | IPV4            | 本端规划   | 添加P-CSCF地址                                                                                                                                                             |
| ADD PCSCFIP         | IPv4地址                         | 10.28.236.11    | 本端规划   | 添加P-CSCF地址                                                                                                                                                             |
| ADD PCSCFIP         | 权重                             | 10              | 本端规划   | 添加P-CSCF地址                                                                                                                                                             |
| ADD PCSCFIP         | P-CSCF获取方式                     | LOCAL           | 本端规划   | 添加P-CSCF地址                                                                                                                                                             |
| ADD PCSCFIMSISDNSEG | IMSI/MSISDN号段名称                | vonr            | 全网规划   | 配置IMSI/MSISDN号码段                                                                                                                                                       |
| ADD PCSCFIMSISDNSEG | IMSI/MSISDN号段类型                | IMSI            | 全网规划   | 配置IMSI/MSISDN号码段                                                                                                                                                       |
| ADD PCSCFIMSISDNSEG | 号段起始字符串                        | 123031200100026 | 全网规划   | 配置IMSI/MSISDN号码段                                                                                                                                                       |
| ADD PCSCFIMSISDNSEG | 号段结束字符串                        | 123031200100027 | 全网规划   | 配置IMSI/MSISDN号码段                                                                                                                                                       |
| ADD PCSCFGRPBNDAPN  | APN名称                          | ims             | 本端规划   | 在APN下将某指定号段绑定到P-CSCF组。也可以将整个APN绑定到P-CSCF组。                                                                                                                             |
| ADD PCSCFGRPBNDAPN  | 缺省标记                           | IMSI_MSISDN_SEG | 本端规划   | 在APN下将某指定号段绑定到P-CSCF组。也可以将整个APN绑定到P-CSCF组。                                                                                                                             |
| ADD PCSCFGRPBNDAPN  | IMSI/MSISDN号段名称                | vonr            | 本端规划   | 在APN下将某指定号段绑定到P-CSCF组。也可以将整个APN绑定到P-CSCF组。                                                                                                                             |
| ADD PCSCFGRPBNDAPN  | 主IPv4P-CSCF组                   | vonr            | 本端规划   | 在APN下将某指定号段绑定到P-CSCF组。也可以将整个APN绑定到P-CSCF组。                                                                                                                             |
| SET SMTIMER         | EPS Fallback保护定时器时长(秒)         | 5               | 全网规划   | 设置EPS Fallback保护定时器时长  说明： 5G语音QoS Flow创建触发EPS Fallback流程后启动该定时器，如果定时器超时后，Handover流程/重定（TAU）还未启动，则SMF指示PCF，语音承载创建失败。 该参数配置时应大于基站侧EPS Fallback的保护定时器时长，并小于IMS的AAR定时器时长。 |
| SET SOFTPARAOFBIT   | BYTE_EX_B330 BIT2              | 1               | 全网规划   | 设置EPS Fallback回落后，TAU过程DOWNLINK NAS TRANSPORT消息携带UE的SRVCC能力。                                                                                                           |

## 操作步骤

以下步骤适用于AMF。

1. 进入“MML命令行-UEG”窗口。-AMF
2. 打开AMF该功能的License配置开关。

   **SET LICENSESWITCH**
3. 配置系统支持IMS Voice Over PS服务。

   **SET NGIMSVOPS**
4. 设置EPS Fallback回落后，TAU过程DOWNLINK NAS TRANSPORT消息携带UE的SRVCC能力。

   **SET SOFTPARAOFBIT**

以下步骤适用于SMF。

5. 进入“MML命令行-UEG”窗口。-SMF
6. 打开SMF该功能的License配置开关。

   **SET LICENSESWITCH**
7. 配置IMS网络APN。

   **ADD CPAPN**
8. 修改APN参数。

   **SET CPAPNIMSATTR**
9. 添加P-CSCF组配置。

   **ADD PCSCFGROUP**
10. 添加P-CSCF地址配置。

    **ADD PCSCFIP**
11. 增加IMSI和MSISDN号段

    **ADD PCSCFIMSISDNSEG**
12. 添加P-CSCF组和APN的绑定关系，可以整APN绑定，或者按照IMSI/MSISDN号段绑定。

    **ADD PCSCFGRPBNDAPN**
13. 设置EPS Fallback保护定时器时长，该参数配置时应大于基站侧EPS Fallback的保护定时器时长，并小于IMS的AAR定时器时长。

    **SET SMTIMER**

## 任务示例

任务描述

激活EPS Fallback特性。

脚本

//进入“MML命令行-UEG”窗口。

//该功能AMF和SMF的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2EFBAM01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2EFBSM01", SWITCH=ENABLE;
```

//配置系统支持IMS Voice Over PS服务。

```
SET NGIMSVOPS: AMFHOMO=SUPPORT,DCVOPS=SUPPORT;
```

//配置IMS网络APN。

```
ADD CPAPN: APN="ims";
```

//修改IMS APN的参数。

```
SET CPAPNIMSATTR: APN="ims", IMSSWITCH=ENABLE;
```

//添加P-CSCF组配置。

```
ADD PCSCFGROUP: GROUPNAME="vonr", IPVERSION=IPV4, ALLOCTYPE=LOCAL;
```

//添加P-CSCF地址配置。

```
ADD PCSCFIP: GROUPNAME="vonr", IPVERSION=IPV4, PCSCFIPV4="10.28.236.11", WEIGHT=10, ALLOCTYPE=LOCAL;
```

//增加IMSI和MSISDN号段。

```
ADD PCSCFIMSISDNSEG: SEGMENTNAME="vonr", SEGMENTTYPE=IMSI, SEGSTART="123031200100026", SEGEND="123031200100027";
```

//将APN绑定到P-CSCF组。

```
ADD PCSCFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="vonr";
```

//在APN下将某指定号段绑定到P-CSCF组。

```
ADD PCSCFGRPBNDAPN: APN="ims", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="vonr", PRIORITY=1, MPCSCFGRPIPV4="vonr";
```

//设置EPS Fallback保护定时器时长，该参数配置时应大于基站侧EPS Fallback的保护定时器时长，并小于IMS的AAR定时器时长。

```
SET SMTIMER: TEPSFB=5;
```

//设置EPS Fallback回落后，TAU过程DOWNLINK NAS TRANSPORT消息携带UE的SRVCC能力。

```
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=330, VALUE=VALUE_1, POSITION=2;
```