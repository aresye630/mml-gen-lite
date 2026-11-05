# 修改AAA计费的密钥

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

UEG上配置的计费密钥必须与计费服务器上配置的NAS（Network Access Server）端密钥保持一致，否则无法计费。

**说明** 

适用于PGW-C、SMF

## 对系统的影响

如果在修改时有用户正在使用该RADIUS Server计费，则会计费失败。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

数据

| 类别              | 参数名称                                 | 取值样例         | 获取方法   | 说明            |
|:----------------|:-------------------------------------|:-------------|:-------|:--------------|
| RADIUS Server信息 | Radius Server Group名称（RDSSVRGRPNAME） | ss           | 本端规划   | ADD RDSSVRGRP |
| RADIUS Server信息 | 服务器类型（SERVERTYPE）                    | ACCOUNTING   | 本端规划   | ADD RDSSVR    |
| RADIUS Server信息 | 服务器IP版本（IPVERSION）                   | IPV4         | 本端规划   | ADD RDSSVR    |
| RADIUS Server信息 | IPv4地址（SERVERIPV4）                   | 192.168.4.26 | 全网规划   | ADD RDSSVR    |
| AAA计费的密钥        | 服务器密钥（加密的）（CIPHERKEY）                | 123          | 与对端协商  | ADD RDSSVR    |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 删除同一VPN下IP地址相同的服务器。

   **RMV RDSSVR**

   **说明** 

   目前的版本不能直接修改密钥，需要先把这个RADIUS Server的配置删除，然后重配。
3. 修改AAA计费密钥。

   **ADD RDSSVR**

## 任务示例

任务描述

修改Radius Server Group实例“ss”下IP地址为“192.168.4.26”的AAA计费密钥为“123”。

脚本

//修改密钥。

```
RMV RDSSVR: RDSSVRGRPNAME="ss",SERVERTYPE=ACCOUNTING,IPVERSION=IPV4,SERVERIPV4="192.168.4.26";
```

```
ADD RDSSVR: RDSSVRGRPNAME="ss",SERVERTYPE=ACCOUNTING,IPVERSION=IPV4,SERVERIPV4="192.168.4.26",CIPHERKEY="123",CIPHERKEYCNFM="123";
```