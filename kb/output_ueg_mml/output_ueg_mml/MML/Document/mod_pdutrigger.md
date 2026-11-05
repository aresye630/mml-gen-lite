# 修改PDU会话级的trigger参数（MOD PDUTRIGGER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于修改PDU会话级的trigger参数。

## 注意事项

该命令执行后只对新激活用户生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称           | 参数说明                                                                                                                                                                                                                                                                                                                                                        |
|:----------------|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CCTMPLTNAME     | 融合计费模板名称       | 可选必选说明：必选参数  参数含义：该参数用于指定融合计费模板的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：  该参数使用ADD CCT命令配置生成。                                                                                                                                                                                                                                           |
| QOSCHG          | QoS更新          | 可选必选说明：可选参数  参数含义：该参数用于设置QoS更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                     |
| ULCHG           | 用户位置更新         | 可选必选说明：可选参数  参数含义：该参数用于设置用户位置更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  用户RAT接入类型为UTRAN时不支持ULCHG。                                          |
| SRVNDCHG        | 服务节点更新         | 可选必选说明：可选参数  参数含义：该参数用于设置服务节点更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                    |
| PRACHG          | 区域用户位置上报更新     | 可选必选说明：可选参数  参数含义：该参数用于设置区域用户位置上报更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                |
| PSDATAOFFCHG    | PS数据关闭状态更新     | 可选必选说明：可选参数  参数含义：该参数用于设置PS数据关闭状态更新trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                 |
| UETZCHG         | 用户时区更新         | 可选必选说明：可选参数  参数含义：该参数用于设置用户时区更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                    |
| PLMNCHG         | PLMN更新         | 可选必选说明：可选参数  参数含义：该参数用于设置PLMN更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                    |
| RATCHG          | RAT更新          | 可选必选说明：可选参数  参数含义：该参数用于设置RAT更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                     |
| ADDUPF          | 添加UPF          | 可选必选说明：可选参数  参数含义：该参数用于添加UPF trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  IUPF和SGW-U类型的UPF不计费，不受该trigger的控制且不上报。                               |
| TIMELIMIT       | 时间阈值           | 可选必选说明：可选参数  参数含义：该参数用于设置PDU会话的数据时间阈值trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：  不支持延迟上报。                                                                                                                  |
| VOLUMELIMIT     | 流量阈值           | 可选必选说明：可选参数  参数含义：该参数用于设置PDU会话的数据流量阈值trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：  不支持延迟上报。                                                                                                                  |
| EVENTLIMIT      | 事件阈值           | 可选必选说明：可选参数  参数含义：该参数用于PDU会话的事件阈值trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：  当前版本暂不支持EVENTLIMIT参数。                                                                                                         |
| MAXNUMCCC       | 计费条件改变阈值       | 可选必选说明：可选参数  参数含义：该参数用于设置计费条件改变阈值trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：无                                                                                                                               |
| UCITIMER        | 业务停止时长         | 可选必选说明：可选参数  参数含义：该参数用于配置PDU会话业务停止时长超时trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：  当前版本暂不支持UCITIMER参数。                                                                                                      |
| INSERTISMF      | 插入I-SMF        | 可选必选说明：可选参数  参数含义：该参数用于设置插入I-SMF trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  依赖于SET N40APIVER命令。当I-SMF功能未使能时，该参数不生效。                          |
| REMOVALISMF     | 删除I-SMF        | 可选必选说明：可选参数  参数含义：该参数用于设置删除I-SMF trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  依赖于SET N40APIVER命令。当I-SMF功能未使能时，该参数不生效。                          |
| CHANGEISMF      | 更新I-SMF        | 可选必选说明：可选参数  参数含义：该参数用于设置更新I-SMF trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  依赖于SET N40APIVER命令。当I-SMF功能未使能时，该参数不生效。                          |
| SESSAMBRCHG     | Session AMBR更新 | 可选必选说明：可选参数  参数含义：该参数用于设置会话AMBR更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  使用SET N40APIVER命令使能SESSIONAMBRCHG功能，未使能此功能时SESSAMBRCHG按QOSCHG处理。 |
| SERVPLMNRTCTCHG | 服务PLMN速率控制更新   | 可选必选说明：可选参数  参数含义：该参数用于设置服务PLMN速率控制更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                              |
| APNRATECTRLCHG  | APN速率控制更新      | 可选必选说明：可选参数  参数含义：该参数用于设置APN速率控制更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                 |
| TAICHG          | 跟踪区标识更新        | 可选必选说明：可选参数  参数含义：该参数用于设置用户TAI更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                   |
| CGISAICHG       | CGISAI更新       | 可选必选说明：可选参数  参数含义：该参数用于设置用户CGISAI更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                |
| RAICHG          | RAI更新          | 可选必选说明：可选参数  参数含义：该参数用于设置用户RAI更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                                                                   |

## 使用实例

修改绑定名称“test”的融合计费模板的PDU会话级的trigger参数，QoS变化的trigger为延迟上报。

```
MOD PDUTRIGGER: CCTMPLTNAME="test", QOSCHG=DEFERRED;
```