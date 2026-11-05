# 配置与P-CSCF的对接数据（适用于SGW-C/PGW-C）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍了SGW-C/PGW-C与P-CSCF的对接配置，用于部署LTE语音业务。

## 必备事项

前提条件

已完成基础网路部署，如Sv接口，SGs接口对接。

数据

| 命令 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD PCSCFGROUP** | P-CSCF组名（GROUPNAME） | pcg\_test1  pcg\_test2 | 本端规划 | 配置P-CSCF分组信息。 |
|  | IP地址版本（IPVERSION） | IPV4 | 本端规划 |  |
| **ADD PCSCFIP** | P-CSCF组名（GROUPNAME） | pcg\_test1  pcg\_test2 | 已配置数据中获取 | 配置P-CSCF服务器。  “P-CSCF组名”从**ADD PCSCFGROUP**中已配置的数据获取，可通过**LST PCSCFGROUP**查询。 |
|  | IP地址版本（IPVERSION） | IPV4 | 本端规划 |  |
|  | IPv4地址（PCSCFIPV4） | 192.168.254.251  192.168.254.252  192.168.254.253  192.168.254.254 | 全网规划 |  |
|  | WEIGHT（权重） | 1  2  3  4 | 本端规划 |  |
| **ADD CPAPN** | APN名称（APN） | ims | 全网规划 | 配置APN实例。 |
| **ADD PCSCFGRPBNDAPN** | APN名称（APN） | ims | 已配置数据中获取 | 将指定的主备P-CSCF分组绑定到APN下。   * “APN名称”从**ADD CPAPN**中已配置的数据获取，可通过**LST CPAPN**查询。 * “主IPv4P-CSCF组”和“备IPv4P-CSCF组”从**ADD PCSCFGROUP**中已配置的数据获取，可通过**LST PCSCFGROUP**查询。 |
|  | 缺省标记（DEFAULTFLAG） | DEFAULT | 全网规划 |  |
|  | 主IPv4P-CSCF组（MPCSCFGRPIPV4） | pcg\_test1 | 已配置数据中获取 |  |
|  | 备IPv4P-CSCF组（SPCSCFGRPIPV4） | pcg\_test2 | 已配置数据中获取 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置P-CSCF分组。

   **ADD PCSCFGROUP**
3. 配置P-CSCF服务器。

   **ADD PCSCFIP**

   在配置P-CSCF服务器时，为了更好的实现负荷分担功能，请按照如下原则配置：

   * 所有服务器都需要配置到主备Group中。
   * 主备Group的配置顺序不能一致。

   比如说有A、B、C、D四台服务器，主备Group都需要配置四台服务器，主Group的顺序为A、B、C、D，备Group的顺序为B、A、D、C。
4. 指定APN实例。

   **ADD CPAPN**
5. 将指定的主备P-CSCF分组绑定到APN下。

   **ADD PCSCFGRPBNDAPN**

## 任务示例

任务描述

配置SGW-C/PGW-C与多个P-CSCF建立IP连接。

脚本

进入“MML命令行-UEG”窗口。

//配置P-CSCF组名。

```
ADD PCSCFGROUP: GROUPNAME="pcg_test1", IPVERSION=IPV4;
```

```
ADD PCSCFGROUP: GROUPNAME="pcg_test2", IPVERSION=IPV4;
```

//配置P-CSCF分组。

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.251", WEIGHT=1;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.252", WEIGHT=2;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.253", WEIGHT=3;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test1", IPVERSION=IPV4, PCSCFIPV4="192.168.254.254", WEIGHT=4;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.252", WEIGHT=2;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.251", WEIGHT=1;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.254", WEIGHT=4;
```

```
ADD PCSCFIP: GROUPNAME="pcg_test2", IPVERSION=IPV4, PCSCFIPV4="192.168.254.253", WEIGHT=3;
```

//指定APN实例。

```
ADD CPAPN: APN="ims";
```

//将指定的主备P-CSCF分组绑定到APN下。

```
ADD PCSCFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="pcg_test1", SPCSCFGRPIPV4="pcg_test2";
```

版权所有 © 华为技术有限公司
