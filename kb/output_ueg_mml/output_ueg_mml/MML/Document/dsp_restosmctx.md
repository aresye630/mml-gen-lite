# 显示容灾用户SM上下文信息（DSP RESTOSMCTX）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

#### 命令功能

**适用网元：MME**

- 本命令用于查询系统内容灾用户的SM上下文信息。
- 输出结果分为SM User上下文、SM PDN上下文、SM PDP上下文等报表。
- 当某一字段显示“NULL”时，表示该字段没有备份。

#### 注意事项

- 输出结果中包含用户的某些个人数据，例如IMSI、IMEI、PDP地址等信息。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。
- 由于无卡用户无签约数据，因此“查询条件”为“IMEI（指定IMEI）”时，按Context ID查询失败显示。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                     |
|:--------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QRYTP         | 查询方式            | 可选必选说明：可选参数 参数含义：该参数用于指定查询承载上下文的方式。 取值范围：“IMSI（指定IMSI）”“STMSI（指定S-TMSI）”“IMEI（指定IMEI）” 默认值：IMSI  说明： 根据IMEI查询仅适用于无卡的紧急呼叫用户。                                              |
| IMSI          | IMSI            | 可选必选说明：条件必选参数 参数含义：该参数用于指定国际移动用户标识。 前提条件：该参数在“查询方式”参数配置为“IMSI（指定IMSI）”时有效。 取值范围：1～15位数字 默认值：无                                                                            |
| STMSI         | STMSI           | 可选必选说明：条件必选参数 参数含义：该参数用于指定用户临时签约标识。 前提条件：该参数在“查询方式”参数配置为“STMSI（指定S-TMSI）”时有效。 取值范围：1～10位十六进制字符串 默认值：无                                                                    |
| IMEI          | IMEI            | 可选必选说明：条件必选参数 参数含义：该参数用于指定用户设备的国际移动设备标识。 前提条件：该参数在“查询方式”参数配置为“IMEI（指定IMEI）”后生效。 取值范围：1～16位数字 默认值：无                                                                       |
| DISPTYPE      | 显示类型            | 可选必选说明：可选参数 参数含义：该参数用于指定显示类型。 取值范围：“BYBEARID/NSAPI（承载标识/网络层业务接入点标识）”：表示通过指定承载标识/网络层业务接入点标识显示。“BYCTXID（上下文标识）”：表示通过指定上下文标识显示。 默认值：BYBEARID/NSAPI（承载标识/网络层业务接入点标识）         |
| BEARIDORNSAPI | 承载ID或网络层业务接入点标识 | 可选必选说明：可选参数 参数含义：该参数用于指定承载ID或网络层业务接入点标识，用于唯一标识一个承载。 前提条件：该参数在“显示类型”设置为“BYBEARID/NSAPI（承载标识/网络层业务接入点标识）”后生效。 取值范围：5～15 默认值：无  说明： 若参数不输入，输出结果为承载的摘要信息。若参数输入，输出结果为承载的详细信息。 |
| CTXID         | 上下文标识           | 可选必选说明：可选参数 参数含义：该参数用于指定签约APN/PDP信息的上下文标识。 前提条件：该参数在“显示类型”设置为“BYCTXID（上下文标识）”后生效 取值范围：0～4294967294 默认值：无  说明： 若参数不输入，输出结果为签约APN/PDP的摘要信息。若参数输入，输出结果为签约APN/PDP的详细信息。      |

#### 使用实例

1. 当“IDTYPE”选择“BYCTXID（上下文标识）”而不输入上下文标识时，只输出签约PDP的摘要信息：

   `DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID;`

   ```
   %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID;%%
   RETCODE = 0  操作成功

   SM上下文基本信息：
   ------------------
     IMSI  =  123035201000001
   RU名称  =  MCR_SP_RU_0064
   进程号  =  6
     TSUI  =  0000000B80090000
   （结果个数 = 1）

   仍有后续报告输出
   ---    END

   +++    mcr        2017-02-15 13:55:47
   O&M   #HWHandle=174
   %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID;%%
   RETCODE = 0  操作成功

   SM上下文基本信息：
   ------------------
    上下文标识  签约的APN    签约的PDN类型  签约的IPv4地址  签约的IPv6地址                         

    1           HUAWEI1.COM  IPv4v6地址     0.0.0.0         0000:0000:0000:0000:0000:0000:0000:0000
    2           IMS          IPv4v6地址     0.0.0.0         0000:0000:0000:0000:0000:0000:0000:0000
    3           HUAWEI3.COM  IPv4v6地址     0.0.0.0         0000:0000:0000:0000:0000:0000:0000:0000
   （结果个数 = 3）

   共有2个报告
   ---    END
   ```
