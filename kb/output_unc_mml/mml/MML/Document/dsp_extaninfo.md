# 显示扩展的AN信息（DSP EXTANINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

如果当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于显示在指定的NGAP本端实体接入的NG-RAN基站的扩展信息，例如基站支持的RAT类型等。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称                | 参数说明                                                                                                                                                                                                                                                      |
|:--------------|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NGAPLEIDX     | NGAP实体索引            | 可选必选说明：必选参数  参数含义：该参数用于指定查询的NGAP实体索引。  数据来源：本端规划  取值范围：整数类型，取值范围是0~1023。  默认值：无  配置原则：无                                                                                                                                                                   |
| PODID         | POD ID              | 可选必选说明：可选参数  参数含义：该参数用于标识系统中的POD ID。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                                                                                                                                                  |
| NGRANNODETYPE | NG-RAN基站类型          | 可选必选说明：可选参数  参数含义：该参数用于指定接入的NG-RAN基站类型。  数据来源：对端协商 取值范围： “Gnb（gNodeB）”：gNodeB“NgEnb（ng-eNB）”：ng-eNB  默认值：无  配置原则：无                                                                                                                                        |
| MCC           | 移动国家码               | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。  参数含义：该参数用于指定PLMN的移动国家码。  数据来源：全网规划  取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。  默认值：无  配置原则：无                                                                                                                |
| MNC           | 移动网号                | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。  参数含义：该参数用于指定PLMN的移动网号。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。  默认值：无  配置原则：无                                                                                                             |
| GNODEBTYPE    | gNodeB类型            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB的类型。  数据来源：对端协商 取值范围： “Gnb（gNB）”：gNB  默认值：无  配置原则：无                                                                                                                                        |
| GNODEBID      | gNodeB标识            | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于指定gNodeB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：无                                                                                                                                   |
| GNBIDBITLEN   | gNodeB ID有效比特长度     | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。  参数含义：该参数用于显示gNodeB ID有效比特长度。  数据来源：本端规划  取值范围：整数类型，取值范围是22~32。  默认值：无  配置原则：无                                                                                                                                   |
| NGENBTYPE     | ng-eNB类型            | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"时为条件必选参数。  参数含义：该参数用于指定ng-eNB类型。  数据来源：对端协商 取值范围： “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB“ShortMacroNgEnb（Short Macro ng-eNB）”：Short Macro ng-eNB“LongMacroNgEnb（Long Macro ng-eNB）”：Long Macro ng-eNB  默认值：无  配置原则：无 |
| MACRONGENBID  | Macro ng-eNB标识      | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~1048575。  默认值：无  配置原则：无                                                                                                                          |
| SHORTMNGENBID | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Short Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~262143。  默认值：无  配置原则：无                                                                                                                |
| LONGMNGENBID  | LongMacro ng-eNB标识  | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。  参数含义：该参数用于指定Long Macro ng-eNB标识。  数据来源：对端协商  取值范围：整数类型，取值范围是0~2097151。  默认值：无  配置原则：无                                                                                                                 |

## 使用实例

查询基站类型为Gnb，Gnb类型为Gnb，Gnb ID为1179985，gNodeB ID有效比特长度为24的基站扩展信息，执行如下命令：

```
%%DSP EXTANINFO:NGAPLEIDX=1;%%
RETCODE = 0  操作成功

结果如下
--------
               POD ID  =  NULL
         NGAP实体索引  =  1
       NG-RAN基站类型  =  gNodeB
           移动国家码  =  123
             移动网号  =  45
           gNodeB类型  =  gNodeB
           gNodeB标识  =  1179985
gNodeB ID有效比特长度  =  24
           ng-eNB类型  =  NULL
     Macro ng-eNB标识  =  0
ShortMacro ng-eNB标识  =  0
 LongMacro ng-eNB标识  =  0
          RAN基站名称  =  NGRANNodeName1
          RAT信息列表  =  NULL
(结果个数  =  1)
---    END
```

## 输出结果说明

| 输出项名称               | 输出项解释                                                                                                                                                                       |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| POD ID              | 该参数用于标识系统中的POD ID。                                                                                                                                                          |
| NGAP实体索引            | 该参数用于指定查询的NGAP实体索引。                                                                                                                                                         |
| NG-RAN基站类型          | 该参数用于指定接入的NG-RAN基站类型。 取值说明： “Gnb（gNodeB）”：gNodeB“NgEnb（ng-eNB）”：ng-eNB                                                                                                      |
| 移动国家码               | 该参数用于指定PLMN的移动国家码。                                                                                                                                                          |
| 移动网号                | 该参数用于指定PLMN的移动网号。                                                                                                                                                           |
| gNodeB类型            | 该参数用于指定gNodeB的类型。 取值说明： “Gnb（gNB）”：gNB                                                                                                                                      |
| gNodeB标识            | 该参数用于指定gNodeB标识。                                                                                                                                                            |
| gNodeB ID有效比特长度     | 该参数用于显示gNodeB ID有效比特长度。                                                                                                                                                     |
| ng-eNB类型            | 该参数用于指定ng-eNB类型。 取值说明： “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB“ShortMacroNgEnb（Short Macro ng-eNB）”：Short Macro ng-eNB“LongMacroNgEnb（Long Macro ng-eNB）”：Long Macro ng-eNB |
| Macro ng-eNB标识      | 该参数用于指定Macro ng-eNB标识。                                                                                                                                                      |
| ShortMacro ng-eNB标识 | 该参数用于指定Short Macro ng-eNB标识。                                                                                                                                                |
| LongMacro ng-eNB标识  | 该参数用于指定Long Macro ng-eNB标识。                                                                                                                                                 |
| RAN基站名称             | 该参数用于显示RAN基站名称。                                                                                                                                                             |
| RAT信息列表             | 该参数用于显示RAN支持的RAT类型列表。当基站支持卫星接入时，基站会在NG SETUP REQUEST消息里按TAI粒度携带支持的RAT Information。本参数显示的内容为各TAI支持的RAT Information汇总后的结果。                                                    |