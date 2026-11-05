# 显示会话管理的用户信息（DSP SMUSERINFO）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

执行该命令时，将可能产生大量详单信息。

执行该命令时，将可能会占用大量系统内存，短时间内连续执行该命令可能会影响系统业务正常运行。如果需要使用该命令请联系华为技术支持。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询SMF/PGW-C/SGW-C/GGSN-C的用户信息。

## 注意事项

查询的用户信息并不保障能查出所有会话。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识      | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                       |
|:----------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN       | APN名称   | 可选必选说明：必选参数  参数含义：该参数用于指定APN名称。表示查询该APN下用户上下文信息。使用用户请求的APN对应的上报属性中“上报给话统的APN名”参数的取值，即在SET CPAPNREPORTATTR命令中设置的该APN的PERFORMANCE的取值，指定使用用户请求的APN还是真实的APN进行统计。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。  默认值：无  配置原则：无                                                                                                            |
| RATTYPE   | 无线接入类型  | 可选必选说明：可选参数  参数含义：该参数用于指定无线接入类型。  数据来源：本端规划 取值范围： EUTRAN（演进型通用陆地无线接入网）HSPA（高速分组接入）WLAN（无线局域网）GAN（通用访问网络）EHRPD（演进的高速包数据网络）EUTRAN_NB_IOT（窄带物联网）UTRAN（通用陆地无线接入网）GERAN（GSM/EDGE无线接入网）NGRAN（5G无线接入网）REDCAP（轻量化5G）  默认值：无  配置原则：无                                                                                                |
| ROAMING   | 漫游状态    | 可选必选说明：可选参数  参数含义：该参数用于指定用户漫游状态。  数据来源：本端规划 取值范围： HOME（本地用户）ROAMING（漫游用户）VISITING（拜访用户）  默认值：无  配置原则：无                                                                                                                                                                                                                     |
| SRUDRTYPE | Srudr类型 | 可选必选说明：可选参数  参数含义：该参数用于指定SRUDR（Secondary RAT Usage Data Report ）类型。  数据来源：本端规划 取值范围： PGW_WITH_SRUDR（PGW接收到Secondary RAT Usage 5G流量上报的承载信息）SPGW_WITH_SRUDR（SPGW接收到Secondary RAT Usage 5G流量上报的承载信息）SGW_WITH_SRUDR（SGW接收到Secondary RAT Usage 5G流量上报的承载信息）SMF_WITH_SRUDR（SMF接收到Secondary RAT Usage 5G流量上报的承载信息）  默认值：无  配置原则：无 |

## 使用实例

显示APN为“huawei.com”的用户信息：

```
%%DSP SMUSERINFO: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
IMSI             IMEI  MSISDN         EBI或者NSAPI  PDU会话ID  用户IP类型  用户IPv4地址  用户IPv6地址  IPv4地址的域标识  POD名称  SMF网元形态  用户激活时间  AMF服务网络功能标识  UPF标识  无线接入类型  
    
123030005003087  NULL  8613900050030  NULL          5          IPv4        192.168.0.1   ::            NULL              sm2-pod-1  SMF          2023-08-31 15:45:56  d3e61349-aba7-0005-af06-db53ebeae81b  upf_instance_100  NGRAN
123030005005905  NULL  8613900050059  NULL          5          IPv4        192.168.0.1   ::            NULL              sm2-pod-1  SMF          2023-08-31 15:46:10  d3e61349-aba7-0005-af06-db53ebeae81b  upf_instance_100  NGRAN
(结果个数 = 2)

---    END
```

## 输出结果说明

| 输出项名称      | 输出项解释                                                                                                                                                                                                                                                                                    |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI       | 该参数用于显示用户永久标识或者国际移动用户标识。                                                                                                                                                                                                                                                                 |
| IMEI       | 该参数用于显示永久设备标识或国际移动设备标识。                                                                                                                                                                                                                                                                  |
| MSISDN     | 该参数用于显示一般公共订阅标识或移动台国际ISDN号码。                                                                                                                                                                                                                                                             |
| EBI或者NSAPI | 该参数用于显示链接的EPS承载标识或者网络层服务接入点标识。                                                                                                                                                                                                                                                           |
| PDU会话ID    | 该参数用于显示PDU会话标识。                                                                                                                                                                                                                                                                          |
| 用户IP类型     | 该参数用于显示用户IP类型。 取值说明： Unknow（Unknow）IPv4（IPv4）IPv6（IPv6）IPv4v6（IPv4v6）Non_IP（Non_IP）Unstructured（Unstructured）Ethernet（Ethernet）                                                                                                                                                          |
| 用户IPv4地址   | 该参数用于显示用户IPv4地址。                                                                                                                                                                                                                                                                         |
| 用户IPv6地址   | 该参数用于显示用户IPv6地址。                                                                                                                                                                                                                                                                         |
| IPv4地址的域标识 | 该参数用于显示IPv4地址的域标识。                                                                                                                                                                                                                                                                       |
| POD名称      | 该参数用于显示POD名称。                                                                                                                                                                                                                                                                            |
| SMF网元形态    | 该参数用于显示SMF网元形态。 取值说明： INVALID（INVALID）SMF（SMF）ISMF（I-SMF）GGSNC（GGSN-C）SGWC（SGW-C）PGWC（PGW-C）SGWC_PGWC（SGW-C/PGW-C）PROXY_SGWC（Proxy SGW-C）PROXY_SGSN（Proxy SGSN）VSMF（VSMF）HSMF（HSMF）MultiDNN_N11SMF（专用DNN N11SMF）MultiDNN_ISMF（专用DNN I-SMF）PROXY_SMF_S8（Proxy SMF S8）PROXY_SMF（Proxy Smf） |
| 用户激活时间     | 该参数用于显示用户激活时间。                                                                                                                                                                                                                                                                           |
| AMF服务NF ID | 该参数用于显示AMF服务NF ID。                                                                                                                                                                                                                                                                       |
| UPF ID     | 该参数用于显示UPF ID。                                                                                                                                                                                                                                                                           |
| 无线接入类型     | 该参数用于显示无线接入类型。                                                                                                                                                                                                                                                                           |