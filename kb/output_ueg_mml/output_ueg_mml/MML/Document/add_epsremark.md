# 增加EPS QoS到TOS/DSCP的映射规则（ADD EPSREMARK）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令用来增加在SAE架构下，QoS参数到IP报头中的DSCP（区别服务编码点）/TOS（服务类型）的映射规则，用户的数据将根据映射得到的DSCP（区别服务编码点）/TOS（服务类型）中的参数值进行转发。

## 注意事项

- 命令执行后只对新接入用户生效。

- UNC支持将用户在会话激活或者更新过程中协商的QoS参数映射为IP报文头中的TOS（服务类型）域或者DSCP（区别服务编码点），这样用户的数据报文在传送过程中，UNC将映射出的TOS或者DSCP填写到用户数据报文的IP头中，该IP报文在传送过程将根据TOS或者DSCP编码获得不同的处理优先级，从而满足服务质量的要求。
- RFC2597推荐的BE编码点：000000；RFC2598推荐的EF编码点：101110。
- 当DSCP的参数值为AF时，如果配置了AF-CLASS和DROP-PRECEDENCE的参数值，则请参照RFC2597推荐的AFij编码点。i表示类别，j表示丢弃优先级，j值越高，则丢弃优先级越高。
- 当没有配置针对某个用户级别/业务级别的DSCP的参数时，采用的Traffic Class到DSCP的映射关系为：Conversation-->EF，StreamingGBRMore25Kbps-->AF31，StreamingGBRLess25Kbps-->AF31，InteractiveTrafficPri1-->AF11，InteractiveTrafficPri2-->AF12，InteractiveTrafficPri3-->AF13，Background-->BE。
- 用户可以根据不同的应用结合差异化服务，给不同用户类型、业务类型给用户配置不同的DSCP值。

