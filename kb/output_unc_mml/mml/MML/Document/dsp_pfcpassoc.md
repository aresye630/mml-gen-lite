# 查询PFCP偶联相关数据（DSP PFCPASSOC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于查询PFCP偶联相关数据，包括偶联状态，以及本端对端地址等信息。

## 注意事项

- 静默状态：当存在正常的代理链路时，静默直连链路处于静默状态，不进行链路状态探测且不承载业务。
- 静默正常状态：当所有代理链路都故障后，静默直连链路在链路探测正常后进入静默正常状态，可以正常进行链路状态探测和承载业务。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识            | 参数名称         | 参数说明                                                                                                                                                                                          |
|:----------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE       | 查询类型         | 可选必选说明：必选参数  参数含义：查询PFCP偶联数据的参数类型。  数据来源：本端规划 取值范围： All_Simple（所有简要）All（所有）UpNodeId（UP节点标识）NfInstanceName（UP唯一标识）  默认值：无  配置原则：无                                                              |
| NFINSTANCENAME  | UPF实例名称      | 可选必选说明：该参数在"QUERYTYPE"配置为"NfInstanceName"时为条件必选参数。  参数含义：UPF的实例名称，用于唯一标识一个UP。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。  默认值：无  配置原则：无 |
| UPNODEIDFQDNVAL | UP节点标识的FQDN值 | 可选必选说明：该参数在"QUERYTYPE"配置为"UpNodeId"时为条件必选参数。  参数含义：UP节点标识的FQDN值。该参数作为输入参数时，查询结果返回为空。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~255。  默认值：无  配置原则：无                                                      |

## 使用实例

- 查询所有偶联状态。
  DSP PFCPASSOC: QUERYTYPE=All;

  ```
  %%DSP PFCPASSOC: QUERYTYPE=All;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  查询类型  UPF实例名称     UP节点标识的FQDN值  本端IP地址1  本端IP地址2  本端端口号  对端IP地址1  链路1状态  对端IP地址2  链路2状态  对端IP地址3  链路3状态  对端IP地址4  链路4状态  对端端口号  偶联状态  权重  S1-U IPv4地址  S1-U IPv6地址  S5/S8 IPv4地址  S5/S8 IPv6地址  Pa IPv4地址  Pa IPv6地址  N3 IPv4地址  N3 IPv6地址  N9 IPv4地址  N9 IPv6地址  UP负载  S11-U IPv4 地址  S11-U IPv6 地址  POD名称   优雅释放时刻  

  所有      upf_instance_2  localupf2           10.2.128.17  NULL         8805        10.70.30.12  未知       NULL         未知       NULL         未知       NULL         未知       8805        未知      0     NULL           NULL           NULL            NULL            NULL         NULL         NULL         NULL         NULL         NULL         0       NULL             NULL             uncpod-0  NULL
  所有      upf_instance_1  localupf1           10.2.128.17  NULL         8805        10.70.30.11  未知       NULL         未知       NULL         未知       NULL         未知       8805        未知      0     NULL           NULL           NULL            NULL            NULL         NULL         NULL         NULL         NULL         NULL         0       NULL             NULL             uncpod-0  NULL
  (结果个数 = 2)

  ---    END
  ```
- 查询FQDN为“localupf1”的UP偶联状态。
  DSP PFCPASSOC: QUERYTYPE=UpNodeId, UPNODEIDFQDNVAL="localupf1";

  ```
  %%DSP PFCPASSOC: QUERYTYPE=UpNodeId, UPNODEIDFQDNVAL="localupf1";%%
  RETCODE = 20111  无数据。

  没有查到相应结果
  ---    END
  ```
- 查询所有偶联状态简要信息。
  DSP PFCPASSOC: QUERYTYPE=All\_Simple;

  ```
  %%DSP PFCPASSOC: QUERYTYPE=All_Simple;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  UPF实例名称     偶联状态  UP负载 

  upf_instance_1  故障      0
  upf_instance_2  未知      0 
  (结果个数 = 2)

  ---    END
  ```

## 输出结果说明

| 输出项名称         | 输出项解释                                                                                          |
|:--------------|:-----------------------------------------------------------------------------------------------|
| UPF实例名称       | UPF的实例名称，用于唯一标识一个UP。                                                                           |
| 偶联状态          | 偶联状态。 取值说明： Unknown（未知）Normal（正常）Error（故障）GracefulRelease（优雅释放状态）                              |
| UP负载          | UP负载水平。                                                                                        |
| 查询类型          | 查询PFCP偶联数据的参数类型。 取值说明： All_Simple（所有简要）All（所有）UpNodeId（UP节点标识）NfInstanceName（UP唯一标识）           |
| UP节点标识的FQDN值  | UP节点标识的FQDN值。该参数作为输入参数时，查询结果返回为空。                                                              |
| 本端IP地址1       | 本端IP地址1。                                                                                       |
| 本端IP地址2       | 本端IP地址2。                                                                                       |
| 本端端口号         | 本端端口号。                                                                                         |
| 对端IP地址1       | 对端IP地址1。                                                                                       |
| 链路1状态         | 链路1状态。 取值说明： Unknown（未知）Normal（正常）Error（故障）GracefulRelease（优雅释放状态）Silent（静默）SilentNormal（静默正常） |
| 对端IP地址2       | 对端IP地址2。                                                                                       |
| 链路2状态         | 链路2状态。 取值说明： Unknown（未知）Normal（正常）Error（故障）GracefulRelease（优雅释放状态）Silent（静默）SilentNormal（静默正常） |
| 对端IP地址3       | 对端IP地址3。                                                                                       |
| 链路3状态         | 链路3状态。 取值说明： Unknown（未知）Normal（正常）Error（故障）GracefulRelease（优雅释放状态）Silent（静默）SilentNormal（静默正常） |
| 对端IP地址4       | 对端IP地址4。                                                                                       |
| 链路4状态         | 链路4状态。 取值说明： Unknown（未知）Normal（正常）Error（故障）GracefulRelease（优雅释放状态）Silent（静默）SilentNormal（静默正常） |
| 对端端口号         | 对端端口号。                                                                                         |
| 权重            | 权重。                                                                                            |
| S1-U IPv4地址   | S1-U IPv4地址。                                                                                   |
| S1-U IPv6地址   | S1-U IPv6地址。                                                                                   |
| S5/S8 IPv4地址  | S5/S8 IPv4地址。                                                                                  |
| S5/S8 IPv6地址  | S5/S8 IPv6地址。                                                                                  |
| Pa IPv4地址     | Pa IPv4地址。                                                                                     |
| Pa IPv6地址     | Pa IPv6地址。                                                                                     |
| N3 IPv4地址     | N3 IPv4地址。                                                                                     |
| N3 IPv6地址     | N3 IPv6地址。                                                                                     |
| N9 IPv4地址     | N9 IPv4地址。                                                                                     |
| N9 IPv6地址     | N9 IPv6地址。                                                                                     |
| S11-U IPv4 地址 | S11-U IPv4地址。                                                                                  |
| S11-U IPv6 地址 | S11-U IPv6地址。                                                                                  |
| POD名称         | 该参数用于显示POD名称。                                                                                  |
| 优雅释放时刻        | 该参数用于显示收到对端优雅释放消息后，释放偶联的时刻。                                                                    |