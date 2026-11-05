# 激活支持GRE

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

本操作指导介绍在运行网络中创建GRE隧道的操作过程。

通用路由封装GRE（Generic Routing Encapsulation）是对某些网络层协议的报文进行封装，使这些被封装的报文能够在另一网络层协议（如IP）中传输。GRE可以作为VPN的第三层隧道协议，为VPN数据提供透明传输通道。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

- 隧道源端口和目的端口已路由可达。
- 待创建的GRE隧道不存在。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。

数据

| 类别           | 参数                    | 取值样例            | 获取方法   | 相关命令              |
|:-------------|:----------------------|:----------------|:-------|:------------------|
| LoopBack接口   | 接口名(IFNAME)           | LoopBack1       | 本端规划   | ADD INTERFACE     |
| LoopBack接口地址 | 接口名(IFNAME)           | LoopBack1       | 本端规划   | ADD IFIPV4ADDRESS |
| LoopBack接口地址 | IPv4地址(IFIPADDR)      | 10.3.3.11       | 全网规划   | ADD IFIPV4ADDRESS |
| LoopBack接口地址 | IPv4地址掩码(SUBNETMASK)  | 255.255.255.255 | 全网规划   | ADD IFIPV4ADDRESS |
| LoopBack接口地址 | IPv4地址类型(ADDRTYPE)    | main            | 本端规划   | ADD IFIPV4ADDRESS |
| Tunnel接口     | 隧道名称(TNLNAME)         | Tunnel1         | 本端规划   | ADD GRETUNNEL     |
| 隧道接口的封装模式    | 隧道类型(TNLTYPE)         | gre             | 本端规划   | ADD GRETUNNEL     |
| 源端IP地址       | IPv4源类型(SRCTYPE)      | if_name         | 本端规划   | ADD GRETUNNEL     |
| 源端IP地址       | IPv6源类型(SRCTYPE6)     | no_type         | 本端规划   | ADD GRETUNNEL     |
| 源端IP地址       | 源接口名称(SRCIFNAME)      | LoopBack1       | 本端规划   | ADD GRETUNNEL     |
| 目的端IP地址      | 目的IPv4地址(DSTIPADDR)   | 10.4.4.11       | 对端规划   | ADD GRETUNNEL     |
| 目的端IP地址      | 目的IPv6地址(DSTIPV6ADDR) | 2001:db8::100   | 对端规划   | ADD GRETUNNEL     |

## 操作步骤

1. 配置LoopBack接口。

   在“MML命令行-UNC”窗口上执行：

   **ADD INTERFACE**:IFNAME="接口名";

   **ADD IFIPV4ADDRESS**: IFNAME="接口名", IFIPADDR="接口IPv4地址", SUBNETMASK="接口IPv4地址掩码", ADDRTYPE=接口IPv4地址类型;
2. 配置Tunnel接口。

   在“MML命令行-UNC”窗口上执行：

   **ADD GRETUNNEL**:TNLNAME="隧道名称", TNLTYPE=隧道类型, SRCTYPE=IPv4源类型, SRCIPADDR=源IPv4地址, DSTIPADDR="目的IPv4地址";

   **ADD IFIPV4ADDRESS**:IFNAME="接口名", IFIPADDR="接口IPv4地址", SUBNETMASK="接口IPv4地址掩码", ADDRTYPE=接口IPv4地址类型;

   **说明** 

   为了不影响GRE隧道收发报文性能，建议使用**MOD INTERFACE**命令配置GRE Tunnel的MTU值，该MTU值小于等于（出接口的MTU值-GRE头的长度），GRE头封装格式为：GRE header + 外层IP header。
3. 配置隧道间静态路由

   在“MML命令行-UNC”窗口上执行：

   ****ADD SRROUTE****: AFTYPE=地址族, PREFIX="路由前缀", MASKLENGTH=路由掩码长度, IFNAME="路由接口名字";
4. 当配置GRE隧道时，需要使能隧道端到端校验功能：

   在“MML命令行-UNC”窗口上执行：

   **ADD GRETUNNEL**:TNLNAME="隧道名称", TNLTYPE=隧道类型, CHECKSUMEN=使能端到端校验功能;
