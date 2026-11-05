# 查询流规则配置（DSP TRAFFICRULE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

该命令用于查看流规则配置信息。

#### 注意事项

- 该命令执行后立即生效。
- MPF独立运维场景下，在UPF网元上，QUERYTYPE不支持选择APPINSTANCEID；在MPF网元上，QUERYTYPE不支持选择MEPID。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                                                                         |
|:--------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE     | 查询类型   | 可选必选说明：必选参数 参数含义：该参数用于指定查询类型。 数据来源：本端规划 取值范围：枚举类型。 APPINSTANCEID：使用app实例号查询。APPNAME：使用app名称查询。MEPID：指定MEP ID操作记录。 默认值：无 配置原则：无                               |
| APPINSTANCEID | APP实例号 | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“APPINSTANCEID”时为必选参数。 参数含义：指定app实例号，可以通过DSP APPLICATIONINFO查出所有的app实例号。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～32。 默认值：无 配置原则：无 |
| MEPID         | MEP ID | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“MEPID”时为必选参数。 参数含义：指定MEP ID，可以通过DSP APPLICATIONINFO查出所有的MEP ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无         |
| APPNAME       | 应用名称   | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“APPNAME” 或 “MEPID”时为必选参数。 参数含义：指定应用名称，可以通过DSP APPLICATIONINFO查出所有的应用名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无 |
| DISPLAYMODE   | 显示模式   | 可选必选说明：必选参数 参数含义：指定显示模式。 数据来源：本端规划 取值范围：枚举类型。 SUMMARY：查询结果中只显示概要信息，如appName、appInstanceId、规则ID。DETAILS：查询结果中显示详细信息，详见输出结果项说明。 默认值：无 配置原则：无                   |
| TRAFFICRULEID | 流规则ID  | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“DETAILS”时为可选参数。 参数含义：指定流规则ID。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～95。 默认值：无 配置原则：无                                         |

#### 使用实例

查看指定app实例号和流规则ID的流规则配置的详细信息，app实例号为"app82020613183145689421553251001"，流规则ID为"23456"：

```
DSP TRAFFICRULE: QUERYTYPE=APPINSTANCEID, APPINSTANCEID="app82020613183145689421553251001", DISPLAYMODE=DETAILS, TRAFFICRULEID="23456";
```

```
RETCODE = 0  操作成功

Traffic规则配置
---------------
Traffic Rule Configuration
--------------------------
Result  =  
Traffic Rule:
{
 "appName": "app8",
 "appInstanceId": "app82020613183145689421553251001",
 "trafficRuleId": "23456",
 "filterType": "FLOW",
 "priority": 1,
 "trafficFilter": [
  {
   "ipAddressType": "IP_V4",
   "srcAddress": [
    "192.168.11.11/32"
   ],
   "dstAddress": [
    "192.168.11.12/32"
   ]
  }
 ],
 "action": "PASSTHROUGH",
 "state": "INACTIVE"
}

(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称            | 输出项解释                                                                  |
|:-----------------|:-----------------------------------------------------------------------|
| appName          | 应用名称。                                                                  |
| appInstanceId    | app实例号。                                                                |
| trafficRuleId    | 流规则ID。                                                                 |
| filterType       | 过滤器类型定义，值为FLOW或PACKET。FLOW表示过滤器匹配的是UE发往EPC的报文，反向报文使用相同上下文处理。           |
| priority         | 流规则的优先级。流规则冲突时，使用优先级较高的规则。（范围为1~255）。                                  |
| trafficFilter    | 用于识别需MPF处理的特定流/报文的过滤器。                                                 |
| ipAddressType    | IP地址类型，包括IP_V4，IP_V6。                                                  |
| srcAddress       | 源IP地址或地址范围。对于IPv4格式，源IP地址是一个IP地址加掩码。对于IPv6格式，源IP地址可以是一个IP前缀或IP前缀范围。    |
| dstAddress       | 目的IP地址或地址范围。对于IPv4格式，目的IP地址是一个IP地址加掩码。对于IPv6格式，目的IP地址可以是一个IP前缀或IP前缀范围。 |
| srcPort          | 源端口或端口范围（可以为单个端口，取值范围是0~65535，或是一段X-Y的范围，X小于等于Y）。                      |
| dstPort          | 目的端口或端口范围（可以为单个端口，取值范围是0~65535，或是一段X-Y的范围，X小于等于Y）。                     |
| Protocol         | 流过滤器的协议（如果是数字的话取值为0~255，如果是字符串的话取值为ANY、ICMP、TCP、UDP、GRE）。              |
| Tag              | 基于令牌的流规则使用的令牌。                                                         |
| srcTunnelAddress | 基于GTP隧道的流规则使用的源地址。                                                     |
| tgtTunnelAddress | 基于GTP隧道的流规则使用的目的地址。                                                    |
| srcTunnelPort    | 基于GTP隧道流规则使用的源端口。                                                      |
| dstTunnelPort    | 基于GTP隧道流规则使用的目的端口。                                                     |
| qCI              | 匹配所有QCI相同的报文。                                                          |
| dSCP             | 匹配所有DSCP相同的IPv4报文。                                                     |
| tC               | 匹配所有TC相同的IPv6报文。                                                       |
| action           | 当报文匹配上流过滤器时，用户数据面采取的动作，如DROP、ALLOW、PASSTHROUGH。                        |
| state            | 流规则状态，当值为"ACTIVE"时，表示此流规则可用；当值为"INACTIVE"时，表示此流规则不可用。                  |