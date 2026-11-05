# 增加地址池组映射关系（ADD POOLGRPMAP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加地址池组和UPF组，位置区组（类型和名称）及APN的映射关系。

## 注意事项

- 该命令执行后立即生效。

- 若地址池组对应的类型为UDM、Radius或DHCP（通过LST ADDRPOOLGRP查询），则UPF组名称不能为空。
- 地址池组对应的类型（通过LST ADDRPOOLGRP查询）与UPF组对应的类型（通过LST ADDRUPGROUP查询）必须保持一致。
- 地址池组映射关系包含地址池组名称，UPF组名称，位置区组类型，位置区组名称，APN名称。相同映射（UPF组名称，位置区组类型，位置区组名称，APN组合）只能对应一个地址池组。
- 如映射关系中包含APN，则APN对应的VPN（通过LST APN查询）与地址池组下所有的地址池（通过LST POOLBINDGRP查询）包含的IP类型对应的VPN（通过LST ADDRPOOL查询）必须一致。
- 当前版本不支持此命令的LOCATIONGRPTYPE、LOCATIONGRPNAME参数。
- 参数APN、UPFGRPNAME和LOCATIONGRPTYPE不能同时为空。
- 参数APN、UPFGRPNAME和LOCATIONGRPNAME必须与SET APNIPALLOCRULE或SET IPALLOCRULE的IPV4FIRSTRULE、IPV4SECONDRULE、IPV4THIRDRULE、IPV6FIRSTRULE、IPV6SECONDRULE、IPV6THIRDRULE取值一致，如IPV4FIRSTRULE取值为“APN-1&UPNODE-1”，则参数APN、UPFGRPNAME需要配置，参数LOCATIONGRPNAME不能配置。

- 最多可输入40000条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                                                                                                                                                                            |
|:----------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAPPINGNAME     | 映射名称   | 可选必选说明：必选参数  参数含义：该参数用于指定地址池组映射规则名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。  默认值：无  配置原则：无                                                                                                             |
| POOLGRPNAME     | 地址池组名称 | 可选必选说明：必选参数  参数含义：该参数用于指定地址池组的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。  默认值：无  配置原则：  该参数使用ADD ADDRPOOLGRP命令配置生成。                                                                                    |
| UPFGRPNAME      | UPF组名称 | 可选必选说明：可选参数  参数含义：该参数用于指定UPF组的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾。  默认值：无  配置原则：  该参数使用ADD ADDRUPGROUP命令配置生成。                                                                                        |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：可选参数  参数含义：该参数用于指定映射地址池组的区域类型。  数据来源：本端规划 取值范围： “LAC（LAC）”：使用3G用户的LAC作为位置区。“TAC（TAC）”：使用4G或5G用户的TAC作为位置区。“None（无）”：不使用用户的位置区作为地址分配规则的匹配条件。  默认值：None  配置原则： 配置类型为TAC，LOCATIONGRPNAME必须由ADD ADDRTACGROUP新增。配置类型为LAC，LOCATIONGRPNAME必须由ADD ADDRTACGROUP新增。 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：该参数在"LOCATIONGRPTYPE"配置为"LAC"、"TAC"时为条件必选参数。  参数含义：该参数用于指定位置组名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~32。  默认值：无  配置原则：  该参数使用ADD ADDRTACGROUP或ADD ADDRLACGROUP命令配置生成。                                                                                        |
| APN             | APN名称  | 可选必选说明：可选参数  参数含义：该参数用于指定APN实例名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，其中字母不区分大小写。  默认值：无  配置原则：  该参数使用ADD APN命令配置生成。                                                                                                   |

## 使用实例

增加地址池组和UPF组的映射关系，映射名称是one，地址池组是spoolgrp1，UPF组是upfgrp1。

```
ADD POOLGRPMAP: MAPPINGNAME="one", POOLGRPNAME="spoolgrp1", UPFGRPNAME="upfgrp1";
```