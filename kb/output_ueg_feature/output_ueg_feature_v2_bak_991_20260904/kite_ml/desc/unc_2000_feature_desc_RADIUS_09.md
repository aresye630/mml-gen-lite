# 配置RADIUS功能

- 操作场景
- 必备事项
- 操作步骤
- 验证方法
- 任务示例

## 操作场景

提供如下基于RADIUS的丰富功能：

- 提供RADIUS鉴权功能。
- 提供RADIUS计费功能。
- 提供3GPP扩展信元的定制功能。

  **说明** 

  适用于PGW-C、SMF

## 必备事项

前提条件

- 当UEG的产品形态为风筝L时，请仔细阅读GWFD-024303 Radius功能特性概述
- 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
- 当UEG的产品形态为风筝L时，完成**ADD CPAPN**。

数据

| 类别                 | 参数名称                                              | 取值样例                      | 获取方法     | 说明                                                           |
|:-------------------|:--------------------------------------------------|:--------------------------|:---------|:-------------------------------------------------------------|
| ADD RDSSVRGRP      | Radius Server Group名称（RDSSVRGRPNAME）              | isprg                     | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius Accounting Request超时时间(秒)（ACCTTIMEOUT）     | 10                        | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius Accounting Request重发次数（ACCTRETRANSMIT）     | 5                         | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius Authentication Request超时时间(秒)（AUTHTIMEOUT） | 10                        | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius Authentication Request重发次数（AUTHRETRANSMIT） | 5                         | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius Accounting超时时长(秒)（ACCTSVRTOUT）             | 12                        | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius计费服务器Down状态保持时长(秒)（ACCTSVRDTIME）            | 180                       | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius鉴权服务器超时时长(秒)（AUTHSVRTOUT）                   | 12                        | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| ADD RDSSVRGRP      | Radius鉴权服务器Down状态保持时长(秒)（AUTHSVRDTIME）            | 180                       | 本端规划     | 配置AAA服务器组、RADIUS消息超时的时间和重发次数。                                |
| SET RDSACCTREQVSA  | Radius Server Group名称（RDSSVRGRPNAME）              | isprg                     | 已配置数据中获取 | 计费/鉴权AAA服务器所在的AAA服务器组，已通过ADD RDSSVRGRP进行配置。                  |
| SET RDSACCTREQVSA  | 支持3gpp私有扩展属性（THREEGPP）                            | ENABLE                    | 与对端协商    | 配置是否支持3GPP计费扩展属性。                                            |
| ADD APNRDSCLIENTIP | APN名称（APN）                                        | apn-test                  | 已配置数据中获取 | 鉴权或计费请求消息的radius client ip。                                  |
| ADD APNRDSCLIENTIP | 鉴权或计费（AUTHORACCT）                                 | AUTHENTICATION ACCOUNTING | 本端规划     | 鉴权或计费请求消息的radius client ip。                                  |
| ADD APNRDSCLIENTIP | 接口名称（INTFNAME）                                    | giif1/0/1                 | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPLOGICINF配置，可以使用LST CPLOGICINF命令进行查询。 |
| ADD APNRDSSVRGRP   | APN名称（APN）                                        | apn-test                  | 已配置数据中获取 | APN下绑定AAA服务器组。                                               |
| ADD APNRDSSVRGRP   | Radius Server Group名称（RDSSVRGRPNAME）              | isprg                     | 已配置数据中获取 | APN下绑定AAA服务器组。                                               |
| SET APNRDSACCTCTRL | APN名称（APN）                                        | apn-test                  | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。           |
| SET APNRDSACCTCTRL | 时间阈值（分）（TIMETHRESHOLD）                            | 30                        | 本端规划     | AAA的计费阈值                                                     |
| SET APNRDSACCTCTRL | 流量阈值（千字节）（VOLUMETHRESHOLD）                        | 20                        | 本端规划     | AAA的计费阈值                                                     |
| SET APNRDSACCTCTRL | 等待计费开始响应消息后才回应激活成功应答消息（SUPPORTACCTRSP）            | ENABLE                    | 本端规划     | 配置是否等待计费响应消息后激活用户。                                           |
| SET APNRDSACCTCTRL | MME或SGSN/SGW发起PDP上下文更新时是否支持发送计费更新（SUPPORTACCTUPD） | ENABLE                    | 本端规划     | -                                                            |
| SET APNRDSACCTCTRL | RAT变化触发计费更新消息（RATTRIGGER）                         | ENABLE                    | 本端规划     | -                                                            |
| SET APNRDSACCTCTRL | 业务报文（通过3/4层规则配置）时触发计费请求消息 （SRVTRIGGER）            | ENABLE                    | 本端规划     | 配置业务触发RADIUS消息发送时的业务报文延时时间                                   |
| SET APNRDSACCTCTRL | 业务报文延时时间（秒）（BUFFERTIMEVALUE）                      | 2                         | 本端规划     | 配置业务触发RADIUS消息发送时的业务报文延时时间                                   |
| SET APNRADIUSATTR  | APN名称（APN）                                        | apn-test                  | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。           |
| SET APNRADIUSATTR  | 增加或剥离域名（DOMAINNAMEACT）                            | ADD_ENABLE_STRIP_DISABLE  | 全网规划     | 配置是否支持域名增加或剥离                                                |
| SET APNRADIUSATTR  | 域名位置（DOMAINNAMEPOS）                               | SUFFIX                    | 全网规划     | 配置是否支持域名增加或剥离                                                |
| SET APNAUTHATTR    | APN名称（APN）                                        | apn-test                  | 已配置数据中获取 | 当UEG的产品形态为风筝L时，已通过ADD CPAPN配置，可以使用LST CPAPN命令进行查询。           |
| SET APNAUTHATTR    | DM开关（DISCONNECT）                                  | ENABLE                    | 与对端协商    | 配置是否支持RADIUS PoD功能                                           |

