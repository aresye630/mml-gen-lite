# 修改RADIUS鉴权消息的超时重发数据

- 操作场景
- 对系统的影响
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

当AAA Server的RADIUS消息的重发次数和超时的时间发生变化时，UEG需要修改相应的配置以便和AAA Server保持一致。

**说明** 

适用于PGW-C、SMF

## 对系统的影响

- 修改的数据，对已经激活的用户生效。
- 鉴权消息和计费消息的超时重发数据可独立配置，不会相互影响。

## 必备事项

前提条件

完成配置RADIUS功能。

数据

| 类别             | 参数名称                                              | 取值样例   | 获取方法     | 说明                                       |
|:---------------|:--------------------------------------------------|:-------|:---------|:-----------------------------------------|
| RADIUS组名称      | Radius Server Group名称（RDSSVRGRPNAME）              | ss     | 已配置数据中获取 | 鉴权服务器所在的Radius服务器组，已通过ADD RDSSVRGRP进行配置。 |
| RADIUS消息的超时的时间 | Radius Authentication Request超时时间（AUTHTIMEOUT）    | 3      | 与对端协商    | MOD RDSSVRGRP                            |
| RADIUS消息的重发次数  | Radius Authentication Request重发次数（AUTHRETRANSMIT） | 1      | 与对端协商    | MOD RDSSVRGRP                            |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 修改RADIUS消息的重发数据。

   **MOD RDSSVRGRP**

## 任务示例

任务描述

修改RADIUS Server实例“ss”下Radius Authentication Request超时时间从“10”修改成“3”，Radius Authentication Request重发次数从“5”修改成“1”。

脚本

//修改RADIUS消息的重发数据。

```
MOD RDSSVRGRP: RDSSVRGRPNAME="ss",AUTHTIMEOUT=3,AUTHRETRANSMIT=1;
```