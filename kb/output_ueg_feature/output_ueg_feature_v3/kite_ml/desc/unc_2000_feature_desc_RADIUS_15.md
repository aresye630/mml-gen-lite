# 修改AAA鉴权的密钥

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

根据要求在UEG上修改与AAA鉴权服务器对应的共享密钥。

适用于PGW-C、SMF

## 对系统的影响

* 修改的数据，对修改后激活的用户生效。
* 如果在修改时有用户正在使用该RADIUS server鉴权，则会鉴权失败。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| RADIUS Server信息 | Radius Server Group名称（RDSSVRGRPNAME） | ss | 本端规划 | **ADD RDSSVRGRP** |
|  | 服务器类型（SERVERTYPE） | AUTHENTICATION | 本端规划 | **ADD RDSSVR** |
|  | 服务器IP版本（IPVERSION） | IPV4 | 本端规划 |  |
|  | IPv4地址（SERVERIPV4） | 192.168.4.26 | 全网规划 |  |
| AAA鉴权的密钥 | 服务器密钥（加密的）（CIPHERKEY） | hi | 与对端协商 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 删除RADIUS服务器组中的鉴权服务器。

   **RMV RDSSVR**

   目前的版本不能直接修改密钥，需要先把这个RADIUS Server的配置删除，然后重配。
3. 配置主备鉴权服务器。

   **ADD RDSSVR**

   UEG上配置的鉴权密钥必须与AAA鉴权服务器上配置的NAS（Network Access Server）端密钥保持一致。

## 任务示例

任务描述

修改与AAA鉴权服务器对应的密钥。

脚本

//修改密钥。

```
RMV RDSSVR: RDSSVRGRPNAME="ss",SERVERTYPE=AUTHENTICATION,IPVERSION=IPV4,SERVERIPV4="192.168.4.26";
```

```
ADD RDSSVR: RDSSVRGRPNAME="ss",SERVERTYPE=AUTHENTICATION,IPVERSION=IPV4,SERVERIPV4="192.168.4.26",CIPHERKEY="hi",CIPHERKEYCNFM="hi";
```

版权所有 © 华为技术有限公司