| 类别         | 参数名称                                 | 取值样例           | 获取方法     | 说明                                                                             |
|:-----------|:-------------------------------------|:---------------|:---------|:-------------------------------------------------------------------------------|
| ADD RDSSVR | Radius Server Group名称（RDSSVRGRPNAME） | isprg          | 本端规划     | 与AAA鉴权服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | 服务器类型（SERVERTYPE）                    | AUTHENTICATION | 全网规划     | 与AAA鉴权服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | 服务器IP版本（IPVERSION）                   | IPV4           | 全网规划     | 与AAA鉴权服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | IPv4地址（SERVERIPV4）                   | 10.168.10.1    | 全网规划     | 与AAA鉴权服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | VPN实例（VPNINSTANCE）                   | vpn1           | 已配置数据中获取 | 在“配置到AAA Server的数据”中当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR | 端口（PORT）                             | 1812           | 与对端协商    | -                                                                              |
| ADD RDSSVR | 服务器密钥（加密的）（CIPHERKEY）                | ispchina       | 与对端协商    | 鉴权和计费AAA服务器的密钥可以不同同一个IP+VPN的Server在不同组里的密钥也不需要进行限制                             |
| ADD RDSSVR | 主备用类型（PRIFLAG）                       | PRIMARY        | 本端规划     | -                                                                              |
| ADD RDSSVR | 服务器优先级（PRIORITY）                     | 1              | 本端规划     | -                                                                              |
| ADD RDSSVR | 确认服务器密钥（加密的）（CIPHERKEYCNFM）          | ispchina       | 与对端协商    | -                                                                              |

