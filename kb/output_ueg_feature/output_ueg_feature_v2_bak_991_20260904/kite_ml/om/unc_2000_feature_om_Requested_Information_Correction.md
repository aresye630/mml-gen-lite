# 激活请求信息纠正功能

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活请求信息纠正功能特性的操作过程。

在激活PDP上下文/PDN连接的过程中，UEG会检查用户请求的APN、PDP/PDN类型和PDP/PDN地址三元组与HLR/HSS中签约的三元组是否一致，如果两者不一致，则拒绝用户的激活请求。这种不一致通常是用户对手机参数设置或签约数据重复等错误引起的，所以，UEG提供了请求信息纠正的功能，减少由于手机参数设置或签约数据重复等错误造成的激活失败。

**说明** 

适用于SGSN、MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-020905 请求信息纠正功能特性概述（适用于SGSN、MME）。
- 完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. **可选：**根据IMSI、PDP Type配置Local APNNI。

   **ADD PDPAPN**

   **说明** 

   参数“SUBRANGE”（用户范围）根据实际情况选择“ALL\_USER（所有用户）”，“IMSI\_PREFIX（指定IMSI前缀）”或“IMSI\_RANGE（指定IMSI范围）”。此处以“IMSI\_PREFIX（指定IMSI前缀）”为例。
4. **可选：**配置公用APN。

   **ADD PUBLICAPNNI**
5. 根据不同场景选取不同的参数配置。
   1. **可选：**根据IMSI号段，直接纠正UE请求的APNNI为配置的APNNI取值。

      **ADD IMSIAPNCONVERT**

      **说明** 

      参数“SUBRANGE”（用户范围）根据实际情况选择“ALL\_USER（所有用户）”，“IMSI\_PREFIX（指定IMSI前缀）”或“IMSI\_RANGE（指定IMSI范围）”。此处以“IMSI\_PREFIX（指定IMSI前缀）”为例。
   2. **可选：**根据IMSI号段增加激活过程控制参数。

      **ADD SMACTCTRL**

      **说明** 

      - 上述配置的参数说明如下：
        - 参数“SUBRANGE”（用户范围）根据实际情况选择“ALL\_USER（所有用户）”、“SPECIAL\_USER（指定用户）”或“SPECIAL\_UETYPE(指定终端类型)”。此处以“SPECIAL\_USER（指定用户）”为例。
        - 参数“POLICY”（处理策略）根据实际情况选择“REJECT(直接拒绝)”、“MATCH\_FAIL\_NOTCORRECT(签约数据匹配失败后不进行纠正)”或“MATCH\_FAIL\_CORRECT(签约数据匹配失败后进行纠正)”。此处以“MATCH\_FAIL\_CORRECT(签约数据匹配失败后进行纠正)”为例。
        - 参数“SINGLESUB”（单组签约数据）根据现网情况选择“SELECT\_LOC\_APN\_ONLY（只选Local APNNI）”或“SELECT\_LOC\_APN\_FIRST（优选Local APNNI）”。
        - 参数“CORRMAPNSUB”（多组签约数据）根据现网情况选择“SELECT\_LOC\_APN\_ONLY（只选Local APNNI）”或“SELECT\_LOC\_APN\_FIRST（优选Local APNNI）”或SELECT\_DEF\_APN\_FIRST（优选Default APNNI）。
        - 参数“WILDCARDPLCY”（野卡签约数据策略）根据现网情况选择“STANDARD（标准）”，“CUSTOMIZATION（定制）或REJECT（拒绝）”。
      - 在配置特定终端类型的请求信息纠正相关策略时，需要提前通过命令**ADD SMACTIMEILIB**配置终端类型与IMEI TAC的映射关系、通过命令**MOD GBIMEICFG**/**MOD IUIMEICFG**/**MOD S1IMEICFG**设置IMEI获取策略为获取IMEI或获取IMEISV。
6. **可选：**配置定制APN纠正。

   - 开启定制APN纠正功能并配置APNNI组号。

     **ADD SMACTCTRL**中“是否启用定制APN纠正策略”为“YES(是)”，并配置“本地APNNI组号”。
   - 配置本地APNNI组信息，定制APN纠正功能会引用该配置参数“本地APNNI组号”。

     **ADD LOCALAPNNIGP**
7. 设置MME下发给UE的APN-NI来源。

   **SET SMFUNC**

   **说明** 

   - 本参数配置后是否生效还取决于软参“DWORD\_EX34 BIT1”的设置，当软参“DWORD\_EX34 BIT1”取值为“1”时，系统将以该软参功能为准。
   - 部分终端会因接收到的APN与请求的APN不一致而拒绝流程，导致业务失败，需要根据现网UE的实际情况进行参数配置。

## 任务示例

任务描述

配置LOCAL APNNI：增加一个用户范围为“所有用户”，PDP/PDN类型为“PT\_IPV4”，“APN NI”为“a”的记录。

配置PUBLICAPNNI：增加APNNI为“CNNET”的APN网络标识为公用APN。

此处以描述中的典型场景举例来说明请求信息纠正规则。

