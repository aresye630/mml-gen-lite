# 查询邻居表项详细信息（DSP NDNBVERBOSE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询邻居表项详细信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                             |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IFQUERYTYPE | 查询接口类型 | 可选必选说明：必选参数 参数含义：该参数用来指定接口查询类型。 数据来源：本端规划 取值范围：枚举类型。 IFINDEX：接口索引。IFNAME：接口名称。 默认值：无                                                                             |
| IFINDEX     | 接口索引   | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。 参数含义：该参数用来指定接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                           |
| IFNAME      | 接口名称   | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。 参数含义：该参数用于指定接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPV6ADDR    | IPv6地址 | 可选必选说明：必选参数 参数含义：该参数用于指定接口IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                                                                                 |

#### 使用实例

- 基于接口名查询邻居表项详细信息：

  ```
  DSP NDNBVERBOSE:IFQUERYTYPE=IFNAME,IFNAME="Ethernet64/0/3",IPV6ADDR="2001:db8::1";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  邻居表项详细信息  =
      uiIfIndex              : 6
      stNbAddr               : 2001:db8::1
      uiReachableTimeElapsed : 102278
      uiPreDetectReachTime   : 102278
      uiTimeStamp            : 10239029
      uiExpire               : 103478
      aucLLAddr              : 00E0-FC40-1504
      ucLLAddrFlag           : 1
      ucIsRouter             : 1
      ucState                : 1
      ucIsStaticEntry        : 0
      ucNsTimes              : 0
      ucNdMissFlag           : 0
      ucToBeDelete           : 0
      uiHaLastUpdateTime     : 0
      uiHaState              : 0
      uiHaTransNo            : 0
      ucMustNotifyFes        : 0
      ucNotifyFesNbState     : 1
      ucNdReqFlag            : 0
      uiNdReqTime            : 25313
      uiWorkIfIndex          : 0
      usVlanID               : 0
      uiVrIndex              : 0
      uiVrfindex             : 0
      uiIfPhyType            : 0
      uiParentIfPhyType      : 0
      uiIfLinkType           : 0
      uiIfEncapType          : 255
      uiFlowId               : 4294967295
      ucNetWorkRole          : 0
      linkinfo               : [
       ETH_INFO(TlvType = 0, TlvLength = 20, SrcMac = 00E0-FC40-1504, DstMac = 00E0-FC20-1504, IfIndex = 6, Priority = 0, Reserved = 0, Flag = 0)
       OTHER_INFO(TlvType = 255, TlvLength = 16)
      ]

  (结果个数 = 1)
  ---    END
  ```
- 基于接口索引查询邻居表项详细信息：

  ```
  DSP NDNBVERBOSE:IFQUERYTYPE=IFINDEX,IFINDEX=6,IPV6ADDR="2001:db8::1";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  邻居表项详细信息  =
      uiIfIndex              : 6
      stNbAddr               : 2001:db8::1
      uiReachableTimeElapsed : 102278
      uiPreDetectReachTime   : 102278
      uiTimeStamp            : 10359054
      uiExpire               : 104678
      aucLLAddr              : 00E0-FC40-1504
      ucLLAddrFlag           : 1
      ucIsRouter             : 1
      ucState                : 2
      ucIsStaticEntry        : 0
      ucNsTimes              : 0
      ucNdMissFlag           : 0
      ucToBeDelete           : 0
      uiHaLastUpdateTime     : 0
      uiHaState              : 0
      uiHaTransNo            : 0
      ucMustNotifyFes        : 0
      ucNotifyFesNbState     : 1
      ucNdReqFlag            : 0
      uiNdReqTime            : 25313
      uiWorkIfIndex          : 0
      usVlanID               : 0
      uiVrIndex              : 0
      uiVrfindex             : 0
      uiIfPhyType            : 0
      uiParentIfPhyType      : 0
      uiIfLinkType           : 0
      uiIfEncapType          : 255
      uiFlowId               : 4294967295
      ucNetWorkRole          : 0
      linkinfo               : [
       ETH_INFO(TlvType = 0, TlvLength = 20, SrcMac = 00E0-FC40-1504, DstMac = 00E0-FC20-1504, IfIndex = 6, Priority = 0, Reserved = 0, Flag = 0)
       OTHER_INFO(TlvType = 255, TlvLength = 16)
      ]

  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称    | 输出项解释              |
|:---------|:-------------------|
| 邻居表项详细信息 | 用于显示查询得到的邻居表项详细信息。 |