| 类别         | 参数名称                                 | 取值样例        | 获取方法     | 说明                                                                             |
|:-----------|:-------------------------------------|:------------|:---------|:-------------------------------------------------------------------------------|
| ADD RDSSVR | Radius Server Group名称（RDSSVRGRPNAME） | isprg       | 本端规划     | 与计费AAA服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | 服务器类型（SERVERTYPE）                    | ACCOUNTING  | 本端规划     | 与计费AAA服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | 服务器IP版本（IPVERSION）                   | IPV4        | 全网规划     | 与计费AAA服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | IPv4地址（SERVERIPV4）                   | 10.168.10.1 | 全网规划     | 与计费AAA服务器的IP地址保持一致。                                                            |
| ADD RDSSVR | VPN实例（VPNINSTANCE）                   | vpn1        | 已配置数据中获取 | 在“配置到AAA Server的数据”中当UEG的产品形态为风筝L时，已通过ADD CPVPNINST配置，可以使用LST CPVPNINST命令进行查询。 |
| ADD RDSSVR | 端口（PORT）                             | 1813        | 与对端协商    | -                                                                              |
| ADD RDSSVR | 服务器密钥（加密的）（CIPHERKEY）                | ispchina    | 与对端协商    | 鉴权和计费AAA服务器的密钥可以不同同一个IP+VPN的Server在不同组里的密钥也不需要进行限制                             |
| ADD RDSSVR | 主备用类型（PRIFLAG）                       | PRIMARY     | 本端规划     | -                                                                              |
| ADD RDSSVR | 服务器优先级（PRIORITY）                     | 1           | 本端规划     | -                                                                              |
| ADD RDSSVR | 确认服务器密钥（加密的）（CIPHERKEYCNFM）          | ispchina    | 与对端协商    | -                                                                              |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置AAA服务器组以及RADIUS消息的重发次数和超时的时间。

   **ADD RDSSVRGRP**
3. 配置鉴权AAA服务器。

   **说明** 

   根据鉴权AAA服务器的接收能力，执行如下命令，通过设置**WALVALUE**参数以限制向鉴权AAA服务器发送的消息数，具体请参见激活系统过载控制功能（适用于SPGW-C）。

   **ADD RDSSVR**
4. **可选：**配置UP列表。

   **ADD UPLIST4RDS**
5. **可选：**配置AAA计费服务器。

   **说明** 

   根据AAA计费服务器的接收能力，执行如下命令，通过设置**WALVALUE**参数以限制向计费AAA服务器发送的消息数，具体请参见激活系统过载控制功能（适用于SPGW-C）。

   **ADD RDSSVR**
6. 配置RADIUS参数。
   1. 配置计费AAA服务器组的私有扩展属性。

      **SET RDSACCTREQVSA**
   2. **可选：**配置计费AAA服务器的可选消息属性。

      **SET RDSACCTREQATTR**
   3. **可选：**配置鉴权请求携带的私有扩展属性

      **SET RDSAUTHREQVSA**
   4. **可选：**配置RADIUS Server Group的可选计费消息属性。

      **MOD RDSSVRGRP**
   5. 配置APN下绑定Client IP。

      **ADD APNRDSCLIENTIP**

      **说明** 

      如果没有配置Client IP，则该APN用户激活失败。
   6. 配置APN下绑定AAA服务器组。

      **ADD APNRDSSVRGRP**
   7. **可选：**配置指定APN实例的RADIUS计费AAA服务器的流量阈值、时间阈值以及其他AAA客户端的计费信令控制属性。

      **SET APNRDSACCTCTRL**
   8. **可选：**开启RADIUS PoD功能。

      **SET APNAUTHATTR**
   9. **可选：**配置APN是否支持增加域名功能（即当用户去鉴权AAA服务器鉴权时，是否携带域名），以及是否支持剥离域名功能。如果需要同时开启这两个功能，则执行该命令两次。

      **SET APNRADIUSATTR**

      **说明** 

      域名做为用户名的一部分，通过前缀或者后缀的形式与用户名连接。

      - 域名做为前缀时，域名+前缀分隔符+用户名（当UEG的产品形态为风筝S时，前缀分隔符由命令配置当UEG的产品形态为风筝L时，前缀分隔符由****SET CPDOMAINSEPARATOR****命令配置）。
      - 域名做为后缀时，用户名+后缀分隔符+域名（当UEG的产品形态为风筝S时，后缀分隔符由命令配置当UEG的产品形态为风筝L时，后缀分隔符由****SET CPDOMAINSEPARATOR****命令配置）。
