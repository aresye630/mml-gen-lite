# 显示媒体中继告警详情（DSP RELAYALMDETAIL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于显示媒体中继告警详情。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                |
|:----------------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PODNAME         | Pod名称      | 可选必选说明：可选参数 参数含义：该参数用来指定Pod名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                          |
| ALARMTYPE       | 告警类型       | 可选必选说明：必选参数 参数含义：该参数用于指定告警类型。 数据来源：本端规划 取值范围：枚举类型。 RELAY_RESOURCE_ALARM：资源过载告警。RELAY_SERVICE_FAULT：业务故障告警。RELAY_DNS_SERVER_NO_RESPONSE：dns服务器无响应告警。RELAY_CPU_OVERLOAD：CPU过载告警。 默认值：无 配置原则：无                                                                                                                                                                         |
| RESOURCETYPE    | 资源类型       | 可选必选说明：条件可选参数 前提条件：该参数在“ALARMTYPE”配置为“RELAY_RESOURCE_ALARM”时为可选参数。 参数含义：该参数用于指定资源类型。 数据来源：本端规划 取值范围：枚举类型。 ALL：ALL。FLOW_TABLE：流表资源。HTTP_REQUEST：HTTP请求资源。PBUFFER：PBuffer 资源。TCP_SOCKET：TCP Socket资源。DNS_DOMAIN_NODE：DNS Domain节点资源。DNS_DOMAIN_HASHNODE：DNS Domain哈希节点资源。IPV4_ADDRESS_POOL：IPv4地址池资源。IPV6_ADDRESS_POOL：IPv6地址池资源。TLS_CONNECTION：TLS连接资源。 默认值：无 配置原则：无 |
| RELAYDOMAINNAME | 媒体中继域名配置名称 | 可选必选说明：条件可选参数 前提条件：该参数在“ALARMTYPE”配置为“RELAY_SERVICE_FAULT”时为可选参数。 参数含义：该参数用于设置媒体中继域名配置名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                               |
| SERVICETYPE     | 业务类型       | 可选必选说明：条件可选参数 前提条件：该参数在“ALARMTYPE”配置为“RELAY_SERVICE_FAULT”时为可选参数。 参数含义：该参数用于指定业务类型。 数据来源：本端规划 取值范围：枚举类型。 ALL：ALL。RELAY_URL_AUTH_ALARM：URL鉴权失败告警。RELAY_REFER_CHECK_ALARM：Referer校验失败告警。RELAY_PULL_ALARM：媒体中继回源失败告警。RELAY_UNKNOWN_MEDIA_TYPE：未知类型的媒体访问告警。USER_RELAY_REQUEST_FAILURE：用户媒体中继请求失败告警。 默认值：无 配置原则：无                                                        |
| DNSSERVERNAME   | DNS服务名称    | 可选必选说明：条件可选参数 前提条件：该参数在“ALARMTYPE”配置为“RELAY_DNS_SERVER_NO_RESPONSE”时为可选参数。 参数含义：该参数用来指定DNS服务名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                         |

#### 使用实例

假如需要显示一组媒体中继告警详情，则命令如下：

```
%%DSP RELAYALMDETAIL: ALARMTYPE=RELAY_CPU_OVERLOAD;
```

```
%%
RETCODE = 0  操作成功
 
结果如下
------------------------
Pod名称     进程ID  告警类型          子告警类型  媒体中继域名配置名称  媒体中继模板名称  DNS服务名称  告警详情  
 
relay-pod-0  2           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  0           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  6           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  4           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  3           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
relay-pod-0  7           CPU Overload Alarm  NULL            NULL                                        NULL                       NULL             NULL          
(结果个数 = 6)
 
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释           |
|:-----------|:----------------|
| Pod名称      | 用来指定Pod名称。      |
| 进程ID       | 用来指定进程ID。       |
| 告警类型       | 用于指定告警类型。       |
| 子告警类型      | 用来指定子告警类型。      |
| 媒体中继域名配置名称 | 用于设置媒体中继域名配置名称。 |
| 媒体中继模板名称   | 用来显示媒体中继模板名称。   |
| DNS服务名称    | 用来指定DNS服务名称。    |
| 告警详情       | 用于显示告警详情。       |