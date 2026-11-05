# 显示PFCP会话信息（DSP PFCPSESSIONINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示PFCP的会话信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                                                                                                              |
|:------------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSPINFOTYPE | 信息呈现方式     | 可选必选说明：必选参数  参数含义：该参数用于指定信息呈现方式。  数据来源：本端规划 取值范围： SIMPLE（简约信息呈现）DETAILED（详细信息呈现）  默认值：无  配置原则：无                                                                                                   |
| QUERYTYPE   | 查询方式       | 可选必选说明：该参数在"DSPINFOTYPE"配置为"SIMPLE"时为条件必选参数。  参数含义：该参数用于指定查询方式。  数据来源：本端规划 取值范围： IMSI（用户IMSI号）  默认值：IMSI  配置原则：无                                                                                  |
| IMSI        | IMSI       | 可选必选说明：该参数在"DSPINFOTYPE"配置为"SIMPLE"时为条件必选参数。  参数含义：该参数用于指定用户永久标识或者国际移动用户标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~15。  默认值：无  配置原则：无                                                                    |
| DETAILTYPE  | 详单类型       | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。  参数含义：该参数用于指定显示的详单类型。  数据来源：本端规划 取值范围： PDR（PDR）FAR（FAR）BAR（BAR）UPCURR（UPC创建的URR）QER（QER）TUNNEL（Tunnel）PFCPSESSION（PFCP会话）  默认值：PFCPSESSION  配置原则：无 |
| CPSEID      | CP的Seid    | 可选必选说明：该参数在"DETAILTYPE"配置为"PFCPSESSION"、"PDR"、"FAR"、"QER"、"BAR"、"UPCURR"、"TUNNEL"时为条件必选参数。  参数含义：该参数用于指定CP的Seid。  数据来源：本端规划  取值范围：整数类型，取值范围是0~9223372036854775807。  默认值：无  配置原则：无                 |
| PDRID       | PDR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"时为条件可选参数。  参数含义：该参数用于显示PDR标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无                                                                                   |
| FARID       | FAR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"FAR"时为条件可选参数。  参数含义：该参数用于显示FAR标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                              |
| QERID       | QER标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"QER"时为条件可选参数。  参数含义：该参数用于显示QER标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                              |
| URRID       | URR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"UPCURR"时为条件可选参数。  参数含义：该参数用于显示URR标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                           |
| BEARERNO    | Bearer标识   | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"、"FAR"、"QER"、"UPCURR"、"TUNNEL"时为条件可选参数。  参数含义：该参数用于显示Bearer标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无                                                  |
| BARID       | BAR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"BAR"时为条件可选参数。  参数含义：该参数用于显示BAR标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~255。  默认值：无  配置原则：无                                                                                     |
| QFI         | QFI        | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"、"FAR"、"QER"、"UPCURR"时为条件可选参数。  参数含义：该参数用于显示QFI。  数据来源：本端规划  取值范围：整数类型，取值范围是0~255。  默认值：无  配置原则：无                                                                  |
| PCCRULEID   | PCC Rule标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"、"FAR"、"QER"时为条件可选参数。  参数含义：该参数用于显示PCC Rule标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无                                                                  |

## 使用实例

- 查询类型为IMSI，查询方式为简单查询，IMSI为123035000100001：

  ```
  %%DSP PFCPSESSIONINFO: DSPINFOTYPE=SIMPLE, QUERYTYPE=IMSI, IMSI="123032111110001";%%
  RETCODE = 0  操作成功

  Pfcpsession Info
  ----------------
                   IMSI  =  123035000100001
            PDU会话标识  =  5
        链接的EPS承载ID  =  0
               CP的Seid  =  8070591282084708358
                 UP角色  =  Access|MainAnchor|5g|BySmfN11
             UP实例标识  =  upf_instance_1
           PFCP会话状态  =  正常
  (结果个数 = 1)

  ---    END
  ```
- 查询类型为TUNNEL，查询方式为详细查询，CPSEID为8070591282084708358的PFCP会话信息，CPSEID可使用本命令的简单查询获得：

  ```
  %%DSP PFCPSESSIONINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=TUNNEL, CPSEID=8070591282084708358;%%
  RETCODE = 0  操作成功

  Pfcpsession Info
  ----------------
  Bearer标识     隧道类型    隧道TEID       IPv4地址       IPv6地址    

  0              1            10           0.0.0.0       2001:db8:0:1:1:1:1:1
  0              2            2            10.0.0.1      ::                  
  0              28           2154692610   10.0.1.1      ::                  
  0              29           11           10.0.2.1      ::                  
  (Number of results = 4)

  ---    END
  ```
