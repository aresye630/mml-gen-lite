# 查询Trunk内部数据（DSP TRUNKINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查看指定IFM组件TRUNK内部数据。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                                                                             |
|:------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE        | 查询内部数据类型 | 可选必选说明：必选参数 参数含义：该参数用来指定查询数据类型。 数据来源：本端规划 取值范围：枚举类型。 CFGADP：配置适配。TRUNKIF：聚合端口。TRUNKMEMBER：聚合成员接口。HA：聚合高可靠性状态。 默认值：无                                              |
| CID         | APP组件CID | 可选必选说明：必选参数 参数含义：该参数用来指定APP组件CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                             |
| IFQUERYTYPE | 接口查询类型   | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“CFGADP”、“TRUNKIF” 或 “TRUNKMEMBER”时为必选参数。 参数含义：该参数用来指定接口查询类型。 数据来源：本端规划 取值范围：枚举类型。 IFINDEX：接口索引。IFNAME：接口名称。 默认值：IFINDEX         |
| IFINDEX     | 接口索引     | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。 参数含义：该参数用来指定接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                           |
| IFNAME      | 接口名称     | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。 参数含义：该参数用于指定接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。 |

#### 使用实例

- 查询Trunk内部HA信息：

  ```
  DSP TRUNKINNERDATA: TYPE=HA, CID="0x807A0017";
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

           Com-Cid:  0x807a0017
          ================================================================================

          HA Global Info:
                  Stage      : Init
                  Batch list : Empty
                  Real list  : Empty
                  Timer      : Stopped

          (结果个数 = 2)
          ---    END
  ```
- 查询Trunk内部接口信息：

  ```
  DSP TRUNKINNERDATA: TYPE=TRUNKIF, CID="0x807A0017", IFQUERYTYPE=IFINDEX, IFINDEX=6;
  ```

  ```
          RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

          Com-Cid:  0x807a0017
          ================================================================================

          TrunkIf Info:
                  Trunk type   : Eth-Trunk
                  Work mode    : Invalid Mode
                  Trunk up min : 1
                  VRid         : 0
                  State        :
                          0->invalid, reasoncode 11
                          1->invalid, reasoncode 11
                  Member list  :
                  Down delay   :
                          Enable            : 0
                          DownDelayFlag     : 1
                          DownDelayInterval : 0
                          DownDelayOper     : 0
                          DownDelayState    : 2
                          StopDelayCB       : 0
                          DownDelayTimerId  : 4294967295

          Subscribe Info:
                  Producer of state level 0: None
                  Consumer of state level 0: None
                  Producer of state level 1: None
                  Consumer of state level 1:
                          1->Consumer ID 9, callBack 0x7f17ded76e90

          LinkQuality Info:
                  LinkQuality  : 0
                  Trunk up min : 1

          Bandwidth Info:
                  Trunk up max    : 4
                  Bandwidth       : 18446744073709551615
                  Max port speed  : 18446744073709551615
                  Working ifindex : 4294967295

          General Attribute Info:
                  0->Attribute find at 0x0
                  1->Attribute find at 0x0

          FesAdp Info:
                  Hash type  : 1
                  State      : invalid
                  Work state : 0
                  Active     : Y
                  Download   : N
                  Batch      : Y

          IfmAdp Info:
                  1->Infotype 46, notifyflag 1
                          *Callback 0x7f17ded81360, notifyflag 1, notifynull 0
                  2->Infotype 1063, notifyflag 1
                          *Callback 0x7f17ded75960, notifyflag 1, notifynull 0
                  3->Infotype 1082, notifyflag 1
                          *Callback 0x7f17ded75960, notifyflag 1, notifynull 0
                  4->Infotype 1105, notifyflag 1
                          *Callback 0x7f17ded74df0, notifyflag 1, notifynull 0

          (结果个数 = 8)
          ---    END
  ```
- 查询Trunk内部配置适配信息：

  ```
  DSP TRUNKINNERDATA: TYPE=CFGADP, CID="0x807A0017", IFQUERYTYPE=IFINDEX, IFINDEX=6;
  ```

  ```
           RETCODE = 0  操作成功。

           结果如下
          ------------------------
          查询结果数据

           Com-Cid:  0x807a0017
          ================================================================================

          CfgAdp Info:
                  Dam data with ifindex(6) not found.

          (结果个数 = 2)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 查询结果数据  | 用来显示查询结果数据。 |