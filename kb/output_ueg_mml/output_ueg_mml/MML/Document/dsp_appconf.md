# 显示APP实例配置信息（DSP APPCONF）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

该命令用于查看APP实例的配置信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                    |
|:--------------|:-------|:--------------------------------------------------------------------------------------------------------|
| APPINSTANCEID | APP实例号 | 可选必选说明：必选参数 参数含义：指定APP实例号，可以通过DSP APPOPERATE查出所有的APP实例号。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：无 |

#### 使用实例

查看指定APP实例配置信息，APP实例号为"202005090511"：

```
DSP APPCONF: APPINSTANCEID="202005090511";
```

```
RETCODE = 0  操作成功

APP配置信息
-----------
Result  =  {
 "appServiceRequired": [
  {
   "serName": "mecservcie0030",
   "serCategory": {
   "href": "hrefString",
   "id": "id111",
   "name": "nameString",
   "version": "version_1_1"
   },
   "version": "2.0",
   "serTransportDependencies": [
    {
     "transport": {
      "type": "REST_HTTP",
      "protocol": "HTTP",
      "version": "2.0",
      "security": "string"
     },
     "serializers": [
      "JSON"
     ],
     "labels": [
      "string"
     ]
    }
   ],
   "requestedPermissions": "string"
  }
 ],
 "appServiceProduced": [
  {
   "serName": "mecservcie0030",
   "serCategory": {
   "href": "hrefString",
   "id": "id111",
   "name": "nameString",
   "version": "version_1_1"
   },
   "version": "2.0",
   "transportsSupported": [
    {
     "transport": {
      "type": "REST_HTTP",
      "protocol": "HTTP",
      "version": "2.0",
      "security": "string"
     },
     "serializers": "JSON"
    }
   ],
   "dnsRuleIdList": [
    "dnsRule5"
   ],
   "trafficRuleIdList": [
    "TrafficRule5"
   ]
  }
 ],
 "appTrafficRule": [
  {
   "trafficRuleId": "trafficRule5",
   "filterType": "ipv4",
   "priority": 1,
   "trafficFilter": [
    {
     "srcAddress": [
      "192.168.1.1/30"
     ],
     "dstAddress": [
      "192.168.1.2/32"
     ],
     "qCI": 2,
     "dSCP": 1
    }
   ]
  },
  {
   "trafficRuleId": "trafficRule8",
   "filterType": "ipv4",
   "priority": 1,
   "trafficFilter": [
    {
     "srcAddress": [
      "192.168.1.3/30"
     ],
     "dstAddress": [
      "192.168.1.4/32"
     ],
     "qCI": 2,
     "dSCP": 1
    }
   ]
  }
 ],
 "appDNSRule": [
  {
   "dnsRuleId": "dnsRule5",
   "domainName": "www.example5.com",
   "ipAddressType": "IP_V4",
   "ipAddress": "192.168.1.5",
   "ttl": 99
  }
 ]
}
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                    | 输出项解释                                                                                                                                                 |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| appServiceRequired       | 移动边缘应用运行所需的服务。                                                                                                                                        |
| serName                  | 服务名称。                                                                                                                                                 |
| serCategory              | 服务的类别参考。                                                                                                                                              |
| version                  | 服务的版本信息。                                                                                                                                              |
| serTransportDependencies | 使用服务时的传输和序列化格式依赖关系。                                                                                                                                   |
| transport                | 传输绑定关系中的传输信息。                                                                                                                                         |
| type                     | 传输类型（REST_HTTP\WEBSOCKET）。                                                                                                                            |
| protocol                 | 使用的协议名称。                                                                                                                                              |
| version                  | 使用的协议版本。                                                                                                                                              |
| security                 | 传输相关的安全信息。                                                                                                                                            |
| serializers              | 传输绑定关系中的串行器信息。                                                                                                                                        |
| labels                   | 定义传输绑定关系组的标签集。                                                                                                                                        |
| requestedPermissions     | 应用访问服务所需的权限。                                                                                                                                          |
| appServiceProduced       | 移动边缘应用能够为平台或其他移动边缘应用提供的服务。                                                                                                                            |
| transportsSupported      | 服务消费应用可用的传输和序列化格式。                                                                                                                                    |
| dnsRuleIdList            | DNS规则列表。                                                                                                                                              |
| trafficRuleIdList        | 流量规则列表。                                                                                                                                               |
| appFeatureRequired       | 移动边缘应用需要运行的功能。                                                                                                                                        |
| featureName              | 特性名称，如UserApps、UEIdentity。                                                                                                                            |
| transportDependencies    | 平台需为当前应用提供的传输资源（可选），用于交付该应用提供的服务。仅业务提供应用涉及。                                                                                                           |
| appTrafficRule           | 移动边缘应用所需的流量规则。                                                                                                                                        |
| trafficRuleId            | 流量规则ID。                                                                                                                                               |
| filterType               | 过滤器类型定义，值为per FLOW或PACKET。                                                                                                                            |
| priority                 | 流量规则的优先级。流量规则冲突时，使用优先级较高的规则。                                                                                                                          |
| trafficFilter            | 用于识别需MEC主机处理的特定流/报文的过滤器。                                                                                                                              |
| srcAddress               | 源IP地址或地址范围。对于IPv4格式，源IP地址可以是一个IP地址加掩码、IP地址、或IP地址范围。对于IPv6格式,源IP地址可以是一个IP前缀或IP前缀范围。                                                                    |
| dstAddress               | 目的IP地址或地址范围。对于IPv4格式，目的IP地址可以是一个IP地址加掩码、IP地址、或IP地址范围。对于IPv6格式,目的IP地址可以是一个IP前缀或IP前缀范围。                                                                 |
| srcPort                  | 源端口或端口范围。                                                                                                                                             |
| dstPort                  | 目的端口或端口范围。                                                                                                                                            |
| Protocol                 | 流过滤器的协议。                                                                                                                                              |
| Token                    | 基于令牌的流量规则使用的令牌。                                                                                                                                       |
| srcTunnelAddress         | 基于GTP隧道的流量规则使用的源地址。                                                                                                                                   |
| tgtTunnelAddress         | 基于GTP隧道的流量规则使用的目的地址。                                                                                                                                  |
| srcTunnelPort            | 基于GTP隧道流量规则使用的源端口。                                                                                                                                    |
| dstTunnelPort            | 基于GTP隧道流量规则使用的目的端口。                                                                                                                                   |
| qCI                      | 匹配所有QCI相同的报文。                                                                                                                                         |
| dSCP                     | 匹配所有DSCP相同的IPv4报文。                                                                                                                                    |
| tC                       | 匹配所有TC相同的IPv6报文。                                                                                                                                      |
| action                   | 当报文匹配上流过滤器时，MEC主机数据面采取的动作，如DROP、FORWARD、DECAPSULATED、FORWARD_AS_IS、PASSTHROUGH、DUPLICATED_DECAPSULATED、DUPLICATE_AS_IS,参考ETSI GS MEC 010-2 V1.1.1 协议。 |
| dstInterface             | 动作为FORWARD时的目的接口信息。                                                                                                                                   |
| interfaceType            | 接口类型，如TUNNEL, MAC, IP。                                                                                                                                |
| tunnelInfo               | 仅在目的地址类型为tunnel时携带。                                                                                                                                   |
| tunnelType               | 隧道类型，如GTP-U, GRE。                                                                                                                                     |
| tunnelDstAddress         | 隧道的目的地址。                                                                                                                                              |
| tunnelSrcAddress         | 隧道的源地址。                                                                                                                                               |
| srcMACAddress            | 若接口类型为MAC，则源地址为接口的MAC地址。                                                                                                                              |
| dstMACAddress            | 若接口类型为MAC，则目的地址为目的MAC地址。仅用于目的接口。                                                                                                                      |
| dstIPAddress             | 若接口类型为IP，则目的地址为目的IP地址。仅用于目的接口。                                                                                                                        |
| appDNSRule               | 移动边缘应用所需的DNS规则。                                                                                                                                       |
| dnsRuleId                | DNS规则ID。                                                                                                                                              |
| domainName               | DNS规则的FQDN。                                                                                                                                           |
| ipAddressType            | IP地址类型，包括IP_V6和IP_V4。                                                                                                                                 |
| ipAddress                | DNS规则提供的IP地址。                                                                                                                                         |
| ttl                      | 生存时间。                                                                                                                                                 |
| appSupportMp1            | 第三方APP是否支持MP1接口，当前UEG对该参数不处理。                                                                                                                         |