- 查询类型为PDR，查询方式为详细查询，CPSEID为8070591282084708358的PFCP会话信息，CPSEID可使用本命令的简单查询获得：

  ```
  %%DSP PFCPSESSIONINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=PDR, CPSEID=8070591282084708358;%%
  RETCODE = 0  操作成功

  Pfcpsession Info
  ----------------
  PDR标识   本端接口类型     PDR类型   PDR优先级     PDR方向                  PCC Rule标识  Bearer标识   QFI   关联的FAR标识   关联的URR列表   关联的QER列表          是否IMS信令  关联的APP标识  

  1025      UpIfTypeN3Upf    1         4294967295    Bidirectional Uplink     65535         0            0     540016641       NULL            1895825408             FALSE        NULL           
  2050      UpIfTypeN9c      2         4294967295    Bidirectional Downlink   65535         0            0     541065218       NULL            1895825408             FALSE        NULL           
  9219      UpIfTypeN3Upf    9         0             Unidirectional Uplink    65535         2            2     547356675       NULL            1929379842             FALSE        NULL           
  10244     UpIfTypeN9c      10        0             Unidirectional Downlink  65535         2            2     548405252       NULL            1929379842             FALSE        NULL           
  9221      UpIfTypeN3Upf    9         0             Unidirectional Uplink    65535         1            1     547356677       NULL            1929379841 1895825408  FALSE        NULL           
  10246     UpIfTypeN9c      10        0             Unidirectional Downlink  65535         1            1     548405254       NULL            1929379841 1895825408  FALSE        NULL           
  (Number of results = 6)

  ---    END
  ```

## 输出结果说明

