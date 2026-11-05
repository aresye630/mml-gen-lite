# 激活IPv4v6双栈接入特性（适用于SGSN/MME）

- 操作场景
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。

UEG支持创建IPv4v6双栈，通过IPv4v6地址为UE提供业务，使UE可以用IPv4v6地址进行数据传输。

**说明** 

适用于SGSN/MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-022903 IPv4v6双栈接入特性概述（适用于2G/3G/4G）。
- 完成加载License。
- 支持IPv4v6的用户已经接入到网络。

数据

| 类别            | 参数名称                                        | 取值样例                       | 获取方法   | 说明       |
|:--------------|:--------------------------------------------|:---------------------------|:-------|:---------|
| SET SMFUNC    | IPv4v6双栈（DUALFLAG）                          | YES                        | 全网规划   | 会话管理扩展功能 |
| ADD SMSUBDATA | 用户范围（SUBRANGE）                              | ALL_USER                   | 全网规划   | 签约数据纠正参数 |
| ADD SMSUBDATA | 签约PDP/PDN类型（PDPTYPE）                        | IPV4                       | 全网规划   | 签约数据纠正参数 |
| ADD SMSUBDATA | 签约IPv4 PDP/PDN地址分配类型（IPV4PDPADDRTYPE）       | ALLOCATION_IPV4PDP_DYNAMIC | 全网规划   | 签约数据纠正参数 |
| ADD SMSUBDATA | 新的签约PDP类型（NEWPDPTYPE）                       | IPV4V6                     | 全网规划   | 签约数据纠正参数 |
| ADD SMSUBDATA | 新的签约IPv4 PDP/PDN地址分配类型（NEWIPV4PDPADDRTYPE）  | ALLOCATION_IPV4PDP_DYNAMIC | 全网规划   | 签约数据纠正参数 |
| ADD SMSUBDATA | 新的签约IPv6 PDP/PDN地址分配类型（NEWIPV6PDPADDRTYPE ） | DYNAMIC                    | 全网规划   | 签约数据纠正参数 |

## 操作流程

激活IPv4v6双栈接入操作流程如图1所示。

**图1** 激活IPv4v6双栈接入操作流程

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开IPv4v6双栈接入特性的License配置开关。

   **SET LICENSESWITCH**
3. 开启IPv4v6双栈接入功能。

   **SET SMFUNC**
4. **可选：**增加签约数据纠正参数。如果S6a口连接的HSS支持IPv4v6双栈，则不需要执行此步骤；若不支持IPv4v6双栈，需要执行此步骤。

   **ADD SMSUBDATA**
5. **可选：**增加GTP-C V0/V1协议兼容性配置。

   **说明** 

   - “TMMSGTYPE”设置为“CREATE\_PDP\_CONTEXT\_REQUEST”或者“UPDATE\_PDP\_CONTEXT\_REQUEST”。
   - 可通过**LST GTPCCMPT**命令查看当前配置，如果携带方式被设置为不携带Common Flags信元时则需要重新配置。

   在“MML命令行-UEG”窗口上执行命令

   **MOD GTPCCMPT**:MSGCLS=TM，TMMSGTYPE=CREATE\_PDP\_CONTEXT\_REQUEST, CRTPDPREQ=COMMON\_FLAGS, UPDPDPREQ=COMMON\_FLAGS, CMFLG=YES;

## 任务示例

任务描述

开启IPv4v6双栈功能S6a口，所以需要增加一条签约数据纠正参数信息，其用户范围为所有用户，匹配条件为签约数据，签约APNNI范围为所有签约APNNI，签约PDP/PDN类型为IPv4，签约IPv4 PDP/PDN地址分配类型为动态分配，不修改签约APNNI，修改新的PDP类型为IPv4v6，新的IPv4地址为动态分配，新的IPv6地址为动态分配。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2DUSA02", SWITCH=ENABLE;
```

//开启IPv4v6双栈。

```
SET SMFUNC: DUALFLAG=YES;
```

//可选：增加签约数据纠正参数。

```
ADD SMSUBDATA: SUBRANGE=ALL_USER, TYPE=SUBSCRIBED_PARAMETER, APNNIRANGE=APNNI_ALL, PDPTYPE=IPV4, IPV4PDPADDRTYPE=ALLOCATION_IPV4PDP_DYNAMIC, CORRECTAPNNI=NO, NEWPDPTYPE=IPV4V6, NEWIPV4PDPADDRTYPE=DYNAMIC, NEWIPV6PDPADDRTYPE=DYNAMIC;
```