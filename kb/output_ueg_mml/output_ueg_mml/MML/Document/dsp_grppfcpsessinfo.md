# 显示PFCP的组会话信息（DSP GRPPFCPSESSINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SMF**

该命令用于显示PFCP的组会话信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                   |
|:-------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSPINFOTYPE  | 信息呈现方式     | 可选必选说明：必选参数  参数含义：该参数用于指定信息呈现方式，“简约信息呈现”显示指定5G Lan组里的会话标识，“详细信息呈现”显示全部或指定规则、隧道、会话等相关信息。  数据来源：本端规划 取值范围： SIMPLE（简约信息呈现）DETAILED（详细信息呈现）  默认值：无  配置原则：无                                                                                                                                                                                                                 |
| QUERYTYPE    | 查询方式       | 可选必选说明：该参数在"DSPINFOTYPE"配置为"SIMPLE"时为条件必选参数。  参数含义：该参数用于指定查询方式，通常以指定5G Lan组ID的方式查询会话标识。  数据来源：本端规划 取值范围： NGLANGROUPID（5G LAN组ID）  默认值：无  配置原则：无                                                                                                                                                                                                                        |
| NGLANGROUPID | 5G LAN组的ID | 可选必选说明：该参数在"QUERYTYPE"配置为"NGLANGROUPID"时为条件必选参数。  参数含义：该参数用于指定5G LAN组的ID。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是18~37。  默认值：无  配置原则：  NGLANGROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |
| DETAILTYPE   | 详单类型       | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。  参数含义：该参数用于指定显示的详单类型，通常查询全部或指定的PFCP会话的相关信息，也可查询全部或指定的规则、隧道相关信息。  数据来源：本端规划 取值范围： PDR（包探测规则）FAR（包转发规则）VNGMURR（VNGM创建的使用上报规则）TUNNEL（传输业务流量的通道）PFCPSESSION（PFCP会话）  默认值：无  配置原则：无                                                                                                                                          |
| CPSEID       | C面的会话端点标识  | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。  参数含义：该参数用于指定C面分配的单一会话标识，可通过SIMPLE方式查询指定5G Lan组ID获得。  数据来源：本端规划  取值范围：整数类型，取值范围是0~9223372036854775807。  默认值：无  配置原则：无                                                                                                                                                                                                   |
| PDRID        | PDR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"时为条件可选参数。  参数含义：该参数用于指定某一个PDR规则，可通过DETAILED方式查询PDR详单类型获得。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无                                                                                                                                                                                                                            |
| FARID        | FAR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"FAR"时为条件可选参数。  参数含义：该参数用于指定某一个FAR规则，可通过DETAILED方式查询FAR详单类型获得。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                                                                                       |
| URRID        | URR标识      | 可选必选说明：该参数在"DETAILTYPE"配置为"VNGMURR"时为条件可选参数。  参数含义：该参数用于指定某一个URR规则，可通过DETAILED方式查询VNGMURR详单类型获得。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                                                                               |

## 使用实例

