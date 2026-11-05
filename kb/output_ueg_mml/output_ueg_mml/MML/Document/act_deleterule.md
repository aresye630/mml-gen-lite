# 删除规则配置（ACT DELETERULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF、MPF**

**须知** 

本命令属于高危命令，此操作会删除对应分流规则，将导致无法进行本地分流。

该命令用于配置残留场景下删除规则配置。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                                                                                                                                                    |
|:--------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RULENAME      | 规则名称   | 可选必选说明：必选参数 参数含义：指定规则名称。 数据来源：本端规划 取值范围：枚举类型。 DYN_DNS_RULE：删除动态DNS规则的信息。TRAFFIC_RULE：删除流规则的信息。DNS_REDIRECT_RULE：删除DNS重定向规则的信息。ACL_RULE：删除ACL规则的信息。BW_ALLOCATION_RULE：删除带宽分配规则的信息。LBS_RULE：删除负载均衡规则信息。 默认值：无 配置原则：无                      |
| DELETETYPE    | 删除类型   | 可选必选说明：条件必选参数 前提条件：该参数在“RULENAME”配置为“BW_ALLOCATION_RULE”、“DNS_REDIRECT_RULE”、“DYN_DNS_RULE” 或 “TRAFFIC_RULE”时为必选参数。 参数含义：指定删除类型。 数据来源：本端规划 取值范围：枚举类型。 APPINSTANCEID：表示删除类型为app实例号。APPNAME：表示删除类型为app名称。MEPID：指定MEP ID操作记录。 默认值：无 配置原则：无 |
| APPNAME       | 应用名称   | 可选必选说明：条件必选参数 前提条件：该参数在“DELETETYPE”配置为“APPNAME” 或 “MEPID”时为必选参数。 可选必选说明：条件必选参数 前提条件：该参数在“RULENAME”配置为“LBS_RULE” 或 “ACL_RULE”时为必选参数。 参数含义：指定应用名称，可以通过DSP APPLICATIONINFO查出所有的应用名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无        |
| MEPID         | MEP ID | 可选必选说明：条件必选参数 前提条件：该参数在“DELETETYPE”配置为“MEPID”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“RULENAME”配置为“ACL_RULE”时为可选参数。 参数含义：指定MEP ID，可以通过DSP APPLICATIONINFO查出所有的MEP ID。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无                             |
| APPINSTANCEID | APP实例号 | 可选必选说明：条件必选参数 前提条件：该参数在“DELETETYPE”配置为“APPINSTANCEID”时为必选参数。 参数含义：指定app实例号，可以通过DSP APPLICATIONINFO查出所有的app实例号。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：无                                                                           |
| RULEID        | 规则ID   | 可选必选说明：条件可选参数 前提条件：该参数在“RULENAME”配置为“DYN_DNS_RULE”、“TRAFFIC_RULE”、“DNS_REDIRECT_RULE” 或 “BW_ALLOCATION_RULE”时为可选参数。 参数含义：指定规则ID。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～95。 默认值：无 配置原则：无                                                         |

#### 使用实例

- 删除指定app实例号的所有动态DNS规则，APPINSTANCEID="qq12580"：

  ```
  ACT DELETERULE: RULENAME=DYN_DNS_RULE, DELETETYPE=APPINSTANCEID, APPINSTANCEID="qq12580";
  ```
- 删除指定app实例号和规则ID的单条动态DNS规则，APPINSTANCEID="qq12580", RULEID="r96"：

  ```
  ACT DELETERULE: RULENAME=DYN_DNS_RULE, DELETETYPE=APPINSTANCEID, APPINSTANCEID="qq12580", RULEID="r96";
  ```
- 删除指定app名称的所有动态DNS规则，APPNAME="TencentQQ"：

  ```
  ACT DELETERULE: RULENAME=DYN_DNS_RULE, DELETETYPE=APPNAME, APPNAME="TencentQQ";
  ```
- 删除指定app名称和规则ID的所有动态DNS规则，APPNAME="TencentQQ", RULEID="r96"：

  ```
  ACT DELETERULE: RULENAME=DYN_DNS_RULE, DELETETYPE=APPNAME, APPNAME="TencentQQ", RULEID="r96";
  ```