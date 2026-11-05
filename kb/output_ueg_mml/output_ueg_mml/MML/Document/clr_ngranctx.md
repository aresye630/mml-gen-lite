# 清除NG-RAN上下文（CLR NGRANCTX）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

执行本命令将导致AMF释放与指定NG-RAN之间的SCTP连接，同时会释放通过该NG-RAN接入的用户上下文或基站上下文，从而导致业务中断。

**适用NF：AMF**

该命令用于在AMF上清除指定的NG-RAN上下文。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                | 参数说明                                                                                                                                                                                                                                                                                          |
|:---------------|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NGRANNODETYPE  | NG-RAN基站类型          | 可选必选说明：必选参数  参数含义：该参数用于指定接入的RAN的类型。  数据来源：对端协商 取值范围： “Gnb（gNodeB）”：gNodeB“NgEnb（ng-eNB）”：ng-eNB“SFgnb（sfgNodeB）”：sfgNodeB  默认值：无  配置原则：无                                                                                                                                                      |
| SFGCLRTYPE     | 感知基站清除方式            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"SFgnb"时为条件必选参数。  参数含义：该参数用于指定感知基站信息的清除方式。  数据来源：本端规划 取值范围： “MasterRanID（指定感知链路主基站ID清除上下文）”：指定感知链路主基站ID清除上下文“SenseRanID（指定感知基站ID删除感知能力）”：指定感知基站ID删除感知能力  默认值：无  配置原则：  若希望仅删除某基站的感知能力，选择“SenseRanID”清除方式。若希望将指定感知主基站链路，以及该链路下挂载的所有感知基站能力都清除，选择“MasterRanID”清除方式。 |
| PLMNID         | PLMN标识              | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。  参数含义：该参数用于指定NG接入网侧基站的PLMN标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                     |
| GNBTYPE        | gNodeB类型            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB的类型。  数据来源：对端协商 取值范围： “Gnb（gNodeB）”：gNodeB  默认值：无  配置原则：无                                                                                                                                                                      |
| GNBID          | gNodeB标识            | 可选必选说明：该参数在"GNBTYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                                          |
| NGENBTYPE      | ng-eNB类型            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"时为条件必选参数。  参数含义：该参数用于指定ng-eNB类型。  数据来源：对端协商 取值范围： “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB“ShortMacroNgEnb（ShortMacro ng-eNB）”：ShortMacro ng-eNB“LongMacroNgEnb（LongMacro ng-eNB）”：LongMacro ng-eNB  默认值：无  配置原则：无                                         |
| MACRONGENBID   | Macro ng-eNB标识      | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~1048575。  默认值：无  配置原则：无                                                                                                                                                              |
| SHORTNGENBID   | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Short Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~262143。  默认值：无  配置原则：无                                                                                                                                                    |
| LONGNGENBID    | LongMacro ng-eNB标识  | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Long Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~2097151。  默认值：无  配置原则：无                                                                                                                                                     |
| GNBIDBITLEN    | gNodeB ID有效比特长度     | 可选必选说明：该参数在"GNBTYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB ID有效比特长度。  数据来源：对端协商  取值范围：整数类型，取值范围是22~32。  默认值：无  配置原则：无                                                                                                                                                                          |
| SFGNBID        | sfgNodeB标识          | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"时为条件必选参数。  参数含义：该参数用于指定感知基站的标识ID。  数据来源：全网规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                               |
| SFGPLMNID      | 通感基站PLMN标识          | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"时为条件必选参数。  参数含义：该参数用于指定感知基站的PLMN标识。  数据来源：全网规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                             |
| SFGMASTERGNBID | 感知主基站标识             | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"、"MasterRanID"时为条件必选参数。  参数含义：该参数用于指定感知基站所属的主基站的标识ID。  数据来源：全网规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                           |
| SFGMASTERPLMN  | 感知主基站PLMN标识         | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"、"MasterRanID"时为条件必选参数。  参数含义：该参数用于指定感知基站所属的主基站的PLMN标识。  数据来源：全网规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                         |

## 使用实例

- 删除基站类型为Gnb，PLMN ID为12303，Gnb类型为Gnb，Gnb ID为1179985，gNodeB ID有效比特长度为24的基站对应的上下文。执行如下命令：

  ```
  CLR NGRANCTX: NGRANNODETYPE=Gnb, PLMNID=12303, GNBTYPE=Gnb, GNBID=1179985, GNBIDBITLEN=24;
  ```
- 删除基站类型为SFgnb，清除方式为指定感知链路主基站ID清除上下文，感知主基站PLMN标识为12303，感知主基站标识为1179985的感知基站对应的上下文。执行如下命令：

  ```
  CLR NGRANCTX: NGRANNODETYPE=SFgnb, SFGCLRTYPE=MasterRanID, SFGMASTERGNBID=12303, SFGMASTERPLMN=1179985;
  ```