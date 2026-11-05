# 激活Pool内Decor

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活Pool内DECOR功能的操作过程。

在支持DCNR（Dual connectivity with New Radio）能力的MME和不支持DCNR能力的MME组Pool的场景下，对于支持DCNR能力的终端接入到不支持DCNR能力的MME上的场景，UNC支持将其重定向到Pool内支持DCNR能力的MME上进行服务。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读WSFD-208003 Pool内Decor。
* eNodeB的配置已经具备，具体请参见该特性页面的应用场景部分描述。
* 完成加载License。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD MMERESELPLCY** | 用户范围（SUBRANGE） | IMSI\_PRE | 全网规划 | 设置重选策略。 |
|  | IMSI前缀（IMSIPRE） | 12303 |  |  |
|  | 重选开关（RESELSW） | ON |  |  |
|  | 重选策略（RESELPLCY） | REROUTE\_NAS |  |  |
|  | 重选条件（RESELCOND） | DCNR\_UUT\_INCLUDE |  |  |
|  | UE USAGE TYPE群组标识（UEUSGTYPEGPID） | 10 |  |  |
|  | 目标MME组索引（TMMEGPIDX） | 0 |  |  |
| **ADD MMEGP** | MME群组索引（MMEGPIDX） | 0 | 全网规划 | 增加MME群组。 |
|  | 移动国家代码（MCC） | 123 |  |  |
|  | 移动网号（MNC） | 03 |  |  |
|  | MME组识别码（MMEGI） | 0001 |  |  |
|  | 描述（DESC） | NSA |  |  |
| **ADD MMEGPMEM** | MME群组索引（MMEGPIDX） | 0 | 全网规划 | 增加MME群组成员。 |
|  | MME编码（MMEC） | 01 |  |  |
|  | 设备能力（CAP） | 10 |  |  |
| **ADD UEUSGTYPEGP** | UE USAGE TYPE群组标识（ UEUSGTYPEGPID ） | 10 | 本端规划 | 增加UE Usage Type群组。 |
|  | 描述（DESC） | NSA |  |  |
| **ADD UEUSGTYPEGPMEM** | UE USAGE TYPE群组标识（UEUSGTYPEGPID） | 10 | 本端规划 | 增加UE USAGE TYPE群组成员。 |
|  | 起始UE USAGE TYPE（UEUSGTYPEGPID） | 130 |  |  |
|  | 终止UE USAGE TYPE（ENDUEUSGTYPE） | 150 |  |  |
| ****SET DCNCTRL**** | 重选策略（RESELECTPLCY） | IMMEDIATE | 全网规划 | 设置DCN控制参数。 |
|  | 携带UE Usage Type（CONTAINUEUSGTYPE） | YES |  |  |
|  | UE USAGE TYPE携带策略（UEUSGTYPECONPLCY） | USED |  |  |
| **STR DCNOFFLOAD** | 迁移用户范围（OFFLOADTYPE） | ALL\_USER | 本端规划 | 启动DCN迁移任务。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 规划支持DCNR能力的MME群组信息。
   1. 增加MME群组

      **ADD MMEGP**
   2. 为MME群组添加成员，如果群组中包含多个MME编码，则多次执行此步骤。

      **ADD MMEGPMEM**
3. **可选：**当4中重选条件中有需要使用UE Usage Type，则需要配置此步骤。
   1. 添加UE Usage Type群组标识。配置该群组标识，用于配置本地的DNS记录。

      **ADD UEUSGTYPEGP**
   2. 添加UE Usage Type群组的成员列表。

      **ADD UEUSGTYPEGPMEM**
4. 配置重选策略。

   **ADD MMERESELPLCY**
5. 配置DECOR相关控制参数

   **SET DCNCTRL**
