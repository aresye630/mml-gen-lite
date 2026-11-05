# 显示SSH客户端的会话统计信息（DSP SSHCSESSIONSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SSH客户端的会话统计信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

无。

#### 使用实例

查询SSH客户端的会话统计信息：

```
DSP SSHCSESSIONSTC:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
             会话索引  =  0
 与CAMLCSI组件的通道ID = 137487
               通道ID  =  5
               用户名  =  admin
            Trace信息  =  StartTime:0-0-0:0-0-0. END
            Socket状态 =  SSHC_CTRL_SOCK_STATE_CREATED
    最近5秒钟数据统计 =  Received packets from client: total-bytes=875, total-count=17, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
    最近1分钟数据统计 =  Received packets from client: total-bytes=1875, total-count=117, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
    最近5分钟数据统计 =  Received packets from client: total-bytes=2875, total-count=217, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
         所有数据统计 =  Received packets from client: total-bytes=9875, total-count=917, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
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
| 最近5秒钟数据统计       | 最近5秒钟客户端与服务器之间的交互数据统计。 |
| 最近1分钟数据统计       | 最近1分钟客户端与服务器之间的交互数据统计。 |
| 最近5分钟数据统计       | 最近5分钟客户端与服务器之间的交互数据统计。 |
| 所有数据统计          | 客户端与服务器之间的所有交互数据统计。    |
| 与CAMLCSI组件的通道ID | 与CAMLCSI组件的通道ID。       |