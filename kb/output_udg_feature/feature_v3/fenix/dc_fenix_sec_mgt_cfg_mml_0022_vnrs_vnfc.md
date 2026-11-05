# 配置GRE VPN安全

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤

## 操作场景

采用GRE VPN方案时，使能识别关键字、端到端报文验证、Keepalive功能，提升数据传输安全性。

## 对系统的影响

该操作对系统正常运行没有影响。

## 必备事项

前提条件

请仔细阅读VPN。

数据

无。

## 操作步骤

1. 配置GRE隧道，并使能识别关键字功能、Keepalive功能、端到端校验功能。

   在“MML命令行-UDG”窗口上执行：

   **ADD GRETUNNEL**: TNLNAME="隧道名称", TNLTYPE=隧道类型, SRCTYPE=源类型, SRCIPADDR="源IP地址", DSTIPADDR="目的IP地址", KEEPALVEN=TRUE, GREKEYEN=TRUE, GREKEY="识别关键字", CHECKSUMEN=TRUE;

版权所有 © 华为技术有限公司
