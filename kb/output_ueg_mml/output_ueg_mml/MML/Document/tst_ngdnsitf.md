# DNS客户端查询接口（TST NGDNSITF）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF**

该命令用于测试指定域名能否被解析。

## 注意事项

- 每个域名最多显示128条主机地址。
- 1) 本命令只是测试用户输入的某个指定域名能否被正确的解析，但是解析的域名是否符合流程预期，通过本命令的输出结果无法判断。所以，如果发生由于DNS查询失败导致业务流程失败，而TST NGDNSITF能正常解析对应域名的情况，参考N26接口DNS查询场景分析，检查查询结果中“接口类型”是否与业务流程预期一致。
- -N26接口DNS查询场景分析：
- -（1）5G终端从4G网络接入移动到5G SA网络的移动性注册，AMF查询MME。
- -（2）5G终端在5G SA网络接入切换到4G网络的Handover流程，AMF查询MME。
- -期望的网元类型：MME。
- -期望的接口类型：N26。
- 2) N26/S8接口涉及NAPTR类型查询，SBI接口只涉及AAAA/A类型查询。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:--------------|:----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INTERFACETYPE | 接口类型      | 可选必选说明：必选参数  参数含义：该参数用于表示接口类型。 接口类型为“SBI”测试指定域名能否被解析功能尚未实现。  数据来源：本端规划 取值范围： N26（N26）SBI（SBI）S8（S8）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                              |
| FQDN          | FQDN      | 可选必选说明：该参数在"INTERFACETYPE"配置为"S8"、"N26"时为条件必选参数。  参数含义：该参数用于表示FQDN。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。FQDN不能以“.”开始，也不能以“.”结束。  默认值：无  配置原则：  按照协议RFC1035规定，FQDN最大有效字符数为253，并且每个Label最大长度为63个字节。                                                                                                                                                                                                                                                                      |
| REQUESTTYPE   | 请求类型      | 可选必选说明：该参数在"INTERFACETYPE"配置为"SBI"时为条件必选参数。  参数含义：该参数用于表示请求域名的类型。  数据来源：本端规划 取值范围： FQDN（FQDN类型）HOSTNAME（HOSTNAME类型）  默认值：无  配置原则：  当前系统针对SBI接口仅支持HOSTNAME类型查询。                                                                                                                                                                                                                                                                                                                                                  |
| REQUESTNAME   | 请求值       | 可选必选说明：该参数在"INTERFACETYPE"配置为"SBI"时为条件必选参数。  参数含义：该参数用于表示请求域名的值。  数据来源：本端规划  取值范围：任意类型，取值范围是1~256。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                               |
| RSVTYPE       | 解析类型      | 可选必选说明：该参数在"INTERFACETYPE"配置为"S8"、"N26"时为条件可选参数。  参数含义：该参数用于指定DnsClient的解析类型。  数据来源：本端规划 取值范围： HOSTFILE（主机文件）SERVER（服务器）L1CACHE（L1缓存）L2CACHE（L2缓存）ALL（所有）  默认值：无  配置原则：  设置为“HOSTFILE(主机文件)”，则域名解析的时候查询主机的HOSTFILE。  设置为“SERVER(服务器)”，则域名解析的时候发送解析请求给DNS服务器，查询成功后，L1CACHE上保留查询结果，L2CACHE上不保留查询结果。  设置为“L1CACHE(L1缓存)”，则域名解析的时候查询一级Cache。  设置为“L2CACHE(L2缓存)”，则域名解析的时候查询二级Cache。  设置为“ALL(所有)”，首先查找主机的HOSTFILE中的记录，如果没有相应的记录，再查找GTP-POD上的一级Cache，如果没有相应的记录，再查找LINK节点SGP进程上的二级Cache，如果没有相应的记录，再向DNS服务器发送解析请求进行解析。 |
| IPTYPE        | IP地址类型    | 可选必选说明：该参数在"RSVTYPE"配置为"SERVER"、"ALL"时为条件可选参数。  参数含义：该参数用于指定IP地址类型。  数据来源：全网规划 取值范围： IPV4（IPv4）IPV6（IPv6）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                        |
| LOCIPV4       | 本地IPV4地址  | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。  参数含义：该参数用于指定发送DNS请求消息的本地IPv4地址。如果不输入则随机选择一个ADD DNSLE对应的IP与Server进行交互。  数据来源：全网规划  取值范围：IPv4地址类型。  默认值：无  配置原则：  该参数在“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”时生效。  该参数必须已经通过ADD DNSLE配置。                                                                                                                                                                                                                                                                                          |
| LOCIPV6       | 本地IPV6地址  | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。  参数含义：该参数用于指定发送DNS请求消息的本地IPv6地址。如果不输入则随机选择一个DNSLE绑定的IP与Server进行交互。  数据来源：全网规划  取值范围：IPv6地址类型。  默认值：无  配置原则：  该参数在“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”并且“IP地址类型”配置为“IPV6(IPV6)”时生效。  该参数必须已经通过ADD DNSLE配置。                                                                                                                                                                                                                                                                     |
| LOCPORT       | 本地端口号     | 可选必选说明：该参数在"RSVTYPE"配置为"SERVER"、"ALL"时为条件可选参数。  参数含义：该参数用于指定发送DNS请求消息的本端端口号。如果不输入则在多个相同IP的DNSLE中随机选择一个绑定的IP与Server进行交互。  数据来源：全网规划  取值范围：整数类型，取值范围是15000~65535。  默认值：无  配置原则：  该参数在“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”时生效。  该参数必须已经通过ADD DNSLE配置。                                                                                                                                                                                                                                                                  |
| SRVIPV4       | 服务器IPV4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。  参数含义：该参数用于指定测试的服务器地址。该值对应于LST DNSS的IP地址。当参数“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”时，如果“服务器IPV4地址”未输入，则默认使用第0组服务器组发起查询。  数据来源：全网规划  取值范围：IPv4地址类型。  默认值：无  配置原则：  该参数在“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”时生效。  该参数必须已经通过ADD DNSS配置。                                                                                                                                                                                                                                                 |
| SRVIPV6       | 服务器IPV6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。  参数含义：该参数用于指定测试的服务器地址。该值对应于LST DNSS的IP地址。当参数“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”时，如果“服务器IPV6地址”未输入，则默认使用第0组服务器组发起查询。  数据来源：全网规划  取值范围：IPv6地址类型。  默认值：无  配置原则：  该参数在“解析类型”配置为“SERVER(服务器)”或“ALL(所有)”并且“IP地址类型”配置为“IPV6(IPV6)”时生效。  该参数必须已经通过ADD DNSS配置。                                                                                                                                                                                                                        |

