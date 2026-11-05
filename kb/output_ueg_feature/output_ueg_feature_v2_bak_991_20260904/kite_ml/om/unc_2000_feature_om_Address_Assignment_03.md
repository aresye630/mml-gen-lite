# 配置静态地址黑名单

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

可以在本地配置静态地址黑名单，判断用户携带地址的合法性，若用户地址出现于黑名单中，标明地址非法，不允许接入。

**说明** 

适用于PGW-C、SMF。

## 必备事项

前提条件

请仔细阅读GWFD-020804 地址分配方式特性概述。

数据

| 类别            | 参数名称                | 取值样例           | 获取方法     | 说明        |
|:--------------|:--------------------|:---------------|:---------|:----------|
| ADD BLACKLIST | 名称（NAME）            | testblacklist1 | 本端规划     | 配置静态地址黑名单 |
| ADD BLACKLIST | IP地址类型（IPVERSION）   | IPV4           | 本端规划     | 配置静态地址黑名单 |
| ADD BLACKLIST | IPv4起始地址（V4STARTIP） | 10.1.1.1       | 本端规划     | 配置静态地址黑名单 |
| ADD BLACKLIST | IPv4结束地址(V4ENDIP)   | 10.1.1.10      | 本端规划     | 配置静态地址黑名单 |
| ADD BLACKLIST | 绑定VPN（HASVPN）       | Enable         | 本端规划     | 配置静态地址黑名单 |
| ADD BLACKLIST | VPN实例名（VPNINSTANCE） | testvpn        | 已配置数据中获取 | -         |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 创建静态地址黑名单。

   **ADD BLACKLIST**

## 任务示例

任务描述

运营商判断10.1.1.1~10.1.1.10地址段内的地址非法，将其配置为静态地址黑名单，用户地址出现于黑名单中时，不允许接入。

脚本

//创建静态地址黑名单。

```
ADD BLACKLIST: NAME="testblacklist", IPVERSION=IPv4, V4STARTIP="10.1.1.1", V4ENDIP="10.1.1.10", HASVPN=Enable, VPNINSTANCE="testvpn";
```