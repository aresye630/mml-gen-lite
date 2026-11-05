# 查询IPv6诊断信息（DSP IPV6INFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询IPv6诊断信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称     | 参数说明                                                                                                                                                                                                                 |
|:--------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPV6QUERYTYPE | 查询类型     | 可选必选说明：必选参数 参数含义：该参数用来指定查询类型。 数据来源：本端规划 取值范围：枚举类型。 LOCAL：IPv6组件的基本信息。IFM：与IFM交互的信息。MCAST：Multicast信息。CPCAR：Cp-car信息。IFMLIB：Ifmlib信息。PARTNER：Partner信息。PIPE：管道信息。PATH：PATH信息。STATISTICS：统计信息。PATHDETAIL：路径详细信息。 默认值：无 |
| IFQUERYTYPE   | 查询接口类型   | 可选必选说明：条件可选参数 前提条件：该参数在“IPV6QUERYTYPE”配置为“IFM”、“MCAST”、“IFMLIB” 或 “STATISTICS”时为可选参数。 参数含义：该参数用来指定接口查询类型。 数据来源：本端规划 取值范围：枚举类型。 IFINDEX：接口索引。IFNAME：接口名称。 默认值：无                                                       |
| IFINDEX       | 接口索引     | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。 参数含义：该参数用来指定接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                                                                               |
| IFNAME        | 接口名称     | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。 参数含义：该参数用于指定接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                                                     |
| IPV6ADDR      | IPv6地址   | 可选必选说明：条件可选参数 前提条件：该参数在“IPV6QUERYTYPE”配置为“MCAST”时为可选参数。 参数含义：该参数用来指定IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                                                                                           |
| PID           | APP组件PID | 可选必选说明：条件可选参数 前提条件：该参数在“IPV6QUERYTYPE”配置为“LOCAL”、“IFM”、“MCAST”、“CPCAR” 或 “IFMLIB”时为可选参数。 参数含义：该参数用来指定APP的PID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                     |
| ISSLAVE       | 是否备用资源单元 | 可选必选说明：可选参数 参数含义：该参数用来指定是否为备用资源单元。 数据来源：本端规划 取值范围：枚举类型。 Master：主资源单元。Slave：备资源单元。 默认值：Master                                                                                                                         |
| VLANID        | VLAN ID  | 可选必选说明：条件可选参数 前提条件：该参数在“IPV6QUERYTYPE”配置为“IFMLIB”时为可选参数。 参数含义：该参数用来显示接口所属的VLAN。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4094。 默认值：无                                                                                               |
| PATHID        | Path ID  | 可选必选说明：条件可选参数 前提条件：该参数在“IPV6QUERYTYPE”配置为“PATHDETAIL”时为可选参数。 参数含义：该参数用于显示PATH ID。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无                                                                                       |

#### 使用实例

- 查询IPv6 Local诊断信息：

  ```
  DSP IPV6INFO:IPV6QUERYTYPE=LOCAL,PID="0x72000F";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =
    Param:
      ParamNo               : 2
      CmdKey                : 1
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : ::
      Pid                   : 0x72000f
    Pid: 0x72000f
      Cid        : 0x80720014
    LOCAL:
      Pid                 : 0x72000f
      Cid                 : 0x80720014
      CompType            : 0x72
      LrId                : 0x0
      VrId                : 0x0
      LocationId          : 0x3e8
      WorkMode            : 0x0
      PktStatTree         : 0
      PmtuTree            : 0
      PmtuDisWalkTree     : 0
      VrTree              : 1
      VrVrfTree           : 0
      PktNoPipeTree       : 0
      SecCfgTree          : 0
      Ip6AddrTree         : 4
      bIsolateEnable      : 1

  (结果个数 = 1)
  ---    END
  ```
