# 修改AAA Server地址

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

在网络调整中切换了AAA Server，需要重新设定AAA Server地址。

适用于PGW-C、SMF

## 对系统的影响

若正有用户使用该AAA server进行鉴权或计费，则在更改IP后，该用户会鉴权失败，或计费丢失。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| AAA Server参数 | Radius Server Group名称（RDSSVRGRPNAME） | mm | 本端规划 | **MOD RDSSVR** |
|  | 服务器类型（SERVERTYPE） | AUTHENTICATION | 本端规划 |  |
|  | 服务器IP版本（IPVERSION） | IPV4 | 本端规划 |  |
|  | IPv4地址（SERVERIPV4） | 192.168.6.20 | 全网规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 在UEG上修改AAA Server鉴权参数。

   **MOD RDSSVR**

## 任务示例

任务描述

修改名字为mm的Radius Server Group下的主鉴权服务器地址为192.168.6.20。

脚本

//修改AAA Server鉴权参数。

```
MOD RDSSVR: RDSSVRGRPNAME="mm",SERVERTYPE=AUTHENTICATION,IPVERSION="IPV4",SERVERIPV4="192.168.6.20";
```

版权所有 © 华为技术有限公司
