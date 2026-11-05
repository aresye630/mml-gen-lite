# 激活基于用户群的灵活鉴权

* 操作场景
* 必备事项
* 操作流程
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活基于用户群的灵活鉴权特性的操作过程。

通过基于用户群的灵活鉴权功能，UEG可以针对不同的用户群的属性使用差异化的安全策略。

适用于SGSN、MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-021510 基于用户群的灵活鉴权特性概述。

* 安全功能被启用：
  + 在Gb模式下，将**ADD GBAUTHCIPH**命令中的“SECPLC”参数设置为“AUTHANDPROTECTED”或“AUTHONLY”。
  + 在Iu模式下，将**ADD IUAUTHCIPH**命令中的“SECPLC”参数设置为“AUTHANDPROTECTED”或“AUTHONLY”。
  + 在S1模式下，将**ADD S1USRSECPARA**命令中的“SECPLC”参数设置为“AUTHANDPROTECTED”；“OPTIONAL”参数设置为“YES”。

* 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD GBAUTHCIPH**  **ADD IUAUTHCIPH**  ****ADD S1USRSECPARA**** | IMSI前缀（IMSIPRE） | 30801 | 全网规划 | 安全配置的相关参数 |
|  | 鉴权事件（AUTHEVENT） | ATTACH | 全网规划 |  |
|  | 鉴权周期（AUTHPERIOD） | 24 | 全网规划 |  |
|  | 鉴权事件上限（AUTHEVENTTHRESHOLD） | 100 | 全网规划 |  |

## 操作流程

激活基于用户群的灵活鉴权操作流程如图1所示。

**图1** 激活基于用户群的灵活鉴权操作流程

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 配置基于用户群的灵活鉴权策略。

   * Gb模式下增加指定用户群的灵活鉴权策略。

     **ADD GBAUTHCIPH**
   * Iu模式下增加指定用户群的灵活鉴权策略。

     **ADD IUAUTHCIPH**
   * S1模式下增加指定用户群的灵活鉴权策略。

     ****ADD S1USRSECPARA****

## 任务示例

任务描述

* 场景一：S1模式下，启用不同PLMN的灵活鉴权功能。

  添加IMSI前缀为“30801”，安全策略为“既鉴权又保护”，鉴权事件为“ATTACH-1”，鉴权事件上限为“3”的HOME PLMN的灵活鉴权参数。

  添加IMSI前缀为“30802”，安全策略为“既鉴权又保护”，鉴权事件为“ATTACH-1&INTRA\_TAU-1”，鉴权事件上限为“2”的CONNECT PLMN的灵活鉴权参数。
* 场景二：启用特定用户群的灵活鉴权功能。

  Gb模式下，添加IMSI前缀为“308010001”，安全策略为“既鉴权又保护”，鉴权事件为“PTMSI\_ATTACH-1&IMSI\_ATTACH-1”，鉴权事件上限为“3”的特定用户群的灵活鉴权参数。

  Iu模式下，添加IMSI前缀为“308010000000001”，安全策略为“既鉴权又保护”，鉴权事件为“INTRA\_RAU-1&IMSI\_ATTACH-1”，鉴权事件上限为“2”的特定用户的灵活鉴权参数。

脚本

* 脚本一

  //开启基于用户群的灵活鉴权功能开关。

  ```
  SET LICENSESWITCH: LICITEM="LKV2FLEXAUTH02", SWITCH=ENABLE;
  ```

  //添加HOME PLMN的灵活鉴权参数。

  ```
  ADD S1USRSECPARA:IMSIPRE="30801",SECPLC=AUTHANDPROTECTED,OPTIONAL=YES,AUTHEVENT=ATTACH-1,AUTHEVENTTHRESHOLD=3;
  ```

  //添加CONNECT PLMN的灵活鉴权参数。

  ```
  ADD S1USRSECPARA:IMSIPRE="30802",SECPLC=AUTHANDPROTECTED,OPTIONAL=YES,AUTHEVENT=ATTACH-1&INTRA_TAU-1,AUTHEVENTTHRESHOLD=2;
  ```

* 脚本二

  //开启基于用户群的灵活鉴权功能开关。

  ```
  SET LICENSESWITCH: LICITEM="LKV2FLEXAUTH02", SWITCH=ENABLE;
  ```

  //Gb模式下，添加特定用户群的灵活鉴权参数。

  ```
  ADD GBAUTHCIPH:IMSIPRE="308010001",SECPLC=AUTHANDPROTECTED,AUTHEVENT=PTMSI_ATTACH-1&IMSI_ATTACH-1,AUTHEVENTTHRESHOLD=3;
  ```

  //Iu模式下，添加特定用户的灵活鉴权参数。

  ```
  ADD IUAUTHCIPH:IMSIPRE="308010000000001",SECPLC=AUTHANDPROTECTED,AUTHEVENT=INTRA_RAU-1&IMSI_ATTACH-1,AUTHEVENTTHRESHOLD=2;
  ```

版权所有 © 华为技术有限公司