- 查询IPv6 Partner诊断信息：

  ```
  DSP IPV6INFO:IPV6QUERYTYPE=PARTNER;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据

    Param:
      ParamNo               : 2
      CmdKey                : 6
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : ::
      Pid                   : 0x0
    Pid: 0x72000f
      Cid        : 0x80720014
      P:0x650004,Type:101,State:0,DeployMode:14,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x650008,Type:101,State:0,DeployMode:14,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x650019,Type:101,State:0,DeployMode:14,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x65002A,Type:101,State:0,DeployMode:14,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x650037,Type:101,State:0,DeployMode:14,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x670013,Type:103,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x6A0016,Type:106,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x78000F,Type:120,State:1,DeployMode:12,Ha:2,MainPID:0x0,CidHead:1,NoOnList
      CID:0x8078000F,Type:120,State:0,DeployMode:0,Ha:0
      P:0x780010,Type:120,State:1,DeployMode:12,Ha:2,MainPID:0x0,CidHead:1,NoOnList
      CID:0x80780010,Type:120,State:0,DeployMode:0,Ha:0
      P:0x780011,Type:120,State:1,DeployMode:12,Ha:2,MainPID:0x0,CidHead:1,NoOnList
      CID:0x80780011,Type:120,State:0,DeployMode:0,Ha:0
      P:0x7A0011,Type:122,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x8F0015,Type:143,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0xD5000E,Type:213,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x8078000F,Type:120,State:0,DeployMode:0,Ha:0,MainPID:0x78000F,CidHead:0,OnList
      P:0x80780010,Type:120,State:0,DeployMode:0,Ha:0,MainPID:0x780010,CidHead:0,OnList
      P:0x80780011,Type:120,State:0,DeployMode:0,Ha:0,MainPID:0x780011,CidHead:0,OnList

    Param:
      ParamNo               : 2
      CmdKey                : 6
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : ::
      Pid                   : 0x0
    Pid: 0x720016
      Cid        : 0x80720015
      P:0x650004,Type:101,State:1,DeployMode:14,Ha:2,MainPID:0x0,CidHead:0,NoOnList
      P:0x650008,Type:101,State:1,DeployMode:14,Ha:2,MainPID:0x0,CidHead:0,NoOnList
      P:0x650019,Type:101,State:1,DeployMode:14,Ha:2,MainPID:0x0,CidHead:0,NoOnList
      P:0x65002A,Type:101,State:1,DeployMode:14,Ha:2,MainPID:0x0,CidHead:0,NoOnList
      P:0x650037,Type:101,State:1,DeployMode:14,Ha:2,MainPID:0x0,CidHead:0,NoOnList
      P:0x670013,Type:103,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x6A0016,Type:106,State:1,DeployMode:1,Ha:2,MainPID:0x0,CidHead:0,NoOnList
      P:0x78000F,Type:120,State:1,DeployMode:12,Ha:2,MainPID:0x0,CidHead:1,NoOnList
      CID:0x8078000F,Type:120,State:0,DeployMode:0,Ha:0
      P:0x780010,Type:120,State:1,DeployMode:12,Ha:2,MainPID:0x0,CidHead:1,NoOnList
      CID:0x80780010,Type:120,State:0,DeployMode:0,Ha:0
      P:0x780011,Type:120,State:1,DeployMode:12,Ha:2,MainPID:0x0,CidHead:1,NoOnList
      CID:0x80780011,Type:120,State:0,DeployMode:0,Ha:0
      P:0x7A0011,Type:122,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x8F0015,Type:143,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0xD5000E,Type:213,State:0,DeployMode:1,Ha:0,MainPID:0x0,CidHead:0,NoOnList
      P:0x8078000F,Type:120,State:0,DeployMode:0,Ha:0,MainPID:0x78000F,CidHead:0,OnList
      P:0x80780010,Type:120,State:0,DeployMode:0,Ha:0,MainPID:0x780010,CidHead:0,OnList
      P:0x80780011,Type:120,State:0,DeployMode:0,Ha:0,MainPID:0x780011,CidHead:0,OnList

  (结果个数 = 2)
  ---    END
  ```
- 查询IPv6 Statistics信息：

  ```
  DSP IPV6INFO:IPV6QUERYTYPE=STATISTICS,IFQUERYTYPE=IFINDEX,IFINDEX=6;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据

    Param:
      ParamNo               : 4
      CmdKey                : 9
      IfIndex               : 6
      Param1                : 0
      Param2                : 0
      Addr                  : ::
      Pid                   : 0x0
    Pid: 0x72000f
      Cid        : 0x80720014
  Interface2(0x6):

    Param:
      ParamNo               : 4
      CmdKey                : 9
      IfIndex               : 6
      Param1                : 0
      Param2                : 0
      Addr                  : ::
      Pid                   : 0x0
    Pid: 0x720016
      Cid        : 0x80720015
  Interface2(0x6):

  (结果个数 = 2)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 查询结果数据  | 用来显示查询结果。 |