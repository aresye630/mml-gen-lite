# 查询接口诊断数据（DSP IFDIAGDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询IFM诊断数据信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE        | 诊断数据类型   | 可选必选说明：必选参数 参数含义：该参数用来指定IFM的诊断数据类型。 数据来源：本端规划 取值范围：枚举类型。 SENDMESSAGE：已发送消息。SWITCHOVERMSG：平滑阶段发送的消息。IFINFO：接口信息。SUBSCRIB_INFO：接口订阅信息。ERROR_MESSAGE：从其他业务组件收到错误消息。COMPONENT_INFO：Partner组件信息。PRODUCER_INFO：生产者信息。CONSUMER_INFO：消费者信息。AM4_STATE_MACHINE：IPv4地址管理状态机信息。AM4_LOCAL_TREE：IPv4地址管理本地地址树信息。AM4_CONFLICT_TREE：IPv4地址管理冲突地址树信息。AM4_REMOTE_TREE：IPv4地址管理远端地址树信息。AM4_WAIT_TREE：IPv4地址管理等待地址树信息。AM6_SERVICE_INFO_IFID：IPv6地址管理按接口IFID查询服务信息。AM6_SERVICE_INFO_DAD：IPv6地址管理按DAD查询服务信息。AM6_LOCAL_TREE：IPv6地址管理本地地址树信息。AM6_CONFLICT_TREE：IPv6地址管理冲突地址树信息。AM6_STATE_MACHINE：IPv6地址管理状态机信息。TMP_SERVICE_TREE：设备管理临时服务树信息。MESSAGE_COUNT：接收的消息计数。RECV_ERR_IFINFO：接收到的错误接口信息。INTERFACE_SRV：接口服务信息。PARTNER_STATE：Partner组件的状态。ADMIN_IF_INFO：管理网口信息。 默认值：无 配置原则：当参数TYPE配置为SENDMESSAGE或SWITCHOVERMSG时，IFINDEX，IFINFOTYPE和PID必须至少配置其中一个参数。 |
| IFINFOTYPE  | 接口信息类型   | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“SENDMESSAGE” 或 “SWITCHOVERMSG”时为可选参数。 参数含义：该参数用来指定接口信息类型。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65535。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IFQUERYTYPE | 接口查询类型   | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“IFINFO”、“SUBSCRIB_INFO” 或 “INTERFACE_SRV”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“AM4_LOCAL_TREE”、“AM4_CONFLICT_TREE”、“AM4_REMOTE_TREE”、“AM4_WAIT_TREE”、“AM6_SERVICE_INFO_IFID” 或 “AM6_SERVICE_INFO_DAD”时为可选参数。 参数含义：该参数用来指定接口查询类型。 数据来源：本端规划 取值范围：枚举类型。 IFINDEX：接口索引。IFNAME：接口名称。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| IFINDEX     | 接口索引     | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“SENDMESSAGE” 或 “SWITCHOVERMSG”时为可选参数。 参数含义：该参数用来指定接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IFNAME      | 接口名称     | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。 参数含义：该参数用于指定接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PID         | APP组件PID | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“COMPONENT_INFO”、“MESSAGE_COUNT” 或 “PARTNER_STATE”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“SENDMESSAGE” 或 “SWITCHOVERMSG”时为可选参数。 参数含义：该参数用来指定APP组件PID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ISSLAVE     | 是否备用资源单元 | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“SENDMESSAGE”、“SWITCHOVERMSG”、“IFINFO”、“SUBSCRIB_INFO”、“ERROR_MESSAGE”、“COMPONENT_INFO”、“PRODUCER_INFO” 或 “CONSUMER_INFO”时为可选参数。 参数含义：该参数用来指定是否为备用资源单元。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

#### 使用实例