7. **可选：****故障场景紧急处理：**配置RADIUS鉴权超时无响应或计费AAA服务器无响应时的一键放通功能。

   **SET FHBYPASS**

   **说明** 

   - 本命令优先级高于**SET APNAUTHATTR**的**“AAANORSPCTRL”**和**SET APNRDSACCTCTRL**的**“****DEACTIVE”**。
   - 由于配置**SET FHBYPASS**将影响用户的激活状态，只有在取得了客户的书面认可后方可使用。
   - 通过**SET FHBYPASS**“HOLDINGTIME”控制故障恢复后对放通用户的后续处理，即永久在线或去激活。
8. **可选：**配置Specific APN。

   当UEG的产品形态为风筝L时，**ADD CPSPECIFICAPNVAL**

   **说明** 

   其中“ONLYROAMSWITCH”为可选参数，当UEG的产品形态为风筝L时，配置**ADD CPSPECIFICAPNVAL**命令的生效范围：仅对漫游用户生效。

   在上报APN时，不仅能携带Request APN/Service APN，UEG支持上报指定的APN，该APN可以是系统中配置的任一APN实例名称或者APN别名的名称。

   当配置了Specific APN时，在上报APN时，Specific APN优先级最高，其次是别名APN、虚拟APN、真实APN。
9. **可选：**配置是否检查RADIUS响应消息源端口。

   **SET RDSRSPADDRCHK**

   **说明** 

   该功能默认开启。如果组网中部署了防火墙或NAT设备，或AAA响应消息会修改IP和Port，RADIUS响应消息端口默认检查功能会失效，因此需要关闭该功能。

## 验证方法

具体步骤请参见调测到AAA Server的数据。

## 任务示例

任务描述

UEG上开启RADIUS功能。

脚本

//配置AAA服务器组。

```
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=MASTER_SLAVE, SIGOPTACCTMSG=DISABLE, ACCTTIMEOUT=10, ACCTRETRANSMIT=5, AUTHTIMEOUT=10, AUTHRETRANSMIT=5, ACCTSVRTOUT=12, ACCTSVRDTIME=180, AUTHSVRTOUT=12, AUTHSVRDTIME=180;
```

//配置鉴权AAA服务器。

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1812, VPNINSTANCE="vpn1", CIPHERKEY="*****", PRIFLAG=PRIMARY, PRIORITY=1, CIPHERKEYCNFM="*****";
```

//配置计费AAA服务器。

```
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1813, VPNINSTANCE="vpn1", CIPHERKEY="*****", PRIFLAG=PRIMARY, PRIORITY=1, CIPHERKEYCNFM="*****";
```

//配置RADIUS参数。

```
SET RDSACCTREQVSA: RDSSVRGRPNAME="isprg",THREEGPP=ENABLE,THREEGPP2=DISABLE;
```

```
ADD APNRDSCLIENTIP: APN="apn-test",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/1";
```

```
ADD APNRDSCLIENTIP: APN="apn-test",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/1";
```

```
ADD APNRDSSVRGRP: APN="apn-test",RDSSVRGRPNAME="isprg";
```

```
SET APNRDSACCTCTRL: APN="apn-test",TIMETHRESHOLD=30,VOLUMETHRESHOLD=20,SUPPORTACCTRSP=ENABLE,SUPPORTACCTUPD=ENABLE,RATTRIGGER=ENABLE,SRVTRIGGER=ENABLE,BUFFERTIMEVALUE=2;
```

```
SET APNRADIUSATTR:APN="apn-test",DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE,DOMAINNAMEPOS=SUFFIX;
```

```
SET APNAUTHATTR: APN="apn-test", DISCONNECT=ENABLE;
```