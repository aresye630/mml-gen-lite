# 查询DNS重定向规则配置（DSP DNSREDIRECTRULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查看DNS重定向规则配置信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识           | 参数名称       | 参数说明                                                                                                                                                           |
|:---------------|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE      | 查询类型       | 可选必选说明：必选参数 参数含义：该参数用于指定查询类型。 数据来源：本端规划 取值范围：枚举类型。 APPINSTANCEID：使用app实例号查询。APPNAME：使用app名称查询。MEPID：指定MEP ID操作记录。 默认值：无 配置原则：无                                 |
| APPNAME        | 应用名称       | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“APPNAME” 或 “MEPID”时为必选参数。 参数含义：指定app名称，可以通过DSP APPLICATIONINFO查出所有的app名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无 |
| MEPID          | MEP ID     | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“MEPID”时为必选参数。 参数含义：指定MEP ID，可以通过DSP APPLICATIONINFO查出所有的MEP ID。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无           |
| APPINSTANCEID  | APP实例号     | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“APPINSTANCEID”时为必选参数。 参数含义：指定app实例号，可以通过DSP APPOPERATE查出所有的app实例号。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：无        |
| DISPLAYMODE    | 显示模式       | 可选必选说明：必选参数 参数含义：指定显示模式。 数据来源：本端规划 取值范围：枚举类型。 SUMMARY：查询结果中只显示概要信息，如appName、appInstanceId、规则ID。DETAILS：查询结果中显示详细信息，详见输出结果项说明。 默认值：无 配置原则：无                     |
| REDIRECTRULEID | DNS重定向规则ID | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“DETAILS”时为可选参数。 参数含义：指定DNS重定向规则ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～95。 默认值：无 配置原则：无                                      |

#### 使用实例

查询指定app名称和DNS重定向规则ID的DNS重定向规则详细信息，app名称为“appName1”，DNS重定向规则ID为：“redirectrule49”：

```
DSP DNSREDIRECTRULE:  APPNAME="appName1", DISPLAYMODE=DETAILS, REDIRECTRULEID="redirectrule49";
```

```
RETCODE = 0 操作成功

DNS重定向规则配置
-------------------------------
Result =
DnsRedirect Rule: 
{
"appName": "appName1",
"dnsRedirectRuleId": "redirectrule49",
"domainName": "www.huawei.com",
"ipAddressType": "IP_V4",
"dnsServerIp": "192.168.11.11"
}

(结果个数 = 1)
```

#### 输出结果说明

| 输出项名称             | 输出项解释                         |
|:------------------|:------------------------------|
| appName           | 应用名称。                         |
| dnsRedirectRuleId | DNS重定向规则ID。                   |
| domainName        | 预期匹配的DNS域名。                   |
| ipAddressType     | IP地址类型，包括IP_V4，IP_V6。         |
| dnsServerIp       | 指定用于解析DNS Query请求的域名服务器的IP地址。 |