- 查询IFM接口信息：

  ```
  DSP IFDIAGDATA:TYPE=IFINFO,IFQUERYTYPE=IFNAME,IFNAME="Gi0/0/1";
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

          IfInfo:IfIndex(1)         Value(HEX):00000004

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:IfName(2)          Value(HEX):61676947

          45746962 72656874 3074656E 312F302F 00000000 00000000 00000000
              00000000
          00000000 00000000 00000000 00000000 00000000 00000000 00000000

            Value:GigabitEthernet0/0/1

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x440058

          IfInfo:LinkType(3)        Value(HEX):00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PhyType(4)         Value(HEX):0000004F

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:Mtu(5)             Value(HEX):000005DC

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:V4State(6)         Value(HEX):00000001 00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:V6State(7)         Value(HEX):00000000 00000002

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:State(8)           Value(HEX):00000001 00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:Bw(9)              Value(HEX):540BE400 00000002

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:DF(15)             Value(HEX):00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:VrfId(16)          Value(HEX):00000002

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:RouterType(18)     Value(HEX):00000002

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:Mtu6(24)           Value(HEX):00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:IfGroupId(28)      Value(HEX):80000004

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PortGroupId(30)    Value(HEX):FFFF0001

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PhyState(2001)     Value(HEX):00000001 00000000 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:LinkState(2002)    Value(HEX):00000001 00000001 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PhyMac(2005)       Value(HEX):15041600 00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:Mac(2006)          Value(HEX):15041600 00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:CfgMtu(2007)       Value(HEX):000005DC

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:CfgMtu6(60004)     Value(HEX):00000000

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PhyUpTime(60005)   Value(HEX):160C07E0 70051B14

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:LinkUpTime(60007)  Value(HEX):160C07E0 70051B14

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:V4StateUpTime(60009) Value(HEX):160C07E0 70051B14

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:ServiceType(46)    Value(HEX):00000004

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:AlarmFlag(60017)   Value(HEX):00000001 00000000 00000001

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:AdminState(60021)  Value(HEX):00000001 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PhyStateSrc(1033)  Value(HEX):00000001 00000000 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PortLinkStateSrc(1094) Value(HEX):00000001 00000001 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:LinkStateSrc(1031) Value(HEX):00000001 00000001 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PortLinkState(2009) Value(HEX):00000001 00000001 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:PortPhyState(2008) Value(HEX):00000001 00000000 00000015

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:IfId(25)           Value(HEX):FF041602 000015FE

            Producer Pid:0x807A0016 InstId:0  Area:0   InnerPid:0x0

          IfInfo:ManageIfActive(60019) Value(HEX):00000005 FFFFFFFF

            Producer Pid:0x807A0016 InstId:0  Area:0  [Addr:0x800A23DC]

          IfInfo:V4Addr(10)         Value(HEX):BD110001 00010010 00000000

            Producer Pid:0x807A0016 InstId:0  Area:0  [Addr:0x9C5A1F7C]

          IfInfo:IsolationState(60052) Value(HEX):00000001 0000002D

            Producer Pid:0x807A0016 InstId:0  Area:0  [Addr:0x9C5A53BC]

          (结果个数 = 75)
          ---    END
  ```
- 查询IFM Partner组件信息：

  ```
  DSP IFDIAGDATA:TYPE=COMPONENT_INFO,PID="0x650030";
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据 =  IFM State:Running         [LOCAL Addr:7f47091c6240]
          Consumer Pid:0x650030   InstId:0  Area:0  State:Register  [Addr:7f46d7d13be4]
            ErrMsgCnt:0

          Producer Info:

          Consumer Info:

          (结果个数 = 1)
          ---    END
  ```
- 查询IFM生产者信息：

  ```
  DSP IFDIAGDATA:TYPE=PRODUCER_INFO;
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

          IFM FSM  Pid:0x7A000F   State:Running
                  State History:
                          2017-02-28 18:55:18.923 Start
                          2017-02-28 18:55:18.923 CollSvc
                          2017-02-28 18:55:19.744 CollDat
                          2017-02-28 18:58:15.329 Running
          Producer Pid:0x740022   State:Running     [Addr:7f46d69dd620]
                  2017-02-28 18:55:19.785 Start
                          2017-02-28 18:55:19.786 Register
                          2017-02-28 18:55:19.786 CollSvc
                          2017-02-28 18:55:19.787 CollDat

                          2017-02-28 18:55:19.787 Running
          Producer Pid:0xFB0005   State:Running     [Addr:7f46d69dd6f4]
                  2017-02-28 18:55:18.924 Start
                          2017-02-28 18:55:19.757 CollDat
                          2017-02-28 18:58:15.329 Running

          (结果个数= 2)
          ---    END
  ```