## 使用实例

在N26接口下，查找FQDN为“MMEC22.MMEGI8001.MME.EPC.MNC123.MCC456.3GPPNETWORK.ORG”的IP地址：
2、在SBI接口下，查找FQDN为“TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG”的IP地址：

```
%%TST NGDNSITF: INTERFACETYPE=N26, FQDN="MMEC22.MMEGI8001.MME.EPC.MNC123.MCC456.3GPPNETWORK.ORG";%%
RETCODE = 0  操作成功

结果如下
------------------------
          FQDN  =  MMEC22.MMEGI8001.MME.EPC.MNC123.MCC456.3GPPNETWORK.ORG
      解析类型  =  所有
           TTL  =  0
本端N26 IP地址  =  10.2.92.13
      失败原因  =  NULL
        IP数目  =  2
      主机地址  =  10.6.7.8
      主机地址  =  10.2.3.4
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
(结果个数 = 1)

---    END

2.
%%TST NGDNSITF: INTERFACETYPE=SBI, REQUESTTYPE=FQDN, REQUESTNAME="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG";%%
RETCODE = 0  Operation succeeded

结果如下
------------------------
          FQDN  =  TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG
      解析类型  =  所有
           TTL  =  0
本端N26 IP地址  =  10.2.92.13
      失败原因  =  NULL
        IP数目  =  1
      主机地址  =  10.31.14.3
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
      主机地址  =  NULL
(结果个数 = 1)

---    END
```