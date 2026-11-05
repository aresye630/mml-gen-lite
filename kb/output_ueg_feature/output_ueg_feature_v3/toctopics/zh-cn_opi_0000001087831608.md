# 激活动态分流规则匹配（UPF）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当运营商想要用户通过动态Traffic Rule、动态DNS Rule或者静态DNS Rule将数据业务分流到本地边缘APP时，需要执行以下操作，开启规则开关，支持对应规则的报文匹配。

适用于UPF。

## 必备事项

前提条件

请仔细阅读动态分流规则匹配（UPF）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET DNSLITEPARA** | 轻量DNS规则匹配开关（DNSLMATCHSW） | ENABLE | 本端规划 | 本参数配置为“ENABLE”后，表示开启DNS Rule开关，支持DNS Rule匹配功能。动态DNS Rule和静态DNS Rule均支持。 |
|  | 轻量DNS策略执行开关（DNSLPOLICYSW） | ENABLE | 本端规划 | 本参数配置为“ENABLE”后，如果DNS Rule匹配成功，则支持UE发起DNS查询并响应。 |
|  | DNS规则状态控制开关（DNSRULESTATSW） | ENABLE | 本端规划 | 该参数仅对静态DNS Rule生效，即静态DNS规则是否通过命令控制。   * 本参数配置为“ENABLE”后，则支持由命令控制静态DNS Rule的激活状态，MPF初次会将DNS Rule置为去激活状态，后续通过**ACT DNSRULE**命令激活状态、**DEA DNSRULE**命令去激活状态。 * 本参数配置为DISABLE后，则静态DNS Rule为激活状态，状态不会改变。 |
| **ADD DNSRULE** | 应用标识(APPLICATIONID) | app3 | 与对端协商 | 与对端SMF协商一致。 |
|  | DNS规则名称(DNSRULENAME) | rule3 | 本端规划 | UPF本地配置的静态DNS Rule。 |
|  | 域名（DOMAIN） | example.com | 与对端协商 | APP域名。 |
|  | IP地址类型（IPVERSION） | IPV4 | 全网规划 | - |
|  | IPv4地址（IPV4ADDRESS） | 192.168.1.8 | 与对端协商 | APP的IP地址。 |
|  | DNS TTL（DNSTTL） | 3 | 本端规划 | - |
| **SET APPTRAFFICPARA** | 应用流量规则开关（TRAFFICRULESW） | ENABLE | 本端规划 | 当“规则来源”设置为“DYNAMIC\_TRAFFIC\_RULE”，表示使用动态Traffic Rule进行规则匹配，携带IP地址的数据报文命中动态Traffic Rule进行本地分流。此时，DNS Rule衍生的基于目的IP地址本地分流功能不生效。  当“规则来源”设置为“DNS\_RULE\_EXTENDED”，表示使用DNS Rule衍生的IP地址匹配，携带IP地址的数据报文命中DNS Rule的IP地址进行本地分流。此时，动态Traffic Rule不生效。  说明：  基于动态Traffic Rule的分流功能和DNS Rule衍生的基于目的IP的本地分流功能不能同时生效，默认配置为“DYNAMIC\_TRAFFIC\_RULE”。 |
|  | 规则来源（RULESOURCE） | DYNAMIC\_TRAFFIC\_RULE | 本端规划 |  |

## 操作步骤

* 配置使用动态Traffic Rule进行业务匹配

  **SET APPTRAFFICPARA**
* 配置使用动态DNS Rule进行业务匹配。

  **SET DNSLITEPARA**

  **SET APPTRAFFICPARA**
* 配置使用静态DNS Rule进行业务匹配。

  **SET DNSLITEPARA**

  **ADD DNSRULE**

  **SET APPTRAFFICPARA**

## 任务示例

任务描述

任务一：配置使用动态Traffic Rule进行业务匹配。

任务二：配置使用动态DNS Rule和动态Traffic Rule进行业务匹配。

任务三：配置使用静态DNS Rule和动态Traffic Rule进行业务匹配。

脚本

//任务一：配置使用动态Traffic Rule进行业务匹配。

```
SET APPTRAFFICPARA: TRAFFICRULESW=ENABLE, RULESOURCE=DYNAMIC_TRAFFIC_RULE;
```

//任务二：配置使用动态DNS Rule和动态Traffic Rule进行业务匹配。该配置下，支持DNS请求消息命中动态DNS Rule，携带IP的业务流命中动态Traffic Rule进行本地分流。

```
SET DNSLITEPARA: DNSLMATCHSW=ENABLE, DNSLPOLICYSW=ENABLE;
SET APPTRAFFICPARA: TRAFFICRULESW=ENABLE, RULESOURCE=DYNAMIC_TRAFFIC_RULE;
```

//任务三：配置使用静态DNS Rule和动态Traffic Rule进行业务匹配。该配置下，支持DNS请求消息命中静态DNS Rule，携带IP的业务流命中动态Traffic Rule进行本地分流。

```
SET DNSLITEPARA:DNSLMATCHSW=ENABLE,DNSLPOLICYSW=ENABLE,DNSRULESTATSW=DISABLE;
ADD DNSRULE:APPLICATIONID="app3",DNSRULENAME="rule3",DOMAIN="example.com",IPVERSION=IPV4,IPV4ADDRESS="10.1.1.1",DNSTTL=3;
SET APPTRAFFICPARA: TRAFFICRULESW=ENABLE, RULESOURCE=DYNAMIC_TRAFFIC_RULE;
```

版权所有 © 华为技术有限公司
