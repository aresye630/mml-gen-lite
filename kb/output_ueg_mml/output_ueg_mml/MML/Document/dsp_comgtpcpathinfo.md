# 显示UAM GTPC路径信息（DSP COMGTPCPATHINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGSN、MME、AMF**

该命令用于显示UAM GTP-C路径信息。

## 注意事项

- 如需要进行MME/SGSN单进程的查询，则需要通过DSP GTPCPATH命令查询。
- 当"RU名称"未输入时，默认只向AMF查询。
- 查询的GTP-C路径数目，最大可显示MME/SGSN以及AMF共5000条，大于5000条需要独立查询原子表。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                                                                                                                                            |
|:-------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPTYPE       | IP地址类型   | 可选必选说明：必选参数  参数含义：该参数用于指定GTP-C路径的IP地址类型。  数据来源：本端规划 取值范围： IPV4（IPV4）IPV6（IPV6）  默认值：无  配置原则：无                                                                                                                                                                                   |
| LOCALIPV4    | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。  参数含义：该参数用于指定GTP-C路径的本端IPv4地址。  数据来源：本端规划  取值范围：IPv4地址类型。  默认值：无  配置原则：无                                                                                                                                                                  |
| LOCALIPV6    | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。  参数含义：该参数用于指定GTP-C路径的本端IPv6地址。  数据来源：本端规划  取值范围：IPv6地址类型。  默认值：无  配置原则：无                                                                                                                                                                  |
| GTPVERIN     | GTP版本    | 可选必选说明：必选参数  参数含义：该参数用于指定GTP-C路径的GTP版本号。  数据来源：本端规划  取值范围：GTPV0只适用于MME/SGSN。 GTPV0（GTP V0）GTPV1（GTP V1）GTPV2（GTP V2）  默认值：无  配置原则：无                                                                                                                                             |
| PEERIPV4     | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。  参数含义：该参数用于指定GTP-C路径的对端IPv4地址。  数据来源：本端规划  取值范围：IPv4地址类型。  默认值：无  配置原则：无                                                                                                                                                                  |
| PEERIPV6     | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。  参数含义：该参数用于指定GTP-C路径的对端IPv6地址。  数据来源：本端规划  取值范围：IPv6地址类型。  默认值：无  配置原则：无                                                                                                                                                                  |
| QRYTP        | 查询类型     | 可选必选说明：可选参数  参数含义：该参数用于指定查询类型。  数据来源：本端规划 取值范围： MEMORY（内存）DDB（数据库）  默认值：MEMORY  配置原则：无                                                                                                                                                                                          |
| INTFTYPEIN   | 接口类型     | 可选必选说明：可选参数  参数含义：该参数用于指定GTP-C路径的接口类型。  数据来源：本端规划  取值范围：AMF只支持选择一种接口类型，包括unknown，Gn，Gp，S11，S5，S8，N26，S4，All；MME/SGSN不支持选择S5，S8，N26。 UNKNOWN（unknown）Gn（Gn）Gp（Gp）S3（S3）S4（S4）S10（S10）S11（S11）S16（S16）Sm（Sm）Sv（Sv）S101（S101）Sn（Sn）N26（N26）S5（S5）S8（S8）ALL（All）  默认值：ALL-1  配置原则：无 |
| RUNAME       | RU名称     | 可选必选说明：可选参数  参数含义：该参数用于指定RU名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。该参数只适用于MME/SGSN，该参数可以通过DSP RU命令查询；AMF默认显示为NULL。  默认值：无  配置原则：无                                                                                                                                              |
| PATHSTATUSIN | 路径状态     | 可选必选说明：可选参数  参数含义：该参数用于指定GTP-C路径的路径状态。  数据来源：本端规划 取值范围： ERROR（故障）NORMAL（正常）ALL（所有）  默认值：ERROR  配置原则：无                                                                                                                                                                           |

## 使用实例

DSP COMGTPCPATHINFO: IPTYPE=IPV4, GTPVERIN=GTPV2, QRYTP=MEMORY, INTFTYPEIN=UNKNOWN-0&Gn-0&Gp-0&S3-0&S4-0&S10-0&S11-0&S16-0&Sm-0&Sv-0&S101-0&Sn-0&N26-0&S5-0&S8-0&ALL-1, PATHSTATUSIN=ALL;

