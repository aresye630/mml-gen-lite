# 配置禁止UE互访功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

为了防止UE之间的恶意攻击，保证UE的安全，可以在UEG上配置整机APN、指定APN内或APN间禁止UE互访。如果涉及跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。

适用于SGW-U、PGW-U、UPF。

## 必备事项

前提条件

无。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET GLOBUEMUTACC** | 同APN内的控制开关（INNERAPNS） | ENABLE | 本端规划 | 整机所有APN内及APN间的UE均不允许互访。 |
|  | 不同APN间的控制开关（INTERAPNS） | ENABLE | 本端规划 |  |

## 操作步骤

1. 开启全局UE互访控制开关。

   **SET GLOBUEMUTACC**

   需要控制指定APN内或者APN间的UE互访，可以通过**SET APNUEMUTACC**命令控制。

   * “不同APN间的控制开关（INTERAPNS）”：用于控制是否允许其他APN向本APN发送报文。如果该参数设置为“ENABLE”，则丢弃其他APN的UE向本APN的UE发送的报文。如果该参数设置为“DISABLE”，则放通其他APN的UE向本APN的UE发送的报文。
   * “同APN内的控制开关（INNERAPNS）”：用于控制是否允许APN内的UE之间互访。如果参数设置为“ENABLE”，则丢弃APN内UE发送的报文。如果该参数设置为“DISABLE”，则放通APN内UE发送的报文。

## 任务示例

任务描述

禁止整机粒度APN内及APN间UE互访。

脚本

//整机粒度APN内UE互访控制开关配置为开启，整机粒度APN间UE互访控制开关配置为开启。

```
SET GLOBUEMUTACC: INNERAPNS=ENABLE, INTERAPNS=ENABLE;
```

版权所有 © 华为技术有限公司
