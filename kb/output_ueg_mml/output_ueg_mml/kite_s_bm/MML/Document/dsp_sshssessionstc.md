# 显示SSH服务器的会话统计信息（DSP SSHSSESSIONSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SSH服务器的会话统计信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

无。

#### 使用实例

查询SSH服务器的会话统计信息：

```
DSP SSHSSESSIONSTC:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
             会话索引  =  0
 与CAMLCSI组件的通道ID = 137487
               通道ID  =  135171
               用户名  =  admin
            Trace信息  =  StartTime:2016-8-4:20-58-23. sock setopt(0)->snd sshver(0)->rev sshver(0)->snd keyinit(0)->rev keyinit(0)->rev gexreq(0)->snd gexgrp(0)->rev gexinit(0)->snd gexreply(0)->snd newkeys(0)->rev newkeys(0)->snd svcreq(0)->snd svcacp(0)->rev userauthreq(0)->snd authfailpsd(0)->rev userauthreq(0)->snd aaaauthreq(0)->snd authsucc(0)->rev chnlopen(0)->snd chnlcfirm(0)->rev chnlreq(0)->snd chnlsucc(0)->rev chnlreq(0)->snd camlcntreq(0)->rev camlcntrsp(0)->snd subscribereq(0)->snd chnlsucc(0)->END
            Socket状态 =  SOCKCONN_STATE_UP
    最近5秒钟数据统计 =  Received packets from client: total-bytes=1507, total-count=12, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
    最近1分钟数据统计 =  Received packets from client: total-bytes=2507, total-count=112, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
    最近5分钟数据统计 =  Received packets from client: total-bytes=3507, total-count=212, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
         所有数据统计 =  Received packets from client: total-bytes=9507, total-count=912, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称           | 输出项解释                  |
|:----------------|:-----------------------|
| 会话索引            | SSH会话索引。               |
| 通道ID            | SSH连接的通道ID。            |
| 用户名             | SSH用户名。                |
| Trace信息         | Trace信息，显示会话的关键路径。     |
| Socket状态        | Socket状态。              |
| 最近5秒钟数据统计       | 最近5秒钟服务器与客户端之间的交互数据统计。 |
| 最近1分钟数据统计       | 最近1分钟服务器与客户端之间的交互数据统计。 |
| 最近5分钟数据统计       | 最近5分钟服务器与客户端之间的交互数据统计。 |
| 所有数据统计          | 服务器与客户端之间的所有交互数据统计。    |
| 与CAMLCSI组件的通道ID | 与CAMLCSI组件的通道ID。       |