2. 当“IDTYPE”选择“BYBEARID/NSAPI（承载标识或网络层业务接入点标识）”而不输入承载ID或网络层业务接入点标识时，只输出激活承载的摘要信息：

   `DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI;`

   ```
   %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI;%%
   RETCODE = 0  操作成功

   SM上下文基本信息：
   ------------------
     IMSI  =  123035201000001
   RU名称  =  MCR_SP_RU_0064
   进程号  =  9
     TSUI  =  0000000B80090000
   （结果个数 = 1）

   仍有后续报告输出
   ---    END

   +++    mcr        2017-02-15 13:56:21
   O&M   #HWHandle=175
   %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI;%%
   RETCODE = 0  操作成功

   SM上下文基本信息：
   -----------------------------
                        承载ID  =  5
                    缺省承载ID  =  5
         实际使用的APN网络标识  =  HUAWEI1.COM
        实际使用的运营商APN_OI  =  MNC003.MCC460.GPRS
             实际使用的PDN类型  =  IPv4地址
            实际使用的IPv4地址  =  10.10.10.10
            实际使用的IPv6地址  =  0000:0000:0000:0000:0000:0000:0000:0000
   （结果个数 = 1）

   共有2个报告
   ---    END
   ```
3. 当“IDTYPE”选择“BYCTXID（上下文标识）”且输入上下文标识时，输出签约PDN的详细信息，包括用户级、PDN级的相关信息：

   `DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID, CTXID=1;`

   ```
   %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID, CTXID=1;%%
   RETCODE = 0  操作成功

   SM上下文基本信息：
   ------------------
     IMSI  =  123035201000001
   RU名称  =  MCR_SP_RU_0064
   进程号  =  6
     TSUI  =  0000000B80090000
   （结果个数 = 1）

   仍有后续报告输出
   ---    END

   +++    mcr        2017-02-15 13:57:25
   O&M   #HWHandle=176
   %%DSP RESTOSMCTX: QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYCTXID, CTXID=1;%%
   RETCODE = 0  操作成功

   SM签约上下文：
   --------------
                                 签约的PDN类型  =  IPv4v6地址
                                     签约的APN  =  HUAWEI1.COM
                             用户签约的EPS QCI  =  5
              用户签约的EPS ARP Priority Level  =  1
      用户签约的EPS ARP Pre-emption Capability  =  不可以抢占其它承载的资源
   用户签约的EPS ARP Pre-emption Vulnerability  =  可以被其它承载抢占资源
                                默认上下文标识  =  1
                             VPLMN地址是否允许  =  允许
                           MIP Home Agent Host  =  NULL
                          MIP Home Agent Realm  =  NULL
                   MIP Home Agent IPv4 Address  =  0.0.0.0
                   MIP Home Agent IPv6 Address  =  0000:0000:0000:0000:0000:0000:0000:0000
                            签约的P-GW分配类型  =  动态
                                签约的计费属性  =  0x0000（None）
                         签约的APN级别的APN OI  =  NULL
                            签约的上行APN-AMBR  =  10000000
                            签约的下行APN-AMBR  =  10000000
                                签约的IPv4地址  =  0.0.0.0
                                签约的IPv6地址  =  0000:0000:0000:0000:0000:0000:0000:0000
   （结果个数 = 1）

   共有2个报告
   ---    END
   ```
