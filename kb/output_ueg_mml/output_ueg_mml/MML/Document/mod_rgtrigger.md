# 修改RG级的trigger参数（MOD RGTRIGGER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于修改RG级的trigger参数。

## 注意事项

该命令执行后只对新激活用户生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称         | 参数说明                                                                                                                                                                                                                                                                                                            |
|:----------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CCTMPLTNAME     | 融合计费模板名称     | 可选必选说明：必选参数  参数含义：该参数用于指定CCT模板的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无  配置原则：  该参数使用ADD CCT命令配置生成。                                                                                                                                                                                                |
| QOSCHG          | QoS更新        | 可选必选说明：可选参数  参数含义：该参数用于设置QoS更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                         |
| ULCHG           | 用户位置更新       | 可选必选说明：可选参数  参数含义：该参数用于设置用户位置更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                        |
| SRVNDCHG        | 服务节点更新       | 可选必选说明：可选参数  参数含义：该参数用于设置服务节点更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                        |
| PRACHG          | 区域用户位置上报更新   | 可选必选说明：可选参数  参数含义：该参数用于设置区域用户位置上报更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                    |
| PSDATAOFFCHG    | PS数据关闭状态更新   | 可选必选说明：可选参数  参数含义：该参数用于设置3GPP PS数据关闭状态更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无               |
| UETZCHG         | 用户时区更新       | 可选必选说明：可选参数  参数含义：该参数用于设置用户时区更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                        |
| PLMNCHG         | PLMN更新       | 可选必选说明：可选参数  参数含义：该参数用于设置PLMN更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                        |
| RATCHG          | RAT更新        | 可选必选说明：可选参数  参数含义：该参数用于设置RAT更新的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                         |
| TIMELIMIT       | 时间阈值         | 可选必选说明：可选参数  参数含义：该参数用于设置RG级时间阈值的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                       |
| VOLUMELIMIT     | 流量阈值         | 可选必选说明：可选参数  参数含义：该参数用于设置RG级流量阈值的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                       |
| EVENTLIMIT      | 事件阈值         | 可选必选说明：可选参数  参数含义：该参数用于设置RG级事件阈值的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：  当前版本暂不支持EVENTLIMIT参数。 |
| QUOTATHRESHOLD  | 配额阈值         | 可选必选说明：可选参数  参数含义：该参数用于设置RG级配额阈值的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：无                                                                                    |
| VT              | 配额有效时长       | 可选必选说明：可选参数  参数含义：该参数用于设置RG级配额有效时长的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：无                                                                                  |
| QHT             | 配额保持时长       | 可选必选说明：可选参数  参数含义：该参数用于设置RG级配额保持时长的trigger上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量  默认值：无  配置原则：无                                                                                  |
| SERVPLMNRTCTCHG | 服务PLMN速率控制更新 | 可选必选说明：可选参数  参数含义：该参数用于设置RG级服务PLMN速率控制更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无               |
| APNRATECTRLCHG  | APN速率控制更新    | 可选必选说明：可选参数  参数含义：该参数用于设置RG级APN速率控制更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                  |
| TAICHG          | 跟踪区标识更新      | 可选必选说明：可选参数  参数含义：该参数用于设置用户TAI更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                       |
| CGISAICHG       | CGISAI更新     | 可选必选说明：可选参数  参数含义：该参数用于设置用户CGISAI更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                    |
| RAICHG          | RAI更新        | 可选必选说明：可选参数  参数含义：该参数用于设置用户RAI更新trigger的上报方式。  数据来源：本端规划 取值范围： “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。“IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。“DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。  默认值：无  配置原则：无                       |

## 使用实例

修改名为“test”的CCT融合计费模板的RG级的trigger参数。

```
MOD RGTRIGGER: CCTMPLTNAME="test", QOSCHG=DEFERRED;
```