| 输出项名称          | 输出项解释                                                                                           |
|:---------------|:------------------------------------------------------------------------------------------------|
| IMSI           | 该参数用于指定用户永久标识或者国际移动用户标识。                                                                        |
| PDU会话标识        | 该参数用于显示PDU会话标识。                                                                                 |
| 链接的EPS承载ID     | 该参数用于显示链接的EPS承载ID。                                                                              |
| CP的Seid        | 该参数用于指定CP的Seid。                                                                                 |
| PDR标识          | 该参数用于显示PDR标识。                                                                                   |
| FAR标识          | 该参数用于显示FAR标识。                                                                                   |
| QER标识          | 该参数用于显示QER标识。                                                                                   |
| QER类型          | 该参数用于显示QER类型。                                                                                   |
| 本端接口类型         | 该参数用于显示本端接口类型。                                                                                  |
| FAR类型          | 该参数用于显示FAR类型。                                                                                   |
| FAR应用动作        | 该参数用于显示FAR应用动作。                                                                                 |
| PDR类型          | 该参数用于显示PDR类型。                                                                                   |
| PDR优先级         | 该参数用于显示PDR优先级。                                                                                  |
| PDR方向          | 该参数用于显示PDR方向。 取值说明： PDRDIRINVALID（无效）PDRDIRU（单向上行）PDRDIRD（单向下行）PDRDIRBIDU（双向上行）PDRDIRBIDD（双向下行） |
| UP角色           | 该参数用于显示UP的角色信息。                                                                                 |
| UP实例标识         | 该参数用于指定UP的实例标识。                                                                                 |
| PFCP会话状态       | 该参数用于显示PFCP会话状态。 取值说明： PFCPNORMAL（正常）PFCPDEL（待删除）                                               |
| UP会话标识         | 该参数用于指定UP的会话标识。                                                                                 |
| 会话建立时间         | 该参数用于显示PFCP会话建立时间。                                                                              |
| UP的Seid        | 该参数用于显示UP的Seid。                                                                                 |
| CP的节点标识        | 该参数用于显示CP的节点标识。                                                                                 |
| UP的节点标识        | 该参数用于显示UP的节点标识。                                                                                 |
| CP的PFCP IP地址   | 该参数用于显示CP的PFCP IP地址。                                                                            |
| CP的PFCP端口号     | 该参数用于显示CP的PFCP端口号。                                                                              |
| UP的PFCP IP地址   | 该参数用于指定UP的PFCP IP地址。                                                                            |
| UP的PFCP端口号     | 该参数用于显示UP的PFCP端口号。                                                                              |
| Bearer标识列表     | 该参数用于显示Bearer标识列表。                                                                              |
| QoS Flow列表     | 该参数用于显示QoS Flow列表。                                                                              |
| PCC Rule标识     | 该参数用于显示PCC Rule标识。                                                                              |
| PCC Rule标识列表   | 该参数用于显示Pcc Rule ID列表。                                                                           |
| PDR列表          | 该参数用于显示PDR列表。                                                                                   |
| QER列表          | 该参数用于显示QER列表。                                                                                   |
| UPC分配的URR列表    | 该参数用于显示UPC分配的URR列表。                                                                             |
| FAR列表          | 该参数用于显示FAR列表。                                                                                   |
| BAR列表          | 该参数用于显示BAR列表。                                                                                   |
| 已经创建的URR列表     | 该参数用于显示已经下发到UPF的URR列表。                                                                          |
| 是否支持DCNR功能     | 该参数用于显示是否支持DCNR功能。 取值说明： TRUE(TRUE)FALSE(FALSE)                                                 |
| URR标识          | 该参数用于显示URR标识。                                                                                   |
| URR类型          | 该参数用于显示URR类型。                                                                                   |
| Bearer标识       | 该参数用于显示Bearer标识。                                                                                |
| BAR标识          | 该参数用于显示BAR标识。                                                                                   |
| QFI            | 该参数用于显示QFI。                                                                                     |
| 关联的FAR标识       | 该参数用于显示关联的FAR标识。                                                                                |
| 关联的URR列表       | 该参数用于显示关联的URR列表。                                                                                |
| 关联的QER列表       | 该参数用于显示关联的QER列表。                                                                                |
| 是否IMS信令        | 该参数用于显示是否IMS信令。 取值说明： TRUE(TRUE)FALSE(FALSE)                                                    |
| 关联的APP标识       | 该参数用于显示关联的APP标识。                                                                                |
| 关联的BAR标识       | 该参数用于显示关联的BAR标识。                                                                                |
| 关联的TCR标识       | 该参数用于显示关联的TCR标识。                                                                                |
| 关联的原始PCC QoS标识 | 该参数用于显示关联的原始PCC QoS标识。                                                                          |
| 对端接口类型         | 该参数用于显示对端接口类型。                                                                                  |
| 外部头IP地址类型      | 该参数用于显示外部头IP地址类型。 取值说明： INVALID（无效值）IPV4（IPv4）IPV6（IPv6）IPV4IPV6（IPV4IPV6）                      |
| Dscp           | 该参数用于显示Dscp值。                                                                                   |
| 门控开关           | 该参数用于显示门控开关。                                                                                    |
| MBR上行速率        | 该参数用于显示MBR上行速率。                                                                                 |
| MBR下行速率        | 该参数用于显示MBR下行速率。                                                                                 |
| GBR上行速率        | 该参数用于显示GBR上行速率。                                                                                 |
| GBR下行速率        | 该参数用于显示GBR下行速率。                                                                                 |
| 是否反射QoS        | 该参数用于显示是否反射QoS。 取值说明： TRUE(TRUE)FALSE(FALSE)                                                    |
| 平均窗口           | 该参数用于显示平均窗口值。                                                                                   |
| 上行包速率          | 该参数用于显示上行包速率。                                                                                   |
| 下线包速率          | 该参数用于显示下线包速率。                                                                                   |
| 测量方法           | 该参数用于显示测量方法。                                                                                    |
| 报告触发器          | 该参数用于显示报告触发器。                                                                                   |
| 扩展报告触发器        | 该参数用于显示扩展报告触发器。                                                                                 |
| 空闲定时器时长        | 该参数用于显示空闲定时器时长。                                                                                 |
| DDN时延          | 该参数用于显示DDN时延。                                                                                   |
| 建议的缓冲数据包个数     | 该参数用于显示建议的缓冲数据包个数。                                                                              |
| 隧道类型           | 该参数用于指定隧道方式。                                                                                    |
| 隧道TEID         | 该参数用于指定隧道Teid。                                                                                  |
| IPv4地址         | 该参数用于指定隧道IPv4地址。                                                                                |
| IPv6地址         | 该参数用于指定隧道IPv6地址。                                                                                |
| 已下发的预定义规则      | 该参数用于指定已下发的预定义规则。                                                                               |
| POD名称          | 该参数用于显示POD名称。                                                                                   |