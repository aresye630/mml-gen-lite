# 查询DNS规则配置（DSP DNSRULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查看DNS Rule配置信息，包括动态DNS Rule和静态DNS Rule。

#### 注意事项

- 该命令执行后立即生效。
- MPF独立运维场景下，在UPF网元上，QUERYTYPE不支持选择APPINSTANCEID；在MPF网元上，QUERYTYPE不支持选择MEPID。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                             |
|:--------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RULETYPE      | 规则类型    | 可选必选说明：必选参数 参数含义：指定DNS规则类型。 数据来源：本端规划 取值范围：枚举类型。 DYNAMIC：查询动态DNS规则配置信息。STATIC：查询静态DNS规则配置信息。 默认值：无 配置原则：无                                                                                                        |
| QUERYTYPE     | 查询类型    | 可选必选说明：条件必选参数 前提条件：该参数在“RULETYPE”配置为“DYNAMIC”时为必选参数。 参数含义：该参数用于指定查询类型。 数据来源：本端规划 取值范围：枚举类型。 APPINSTANCEID：使用app实例号查询。APPNAME：使用app名称查询。MEPID：指定MEP ID操作记录。 默认值：无 配置原则：无                                          |
| APPINSTANCEID | APP实例号  | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“APPINSTANCEID”时为必选参数。 参数含义：指定app实例号，可以通过DSP APPLICATIONINFO查出所有的app实例号。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：无                                                     |
| MEPID         | MEP ID  | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“MEPID”时为必选参数。 参数含义：指定MEP ID，可以通过DSP APPLICATIONINFO查出所有的MEP ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无                                                             |
| APPNAME       | 应用名称    | 可选必选说明：条件必选参数 前提条件：该参数在“RULETYPE”配置为“STATIC”时为必选参数。 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“APPNAME” 或 “MEPID”时为必选参数。 参数含义：指定应用名称，可以通过DSP APPLICATIONINFO查出所有的应用名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无 |
| DISPLAYMODE   | 显示模式    | 可选必选说明：必选参数 参数含义：指定显示模式。 数据来源：本端规划 取值范围：枚举类型。 SUMMARY：查询结果中只显示概要信息，如appName、appInstanceId、规则ID。DETAILS：查询结果中显示详细信息，详见输出结果项说明。 默认值：无 配置原则：无                                                                       |
| DNSRULEID     | DNS规则ID | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“DETAILS”时为可选参数。 参数含义：指定DNS规则ID，其中静态DNS规则ID是通过ADD DNSRULE命令配置的，可以通过LST DNSRULE命令查询。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～95。 默认值：无 配置原则：无                                        |

#### 使用实例

查询指定app名称和DNS规则ID的静态DNS Rule配置的详细信息，app名称为"app8"，DNS规则ID为"dnsRule1"：

```
DSP DNSRULE: RULETYPE=DYNAMIC, QUERYTYPE=APPNAME, APPNAME="app8", DISPLAYMODE=DETAILS, DNSRULEID="dnsRule1";
```

```
RETCODE = 0  操作成功

DNS规则配置
-----------
Result  =  
Dynamic DNS Rule:
{
 "appName": "app8",
 "appInstanceId": "app82020613183145689421553251001",
 "dnsRuleId": "dnsRule1",
 "domainName": "www.example.com",
 "ipAddressType": "IP_V4",
 "ipAddress": "192.168.3.94",
 "ttl": 99,
 "state": "INACTIVE"
}

(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释                                                       |
|:--------------|:------------------------------------------------------------|
| appName       | 应用名称。                                                       |
| appInstanceId | app实例号。                                                     |
| dnsRuleId     | DNS规则ID。                                                    |
| domainName    | DNS规则的FQDN。                                                 |
| ipAddressType | IP地址类型，包括IP_V6和IP_V4。                                       |
| ipAddress     | DNS规则提供的IP地址。                                               |
| ttl           | IP地址的有效时长，单位是秒。                                             |
| state         | DNS规则状态，当值为"ACTIVE"时，表示此DNS规则可用；当值为"INACTIVE"时，表示此DNS规则不可用。 |