4. 当“IDTYPE”选择“BYBEARID/NSAPI”且输入“Bearer ID Or NSAPI”时，输出激活承载的详细信息，包括用户级、PDN级、承载级的相关信息：

   `DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;`

   ```
   %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
   RETCODE = 0  操作成功

   SM上下文基本信息：
   ------------------
     IMSI  =  123035201000001
   RU名称  =  MCR_SP_RU_0064
   进程号  =  6
     TSUI  =  0000000580060000
   （结果个数 = 1）

   仍有后续报告输出
   ---    END

   +++    mcr        2017-02-15 13:58:05
   O&M   #HWHandle=177
   %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
   RETCODE = 0  操作成功

   SM User上下文:
   --------------
     S-GW控制面IP地址（S11）  =  10.10.10.10
   S-GW控制面IPv6地址（S11）  =  0000:0000:0000:0000:0000:0000:0000:0000
       S-GW控制面TEID（S11）  =  0x989682
                    S-GW名称  =  TOPON.SGW.SGW1.NODES.EPC.ENVID52.MNC03.MCC460.3GPPNETWORK.ORG
   （结果个数 = 1）

   仍有后续报告输出
   ---    END

   +++    mcr        2017-02-15 13:58:05
   O&M   #HWHandle=177
   %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
   RETCODE = 0  操作成功

   SM PDN上下文:
   -------------
         实际使用的APN网络标识  =  HUAWEI1.COM
        实际使用的运营商APN_OI  =  MNC003.MCC460.GPRS
         APN Restriction Value  =  NULL
                   APN选择模式  =  签约的
            实际使用的IPv4地址  =  10.10.10.10
            实际使用的IPv6地址  =  0000:0000:0000:0000:0000:0000:0000:0000
                    缺省承载ID  =  5
     P-GW控制面IP地址（S5/S8）  =  10.10.10.10
   P-GW控制面IPv6地址（S5/S8）  =  0000:0000:0000:0000:0000:0000:0000:0000
       P-GW控制面TEID（S5/S8）  =  0x989683
                      P-GW名称  =  TOPON.PGW.GW1.NODES.EPC.MNC03.MCC460.3GPPNETWORK.ORG
        实际使用的上行APN-AMBR  =  10000000
        实际使用的下行APN-AMBR  =  10000000
                      计费属性  =  0x0000（None）
                  位置上报类型  =  NULL
                       PRA动作  =  启动PRA订阅
                       PRA标识  =  0x800000
   （结果个数 = 1）

   仍有后续报告输出
   ---    END

   +++    mcr        2017-02-15 13:58:05
   O&M   #HWHandle=177
   %%DSP RESTOSMCTX:QRYTP=IMSI, IMSI="123035201000001", DISPTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
   RETCODE = 0  操作成功

   SM承载上下文:
   -------------
                                            承载ID  =  5
                          S-GW用户面IP地址（S1-U）  =  10.10.10.10
                        S-GW用户面IPv6地址（S1-U）  =  0000:0000:0000:0000:0000:0000:0000:0000
                            S-GW用户面TEID（S1-U）  =  0x989684
                         P-GW用户面IP地址（S5/S8）  =  10.10.10.10
                       P-GW用户面IPv6地址（S5/S8）  =  0000:0000:0000:0000:0000:0000:0000:0000
                           P-GW用户面TEID（S5/S8）  =  0x989685
              用户实际使用的EPS ARP Priority Level  =  1
   用户实际使用的EPS ARP Pre-emption Vulnerability  =  可以被其它承载抢占资源
      用户实际使用的EPS ARP Pre-emption Capability  =  不可以抢占其它承载的资源
                             用户实际使用的EPS QCI  =  5
                          实际使用的上行最大比特率  =  0
                          实际使用的下行最大比特率  =  0
                          实际使用的上行保证比特率  =  0
                          实际使用的下行保证比特率  =  0
                                        激活发起方  =  MS发起的激活
                                                Ti  =  0
                         Packet Flow Context的标识  =  8
                                    业务接入点标识  =  3
                                        无线优先级  =  2
   （结果个数 = 1）

   共有4个报告
   ---    END
   ```

#### 输出结果说明

