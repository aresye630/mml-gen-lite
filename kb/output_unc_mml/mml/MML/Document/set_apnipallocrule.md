# 设置基于APN的地址分配规则（SET APNIPALLOCRULE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于配置基于APN的地址分配规则。

## 注意事项

- 该命令执行后立即生效。

- 支持IPv4和IPv6三种地址分配规则优先级配置。
- APNIPALLOCRULE不配置时，ALLOCATTR默认为继承全局。
- 不同优先级的规则不可以配置为相同。
- 三级优先级独立配置，配置低优先级时不要求必须配置高优先级。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：IPV4ALLOCATTR：INHERIT，IPV4FIRSTRULESW：DISABLE，IPV4FIRSTRULE：NULL，IPV4SECONDRULESW：DISABLE，IPV4SECONDRULE：NULL，IPV4THIRDRULESW：DISABLE，IPV4THIRDRULE：NULL，IPV6ALLOCATTR：INHERIT，IPV6FIRSTRULESW：DISABLE，IPV6FIRSTRULE：NULL，IPV6SECONDRULESW：DISABLE，IPV6SECONDRULE：NULL，IPV6THIRDRULESW：DISABLE，IPV6THIRDRULE：NULL。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识             | 参数名称        | 参数说明                                                                                                                                                                                                                                                                              |
|:-----------------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN              | APN名称       | 可选必选说明：必选参数  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，其中字母不区分大小写。  默认值：无。  配置原则：  该参数使用ADD APN命令配置生成。                                                                                                                    |
| IPV4ALLOCATTR    | IPv4地址分配属性  | 可选必选说明：必选参数  参数含义：该参数用于指定该APN是否使用本地IPv4分配规则。  数据来源：本端规划 取值范围： “INHERIT（继承全局规则）”：使用SET IPALLOCRULE命令配置的地址分配全局规则。“LOCAL（使用本APN指定规则）”：使用基于本APN配置的地址分配规则。  默认值：无。  配置原则：无                                                                                                             |
| IPV4FIRSTRULESW  | IPv4第一级规则开关 | 可选必选说明：该参数在"IPV4ALLOCATTR"配置为"LOCAL"时为条件可选参数。  参数含义：该参数用于指定IPv4第一级规则开关，配置使能或去使能IPv4第一优先级规则。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：不使用当前标识作为地址分配规则的匹配条件。“ENABLE（使能）”：使用当前标识作为地址分配规则的匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无                      |
| IPV4FIRSTRULE    | IPv4第一级规则   | 可选必选说明：该参数在"IPV4FIRSTRULESW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定分配IPv4地址的第一优先级规则。  数据来源：本端规划 取值范围： “APN（APN）”：使用会话的APN作为地址池匹配条件。“LOCATION（位置区）”：使用UE的接入位置作为地址池匹配条件。“UPNODE（UP节点）”：使用选择的UPF群组标识作为地址池匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无  |
| IPV4SECONDRULESW | IPv4第二级规则开关 | 可选必选说明：该参数在"IPV4ALLOCATTR"配置为"LOCAL"时为条件可选参数。  参数含义：该参数用于指定IPv4第二级规则开关，配置使能或去使能IPv4第二优先级规则。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：不使用当前标识作为地址分配规则的匹配条件。“ENABLE（使能）”：使用当前标识作为地址分配规则的匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无                      |
| IPV4SECONDRULE   | IPv4第二级规则   | 可选必选说明：该参数在"IPV4SECONDRULESW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定分配IPv4地址的第二优先级规则。  数据来源：本端规划 取值范围： “APN（APN）”：使用会话的APN作为地址池匹配条件。“LOCATION（位置区）”：使用UE的接入位置作为地址池匹配条件。“UPNODE（UP节点）”：使用选择的UPF群组标识作为地址池匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无 |
| IPV4THIRDRULESW  | IPv4第三级规则开关 | 可选必选说明：该参数在"IPV4ALLOCATTR"配置为"LOCAL"时为条件可选参数。  参数含义：该参数用于指定IPv4第三级规则开关，配置使能或去使能IPv4第三优先级规则。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：不使用当前标识作为地址分配规则的匹配条件。“ENABLE（使能）”：使用当前标识作为地址分配规则的匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无                      |
| IPV4THIRDRULE    | IPv4第三级规则   | 可选必选说明：该参数在"IPV4THIRDRULESW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定分配IPv4地址的第三优先级规则。  数据来源：本端规划 取值范围： “APN（APN）”：使用会话的APN作为地址池匹配条件。“LOCATION（位置区）”：使用UE的接入位置作为地址池匹配条件。“UPNODE（UP节点）”：使用选择的UPF群组标识作为地址池匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无  |
| IPV6ALLOCATTR    | IPv6分配属性    | 可选必选说明：必选参数  参数含义：该参数用于指定该APN是否使用本地IPv6分配规则。  数据来源：本端规划 取值范围： “INHERIT（继承全局规则）”：使用SET IPALLOCRULE命令配置的地址分配全局规则。“LOCAL（使用本APN指定规则）”：使用基于本APN配置的地址分配规则。  默认值：无。  配置原则：无                                                                                                             |
| IPV6FIRSTRULESW  | IPv6第一级规则开关 | 可选必选说明：该参数在"IPV6ALLOCATTR"配置为"LOCAL"时为条件可选参数。  参数含义：该参数用于指定IPv6第一级规则开关，配置使能或去使能IPv6第一优先级规则。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：不使用当前标识作为地址分配规则的匹配条件。“ENABLE（使能）”：使用当前标识作为地址分配规则的匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无                      |
| IPV6FIRSTRULE    | IPv6第一级规则   | 可选必选说明：该参数在"IPV6FIRSTRULESW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定分配IPv6地址的第一优先级规则。  数据来源：本端规划 取值范围： “APN（APN）”：使用会话的APN作为地址池匹配条件。“LOCATION（位置区）”：使用UE的接入位置作为地址池匹配条件。“UPNODE（UP节点）”：使用选择的UPF群组标识作为地址池匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无  |
| IPV6SECONDRULESW | IPv6第二级规则开关 | 可选必选说明：该参数在"IPV6ALLOCATTR"配置为"LOCAL"时为条件可选参数。  参数含义：该参数用于指定IPv6第二级规则开关，配置使能或去使能IPv6第二优先级规则。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：不使用当前标识作为地址分配规则的匹配条件。“ENABLE（使能）”：使用当前标识作为地址分配规则的匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无                      |
| IPV6SECONDRULE   | IPv6第二级规则   | 可选必选说明：该参数在"IPV6SECONDRULESW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定分配IPv6地址的第二优先级规则。  数据来源：本端规划 取值范围： “APN（APN）”：使用会话的APN作为地址池匹配条件。“LOCATION（位置区）”：使用UE的接入位置作为地址池匹配条件。“UPNODE（UP节点）”：使用选择的UPF群组标识作为地址池匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无 |
| IPV6THIRDRULESW  | IPv6第三级规则开关 | 可选必选说明：该参数在"IPV6ALLOCATTR"配置为"LOCAL"时为条件可选参数。  参数含义：该参数用于指定IPv6第三级规则开关，配置使能或去使能IPv6第三优先级规则。  数据来源：本端规划 取值范围： “DISABLE（去使能）”：不使用当前标识作为地址分配规则的匹配条件。“ENABLE（使能）”：使用当前标识作为地址分配规则的匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无                      |
| IPV6THIRDRULE    | IPv6第三级规则   | 可选必选说明：该参数在"IPV6THIRDRULESW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于指定分配IPv6地址的第三优先级规则。  数据来源：本端规划 取值范围： “APN（APN）”：使用会话的APN作为地址池匹配条件。“LOCATION（位置区）”：使用UE的接入位置作为地址池匹配条件。“UPNODE（UP节点）”：使用选择的UPF群组标识作为地址池匹配条件。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNIPALLOCRULE查询当前参数配置值。  配置原则：无  |

## 使用实例

设置名为apn1.com的APN实例按照只从APN映射的地址范围分配IPv4地址，其规则为第一优先级按照APN映射的地址范围内分配地址，第二优先级按照从UPNODE映射的地址范围分配地址，IPv6地址分配继承全局配置：

```
SET APNIPALLOCRULE: APN="apn1.com", IPV4ALLOCATTR=LOCAL, IPV4FIRSTRULESW=ENABLE, IPV4FIRSTRULE=APN-1, IPV4SECONDRULESW=ENABLE, IPV4SECONDRULE=UPNODE-1, IPV4THIRDRULESW=DISABLE, IPV6ALLOCATTR=INHERIT;
```