- 查询IFM消费者信息：

  ```
  DSP IFDIAGDATA:TYPE=CONSUMER_INFO;
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

          Consumer Pid:0x740022   InstId:0          Area:0          State:Register
            [Addr:7f46d7d130e4]
                  State History:
                          2017-02-28 18:55:19.786 Register
          Consumer Pid:0x650009   InstId:0          Area:0          State:Register
            [Addr:7f46d7d13194]
                  State History:
                          2017-02-28 18:55:19.808 Register
          Consumer Pid:0xD5000D   InstId:0          Area:0          State:Register
            [Addr:7f46d7d13244]
                  State History:
                          2017-02-28 18:55:19.808 Register
          Consumer Pid:0x77000A   InstId:0          Area:0          State:Running

            [Addr:7f46d7d132f4]
                  State History:
                          2017-02-28 18:55:19.808 Register
                          2017-02-28 18:55:21.887 Running
          Consumer Pid:0x660012   InstId:0          Area:0          State:Running
            [Addr:7f46d7d133a4]
                  State History:
                          2017-02-28 18:55:19.808 Register
                          2017-02-28 19:16:18.933 Running
          Consumer Pid:0xA60027   InstId:0          Area:0          State:Running
            [Addr:7f46d7d13454]
                  State History:
                          2017-02-28 18:55:19.808 Register

                          2017-02-28 18:55:19.941 Running
          Consumer Pid:0x69002E   InstId:6881326    Area:0          State:Running
            [Addr:7f46d7d13504]
                  State History:
                          2017-02-28 18:55:19.808 Register
                          2017-02-28 18:55:24.794 Running
          Consumer Pid:0x260006   InstId:0          Area:0          State:Register
            [Addr:7f46d7d135b4]
                  State History:
                          2017-02-28 18:55:19.883 Register
          Consumer Pid:0x650005   InstId:0          Area:0          State:Register
            [Addr:7f46d7d13664]
                  State History:

                          2017-02-28 18:55:19.883 Register
          Consumer Pid:0x650018   InstId:0          Area:0          State:Running
            [Addr:7f46d7d13714]
                  State History:
                          2017-02-28 18:55:19.883 Register
                          2017-02-28 19:36:19.493 Running
          Consumer Pid:0x92002B   InstId:0          Area:0          State:Running
            [Addr:7f46d7d137c4]
                  State History:
                          2017-02-28 18:55:19.883 Register
                          2017-02-28 18:55:22.879 Running
          Consumer Pid:0x93002C   InstId:0          Area:0          State:Running

            [Addr:7f46d7d13874]
                  State History:
                          2017-02-28 18:55:19.883 Register
                          2017-02-28 18:55:22.879 Running
          Consumer Pid:0x210003   InstId:0          Area:0          State:Register
            [Addr:7f46d7d13924]
                  State History:
                          2017-02-28 18:55:19.887 Register
          Consumer Pid:0x220001   InstId:0          Area:0          State:Running
            [Addr:7f46d7d139d4]
                  State History:
                          2017-02-28 18:55:19.887 Register
                          2017-02-28 18:55:22.193 Running

          Consumer Pid:0x6F0002   InstId:0          Area:0          State:Running
            [Addr:7f46d7d13a84]
                  State History:
                          2017-02-28 18:55:19.887 Register
                          2017-02-28 18:55:22.193 Running
          Consumer Pid:0x700004   InstId:0          Area:0          State:Register
            [Addr:7f46d7d13b34]
                  State History:
                          2017-02-28 18:55:19.887 Register
          Consumer Pid:0x650030   InstId:0          Area:0          State:Register
            [Addr:7f46d7d13be4]
                  State History:
                          2017-02-28 18:55:19.887 Register

          Consumer Pid:0x670011   InstId:0          Area:0          State:Running
            [Addr:7f46d7d13c94]
                  State History:
                          2017-02-28 18:55:24.931 Register
                          2017-02-28 18:59:54.954 Running

          (结果个数 = 7)
          ---    END
  ```
- 查询IFM IPv4地址管理状态机信息：

  ```
  DSP IFDIAGDATA:TYPE=AM4_STATE_MACHINE;
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据 =    AM4 State:Proc End
          (结果个数 = 1)
          ---    END
  ```
- 查询IFM IPv4本地地址树信息：

  ```
  DSP IFDIAGDATA:TYPE=AM4_LOCAL_TREE,IFQUERYTYPE=IFINDEX,IFINDEX=4;
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据  =
          NetAddr/Mask:192.168.0.0/16
          IpAddr/Mask:192.168.0.1/16 AddrType:MainAddr, IfIndex:4, BrwIfIndex:0

          NetAddr/Mask:192.168.0.1/32
          IpAddr/Mask:192.168.0.1/16 AddrType:MainAddr, IfIndex:4, BrwIfIndex:0

          (结果个数 = 1)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释           |
|:--------|:----------------|
| 查询结果数据  | 用来显示IFM的查询结果数据。 |