5. 当配置GRE隧道时，需要使能隧道识别关键字验证功能：

   在“MML命令行-UNC”窗口上执行：

   **ADD GRETUNNEL**:TNLNAME="隧道名称", TNLTYPE=隧道类型, GREKEYEN=使能识别关键字功能, GREKEY="识别关键字";

   **说明** 

   如果在隧道两端设置识别关键字，则必须指定相同的识别关键字；或隧道两端都不设置识别关键字。
6. 当配置GRE隧道时，需要使能隧道Keepalive功能：

   在“MML命令行-UNC”窗口上执行：

   **ADD GRETUNNEL**:TNLNAME="隧道名称", TNLTYPE=隧道类型, KEEPALVEN=使能Keepalive功能, KEEPALVPERIOD=Keepalive报文发送周期, KEEPALVRETRYCNT=不可达计数器参数;

   **说明** 

   - 若不填写参数KEEPALVPERIOD，则Keepalive报文发送周期默认为5秒。
   - 若不填写参数KEEPALVRETRYCNT，则不可达计数器参数默认为3次。

## 验证方法

查询指定Tunnel接口的信息是否与数据规划表中一致。

在“MML命令行-UNC”窗口上执行：

**LST GRETUNNEL**:TNLNAME="隧道名称", TNLTYPE=隧道类型;

**预期结果：**查询结果与规划值一致。

```
RETCODE = 0  操作成功

结果如下
-------------------------
             隧道名称  =  Tunnel1
             隧道类型  =  GRE隧道
           IPv4源类型  =  IP地址
           IPv6源类型  =  无类型 
           源IPv4地址  =  10.3.3.11
         目的IPv4地址  =  10.4.4.11
           源IPv6地址  =  ::
         目的IPv6地址  =  ::
    使能Keepalive功能  =  TRUE
Keepalive报文发送周期  =  5
     不可达计数器参数  =  3
           源接口名称  =  NULL
          目的VPN名称  =  _public_
   使能识别关键字功能  =  去使能
           识别关键字  =  *****
   使能端到端校验功能  =  FALSE
     使能报文统计功能  =  FALSE
     使能备份隧道功能  =  FALSE
(结果个数 = 1)
---    END
```

## 任务示例

任务描述

**本端GRE隧道配置：**

创建LoopBack1接口，配置接口源IP地址为10.3.3.11/32，目的IP地址为10.4.4.11。

创建Tunnel1接口，Tunnel接口为“GRE”隧道模式。配置接口源IP地址为10.10.1.201/24，目的地址为10.10.1.202。

**对端GRE隧道配置：**

创建LoopBack1接口，配置接口源IP地址为10.4.4.11/32，目的IP地址为10.3.3.11。

创建Tunnel1接口，Tunnel接口为“GRE”隧道模式。配置接口源IP地址为10.10.1.202/24，目的地址为10.10.1.201。

**说明** 

隧道的源接口IP地址和目的IP地址分别对应GRE报文头中的源IP地址和目的IP地址。

**图1** 激活GRE特性组网

脚本

**本端GRE隧道配置脚本：**

//创建LoopBack接口，并配置IP地址10.3.3.11/32。

```
ADD INTERFACE:IFNAME="LoopBack1";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;
```

//创建Tunnel接口，并配置IP地址10.10.1.201/24。

```
ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11";
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.201", SUBNETMASK="255.255.255.0", ADDRTYPE=main;
```

//增加隧道间静态路由

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=24,IFNAME="Tunnel1";
```

//使能隧道端到端校验功能。

```
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;
```

//使能隧道识别关键字功能。

```
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="123";
```

//使能隧道Keepalive功能。

```
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;
```

**对端GRE隧道配置脚本：**

//创建LoopBack接口，并配置IP地址10.4.4.11/32。

```
ADD INTERFACE:IFNAME="LoopBack1";
```

```
ADD IFIPV4ADDRESS:IFNAME="LoopBack1", IFIPADDR="10.4.4.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;
```

//创建Tunnel接口，并配置IP地址10.10.1.202/24。

```
ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.3.3.11";
```

```
ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.202", SUBNETMASK="255.255.255.0", ADDRTYPE=main;
```

//增加隧道间静态路由

```
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.201",MASKLENGTH=24,IFNAME="Tunnel1";
```

//使能隧道端到端校验功能。

```
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;
```

//使能隧道识别关键字功能。

```
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="123";
```

//使能隧道Keepalive功能。

```
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;
```