# 查询GRE消息诊断信息（DSP GREMSGSTATINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询GRE消息诊断信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称     | 参数说明                                                                                |
|:-----------|:---------|:------------------------------------------------------------------------------------|
| MSGSTATCLR | 消息统计清除标记 | 可选必选说明：可选参数 参数含义：该参数用来指定是否清除消息统计信息。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 |

#### 使用实例

查询GRE消息诊断信息：

```
DSP GREMSGSTATINFO:;
```

```
        RETCODE = 0  操作成功。

        结果如下
        --------
        诊断信息数据

        Time              Message Statistic Information
        -------------------------------------------------------------------------------------------------------------------------------------
        [09 01:30:05:613] [Snd to   IFM    0x7a03fa   MsgType: 13 Len: 24    Seq: 0    Trans: 0  Ack: 0]
        [09 01:30:05:614] [Snd to   RMIPV4 0x712716   MsgType: 12 Len: 4096  Seq: 0    Trans: 1473384605 Ack: 0]
        [09 01:30:05:614] [Snd to   RMIPV6 0x232715   MsgType: 12 Len: 4096  Seq: 0    Trans: 1473384606 Ack: 0]
        [09 01:30:05:615] [Rcv from TNLM   0x202717   MsgType: 3  Len: 20    Seq: 0    Trans: 0  Ack: 0]
        [09 01:30:05:615] [Snd to   TNLM   0x202717   MsgType: 3  Len: 20    Seq: 0    Trans: 0  Ack: 1]
        [09 01:30:05:615] [Snd to   TNLM   0x202717   MsgType: 4  Len: 28    Seq: 0    Trans: 1473384607 Ack: 0]
        [09 01:30:05:615] [Rcv from TNLM   0x202717   MsgType: 4  Len: 28    Seq: 0    Trans: 1473384607 Ack: 1]
        [09 01:30:05:615] [Snd to   TNLM   0x202717   MsgType: 5  Len: 76    Seq: 0    Trans: 1473384607 Ack: 0]
        [09 01:30:05:615] [Rcv from RMIPV6 0x232715   MsgType: 12 Len: 60    Seq: 0    Trans: 1473384606 Ack: 1]
        [09 01:30:05:615] [Rcv from TNLM   0x202717   MsgType: 5  Len: 76    Seq: 0    Trans: 1473384607 Ack: 1]
        [09 01:30:05:615] [Snd to   TNLM   0x202717   MsgType: 6  Len: 28    Seq: 0    Trans: 1473384607 Ack: 0]
        [09 01:30:05:615] [Rcv from RMIPV4 0x712716   MsgType: 12 Len: 60    Seq: 0    Trans: 1473384605 Ack: 1]
        [09 01:30:05:615] [Rcv from TNLM   0x202717   MsgType: 6  Len: 28    Seq: 0    Trans: 1473384607 Ack: 1]
        [09 01:30:05:616] [Rcv from TNLM   0x202717   MsgType: 8  Len: 52    Seq: 0    Trans: 2  Ack: 0]
        [09 01:30:05:616] [Snd to   TNLM   0x202717   MsgType: 8  Len: 52    Seq: 0    Trans: 2  Ack: 1]

        (结果个数 = 15)
        ---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 诊断信息数据  | 用来指定诊断信息数据。 |