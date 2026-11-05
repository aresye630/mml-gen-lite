# 查询SLA调试数据（DSP SLADBGDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SLA调试数据。

#### 注意事项

该命令最多返回8K字节，当数据内容过多时，可能会显示不全。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                      |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | 调试数据类型 | 可选必选说明：必选参数 参数含义：该参数用来指定SLA的调试数据类型。 数据来源：本端规划 取值范围：枚举类型。 ICMP：SLA的ICMP调试数据。TRACE：SLA的trace调试数据。LSPPING：SLA的LSP ping调试数据。LSPTRACE：SLA的LSP trace调试数据。 默认值：无 |

#### 使用实例

- 查询SLA的ICMP调试数据：

  ```
  DSP SLADBGDATA: TYPE=ICMP;
  ```

  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      PingTime                 AddrType  DestAddr            SourAddr      VrfIndex      IfIndex       PacketCount  PacketSize   Interval   Timeout      Ttl     Tos     SessionId    OperationType     MsgId
      2017-04-01 15:09:35.532  1         10.137.144.1        10.0.0.1       0             0             5            56           500        2000         255     255     64           0                 64
      (结果个数 = 1)
      ---    END
  ```
- 查询SLA的trace调试数据：

  ```
  DSP SLADBGDATA: TYPE=TRACE;
  ```

  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      TraceTime                 AddrType  DestAddr      SourAddr   VrfIndex   PacketSize   Timeout  InitTtl  MaxTtl  SessionId  OperationType  MsgId
      2017-04-01 15:13:26.330   1         10.137.144.1  10.0.0.1   0          12           5000     1        30      64         0              64
      (结果个数 = 1)
      ---    END
  ```
- 查询SLA的LSP ping调试数据：

  ```
  DSP SLADBGDATA: TYPE=LSPPING;
  ```

  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      PingTime                 DestAddr         MaskLen   LspType   ReplyMode  SourAddr         PacketCount   PacketSize   Interval   Timeout      Ttl   Exp   SessionId   OperationType   MsgId
      2017-04-01 15:10:45.817  10.137.144.1     32        0         2          0.0.0.0          5             100          2000       2000         64    0     64          0               64
      (结果个数 = 1)
      ---    END
  ```
- 查询SLA的LSP trace调试数据：

  ```
  DSP SLADBGDATA: TYPE=LSPTRACE;
  ```

  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      TraceTime                DestAddr         MaskLen   LspType   ReplyMode  SourAddr         PacketSize    Timeout      InitTtl    MaxTtl      Exp   SessionId   OperationType   MsgId
      2017-04-01 15:12:30.716  10.137.144.1     32        0         2          0.0.0.0          0             2000         0          255         0     64          0               64
      (结果个数 = 1)
      ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释           |
|:--------|:----------------|
| 查询结果信息  | 用来显示SLA的查询结果数据。 |