# 增加UNC接口名称（ADD UNCINTF）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGSN、MME、SGW-C、AMF、PGW-C、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于增加需要上报至网管北向的UNC网元所有业务或者管理接口的名称。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1000条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NRMVNFTYPE   | INTFTYPE   |
|:-------------|:-----------|
| SMF          | Mgt        |
| SMF          | N4         |
| SMF          | Nnrf       |
| SMF          | N10        |
| SMF          | N7         |
| SMF          | N16a       |
| SMF          | N11        |
| SMF          | Nbsf       |
| SMF          | N40        |
| SMF          | Radius     |
| SGWC         | Mgt        |
| SGWC         | Sx         |
| SGWC         | Ga         |
| SGWC         | S5_S       |
| SGWC         | S8_S       |
| SGWC         | S11        |
| PGWC         | Mgt        |
| PGWC         | Sx         |
| PGWC         | Ga         |
| PGWC         | Radius     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                |
|:-----------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRMVNFTYPE | 北向网元类型 | 可选必选说明：必选参数  参数含义：该参数用于指定UNC网元的北向网元类型。  数据来源：本端规划 取值范围： AMF（AMF）MME（MME）SGSN（SGSN）SMF（SMF）PGWC（PGWC）SGWC（SGWC）GGSNC（GGSNC）ProxySGWC（ProxySGWC）NRF（NRF）NSSF（NSSF）SMSF（SMSF）CHF（CHF）ProxySMF（ProxySMF）  默认值：无  配置原则：无 |
| INTFTYPE   | 接口类型   | 可选必选说明：必选参数  参数含义：该参数用于指定UNC网元的接口名称。其中，Mgt为网元和网管的对接接口；DnsQry为SGSN、MME、AMF网元的DNS本端实体与DNS服务器进行通信的接口；Bx为NCG网元与计费账务域交互的文件接口；其他为协议定义的接口。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~32。  默认值：无  配置原则：无                              |

## 使用实例

增加需要上报至网管北向UNC网元的所有业务或者管理接口的名称，执行以下命令：

```
ADD UNCINTF:NRMVNFTYPE=ProxySMF,INTFTYPE="Mgt";
```