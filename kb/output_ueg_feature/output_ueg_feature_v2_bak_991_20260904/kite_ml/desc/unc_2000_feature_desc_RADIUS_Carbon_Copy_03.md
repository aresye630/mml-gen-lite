# 激活支持RADIUS抄送功能

- 操作场景
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

当运营商部署分组交换网，在将RADIUS消息发往计费AAA Server时，需要将用户信息同时发给多个AAA抄送服务器，需要激活支持RADIUS抄送功能。

**说明** 

适用于PGW-C、SMF

## 必备事项

前提条件

- 当UEG的产品形态为风筝L时，请仔细阅读GWFD-024304 支持Radius抄送功能特性概述。
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- 当UEG的产品形态为风筝L时，完成**ADD CPAPN**。
- 完成激活RADIUS功能。

数据

| 类别                           | 参数名称                                 | 取值样例     | 获取方法     | 说明                                                       |
|:-----------------------------|:-------------------------------------|:---------|:---------|:---------------------------------------------------------|
| ADD RDSSVRGRP                | Radius Server Group名称（RDSSVRGRPNAME） | isprg    | 本端规划     | 使用的RADIUS组，已通过命令ADD RDSSVRGRP配置，可以使用命令LST RDSSVRGRP进行查询。 |
| 当UEG的产品形态为风筝L时，ADD CPVPNINST | VPN实例名（VPNINSTANCE）                  | vpntest  | 本端规划     | -                                                        |
| 当UEG的产品形态为风筝L时， ADD CPAPN    | APN名称（APN）                           | apn-test | 本端规划     | -                                                        |
| ADD APNRDSSVRGRP             | APN名称（APN）                           | apn-test | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。       |
| ADD APNRDSSVRGRP             | Radius Server Group名称（RDSSVRGRPNAME） | isprg    | 已配置数据中获取 | 已通过命令ADD RDSSVRGRP配置，可以使用LST RDSSVRGRP命令进行查询。            |

| 类别         | 参数名称                                 | 取值样例                                      | 获取方法     | 说明                                                                                                                      |
|:-----------|:-------------------------------------|:------------------------------------------|:---------|:------------------------------------------------------------------------------------------------------------------------|
| ADD RDSSVR | Radius Server Group名称（RDSSVRGRPNAME） | isprg                                     | 本端规划     | 与AAA计费服务器的IP地址保持一致。                                                                                                     |
| ADD RDSSVR | 服务器类型（SERVERTYPE）                    | ACCOUNTING                                | 本端规划     | 与AAA计费服务器的IP地址保持一致。                                                                                                     |
| ADD RDSSVR | 服务器IP版本（IPVERSION）                   | IPV4                                      | 本端规划     | 与AAA计费服务器的IP地址保持一致。                                                                                                     |
| ADD RDSSVR | 主备用类型（PRIFLAG）                       | PRIMARY SECONDARY CARBON_COPY             | 本端规划     | 与AAA计费服务器的IP地址保持一致。                                                                                                     |
| ADD RDSSVR | IPv4地址（SERVERIPV4）                   | 192.168.8.181 192.168.8.182 192.168.8.183 | 全网规划     | 与AAA计费服务器的IP地址保持一致。                                                                                                     |
| ADD RDSSVR | 端口（PORT）                             | 1819                                      | 与对端协商    | -                                                                                                                       |
| ADD RDSSVR | VPN实例（VPNINSTANCE）                   | vpntest                                   | 已配置数据中获取 | 当UEG的产品形态为风筝S时，已通过配置，当UEG的产品形态为风筝L时，已通过ADD CPVPNINS配置，当UEG的产品形态为风筝S时，可以使用命令进行查询。当UEG的产品形态为风筝L时，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR | 服务器密钥（加密的）（CIPHERKEY）                | ispchina                                  | 与对端协商    | -                                                                                                                       |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置AAA服务器组。

   **ADD RDSSVRGRP**
3. 创建VPN实例。

   当UEG的产品形态为风筝L时，**ADD CPVPNINST**
4. **可选：**配置UP列表。

   **ADD UPLIST4RDS**
5. 配置AAA计费服务器。

   **ADD RDSSVR**

   **说明** 

   如需配置多个服务器，则需要执行该命令多次。
6. 配置APN下绑定AAA服务器组。

   当UEG的产品形态为风筝L时，**ADD CPAPN**

   **ADD APNRDSSVRGRP**

## 验证方法

具体步骤请参见调测支持RADIUS抄送功能。

## 任务示例

任务描述

配置抄送鉴权消息和计费消息任务。

脚本

//配置AAA服务器组、使用的APN

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=MASTER_SLAVE, SIGOPTACCTMSG=DISABLE;
```

当UEG的产品形态为风筝L时，

```
ADD CPVPNINST: VPNINSTANCE="vpntest";
```

//配置AAA计费服务器。

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="192.168.8.181", PORT=1819, VPNINSTANCE="vpntest", CIPHERKEY="*****", PRIFLAG=PRIMARY;
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="192.168.8.182", PORT=1819, VPNINSTANCE="vpntest", CIPHERKEY="*****", PRIFLAG=SECONDARY;
```

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="192.168.8.183", PORT=1819, VPNINSTANCE="vpntest", CIPHERKEY="*****", PRIFLAG=CARBON_COPY;
```

//配置APN下绑定AAA服务器组。

当UEG的产品形态为风筝L时，

```
ADD CPAPN: APN="apn-test";
ADD APNRDSSVRGRP: APN="apn-test",RDSSVRGRPNAME="isprg";
```