| 输出项名称                                      | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI                                       | 显示用户的国际移动用户标识，该参数在用户和运用商签约时由运营商指定。 取值范围：6～15位数字。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| STMSI                                      | 显示用户的临时签约标识。 取值范围：1～10位十六进制字符串。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| BEARIDORNSAPI                              | 显示承载ID或网络层业务接入点标识。 取值范围：5～15。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 缺省上下文标识                                    | 显示缺省的上下文标识，用来唯一标识一个上下文。 取值范围：0～4294967294。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| RU名称                                       | 参数含义：该参数用于指定资源单元名称。 取值范围：1~63位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 进程号                                        | 显示系统内容灾用户的SM上下文信息所属的SAP进程的进程号。 取值范围：0～12。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TSUI                                       | 显示SDAP协议用户的临时标识。 取值范围：1～16位数字。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 签约的PDN类型                                   | 显示签约的PDN类型。 取值范围：“IPv4地址”“IPv6地址”“IPv4v6地址”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的APN                                     | 显示签约的APN。 取值范围：1～64位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 用户签约的EPS QCI                               | 显示用户签约的EPS QCI，是体现EPS承载服务质量等级的参数之一。 取值范围：0～255                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 用户签约的EPS ARP Priority Level                | 显示用户签约的EPS ARP Priority Level，是体现EPS承载服务质量等级的参数之一。 取值范围：0～15                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 用户签约的Evolved ARP Pre-emption Capability    | 显示用户签约的Evolved ARP Pre-emption Capability。 取值范围：“可以抢占其它承载的资源”“不可以抢占其它承载的资源”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 用户签约的Evolved ARP Pre-emption Vulnerability | 显示用户签约的Evolved ARP Pre-emption Vulnerability。 取值范围：“可以被其它承载抢占资源”“不可以被其它承载抢占资源”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VPLMN地址是否允许                                | 显示漫游用户，MME根据其签约信息中的VPLMN地址是否被允许的取值来决定是否能连接到拜访地和归属地P-GW。 取值范围：“允许”：漫游用户可以连接到拜访地和归属地P-GW。“不允许”：漫游用户只能连接到归属地P-GW。                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 拜访地网络标识                                    | 显示拜访地网络标识。 取值范围：1～64个字符                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 签约的P-GW分配类型                                | 显示签约的PDN GW是静态分配或动态选择。 取值范围：“静态”：静态分配的P-GW，在P-GW选择时不会改变。“动态”：动态分配的P-GW，在P-GW选择时动态选择P-GW。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 签约的计费属性                                    | 显示提供给MS的计费属性。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 签约的APN级别的APN OI                            | 显示签约的APN级别的APN OI。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 签约的上行APN-AMBR                              | 显示签约的上行APN-AMBR。该APN非GBR承载的上行最大比特率。 取值范围：0～4294967295bit/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 签约的下行APN-AMBR                              | 显示签约的下行APN-AMBR（kbit/s）。该APN非GBR承载的下行最大比特率。 取值范围：0～4294967295bit/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 签约的QoS版本                                   | 显示签约QoS的版本。各版本差异参见表1。 取值范围：“QoS98”“QoS99”“QoSR5”“QoSR7”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 签约的延迟等级                                    | 显示签约QoS的延迟等级属性。取值含义参见表2。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 签约的可靠性                                     | 显示签约QoS的可靠性属性。 取值范围：“Unack GTP/LLC/RLC Unprotected”表示GTP， LLC，RLC被确认；数据被保护。“Unack GTP/LLC/RLC Protected”表示GTP未被确认；LLC、RLC被确认；数据被保护。“Unack GTP/LLC Ack RLC Protected”表示GTP、LLC未被确认，RLC被确认；数据被保护。“Unack GTP Ack LLC/RLC Protected”表示GTP、LLC、RLC未被确认；数据被保护。“Ack GTP/LL/RLC Protected”表示GTP、LLC、RLC未被确认；数据未被保护。                                                                                                                                                                                                                                                                            |
| 签约的最大吞吐量（octet/s）                          | 显示指定SGSN支持的缺省QoS最大吞吐量。 取值范围：“PT1（Up to 1000）”：1000 octet/s。“PT2（Up to 2000）”：2000 octet/s。“PT3（Up to 4000）”：4000 octet/s。“PT4（Up to 8000）”：8000 octet/s。“PT5（Up to 16000）”：16000 octet/s。“PT6（Up to 32000）”：32000 octet/s。“PT7（Up to 64000）”：64000 octet/s。“PT8（Up to 128000）”：128000 octet/s。“PT9（Up to 256000）”：256000 octet/s。                                                                                                                                                                                                                                                      |
| 签约的优先级                                     | 显示签约QoS的优先级属性。 取值范围：“高优先级”“普通优先级”“低优先级”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 签约的平均吞吐量（octet/h）                          | 显示指定SGSN支持的缺省QoS平均吞吐量。 取值范围：“MT1（100）”：100 octet/h。“MT2（200）”：200 octet/h。“MT3（500）”：500 octet/h。“MT4（1000）”：1000 octet/h。“MT5（2000）”：2000 octet/h。“MT6（5000）”：5000 octet/h。“MT7（10000）”：10000 octet/h。“MT8（20000）”：20000 octet/h。“MT9（50000）”：50000 octet/h。“MT10（100000）”：100000 octet/h。“MT11（200000）”：200000 octet/h。“MT12（500000）”：500000 octet/h。“MT13（1000000）”：1000000 octet/h。“MT14（2000000）”：2000000 octet/h。“MT15（5000000）”：5000000 octet/h。“MT16（10000000）”：10000000 octet/h。“MT17（20000000）”：20000000 octet/h。“MT18（50000000）”：50000000 octet/h。“MT31（Best effort）”：尽力而为。 |
| 签约的分配/保留优先级                                | 显示签约QoS的分配/保留优先级属性。 取值范围：“高端用户”“普通用户”“低端用户”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的流量等级                                    | 显示签约QoS的流量等级属性。 取值范围：“Conversational class”“Streaming class”“Interactive class”“Background class”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 签约的发送次序                                    | 显示签约QoS的发送次序属性。 取值范围：“With delivery order”“Without delivery order”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 签约的发送错误SDU                                 | 显示签约QoS的发送错误SDU属性。 取值范围：“subscribed delivery of erroneous SDUs”“No detect”“Erroneous SDUs are delivered”“Erroneous SDUs are not delivered”                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 签约的最大SDU长度                                 | 显示签约QoS的最大SDU长度属性。此参数定义了MME支持的缺省QoS最大SDU长度。 取值范围：10octets～1520octets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 签约的上行最大速率                                  | 显示签约QoS的上行最大速率属性。 MME支持的缺省QoS上行最大速率。 取值范围：0kbit/s～8640kbit/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 签约的下行最大速率                                  | 显示签约QoS的下行最大速率属性。MME支持的缺省QoS下行最大速率。 取值范围：0kbit/s～8640kbit/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的保留BER                                   | 显示签约QoS的保留BER属性。 取值范围：5 * 10-21 * 10-25 * 10-34 * 10-31 * 10-31 * 10-41 * 10-51 * 10-66 * 10-8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 签约的SDU误码率                                  | 显示签约QoS的SDU误码率属性。 取值范围：1 * 10-27 * 10-31 * 10-31 * 10-41 * 10-51 * 10-61 * 10-1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 签约的传递时延                                    | 显示签约QoS的传递时延属性。MME支持的缺省QoS传递时延。 取值范围： 10ms～4000ms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 签约的发送控制优先级                                 | 显示签约QoS的发送控制优先级属性。MME支持的缺省QoS发送控制优先级。 取值范围：“Priority level 1”“Priority level 2”“Priority level 3”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 签约的上行保证速率                                  | 显示签约QoS的上行保证速率属性。MME支持的缺省QoS上行保证速率。参考“签约的上行最大速率”参数。 取值范围：0kbit/s～8640kbit/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的下行保证速率                                  | 显示签约QoS的下行保证速率属性。MME支持的缺省QoS下行保证速率。参考“签约的上行最大速率”参数。 取值范围：0kbit/s～8640kbit/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的信令指示                                    | 显示签约QoS的信令指示属性。 取值范围：“not optimised for signalling traffic”“optimised for signalling traffic”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 签约的源统计特性                                   | 显示签约QoS的源统计特性属性。 取值范围：“unknown”“speech”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 签约的扩展下行最大速率                                | 显示签约QoS的扩展下行最大速率属性。 取值范围：0kbit/s8700kbit/s～16000kbit/s17Mbit/s～256Mbit/s  说明： 当本参数的取值为“0”时，下行的最大速率的限制取决于“签约的下行最大速率”参数的取值。当本参数的取值不为“0”时，下行最大速率的限制取决于本参数的取值，“签约的下行最大速率”参数的取值被忽略。                                                                                                                                                                                                                                                                                                                                                                                                         |
| 签约的扩展下行保证速率                                | 显示签约QoS的扩展下行保证速率属性。 取值范围：0kbit/s，8700kbit/s～16000kbit/s，17Mbit/s～256Mbit/s  说明： 当本参数的取值为“0”时，下行保证速率的限制取决于“签约的下行保证速率”参数的取值。当本参数的取值不为“0”时，下行保证速率的限制取决于本参数的取值，“签约的下行保证速率”参数的取值被忽略。                                                                                                                                                                                                                                                                                                                                                                                                        |
| 签约的扩展上行最大速率                                | 显示签约QoS的扩展上行最大速率属性。 取值范围：0kbit/s，8700kbit/s～16000kbit/s，17Mbit/s～256Mbit/s  说明： 当本参数的取值为“0”时，上行最大速率的限制取决于“签约的上行最大速率”参数的取值。当本参数的取值不为“0”时，上行最大速率的限制取决于本参数的取值，“签约的上行最大速率”参数的取值被忽略。                                                                                                                                                                                                                                                                                                                                                                                                        |
| 签约的扩展上行保证速率                                | 显示签约QoS的扩展上行保证速率属性。 取值范围：0kbit/s，8700kbit/s～16000kbit/s，17Mbit/s～256Mbit/s  说明： 当本参数的取值为“0”时，上行保证速率的限制取决于“签约的上行保证速率”参数的取值。当本参数的取值不为“0”时，上行保证速率的限制取决于本参数的取值，“签约的上行保证速率”参数的取值被忽略。                                                                                                                                                                                                                                                                                                                                                                                                        |
| S-GW控制面IP地址（S4）                            | 显示S4接口S-GW控制面IP地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| S-GW控制面TEID（S4）                            | 显示S4接口S-GW控制面TEID。 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| S-GW控制面IP地址（S11）                           | 显示S11接口S-GW控制面IP地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| S-GW控制面IPv6地址（S11）                         | 显示S11接口S-GW控制面IPV6地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| S-GW控制面TEID（S11）                           | 显示S11接口S-GW控制面TEID。 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| S-GW名称                                     | 显示S-GW的域名名称。 取值范围：0～256位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 实际使用的APN网络标识                               | 显示标识使用的APN的网络。 取值范围：0～64位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 实际使用的运营商APN_OI                             | 显示标识当前使用的APN的运营商。 取值范围：0～38位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| APN选择模式                                    | APN选择模式。 取值范围：“签约的”：MS或网络提供的APN，已核实签约数据。“MS选择的”：MS提供的APN，未核实签约数据。“网络选择的”：网络提供的APN，未核实签约数据。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 实际使用的PDN类型                                 | 实际使用的PDN地址类型： 取值范围：“IPv4地址”“IPv6地址”“IPv4v6地址”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 实际使用的IPv4地址                                | 显示实际使用的IPv4地址。参考静态的“签约的IPv4地址”参数。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 实际使用的IPv6地址                                | 显示实际使用的IPv4地址。参考静态的“签约的IPv6地址”参数。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 缺省承载ID                                     | 显示缺省EPS承载ID。 取值范围：5～15                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| P-GW控制面IP地址（S5/S8）                         | 显示S5/S8接口P-GW控制面IPv4地址，用来标识通过S5/S8接口与S-GW通信的P-GW控制面的IPv4地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| P-GW控制面IPv6地址（S5/S8）                       | 显示S5/S8接口P-GW控制面IPv6地址，用来标识通过S5/S8接口与S-GW通信的P-GW控制面的IPv6地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| P-GW控制面TEID（S5/S8）                         | 显示S5/S8接口P-GW控制面TEID，用来标识通过S5/S8接口与S-GW通信的P-GW控制面的隧道。 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P-GW名称                                     | 显示P-GW的域名名称。 取值范围：0～256位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 实际使用的上行APN-AMBR                            | 显示实际使用的上行APN-AMBR。参考“签约的上行APN-AMBR”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 实际使用的下行APN-AMBR                            | 显示实际使用的下行APN-AMBR。参考“签约的下行APN-AMBR”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 计费属性                                       | 该用户的签约的计费属性。 取值范围：1～6位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 位置上报类型                                     | 显示位置变化报告行为。 取值范围：“停止上报”“开始上报CGI/SAI”“开始上报RAI”“开始上报TAI”“开始上报ECGI”“开始上报CGI/SAI和RAI”“开始上报TAI和ECGI”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 承载ID                                       | 显示EPS承载ID。 取值范围：0～5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| S-GW用户面IP地址（S4）                            | 显示S4接口S-GW用户面IP地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| S-GW用户面TEID（S4）                            | 显示S4接口S-GW用户面TEID。 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| S-GW用户面IP地址（S12）                           | 显示S12接口S-GW用户面IP地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| S-GW用户面TEID（S12）                           | 显示S12接口S-GW用户面TEID。 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| S-GW用户面IP地址（S1-U）                          | 显示S1-U接口S-GW用户面IPv4地址，用来标识通过S1–U接口与E-UTRAN通信的服务网关的IPv4地址 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| S-GW用户面IPv6地址（S1-U）                        | 显示S1-U接口S-GW用户面IPv6地址，用来标识通过S1–U接口与E-UTRAN通信的服务网关的IPv6地址 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| S-GW用户面TEID（S1-U）                          | 显示S1-U接口S-GW用户面TEID，用来标识通过S1–U接口与E-UTRAN通信的服务网关的隧道端点标识。 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| P-GW用户面IP地址（S5/S8）                         | 显示S5/S8接口P-GW用户面IPv4地址，用来标识通过S5/S8接口与服务网关通信的PDN网关用户面的IPv4地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| P-GW用户面IPv6地址（S5/S8）                       | 显示S5/S8接口P-GW用户面IPv6地址，用来标识通过S5/S8接口与服务网关通信的PDN网关用户面的IPv6地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| P-GW用户面TEID（S5/S8）                         | 显示S5/S8接口P-GW用户面TEID，用来标识通过S5/S8接口与服务网关通信的PDN网关用户面的TEID 取值范围：0～10位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 用户实际使用的EPS ARP Priority Level              | 显示用户实际使用的EPS ARP Priority Level。 取值范围：0～15                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 用户实际使用的EPS ARP Pre-emption Vulnerability   | 显示用户实际使用的EPS ARP Pre-emption Vulnerability。 取值范围：“可以被其它承载抢占资源”“不可以被其它承载抢占资源”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 用户实际使用的EPS ARP Pre-emption Capability      | 显示用户实际使用的EPS ARP Pre-emption Capability。 取值范围：“可以抢占其它承载的资源”“不可以抢占其它承载的资源”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 用户实际使用的EPS QCI                             | 显示用户实际使用的EPS QCI。参考“用户签约的EPS QCI”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 实际使用的上行最大速率                                | 显示实际使用的上行最大速率。参考“签约的上行最大速率”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 实际使用的下行最大速率                                | 显示实际使用的下行最大速率。参考“签约的下行最大速率”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 实际使用的上行保证速率                                | 显示实际使用的上行保证速率。参考“签约的上行保证速率”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 实际使用的下行保证速率                                | 显示实际使用的下行保证速率。参考“签约的下行保证速率”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 激活发起方                                      | 标识是由MS发起的激活还是由网络侧发起的激活。 取值范围：“MS发起的激活”“不可以抢占其它承载的资源”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Ti                                         | 显示Transaction Identifier。 取值范围：0～255                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Packet Flow Context的标识                     | 显示Packet Flow Context的标识，用来唯一标识一个Packet Flow Context。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 业务接入点标识                                    | 显示业务接入点标识，用来唯一标识一个业务接入点。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 无线优先级                                      | 显示QoS的无线优先级。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MIP Home Agent Host                        | 显示MIP Home Agent Host。 取值范围：0～256位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MIP Home Agent Realm                       | 显示MIP Home Agent Realm。 取值范围：0～256位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MIP Home Agent IPv4 Address                | 显示MIP Home Agent IPv4 Address。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MIP Home Agent IPv6 Address                | MIP Home Agent IPv6 Address。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的IPv4地址                                  | 显示签约的IPv4地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 签约的IPv6地址                                  | 显示签约的IPv6地址。 取值范围：0～128位字符串                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 默认上下文标识                                    | 显示默认上下文标识。 取值范围：0～4294967294                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PRA动作                                      | 显示指定PDN连接的PRA（Presence Reporting Area）订阅状态。 取值范围：“启动PRA订阅”“停止PRA订阅”  说明： 当PDN连接没有被订阅指定区域用户位置上报（PRA），本参数取值为“NULL”。此时，“PRA标识”取值也为“NULL”。当本参数取值为“停止PRA订阅”时，“PRA标识”为PDN连接上下文中最近一次PRA信息。                                                                                                                                                                                                                                                                                                                                                                                                    |
| PRA标识                                      | 显示指定PDN连接被订阅的PRA（Presence Reporting Area）标识。 取值范围：0x800000～0xFFFFFF  说明： 当“指定区域用户位置上报（PRA）”License关闭时，本参数不再刷新，为PDN连接上下文中保存的最近一次PRA标识。                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 签约的5GS互操作标识                                | 显示签约的5GS互操作标识。 取值范围： “未签约”“签约”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### 参考信息

