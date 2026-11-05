# 修改指定群组的5G LAN会话扩展参数（MOD GRPNGLANFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

该命令用于修改指定会话组NGLAN扩展功能。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                   | 参数说明                                                                                                                                                                                                                                                                                                                                        |
|:----------------|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GROUPID         | 5G LAN组ID              | 可选必选说明：必选参数  参数含义：该参数用于指定5G LAN群组的ID。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~255。字母大小写不敏感且全局唯一。  默认值：无  配置原则：  GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |
| N19SUPPORT      | 是否支持N19通信              | 可选必选说明：可选参数  参数含义：该参数用于控制5G LAN会话的跨园区会话场景下是否支持通过UPF间的N19接口进行通信。  数据来源：本端规划 取值范围： INHERIT（继承）SUPPORT（支持）NOTSUPPORT（不支持）  默认值：无  配置原则：  当此参数配置为INHERIT时继承SET NGLANFUNC配置的N19SUPPORT取值。                                                                                                                                                        |
| PSAPRIFLAG      | 优选5G LAN组内已有的主锚点UPF的开关 | 可选必选说明：可选参数  参数含义：该参数控制是否支持优选5G LAN组内已建立组会话的锚点UPF。  数据来源：本端规划  取值范围：该参数用于控制是否支持优选5G LAN组内已建立组会话的锚点UPF。 INHERIT（继承）SUPPORT（支持）NOTSUPPORT（不支持）  默认值：无  配置原则：  当此参数配置为INHERIT时继承SET NGLANFUNC配置的PSAPRIFLAG取值。                                                                                                                                  |
| MULTICAST       | 是否创建组播PDR规则            | 可选必选说明：可选参数  参数含义：该参数用于控制是否创建组播PDR规则，以支持5G LAN组通过N6接口或N19接口进行组播通信。  数据来源：本端规划 取值范围： INHERIT（继承）SUPPORT（支持）NOTSUPPORT（不支持）  默认值：无  配置原则：  当此参数配置为INHERIT时继承SET NGLANFUNC配置的MULTICAST取值。                                                                                                                                                      |
| N6BROADCASTSW   | 是否支持N6侧上行广播            | 可选必选说明：可选参数  参数含义：该参数用于控制是否为5G LAN PDU会话创建N6上行广播规则，以支持UE与存量网络通过N6接口进行上行广播。  数据来源：全网规划 取值范围： INHERIT（继承）SUPPORT（支持）NOTSUPPORT（不支持）  默认值：无  配置原则：  当此参数配置为INHERIT时继承SET NGLANFUNC配置的N6BROADCASTSW取值。                                                                                                                                          |
| PKTELIMINATESSW | 是否支持报文增殖消除             | 可选必选说明：可选参数  参数含义：该参数用于控制标准5G LAN是否支持报文增殖消除方案，避免报文环回。  数据来源：全网规划 取值范围： INHERIT（继承）SUPPORT（支持）NOTSUPPORT（不支持）  默认值：无  配置原则：  当此参数配置为INHERIT时继承SET NGLANFUNC配置的PKTELIMINATESSW取值。                                                                                                                                                             |
| MACPROCMODE     | MAC地址处理模式              | 可选必选说明：可选参数  参数含义：该参数用于控制UPF上报单播、组播MAC时，SMF的处理模式。  数据来源：全网规划 取值范围： SINGLE（MAC地址单条上报）FULL（MAC地址全量上报）  默认值：无  配置原则：  同一组内该配置需要与UPF上的MAC地址上报方式保持一致。                                                                                                                                                                                            |
| LDRSW           | 环路检测开关                 | 可选必选说明：可选参数  参数含义：该参数用于控制SMF是否支持处理UPF发起的环路检测上报。  数据来源：本端规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无  配置原则：  同一组内该配置建议与UPF上的环路检测开关保持一致。                                                                                                                                                                                                       |
| MACASSEMMODE    | MAC地址组装模式              | 可选必选说明：可选参数  参数含义：该参数用于控制UPF上报单播、组播MAC时，SMF的PDR组装模式。  数据来源：全网规划 取值范围： “SINGLE（MAC地址单条下发）”：MAC地址与PDR一一对应。“FULL（MAC地址全量下发）”：一个PDR中包含单用户全量的MAC地址/单UPF全量的组播MAC地址。  默认值：无  配置原则：  同一组内该配置需要与UPF上的MAC地址组装方式保持一致。                                                                                                                                  |
| N19ENHANCE      | N19 Fullmesh组网增强功能     | 可选必选说明：可选参数  参数含义：该参数用于控制在N19组网下SMF是否支持N19 Fullmesh组网增强功能。开关开启后，5G LAN组内首个终端上线后SMF在组内所有UPF上建立组会话。5G LAN组内所有终端下线后，SMF删除组内所有UPF上的组会话。  数据来源：本端规划 取值范围： NOTSUPPORT（不支持）SUPPORT（支持）  默认值：无  配置原则：  该参数在N19SUPPORT置为SUPPORT时生效；  或N19SUPPORT置为INHERIT且SET NGLANFUNC中N19SUPPORT置为SUPPORT时生效。                                                      |

## 使用实例

将当前GROUPID="A0000001-460-003-01"的记录中的N19SUPPORT和PSAPRIFLAG参数修改为NOTSUPPORT和NOTSUPPORT。

```
MOD GRPNGLANFUNC: GROUPID="A0000001-460-003-01", N19SUPPORT=NOTSUPPORT, PSAPRIFLAG=NOTSUPPORT;
```