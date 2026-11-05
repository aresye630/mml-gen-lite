# 激活DECOR功能

* 操作场景
* 对系统的影响
* 必备事项
* 操作流程
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活DECOR基础功能的操作过程。

当TOB和TOC用户共用基站时，运营商可以通过DECOR特性将TOC用户重定向至大网核心网，TOB用户接入到园区核心网进行服务。

适用于MME

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

* 请仔细阅读DECOR功能。
* eNodeB的配置已经具备，具体请参见该特性页面的应用场景部分描述。
* 已经加载支持该特性的License，对应的License项为“81202740 LKV2DECOR00 DECOR基础功能”和“82207914 LKV2DECOR01 DECOR”。

数据

需要准备全网规划的数据，无需准备与对端网元协商的数据，如下表所示。

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD DCN**** | DCN ID（DCNID） | 0 | 全网规划 | - |
|  | 移动国家代码（MCC） | 123 |  |  |
|  | 移动网号（MNC） | 03 |  |  |
|  | DCN类型（DCNTYPE） | COMMON |  |  |
| ****ADD DCNMEMBER**** | DCN ID（DCNID） | 0 | 全网规划 | - |
|  | MME组识别码（MMEGI） | 0000 |  |  |
| ****ADD DCNMAP**** | DCN ID（DCNID） | 0 | 全网规划 | - |
|  | 起始UE USAGE TYPE（BGNUEUSAGETYPE） | 0 |  |  |
|  | 终止UE USAGE TYPE（ENDUEUSAGETYPE） | 10 |  |  |
| **ADD DCNPLCY** | 用户范围（SUBRANGE） | IMSI\_PRE | 全网规划 | - |
|  | IMSI前缀（IMSIPRE） | 123033601 |  |  |
|  | DCN开关（DCNSW） | ON |  |  |
|  | 源侧UE USAGE TYPE策略（SRUEUSAGETYPE） | YES |  |  |
|  | UE USAGE TYPE获取策略（UEUSAGETYPEPLCY） | HSS |  |  |
| ****SET DCNCTRL**** | 重选策略（RESELECTPLCY） | IMMEDIATE | 全网规划 | - |
|  | 携带UE Usage Type（CONTAINUEUSGTYPE） | YES |  |  |
|  | UE USAGE TYPE携带策略（UEUSGTYPECONPLCY） | USED |  |  |
|  | 非广播TAI（NONTAI） | 0000000000 |  |  |
|  | MMEGI查询策略（MMEGIQUERYPLCY） | LOCAL |  |  |
|  | DNSROLLBACK（域名回退查询） | 0 |  |  |
|  | BACKOFFSW （Backoff Timer分配开关） | OFF |  |  |

## 操作流程

激活DECOR功能操作流程如图1所示。

**图1** 激活DECOR功能操作流程图

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 通过本地配置方式按MME粒度规划DCN。

   运营商可以在本地配置DCN服务的MMEGI的列表。

   1. 为PLMN增加DCN标识

      ****ADD DCN****

      * 建议为PLMN配置一个默认DCN，从而使接入不到普通DCN的用户接入默认DCN完成业务流程。
      * 如果组网上是多PLMN共享MME，则在MME上为每个PLMN配置部署的DCN。例如12303在MME上部署DCN1，12301在MME上部署DCN2，则需要执行如下命令：

        ```
        ADD DCN: DCNID=1, MCC="123", MNC="03", DCNTYPE=COMMON, DESC="eMTC";
        ADD DCN: DCNID=2, MCC="123", MNC="01", DCNTYPE=COMMON, DESC="eMTC";
        ```
   2. 为DCN添加成员列表。

      按DCN的网络规划范围，为DCN添加MMEGI成员。如果DCN包含多个MME POOL，则多次执行此步骤。

      ****ADD DCNMEMBER****
   3. 配置DCN与UE Usage Type的映射关系。

      ****ADD DCNMAP****
   4. 配置MMEGI查询策略以及相关控制参数。

      通过此步骤设置用本地配置查询MMEGI。

      ****SET DCNCTRL****
3. 打开DCN开关并配置DCN业务相关参数。

   **ADD DCNPLCY**

## 任务示例

任务描述

PLMN为12303的运营商规划了两个普通类型的核心网。DCN1（DCNID为0，eMBB网络）和DCN2（DCNID为1，园区网络）。DCN1的规划范围是MMEGI为01，对应的UE Usage Type为0~10的用户。开启所有用户重定向，其中园区基于号段关闭。配置使用本地配置UE Usage Type来识别DCN。

脚本

//增加DCN。

```
ADD DCN: DCNID=0, MCC="123", MNC="03", DCNTYPE=COMMON, DESC="TOC";
```

```
//为DCN增加MME群组成员记录。
```

```
ADD DCNMEMBER: DCNID=0, MMEGI="0001";
```

//配置DCN与UE Usage Type的映射关系。

```
ADD DCNMAP: DCNID=0, BGNUEUSAGETYPE=0, ENDUEUSAGETYPE=10;
```

//配置DCN业务相关参数，配置园区基于号段全关闭。

```
ADD DCNPLCY:SUBRANGE=ALL_USER, DCNSW=ON, SRUEUSAGETYPE=YES, UEUSAGETYPEPLCY=LOCAL, UEUSAGETYPE=10, GWSELPLCY=NO;
ADD DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="12300630", DCNSW=OFF;
```

//配置DCN控制参数。

```
SET DCNCTRL:RESELECTPLCY=IMMEDIATE, CONTAINUEUSGTYPE=NO, NONTAI="0000000000", MMEGIQUERYPLCY=LOCAL, DNSROLLBACK=MME-0&PGW-0&SGW-0, BACKOFFSW=OFF;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2DECOR00", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV2DECOR01", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