| QoS版本   | 属性_延迟等级   | 属性_可靠性   | 属性_最大吞吐量   | 属性_优先级   | 属性_平均吞吐量   | 属性_分配/保留优先级   | 属性_流量等级   | 属性_发送次序   | 属性_发送错误SDU   | 属性_最大SDU长度   | 属性_上行最大速率   | 属性_下行最大速率   | 属性_保留BER   | 属性_SDU误码率   | 属性_传递时延   | 属性_发送控制优先级   | 属性_上行保证速率   | 属性_下行保证速率   | 属性_扩展上行最大速率   | 属性_扩展下行最大速率   | 属性_扩展上行保证速率   | 属性_扩展下行保证速率   |
|:--------|:----------|:---------|:-----------|:---------|:-----------|:--------------|:----------|:----------|:-------------|:-------------|:------------|:------------|:-----------|:------------|:----------|:-------------|:------------|:------------|:--------------|:--------------|:--------------|:--------------|
| QoS98   | √         | √        | √          | √        | √          | -             | -         | -         | -            | -            | -           | -           | -          | -           | -         | -            | -           | -           | -             | -             | -             | -             |
| QoS99   | √         | √        | √          | √        | √          | √             | √         | √         | √            | √            | √           | √           | √          | √           | √         | √            | √           | √           | -             | -             | -             | -             |
| QoSR5   | √         | √        | √          | √        | √          | √             | √         | √         | √            | √            | √           | √           | √          | √           | √         | √            | -           | √           | -             | √             | -             | -             |
| QoSR7   | √         | √        | √          | √        | √          | √             | √         | √         | √            | √            | √           | √           | √          | √           | √         | √            | √           | √           | √             | √             | √             | √             |

**说明** 

表中，“√”表示有效，“-”代表无效。

|   延迟等级 | 延迟（最大值）_SDU大小：128八位数组_平均传输延迟（秒）   | 延迟（最大值）_SDU大小：128八位数组_95%延迟（秒）   | 延迟（最大值）_SDU大小：1024八位数组_平均传输延迟（秒）   | 延迟（最大值）_SDU大小：1024八位数组_95%延迟（秒）   |
|-------:|:----------------------------------|:---------------------------------|:-----------------------------------|:----------------------------------|
|      1 | <0.5                              | <1.5                             | <2                                 | <7                                |
|      2 | <5                                | <25                              | <15                                | <75                               |
|      3 | <50                               | <250                             | <75                                | <375                              |
|      4 | 尽力发送                              | 尽力发送                             | 尽力发送                               | 尽力发送                              |