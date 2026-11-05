# 查询计费上下文信息（DSP CPPDPCHGINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询用户在内容计费及PDP计费情况下的上下文信息，检查话单信息或CCR消息信息。

#### 注意事项

所查询到的用户配额用量为SMF/PGW-C上已收集但未上报的部分。这部分配额用量既不是用户上线以来的总流量，也不是上次上报计费中心以来的总流量，而是上次上报计费中心以后从UPF/PGW-U获取的还未上报计费中心的流量。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                           |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBSCRIBERID | 用户标识类型 | 可选必选说明：必选参数 参数含义：指定需要查询的用户标识类型。 数据来源：本端规划 取值范围：枚举类型。 IMSI：用户的IMSI号。MSISDN：用户的MSISDN号。IPv4：用户的IPv4地址。IPv6：用户的IPv6地址。 默认值：无 配置原则：无                               |
| IMSI         | IMSI   | 可选必选说明：条件必选参数 前提条件：该参数在“SUBSCRIBERID”配置为“IMSI”时为必选参数。 参数含义：用户的IMSI号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无 配置原则：配置IMSI表示查询指定IMSI号的用户的计费信息。                   |
| MSISDN       | MSISDN | 可选必选说明：条件必选参数 前提条件：该参数在“SUBSCRIBERID”配置为“MSISDN”时为必选参数。 参数含义：用户的MSISDN号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。 默认值：无 配置原则：配置MSISDN表示查询指定的MSISDN号的用户的计费信息。          |
| IPV4         | IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“SUBSCRIBERID”配置为“IPv4”时为必选参数。 参数含义：用户的IP地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无 配置原则：配置IPv4表示查询指定的IPv4地址的用户的计费信息。                           |
| IPV6         | IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“SUBSCRIBERID”配置为“IPv6”时为必选参数。 参数含义：IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。 默认值：无 配置原则：配置IPv6表示查询指定的IPv6地址的用户的计费信息。 |
| NSAPI        | NSAPI  | 可选必选说明：可选参数 参数含义：用户的NSAPI号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～63。 默认值：无 配置原则：无                                                                                        |

#### 使用实例

查询IMSI号为231011223344551的用户的上下文信息：

```
DSP CPPDPCHGINFO:SUBSCRIBERID=IMSI,IMSI="231011223344551";
```

```
计费上下文信息
-------------------------
Result   =  
                   IMSI = 231011223344551
                 MSISDN = 8613801040011
               IPv4地址 = 192.168.1.1
                  NSAPI = 5
                    APN = huawei
           User profile = huawei
           ChargingType = Prepaid
            CCFH status = 0
                Roaming = Empty
        PDP create time = 2016-03-09 16:01:01
     Last activity time = Empty
     
   Online chargine info:
   --------------------- 
           Rating group = 100
             Service ID = 100
                CC-time = 1000 S
          Total octets  = 1000 B
               Duration = 200 S
         Up-link volume = 0-100 B
       Down-link volume = 0-300 B
             Valid time = 100 S
 Volume quota threshold = 0-200 B
   Time quota threshold = 200 S
  
   Offline charging info:
   --------------------- 
           Rating group = 100
             Service ID = 100
   Time quota mechanism = QCT (10 S)
               Duration = 400 S
         Up-link volume = 100 B
       Down-link volume = 300 B
            Report time = 2016-03-09 16:01:01
      Last charged time = Empty
       Change condition = Threshold
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称                      | 输出项解释                               |
|:---------------------------|:------------------------------------|
| IMSI                       | 国际移动用户标识，当用户接入不携带IMSI时，显示为“NULL”。   |
| MSISDN                     | 用户的MSISDN号。                         |
| IPv4                       | PDP上下文/Session会话IPv4地址。             |
| IPv6                       | PDP上下文/Session会话IPv6地址。             |
| NSAPI                      | 用户的NSAPI。                           |
| APN                        | APN名称。                              |
| User profile               | User profile名称。                     |
| ChargingType               | 运营商定义的计费类型。                         |
| CCFH status                | 用户在线转离线标识。                          |
| Roaming                    | 漫游标识。                               |
| PDP create time            | 用户激活时间。                             |
| Session create time        | 会话激活时间。                             |
| RGApplied                  | SMF与CHF交互时的业务申请上报模式。                |
| Last activity time         | 用户业务结束时间。                           |
| Rating group               | 费率组。                                |
| Quota Management Indicator | 配额管理类型。                             |
| Service ID                 | 服务识别码。                              |
| CC-time                    | 时长配额。                               |
| Total octets               | 流量配额。                               |
| Duration                   | 时长。                                 |
| Up-link volume             | 上行流量。                               |
| Down-link volume           | 下行流量。                               |
| Valid time                 | 配额有效时长。                             |
| Volume quota threshold     | 流量门限值。                              |
| Time quota threshold       | 时长门限值。                              |
| Report time                | 业务容器关闭时间。                           |
| Last charged time          | 业务结束时间。                             |
| Change condition           | 业务容器关闭原因（当业务容器未关闭时，统一显示为openstate）。 |
| dataVolumeUplink           | 5G上行流量。                             |
| dataVolumeDownlink         | 5G下行流量。                             |
| rANStartTime               | 5G业务开始时间。                           |
| rANEndTime                 | 5G业务结束时间。                           |
| secondaryRATType           | 5G接入类型。                             |