6. 当4中重选条件中包含UE Usage Type，则需要此步骤，向HSS获取UE Usage Type。

   实际部署时，需要根据HSS是否支持本特性，组合如下命令进行配置，
   * 所有HSS都支持此特性：

     ```
     SET DMCMPT: SF2=FLSTID2_BIT20-1;
     ```
   * 本网所有的HSS支持此特性，外网所有HSS不支持此特性：

     ```
     ADD DMCMPTBYIMSI: SUBRANGE=HOME_USER, NOID=0, SF2=FLSTID2_BIT20-1;
     ```
   * 仅46123和46321为IMSI前缀的用户注册的HSS支持此特性：

     ```
     ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46123",  SF2=FLSTID2_BIT20-1;
     ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46321", SF2=FLSTID2_BIT20-1;
     ```

   * 查询系统中Diameter兼容性配置

     命令**ADD DMCMPTBYIMSI**与**SET DMCMPT**中除“用户范围”、“运营商标识”以及“IMSI前缀”外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令**ADD DMCMPTBYIMSI**的配置。因此在配置**ADD DMCMPTBYIMSI**前需先执行**LST DMCMPT**查询系统中**SET DMCMPT**的配置记录，确保命令**ADD DMCMPTBYIMSI**的配置记录中所携带的参数默认值不影响系统已有配置。

     **LST DMCMPT**: ;
   * 本网用户

     **ADD DMCMPTBYIMSI**: SUBRANGE=HOME\_USER, NOID=运营商标识, SF2=特性列表;
   * 外网用户

     **ADD DMCMPTBYIMSI**: SUBRANGE=FOREIGN\_USER, NOID=运营商标识, SF2=特性列表;
   * 特定IMSI前缀的用户

     **ADD DMCMPTBYIMSI**: SUBRANGE=IMSI\_PREFIX, IMSIPRE=IMSI前缀, SF2=特性列表;
7. 打开本功能的License配置开关。

   **SET LICENSESWITCH**
8. **可选：**配置专网用户迁移。需要将本MME的用户快速归属到各自DCN中时，执行此步骤。

   **STR DCNOFFLOAD**

## 任务示例

任务描述

假设本网HSS支持本特性，其他用户的归属HSS不支持本特性。在如下场景下激活本特性：

PLMN为12303的运营商规划了不支持DCNR能力的MME1和支持DCNR能力的MME2组成MME Pool，在MME1上配置为IMSI前缀为12303的终端，使用UE网络能力和UE Usage Type作为重选判定条件来决定是否为UE进行Pool内重选。当MME1上有IMSI前缀为12303，UE Usage Type为140的终端接入，终端支持DCNR能力并且终端的UE Usage Type在所配置的UE USAGE TYPE群组范围内，MME1将其重选到支持DCNR能力的MME2上，MME2的MMEC为01。

脚本

//以下脚本在MME1上进行配置。

//增加支持DCNR能力的MME群组。

```
ADD MMEGP: MMEGPIDX=0, MCC="123", MNC="03", MMEGI="0001", DESC="NSA";
```

//增加MME群组成员记录。

```
ADD MMEGPMEM: MMEGPIDX=0, MMEC="01", CAP=10;
```

//可选，配置UE Usage Type群组。

```
ADD UEUSGTYPEGP: UEUSGTYPEGPID=10, DESC="NSA";
ADD UEUSGTYPEGPMEM: UEUSGTYPEGPID=10, BGNUEUSGTYPE=130, ENDUEUSGTYPE=150;
```

//配置MME的策略参数。

```
ADD MMERESELPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", RESELSW=ON, RESELPLCY=REROUTE_NAS, RESELCOND=DCNR_UUT_INCLUDE, UEUSGTYPEGPID=10, TMMEGPIDX=0;
```

//配置DCN控制参数。

```
SET DCNCTRL: RESELECTPLCY=IMMEDIATE, CONTAINUEUSGTYPE=YES, UEUSGTYPECONPLCY=USED;
```

//可选，本网用户以外的其他用户的归属HSS都不支持本特性。

```
SET DMCMPT: SF2=FLSTID2_BIT20-0;
```

//查询系统中Diameter兼容性配置。

```
LST DMCMPT:;
```

//设置本HSS支持DECOR特性， 需确保命令ADD DMCMPTBYIMSI中其他参数所携带的默认值不影响系统已有的Diameter兼容性配置。

```
ADD DMCMPTBYIMSI: SUBRANGE=HOME_USER, NOID=0, SF2=FLSTID2_BIT20-1, HSIMSVOPS=BY_SYS_CAP;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2DECOR02", SWITCH=ENABLE;
```

//可选，启动迁移任务。将本MME的用户快速归属到各自DCN中。

```
STR DCNOFFLOAD: OFFLOADTYPE=ALL_USER;
```

版权所有 © 华为技术有限公司