- 最多可输入1000条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称             | 参数说明                                                                                                                                                                                                                                                 |
|:---------------|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QOSPROFILENAME | QoS Profile名称    | 可选必选说明：必选参数  参数含义：该参数指定QoS Profile的名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：  QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功，可以通过LST QOSPROFILE或LST CPQOSGLOBAL命令查询。                                                            |
| QCI            | QCI              | 可选必选说明：必选参数  参数含义：该参数表示QoS流量级别。  数据来源：全网规划  取值范围：整数类型，取值范围是1~255。  默认值：无  配置原则：无                                                                                                                                                                     |
| ARPPL          | ARP的优先级别         | 可选必选说明：必选参数  参数含义：该参数表示ARP的优先级别。  数据来源：全网规划  取值范围：整数类型，取值范围是0~15。  默认值：无  配置原则： 0：General，通用用户。如果某业务级别各个优先级的用户都没有配置DSCP，则用General配置的值。1~15：用户的优先级，其中1的优先级最高。                                                                                         |
| REMARKTYPE     | 标记类型             | 可选必选说明：必选参数  参数含义：该参数用于表示映射到DSCP或者TOS。  数据来源：全网规划 取值范围： DSCP（映射到Dscp）TOS（映射到TOS）  默认值：无  配置原则：无                                                                                                                                                      |
| DSCP           | DSCP             | 可选必选说明：该参数在"REMARKTYPE"配置为"DSCP"时为条件必选参数。  参数含义：该参数用于表示DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无              |
| AFCLASS        | AF级别             | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                                |
| AFDROPPREC     | AF丢弃优先级          | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                                 |
| TOSVALUE       | TOS值             | 可选必选说明：该参数在"REMARKTYPE"配置为"TOS"时为条件必选参数。  参数含义：该参数表示映射到TOS的值，分别对应IP优先级的8个队列ID，优先值高的报文先于优先值低的报文发送。  数据来源：全网规划  取值范围：整数类型，取值范围是0~7。  默认值：无  配置原则：无                                                                                                     |
| DSCPVALUE      | DSCP值            | 可选必选说明：该参数在"DSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                                     |
| S1UDSCPSWITCH  | S1-U DSCP配置开关    | 可选必选说明：可选参数  参数含义：该参数用于表示S1-U接口DSCP配置开关。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：无                                                                                                                                                |
| S1UDSCP        | S1-U DSCP        | 可选必选说明：该参数在"S1UDSCPSWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于表示S1U DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无     |
| S1UAFCLASS     | S1-U AF级别        | 可选必选说明：该参数在"S1UDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示S1U接口AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                        |
| S1UAFDROPPREC  | S1-U AF丢弃优先级     | 可选必选说明：该参数在"S1UDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示S1U接口AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                         |
| S1UDSCPVALUE   | S1-U DSCP值       | 可选必选说明：该参数在"S1UDSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的S1U接口DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                             |
| S5SDSCPSWITCH  | SGW S5 DSCP配置开关  | 可选必选说明：可选参数  参数含义：该参数用于表示SGW S5接口DSCP配置开关。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：无                                                                                                                                              |
| S5SDSCP        | SGW S5 DSCP      | 可选必选说明：该参数在"S5SDSCPSWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于表示SGW S5 DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无  |
| S5SAFCLASS     | SGW S5 AF级别      | 可选必选说明：该参数在"S5SDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示SGW S5接口AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                     |
| S5SAFDROPPREC  | SGW S5 AF丢弃优先级   | 可选必选说明：该参数在"S5SDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示SGW S5接口AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                      |
| S5SDSCPVALUE   | SGW S5 DSCP值     | 可选必选说明：该参数在"S5SDSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的SGW S5接口DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                          |
| S5PDSCPSWITCH  | PGW S5 DSCP配置开关  | 可选必选说明：可选参数  参数含义：该参数用于表示PGW S5接口DSCP配置开关。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：无                                                                                                                                              |
| S5PDSCP        | PGW S5 DSCP      | 可选必选说明：该参数在"S5PDSCPSWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于表示PGW S5 DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无  |
| S5PAFCLASS     | PGW S5 AF级别      | 可选必选说明：该参数在"S5PDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示PGW S5接口AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                     |
| S5PAFDROPPREC  | PGW S5 AF丢弃优先级   | 可选必选说明：该参数在"S5PDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示PGW S5接口AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                      |
| S5PDSCPVALUE   | PGW S5 DSCP值     | 可选必选说明：该参数在"S5PDSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的PGW S5接口DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                          |
| S8SDSCPSWITCH  | SGW S8 DSCP配置开关  | 可选必选说明：可选参数  参数含义：该参数用于表示SGW S8接口DSCP配置开关。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：无                                                                                                                                              |
| S8SDSCP        | SGW S8 DSCP      | 可选必选说明：该参数在"S8SDSCPSWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于表示SGW S8 DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无  |
| S8SAFCLASS     | SGW S8 AF级别      | 可选必选说明：该参数在"S8SDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示SGW S8接口AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                     |
| S8SAFDROPPREC  | SGW S8 AF丢弃优先级   | 可选必选说明：该参数在"S8SDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示SGW S8接口AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                      |
| S8SDSCPVALUE   | SGW S8 DSCP值     | 可选必选说明：该参数在"S8SDSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的SGW S8接口DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                          |
| S8PDSCPSWITCH  | PGW S8 DSCP配置开关  | 可选必选说明：可选参数  参数含义：该参数用于表示PGW S8接口DSCP配置开关。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：无                                                                                                                                              |
| S8PDSCP        | PGW S8 DSCP      | 可选必选说明：该参数在"S8PDSCPSWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于表示PGW S8 DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无  |
| S8PAFCLASS     | PGW S8 AF级别      | 可选必选说明：该参数在"S8PDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示PGW S8接口AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                     |
| S8PAFDROPPREC  | PGW S8 AF丢弃优先级   | 可选必选说明：该参数在"S8PDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示PGW S8接口AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                      |
| S8PDSCPVALUE   | PGW S8 DSCP值     | 可选必选说明：该参数在"S8PDSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的PGW S8接口DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                          |
| SGIDSCPSWITCH  | PGW SGi DSCP配置开关 | 可选必选说明：可选参数  参数含义：该参数用于表示PGW SGi接口DSCP配置开关。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：无                                                                                                                                             |
| SGIDSCP        | PGW SGi DSCP     | 可选必选说明：该参数在"SGIDSCPSWITCH"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于表示PGW SGi DSCP。  数据来源：全网规划 取值范围： EF（对应的DSCP的值为101110）AF（对应的DSCP的值由参数AfClass和AfDropPres界定）BE（对应的DSCP的值为000000）CS6（对应的DSCP的值为110000）CS7（对应的DSCP的值为111000）DSCP_VALUE（映射的DSCP值）  默认值：无  配置原则：无 |
| SGIAFCLASS     | PGW SGi AF级别     | 可选必选说明：该参数在"SGIDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数用于表示PGW SGi接口AF队列序号。  数据来源：全网规划  取值范围：整数类型，取值范围是1~4。  默认值：无  配置原则：无                                                                                                                                    |
| SGIAFDROPPREC  | PGW SGi AF丢弃优先级  | 可选必选说明：该参数在"SGIDSCP"配置为"AF"时为条件必选参数。  参数含义：该参数表示PGW SGi接口AF丢弃优先级。  数据来源：全网规划  取值范围：整数类型，取值范围是1~3。  默认值：无  配置原则：无                                                                                                                                     |
| SGIDSCPVALUE   | PGW SGi DSCP值    | 可选必选说明：该参数在"SGIDSCP"配置为"DSCP_VALUE"时为条件必选参数。  参数含义：该参数用于表示映射的PGW SGi接口DSCP值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~63。  默认值：无  配置原则：无                                                                                                                         |

## 使用实例

为名为“qosprofile1”的QoS Profile添加一条EPS remark配置，参数“QCI”为“1”，“ArpPl”为“15”，“Remark type”为“DSCP”，“DSCP”为“EF”，S1U接口的DSCP开关为开启并且DSCP值为22，SGW S5接口的DSCP开关为开启并且DSCP值为23，PGW S5接口的DSCP开关为开启并且DSCP值为24，SGW S8接口的DSCP开关为开启并且DSCP值为25，PGW S8接口的DSCP开关为开启并且DSCP值为26，SGi接口的DSCP开关为开启并且DSCP值为27。

```
ADD EPSREMARK: QOSPROFILENAME="qosprofile1", QCI=1, ARPPL=15, REMARKTYPE=DSCP, DSCP=EF, S1UDSCPSWITCH=ENABLE, S1UDSCP=DSCP_VALUE, S1UDSCPVALUE=22, S5SDSCPSWITCH=ENABLE, S5SDSCP=DSCP_VALUE, S5SDSCPVALUE=23, S5PDSCPSWITCH=ENABLE, S5PDSCP=DSCP_VALUE, S5PDSCPVALUE=24, S8SDSCPSWITCH=ENABLE, S8SDSCP=DSCP_VALUE, S8SDSCPVALUE=25, S8PDSCPSWITCH=ENABLE, S8PDSCP=DSCP_VALUE, S8PDSCPVALUE=26, SGIDSCPSWITCH=ENABLE, SGIDSCP=DSCP_VALUE, SGIDSCPVALUE=27;
```