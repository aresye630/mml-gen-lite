# 复位AN（RST AN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令触发AMF发送到指定NG-RAN的RESET消息；当NG-RAN收到AMF的RESET消息后将立即释放UE的NG连接和UU连接资源，造成相关用户的业务中断。

**适用NF：AMF**

当AMF发生局部故障（比如个别业务进程异常）或者整体故障恢复后，会向NG-RAN发送RESET消息以同步UE的状态；NG-RAN收到AMF的RESET消息后，会释放指定用户的上下文（包括NG连接和UU连接资源）。该命令用于测试或者特殊运维场景下触发NG Reset流程。

## 注意事项

- 该命令执行后立即生效。

- NG-RAN收到AMF的RESET消息后将立即释放相关UE的NG连接和UU连接资源，造成用户业务中断，故本命令应在充分评估影响后执行。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                | 参数说明                                                                                                                                                                                                                                                  |
|:--------------|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESETTYPE     | 重置类型                | 可选必选说明：必选参数  参数含义：该参数用于指定Reset类型。  数据来源：本端规划 取值范围： “ResetAll（重置全部）”：重置全部“ResetPart（重置部分）”：重置部分  默认值：无  配置原则：无                                                                                                                                         |
| COUNT         | AN重置数量              | 可选必选说明：可选参数  参数含义：该参数用于指定AN部分reset时reset的数量。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                  |
| NGRANNODETYPE | NG-RAN基站类型          | 可选必选说明：必选参数  参数含义：该参数用于指定NG-RAN基站类型。  数据来源：对端协商 取值范围： “Gnb（gNodeB）”：gNodeB“NgEnb（ng-eNB）”：ng-eNB  默认值：无  配置原则：无                                                                                                                                       |
| PLMNID        | PLMN标识              | 可选必选说明：必选参数  参数含义：该参数用于指定PLMN标识。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                                              |
| GNBTYPE       | gNodeB类型            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB类型。  数据来源：对端协商 取值范围： “Gnb（gNodeB）”：gNodeB  默认值：无  配置原则：无                                                                                                                               |
| GNBID         | gNodeB标识            | 可选必选说明：该参数在"GNBTYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                  |
| NGENBTYPE     | ng-eNB类型            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"时为条件必选参数。  参数含义：该参数用于指定ng-eNB类型。  数据来源：对端协商 取值范围： “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB“ShortMacroNgEnb（ShortMacro ng-eNB）”：ShortMacro ng-eNB“LongMacroNgEnb（LongMacro ng-eNB）”：LongMacro ng-eNB  默认值：无  配置原则：无 |
| MACRONGENBID  | Macro ng-eNB标识      | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~1048575。  默认值：无  配置原则：无                                                                                                                      |
| SHORTNGENBID  | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定ShortMacro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~262143。  默认值：无  配置原则：无                                                                                                             |
| LONGNGENBID   | LongMacro ng-eNB标识  | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定LongMacro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~2097151。  默认值：无  配置原则：无                                                                                                              |
| GNBIDBITLEN   | gNodeB ID有效比特长度     | 可选必选说明：该参数在"GNBTYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定AN有效比特位。  数据来源：对端协商  取值范围：整数类型，取值范围是22~32。  默认值：无  配置原则：无                                                                                                                                          |

## 使用实例

触发NgReset流程通知NG-RAN释放本AMF所有用户的上下文，基站类型为Gnb，PLMN ID为12303，Gnb类型为Gnb，Gnb ID为1179985，gNodeB ID有效比特长度为24的基站。执行如下命令：

```
RST AN: RESETTYPE=ResetAll, NGRANNODETYPE=Gnb, PLMNID=12303, GNBTYPE=Gnb, GNBID=1179985, GNBIDBITLEN=24;
```