- 查询指定GroupID的组会话上的PFCP会话信息，执行具体如下：

  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=SIMPLE, QUERYTYPE=NGLANGROUPID, NGLANGROUPID="a0000001-460-03-01";%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
         5G LAN组ID  =  a0000001-460-03-01
       UP的实例标识  =  upf_instance_1
  C面的会话端点标识  =  140752789241857
   对端网元的IP地址  =  192.168.0.1
  (结果个数 = 1)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话信息，执行具体如下：

  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=PFCPSESSION, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
  	   5G LAN组ID  =  a0000001-460-03-01
  	 UP的实例标识  =  upf_instance_1
      C面的会话端点标识  =  140752789241857
      U面的会话端点标识  =  2
                PDR列表  =  4097 8194 16387
                FAR列表  =  1075838977 1074790402 1077936131
                URR列表  =  NULL
                POD名称  =  uncpod-0
       对端网元的IP地址  =  192.168.0.1
  (结果个数 = 1)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话的隧道信息（当前仅有N19的隧道信息），执行具体如下：

  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=TUNNEL, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
             隧道类型  =  TunnelTypeN19
             隧道TEID  =  10
             IPv4地址  =  10.0.0.1
             IPv6地址  =  ::
  (结果个数 = 1)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话的PDR信息（可指定PDR ID），执行具体如下：

  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=PDR, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
  PDR标识    PDR类型        PDR优先级      PDR方向		    关联的URR列表   关联的FAR标识    本端接口类型  

  4097       PdrTypeN6Dl    4294967295     Unidirectional Downlink    1075838977      NULL             UpItfTypeN6           
  8194       PdrTypeN6Ul    4294967295     Unidirectional Uplink      1074790402      NULL             UpItfTypeInvalid      
  16387      PdrTypeN19Dl   4294967295     Unidirectional Downlink    1077936131      NULL             UpItfTypeN19          
  (结果个数 = 3)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话的FAR信息（可指定FAR ID），执行具体如下：

  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=FAR, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
  FAR标识        FAR类型         对端接口类型         FAR应用动作  

  1075838977     FarTypeN6Dl     UpItfTypeInvalid     Forw              
  1074790402     FarTypeN6Ul     UpItfTypeN6          Forw              
  1077936131     FarTypeN19Dl    UpItfTypeInvalid     Forw              
  (结果个数 = 3)

  ---    END
  ```

## 输出结果说明

| 输出项名称      | 输出项解释                                                                        |
|:-----------|:-----------------------------------------------------------------------------|
| 5G LAN组的ID | 该参数用于指定5G LAN组的ID。                                                           |
| UP实例标识     | 该参数用于指定UP的实例标识。                                                              |
| C面的会话端点标识  | 该参数用于指定C面分配的单一会话标识，可通过SIMPLE方式查询指定5G Lan组ID获得。                               |
| U面的会话端点标识  | 该参数用于指定U面分配的单一会话标识。                                                          |
| PDR列表      | 该参数用于显示所有符合筛选条件的PDR标识。                                                       |
| FAR列表      | 该参数用于显示所有符合筛选条件的FAR标识。                                                       |
| URR列表      | 该参数用于显示所有符合筛选条件的URR标识。                                                       |
| POD名称      | 该参数用于显示POD名称。                                                                |
| 隧道类型       | 该参数用于指定隧道方式。                                                                 |
| 隧道端点标识     | 该参数用于指定两个网元之间的一段隧道。                                                          |
| 隧道IPv4     | 该参数用于指定N19隧道IPv4地址。                                                          |
| 隧道IPv6     | 该参数用于指定N19隧道IPv6地址。                                                          |
| PDR标识      | 该参数用于指定某一个PDR规则，可通过DETAILED方式查询PDR详单类型获得。                                    |
| PDR类型      | 该参数用于显示PDR类型。                                                                |
| PDR优先级     | 该参数用于显示PDR在PFCP会话的所有PDRs中应用的优先级。                                             |
| PDR方向      | 该参数用于显示数据包来源的方向。 取值说明： PDRDIRINVALID（无效）PDRDIRUL（单向上行）PDRDIRDL（单向下行）         |
| 关联的FAR标识   | 该参数用于显示关联特定PDR的FAR标识。                                                        |
| 关联的URR列表   | 该参数用于显示关联特定PDR的所有URR标识。                                                      |
| 本端接口类型     | 该参数用于显示数据包接收来源的接口类型，包括Core、Access、SGi-LAN/N6-LAN、CP-function、5G Vn Internal。 |
| FAR标识      | 该参数用于指定某一个FAR规则，可通过DETAILED方式查询FAR详单类型获得。                                    |
| FAR类型      | 该参数用于显示FAR类型。                                                                |
| 对端接口类型     | 该参数用于显示数据包转发目标的接口类型，包括Core、Access、SGi-LAN/N6-LAN、CP-function、5G Vn Internal。 |
| FAR应用动作    | 该参数用于显示对数据包应用的动作，如转发、缓存、丢弃等。                                                 |
| URR标识      | 该参数用于指定某一个URR规则，可通过DETAILED方式查询VNGMURR详单类型获得。                                |
| URR类型      | 该参数用于显示URR类型。                                                                |
| 测量方法       | 该参数用于显示测量网络资源使用的方法。                                                          |
| 上报触发器      | 该参数用于显示触发UPF上报SMF的事件。                                                        |
| 对端网元的IP地址  | 该参数用于显示5G LAN组会话对端网元的IP地址。                                                   |