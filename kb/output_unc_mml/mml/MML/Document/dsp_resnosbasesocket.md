# 查询NOS Base平面网络的Socket信息（DSP RESNOSBASESOCKET）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询VNFP所有资源的NOS Base平面网络Socket信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                              |
|:--------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------|
| RESNAME       | 资源名称     | 可选必选说明：可选参数 参数含义：该参数用于指定资源名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：当不输入时显示所有的资源的信息。使用DSP RES查看资源名称。           |
| PEERADDRESSIN | 远端地址     | 可选必选说明：可选参数 参数含义：该参数指定远端地址。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：当不输入时显示包含所有远端地址的信息。                          |
| VERBOSE       | 是否查询详细信息 | 可选必选说明：可选参数 参数含义：该参数表示是否显示详细信息。 数据来源：本端规划 取值范围：枚举类型。 TRUE(是)：显示详细信息。FALSE(否)：不显示详细信息。 默认值：FALSE(否) 配置原则：仅当参数指定为“TRUE(是)”时，显示详细信息。 |

#### 使用实例

- 查询VNFP所有资源的NOS Base平面网络Socket信息：

  ```
  DSP RESNOSBASESOCKET:;
  ```

  ```
  RETCODE = 0  操作成功
   
  结果如下:
  --------------
  资源名称  状态    接收队列  发送队列  本端地址：端口       远端地址：端口             进程         TCP内部信息  

  OMU1      LISTEN  0         128       192.168.0.217:40083  0.0.0.0:*                  monitor      NULL         
  OMU1      ESTAB   0         0         192.168.0.217:41640  192.168.0.201:41022        dsle_boot    NULL         
  OMU1      ESTAB   0         0         192.168.0.217:54671  192.168.0.136:41022        monitor      NULL                 
  OMU2      ESTAB   0         0         192.168.0.217:43325  192.168.0.129:41022        monitor      NULL         
  (结果个数 = 4)

  ---    END
  ```

- 查询VNFP所有资源的NOS Base平面网络Socket详细信息：

  ```
  DSP RESNOSBASESOCKET: VERBOSE=TRUE;
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ----------
  资源名称  状态    接收队列  发送队列  本端地址：端口       远端地址：端口             进程         TCP内部信息                                                                                                                                                                                                                                                                                                                                                                                                                                         

  OMU1      LISTEN  0         128       192.168.0.217:40083  0.0.0.0:*                  monitor      cubic cwnd:10                                                                                                                                                                                                                                                                                                                                                                                                                                       
  OMU1      ESTAB   0         0         192.168.0.217:34943  192.168.0.201:41022        monitor      cubic wscale:9,9 rto:205 rtt:4.321/7.321 ato:40 mss:1398 pmtu:1450 rcvmss:537 advmss:1398 cwnd:10 bytes_acked:133202339 bytes_received:87350895 segs_out:2855790 segs_in:2075613 data_segs_out:1696134 data_segs_in:1592531 send 25.9Mbps lastsnd:79 lastrcv:79 lastack:79 pacing_rate 51.8Mbps delivery_rate 406.7Mbps delivered:1696135 app_limited busy:6541949ms retrans:0/34 rcv_rtt:58795.5 rcv_space:34249 rcv_ssthresh:178282 minrtt:0.04   
  OMU2      ESTAB   0         0         192.168.0.25:56925   192.168.0.136:41022        monitor      cubic wscale:9,9 rto:201 rtt:0.201/0.046 ato:40 mss:1398 pmtu:1450 rcvmss:536 advmss:1398 cwnd:10 bytes_acked:34011839 bytes_received:52534821 segs_out:319362 segs_in:159682 data_segs_out:159680 data_segs_in:159680 send 556.4Mbps lastsnd:166 lastrcv:166 lastack:166 pacing_rate 1108.0Mbps delivery_rate 141.6Mbps delivered:159681 app_limited busy:33998ms rcv_rtt:88290.3 rcv_space:29382 rcv_ssthresh:178282 minrtt:0.079                 
  OMU2      ESTAB   0         0         192.168.0.25:60034   192.168.0.201:41022        dsle_boot    cubic wscale:9,9 rto:201 rtt:0.249/0.04 ato:40 mss:1398 pmtu:1450 rcvmss:536 advmss:1398 cwnd:10 bytes_acked:34078295 bytes_received:52637468 segs_out:319986 segs_in:159994 data_segs_out:159992 data_segs_in:159992 send 449.2Mbps lastsnd:764 lastrcv:764 lastack:764 pacing_rate 895.2Mbps delivery_rate 169.5Mbps delivered:159993 app_limited busy:45052ms rcv_rtt:88071.9 rcv_space:29381 rcv_ssthresh:178282 minrtt:0.066                   
  (结果个数 = 4)

  ---    END
  ```

- 查询VNFP的“OMU1”的NOS Base网络Socket信息：

  ```
  DSP RESNOSBASESOCKET: RESNAME="OMU1";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ----------
  资源名称  状态    接收队列  发送队列  本端地址：端口       远端地址：端口             进程         TCP内部信息  

  OMU1      LISTEN  0         128       192.168.0.217:40083  0.0.0.0:*                  monitor      NULL         
  OMU1      LISTEN  0         128       192.168.0.217:10021  0.0.0.0:*                  ftpserver    NULL         
  OMU1      ESTAB   0         0         192.168.0.217:34943  192.168.0.201:41022        monitor      NULL         
  OMU1      ESTAB   0         0         192.168.0.217:41640  192.168.0.201:41022        dsle_boot    NULL         
  (结果个数 = 4)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                  |
|:--------|:-----------------------|
| 资源名称    | 表示资源名称。                |
| 状态      | 表示状态。                  |
| 接收队列    | 表示接收队列。                |
| 发送队列    | 表示发送队列。                |
| 本端地址：端口 | 表示NOS Base平面网络本端地址和端口。 |
| 远端地址：端口 | 表示远端地址和端口。             |
| 进程      | 表示进程名称。                |
| TCP内部信息 | 表示TCP内部信息。             |