```
%%DSP COMGTPCPATHINFO: IPTYPE=IPV4, GTPVERIN=GTPV2, QRYTP=MEMORY, INTFTYPEIN=UNKNOWN-0&Gn-0&Gp-0&S3-0&S4-0&S10-0&S11-0&S16-0&Sm-0&Sv-0&S101-0&Sn-0&N26-0&S5-0&S8-0&ALL-1, PATHSTATUSIN=ALL;%%
RETCODE = 0  操作成功

结果如下
------------------------
                    IP地址类型  =  IPV4
                    本端IP地址  =  192.168.138.2
                    对端IP地址  =  10.70.240.1
                      进程类型  =  NULL
                        进程号  =  0
                 GTP-C路径数目  =  0
             GTP-C路径网络类型  =  5G Core Network
           发送Echo Request开关  =  ON
                      接口类型  =  S11
               路径断去激活会话时间  =  00:00:00
对端Recovery变化去激活会话时间  =  00:00:00
                       对端Recovery值  =  0
                       Prn标志  =  Disable
                       Ntsr标志  =  Disable
                       RU名称  =  NULL
                     路径状态  =  NORMAL
                    GTP版本  =  GTP V2
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称               | 输出项解释                                                                                                                                               |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| IP地址类型              | 该参数用于指定GTP-C路径的IP地址类型。 取值说明： IPV4（IPV4）IPV6（IPV6）                                                                                                   |
| 进程类型                | 该参数用于指定进程类型。 取值说明： SPP（SPP）UPP（UPP）NULL0（NULL）NULL255（NULL）                                                                                         |
| 进程号                 | 该参数用于指定进程号。                                                                                                                                         |
| GTP-C路径数目           | 该参数用于显示查询的GTP-C路径数目，最大可显示MME/SGSN以及AMF各5000条，大于5000条需要独立查询原子表。                                                                                      |
| GTP-C路径网络类型         | 该参数用于指定GTP-C路径网络类型。 取值说明： GPRS/UMTS（2G或3G网络）EPC（4G网络）TEST（测试）INTF_BUTT（空）CORE5G（5G网络）NULL255（空）                                                     |
| 发送Echo Request开关    | 该参数用于指定MME/SGSN是否发送Echo Request。 取值说明： OFF（关闭）ON（开启）NULL255（空）                                                                                      |
| 接口类型                | 该参数用于指定GTP-C路径的接口类型。 取值说明： UNKNOWN（unknown）Gn（Gn）Gp（Gp）S3（S3）S4（S4）S10（S10）S11（S11）S16（S16）Sm（Sm）Sv（Sv）S101（S101）Sn（Sn）N26（N26）S5（S5）S8（S8）ALL（All） |
| 路径断去激活会话时间          | 该参数用于指定当GTP-C路径持续故障后，使用该GTP-C路径在该时间之前接入的会话会被去激活，仅适用于AMF。                                                                                            |
| 对端Recovery变化去激活会话时间 | 该参数用于指定当对端Recovery变化后，在该时间之前和对端创建的会话会被去激活，仅适用于AMF。                                                                                                  |
| 对端Recovery值         | 该参数用于指定该GTP-C路径指示的对端网元的Recovery值。                                                                                                                   |
| Prn标志               | 该参数用于指定该GTP-C路径指示的对端网元是否支持PRN功能，仅适用于AMF。 取值说明： Enable（Enable）Disable（Disable）                                                                       |
| Ntsr标志              | 该参数用于指定该GTP-C路径指示的对端网元是否支持NTSR功能，仅适用于AMF。 取值说明： Enable（Enable）Disable（Disable）                                                                      |
| RU名称                | 该参数用于指定RU名称。                                                                                                                                        |
| 路径状态                | 该参数用于指定GTP-C路径的路径状态。 取值说明： NORMAL（正常）ERROR（故障）IDLE（Idle）DETECT（探测）NULL（空）NULL255（null）                                                              |
| GTP版本               | 该参数用于指定GTP-C路径的GTP版本号。 取值说明： GTPV0（GTP V0）GTPV1（GTP V1）GTPV2（GTP V2）UNKNOWN（未知）NULL255（Null）                                                        |
| 本端IP地址              | 该参数用于指定GTP-C路径的本端IP地址。                                                                                                                              |
| 对端IP地址              | 该参数用于指定GTP-C路径的对端IP地址。                                                                                                                              |