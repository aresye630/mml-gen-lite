# 查询NOS Base平面网络的Socket信息（DSP NOSBASESOCKET）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询NOS Base平面网络的Socket信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称     | 参数说明                                                                                                                        |
|:----------------|:---------|:----------------------------------------------------------------------------------------------------------------------------|
| RUNAME          | RU名称     | 可选必选说明：可选参数 参数含义：该参数用于指定RU名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：当不输入时显示所有的RU的信息。使用DSP RU查看RU名称。      |
| PEERADDRESSIN   | 远端地址     | 可选必选说明：可选参数 参数含义：该参数指定远端地址。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：当不输入时显示包含所有远端地址的信息。                    |
| VERBOSE         | 是否查询详细信息 | 可选必选说明：可选参数 参数含义：该参数表示是否显示详细信息。 数据来源：本端规划 取值范围：枚举类型。 TRUE(是)：显示详细信息。FALSE(否)：不显示详细信息。 默认值：FALSE(否) 配置原则：当不输入时默认不显示详细信息      |
| SERVICEINSTANCE | 服务实例     | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

#### 使用实例

- 查询指定大颗粒服务实例的所有NOS Base平面网络Socket信息：

  ```
  DSP NOSBASESOCKET: SERVICEINSTANCE="ACS";
  ```

  ```
  RETCODE = 0  操作成功
   
  结果如下:
  --------------
  RU名称          状态       接收队列  发送队列  本端地址：端口     远端地址：端口              进程         TCP内部信息  

  ACS_OM_RU_0001  LISTEN     0         128       192.168.1.5:hbci   0.0.0.0:*                   monitor      NULL         
  ACS_OM_RU_0001  ESTAB      0         0         192.168.1.5:46940  192.168.1.242:21087         monitor      NULL         
  ACS_OM_RU_0002  ESTAB      0         0         192.168.1.5:41022  192.168.2.240:21084         monitor      NULL         
  ACS_OM_RU_0002  TIME-WAIT  0         0         192.168.1.5:38469  192.168.0.217:2341          NULL         NULL         
  (结果个数 = 4)
   
  ---    END
  ```

- 查询指定大颗粒服务实例的所有NOS Base平面网络Socket详细信息：

  ```
  DSP NOSBASESOCKET: VERBOSE=TRUE, SERVICEINSTANCE="ACS";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ----------
  RU名称          状态       接收队列  发送队列  本端地址：端口     远端地址：端口              进程       TCP内部信息                                                                                                                                                                                                                                                                                                                                                                                                                         

  ACS_OM_RU_0001  LISTEN     0         128       192.168.1.5:40062  0.0.0.0:*                   monitor    cubic cwnd:10                                                                                                                                                                                                                                                                                                                                                                                                                       
  ACS_OM_RU_0001  ESTAB      0         0         192.168.1.5:53994  192.168.1.242:21087         monitor    cubic wscale:9,1 rto:201 rtt:0.262/0.317 ato:40 mss:1398 pmtu:1450 rcvmss:1398 advmss:1398 cwnd:10 bytes_acked:4328 bytes_received:5403 segs_out:407 segs_in:403 data_segs_out:5 data_segs_in:6 send 426.9Mbps lastsnd:1502287 lastrcv:1502286 lastack:721 pacing_rate 852.5Mbps delivery_rate 219.3Mbps delivered:6 app_limited busy:3ms rcv_rtt:2.656 rcv_space:28200 rcv_ssthresh:42180 minrtt:0.055                             
  ACS_OM_RU_0001  TIME-WAIT  0         0         192.168.1.5:36251  192.168.0.217:2341          NULL       NULL                                                                                                                                                                                                                                                                                                                                                                                                                                
  ACS_OM_RU_0001  ESTAB      0         0         192.168.1.5:51764  192.168.2.99:21095          monitor    cubic wscale:9,1 rto:201 rtt:0.281/0.309 ato:40 mss:1398 pmtu:1450 rcvmss:1398 advmss:1398 cwnd:10 bytes_acked:4327 bytes_received:5403 segs_out:407 segs_in:40
  (结果个数 = 4)

  ---    END
  ```

- 查询指定大颗粒服务实例指定远端地址的NOS Base平面网络Socket信息：

  ```
  DSP NOSBASESOCKET: PEERADDRESSIN="192.168.0.105", SERVICEINSTANCE="ACS";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ----------
  RU名称          状态   接收队列  发送队列  本端地址：端口     远端地址：端口      进程     TCP内部信息  

  ACS_OM_RU_0001  ESTAB  0         0         192.168.1.5:45268  192.168.0.105:21023 monitor  NULL         
  ACS_OM_RU_0001  ESTAB  0         0         192.168.1.5:38488  192.168.0.105:21053 monitor  NULL         
  ACS_OM_RU_0001  ESTAB  0         0         192.168.1.5:43746  192.168.0.105:21053 monitor  NULL         
  ACS_OM_RU_0001  ESTAB  0         0         192.168.1.5:35180  192.168.0.105:21076 monitor  NULL         
  (结果个数 = 4)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                  |
|:--------|:-----------------------|
| RU名称    | 表示RU名称。                |
| 状态      | 表示状态。                  |
| 接收队列    | 表示接收队列。                |
| 发送队列    | 表示发送队列。                |
| 本端地址：端口 | 表示NOS Base平面网络本端地址和端口。 |
| 远端地址：端口 | 表示远端地址和端口。             |
| 进程      | 表示进程名称。                |
| TCP内部信息 | 表示TCP内部信息。             |