- 场景1：对所有单签约非野卡用户匹配失败后进行请求信息纠正。
- 场景2：对所有单签约野卡用户匹配失败后进行请求信息纠正，并对野卡签约数据采用如下纠正策略：优先使用请求的APN，没有请求的APN就使用Local APN。
- 场景3：对所有多签约不包含野卡用户匹配失败后进行请求信息纠正。
- 场景4：对所有多签约包含野卡用户匹配失败后进行请求信息纠正，并对野卡签约数据采用如下纠正策略：优先使用请求的APN，没有请求的APN就使用Local APN。
- 场景5：某终端类型可以在签约数据匹配失败或DNS解析失败后，再次请求接入时可以自动纠正并携带正确的APN。此时，配置针对该终端类型在签约数据匹配失败后或者DNS解析失败后不进行APN纠错纠正。

脚本

//设置请求信息纠正License开关为“ENABLE”。

```
SET LICENSESWITCH: LICITEM="LKV2RINCOR02", SWITCH=ENABLE;
```

//增加一个用户范围为“所有用户”，PDP/PDN类型为“PT\_IPV4”，“APN NI”为“a”的记录。

```
ADD PDPAPN: SUBRANGE=ALL_USER, PDPTYPE=PT_IPV4, APNNI="a";
```

//设置MME下发给UE的APN-NI来源。

```
SET SMFUNC: APNNISOURCE=APNNI_AFTER_SUBDATA_MATCH;
```

//配置一条记录，增加APNNI为“CNNET”的APN网络标识为公用APN。

```
ADD PUBLICAPNNI: APNNI="CNNET";
```

根据不同场景配置不同的请求信息纠正规则。

- 场景1脚本

  //对所有单签约非野卡用户匹配失败后进行请求信息纠正。

  ```
  ADD SMACTCTRL: SUBRANGE=ALL_USER, APNTYPE=ALL_APN, POLICY=MATCH_FAIL_CORRECT, CORRPDPTYPE=NO, CORRTIP=NO, SINGLESUB=SELECT_LOC_APN_FIRST;
  ```
- 场景2脚本

  //对所有单签约野卡用户匹配失败后进行请求信息纠正，野卡签约数据策略设置为标准（优先使用请求的APN，没有请求的APN就使用Local APN）。

  ```
  ADD SMACTCTRL: SUBRANGE=ALL_USER, APNTYPE=ALL_APN, POLICY=MATCH_FAIL_CORRECT, CORRPDPTYPE=NO, CORRTIP=NO, SINGLESUB=SELECT_LOC_APN_FIRST, CORRMAPNSUB=NO, WILDCARDPLCY=STANDARD;
  ```
- 场景3脚本

  //对所有多签约不包含野卡用户匹配失败后进行请求信息纠正。

  ```
  ADD SMACTCTRL: SUBRANGE=ALL_USER, APNTYPE=ALL_APN, POLICY=MATCH_FAIL_CORRECT, CORRPDPTYPE=NO, CORRTIP=NO, SINGLESUB=NO, CORRMAPNSUB=SELECT_LOC_APN_FIRST;
  ```
- 场景4脚本

  //对所有多签约包含野卡用户匹配失败后进行请求信息纠正，野卡签约数据策略设置为标准（优先使用请求的APN，没有请求的APN就使用Local APN）。

  ```
  ADD SMACTCTRL: SUBRANGE=ALL_USER, APNTYPE=ALL_APN, POLICY=MATCH_FAIL_CORRECT, CORRPDPTYPE=NO, CORRTIP=NO, SINGLESUB=NO, CORRMAPNSUB=SELECT_LOC_APN_FIRST, WILDCARDPLCY=STANDARD;
  ```
- 场景5脚本

  ```
  //配置IMEI TAC与终端类型的映射关系。
  ```

  ```
  ADD SMACTIMEILIB: IMEITAC="12345678", UETYPE=BLACKBERRY;
  ADD SMACTIMEILIB: IMEITAC="22345678", UETYPE=BLACKBERRY;
  ```

  //配置IMEI获取策略。

  ```
  MOD GBIMEICFG: SUBRANGE=ALL_USER, GETIMEIPLC=IMEI;
  MOD IUIMEICFG: SUBRANGE=ALL_USER, GETIMEIPLC=IMEI;
  MOD S1IMEICFG: SUBRANGE=ALL_USER, GETIMEIPLC=IMEI;
  ```

  //配置针对BLACKBERRY终端类型，如果请求消息未携带APN，不进行请求信息纠正。且在用户签约野卡的情况下不进行纠错，拒绝该用户的激活请求。

  ```
  ADD SMACTCTRL: SUBRANGE=SPECIAL_UETYPE, UETYPE=BLACKBERRY, APNTYPE=NULL_APN, POLICY=MATCH_FAIL_NOTCORRECT, WILDCARDPLCY=REJECT;
  ```

  //配置针对BLACKBERRY终端类型，如果请求消息携带APN，不进行请求信息纠正。且在用户签约野卡的情况下，如果DNS解析失败不进行纠错，拒绝该用户的激活请求。

  ```
  ADD SMACTCTRL: SUBRANGE=SPECIAL_UETYPE, UETYPE=BLACKBERRY, APNTYPE=NOT_NULL_APN, POLICY=MATCH_FAIL_NOTCORRECT, WILDCARDPLCY=STANDARD;
  ```