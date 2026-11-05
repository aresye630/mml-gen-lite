# 迁移PFCP会话（MIG PFCPSESSION）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令仅用于迁移PFCP会话。操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于将指定UPF源路径上的PFCP会话迁移到目标路径。

## 注意事项

- 该命令执行后立即生效。

- 基于UPF迁移时，需通过LCK UPFADDR锁定除目的路径外的其他所有路径（包含源路径），达到路径限制的效果；
- 基于UPF迁移时，如果正在执行迁移任务时发现某个UPF有除目的路径外的其他路径没有被锁定，需要将该UPF从迁移任务中移除；
- 基于UPF迁移时，如果正在执行迁移任务时发现某个UPF所有可选路径的链路都发生故障，需要将该UPF从迁移任务中移除；
- 基于UPF迁移时，对于同一个UPF只能下发一个迁移任务；
- 可以对不同的UPF同时下发迁移任务（限制最大数量为50个）；
- 该命令允许将某UPF的PFCP会话从直连路径迁移至UPG代理路径，或将PFCP会话在UPG代理路径之间迁移，不允许将直连路径设置为PFCP会话迁移的目的路径；
- 基于IMSI号段迁移时，需要通过LCK UPFADDR锁定目的路径，防止新用户选择到该新路径；
- 当配置基于IMSI号段进行迁移时，不支持同时基于UPF进行迁移；
- 基于IMSI号段迁移时，如果需要删除、停止或清除某一个IMSI号段类型迁移任务，指定IMSI号段范围需要与添加迁移任务的STARTIMSI和ENDIMSI完全相同，不支持针对IMSI号段中的一部分进行操作；
- 使用该命令前需配置UPFADDRATTR，通过该配置中的ISPROXY参数，说明直连路径和代理路径的地址。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTIONTYPE     | 操作类型          | 可选必选说明：必选参数  参数含义：该参数用于指定操作类型。  数据来源：本端规划 取值范围： ADD（添加待启动任务）REMOVE（删除待启动任务）START（启动迁移任务）STOP（停止迁移任务）CLEAR（清除已启动任务）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                          |
| MIGTYPE        | 迁移类型          | 可选必选说明：该参数在"ACTIONTYPE"配置为"REMOVE"、"STOP"、"CLEAR"时为条件必选参数。  参数含义：该参数用于指定PFCP会话的迁移类型。  数据来源：本端规划 取值范围： UPF（指定UPF）IMSISEG（指定IMSI号段）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                           |
| ADDMIGTYPE     | 迁移类型          | 可选必选说明：该参数在"ACTIONTYPE"配置为"ADD"时为条件必选参数。  参数含义：该参数用于指定PFCP会话的迁移类型。  数据来源：本端规划 取值范围： UPF（指定UPF）IMSISEG（指定IMSI号段）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                             |
| STARTIMSI      | 起始IMSI        | 可选必选说明：该参数在"ADDMIGTYPE"配置为"IMSISEG"时为条件必选参数。该参数在"MIGTYPE"配置为"IMSISEG"时为条件可选参数。  参数含义：该参数用于指定IMSI号段的起始IMSI，当只有一个IMSI时，起始IMSI和末位IMSI相同。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~15。  默认值：无  配置原则：  STARTIMSI参数每一位只能是数字0-9;当STARTIMSI长度不足15位时，会自动低位补0直到15位。                                                                                                                                                                                                           |
| ENDIMSI        | 终止IMSI        | 可选必选说明：该参数在"ADDMIGTYPE"配置为"IMSISEG"时为条件必选参数。该参数在"MIGTYPE"配置为"IMSISEG"时为条件可选参数。  参数含义：该参数用于标识IMSI号段的最后一个IMSI，包含在号段内。当只有一个IMSI时，起始IMSI和末位IMSI相同。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~15。  默认值：无  配置原则：  ENDIMSI参数每一位只能是数字0-9;当ENDIMSI长度不足15位时，会自动低位补9直到15位。                                                                                                                                                                                                      |
| NFINSTANCENAME | UPF实例名称       | 可选必选说明：该参数在"ADDMIGTYPE"配置为"UPF"时为条件必选参数。该参数在"MIGTYPE"配置为"UPF"时为条件可选参数。  参数含义：该参数用于指定UPF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~36。不区分大小写。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                     |
| UPFIPADDRTYPE  | IP地址类型        | 可选必选说明：该参数在"ADDMIGTYPE"配置为"UPF"时为条件必选参数。  参数含义：该参数用于指定IP地址类型。  数据来源：全网规划 取值范围： IPV4（IPV4）IPV6（IPV6）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                         |
| IPADDRTYPE     | IP地址类型        | 可选必选说明：该参数在"ADDMIGTYPE"配置为"IMSISEG"时为条件可选参数。  参数含义：该参数用于指定IP地址类型。  数据来源：本端规划 取值范围： IPV4（IPV4）IPV6（IPV6）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                     |
| SRCIPV4ADDR    | 迁移源路径IPv4地址   | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV4"时为条件必选参数。  参数含义：该参数用于指定迁移源路径的对端IPv4类型地址。  数据来源：全网规划  取值范围：IPv4地址类型。IPv4支持A，B，C类地址及0.0.0.0。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV4ADDRESS1、IPV4ADDRESS2、IPV4ADDRESS3、IPV4ADDRESS4其中一个相同。                                                                                                                                                                                                                            |
| DSTIPV4ADDR1   | 迁移目的路径IPv4地址1 | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV4"时为条件可选参数。该参数在"IPADDRTYPE"配置为"IPV4"时为条件可选参数。  参数含义：该参数用于指定迁移目的路径的对端IPv4类型地址。  数据来源：全网规划  取值范围：IPv4地址类型。IPv4支持A，B，C类地址及0.0.0.0。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV4ADDRESS1、IPV4ADDRESS2、IPV4ADDRESS3、IPV4ADDRESS4其中一个相同。 需要与SRCIPV4ADDR、DSTIPV4ADDR2、DSTIPV4ADDR3不同。 当DSTIPV4ADDR1、DSTIPV4ADDR2和DSTIPV4ADDR3均为空时，表示迁移至任意路径。                                                                                      |
| DSTIPV4ADDR2   | 迁移目的路径IPv4地址2 | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV4"时为条件可选参数。该参数在"IPADDRTYPE"配置为"IPV4"时为条件可选参数。  参数含义：该参数用于指定迁移目的路径的对端IPv4类型地址。  数据来源：全网规划  取值范围：IPv4地址类型。IPv4支持A，B，C类地址及0.0.0.0。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV4ADDRESS1、IPV4ADDRESS2、IPV4ADDRESS3、IPV4ADDRESS4其中一个相同。 需要与SRCIPV4ADDR、DSTIPV4ADDR1、DSTIPV4ADDR3不同。 当DSTIPV4ADDR1、DSTIPV4ADDR2和DSTIPV4ADDR3均为空时，表示迁移至任意路径。                                                                                      |
| DSTIPV4ADDR3   | 迁移目的路径IPv4地址3 | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV4"时为条件可选参数。该参数在"IPADDRTYPE"配置为"IPV4"时为条件可选参数。  参数含义：该参数用于指定迁移目的路径的对端IPv4类型地址。  数据来源：全网规划  取值范围：IPv4地址类型。IPv4支持A，B，C类地址及0.0.0.0。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV4ADDRESS1、IPV4ADDRESS2、IPV4ADDRESS3、IPV4ADDRESS4其中一个相同。 需要与SRCIPV4ADDR、DSTIPV4ADDR1、DSTIPV4ADDR3不同。 当DSTIPV4ADDR1、DSTIPV4ADDR2和DSTIPV4ADDR3均为空时，表示迁移至任意路径。                                                                                      |
| SRCIPV6ADDR    | 迁移源路径IPv6地址   | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV6"时为条件必选参数。  参数含义：该参数用于指定迁移源路径的对端IPv6类型地址。  数据来源：全网规划  取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV6ADDRESS1、IPV6ADDRESS2、IPV6ADDRESS3、IPV6ADDRESS4其中一个相同。                                                                                                                                       |
| DSTIPV6ADDR1   | 迁移目的路径IPv6地址1 | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV6"时为条件可选参数。该参数在"IPADDRTYPE"配置为"IPV6"时为条件可选参数。  参数含义：该参数用于指定迁移目的路径的对端IPv6类型地址。  数据来源：全网规划  取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV6ADDRESS1、IPV6ADDRESS2、IPV6ADDRESS3、IPV6ADDRESS4其中一个相同。 需要与SRCIPV6ADDR、DSTIPV6ADDR1、DSTIPV6ADDR2不同。 当DSTIPV6ADDR1、DSTIPV6ADDR2和DSTIPV6ADDR3均为空时，表示迁移至任意路径。 |
| DSTIPV6ADDR2   | 迁移目的路径IPv6地址2 | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV6"时为条件可选参数。该参数在"IPADDRTYPE"配置为"IPV6"时为条件可选参数。  参数含义：该参数用于指定迁移目的路径的对端IPv6类型地址。  数据来源：全网规划  取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV6ADDRESS1、IPV6ADDRESS2、IPV6ADDRESS3、IPV6ADDRESS4其中一个相同。 需要与SRCIPV6ADDR、DSTIPV6ADDR1、DSTIPV6ADDR2不同。 当DSTIPV6ADDR1、DSTIPV6ADDR2和DSTIPV6ADDR3均为空时，表示迁移至任意路径。 |
| DSTIPV6ADDR3   | 迁移目的路径IPv6地址3 | 可选必选说明：该参数在"UPFIPADDRTYPE"配置为"IPV6"时为条件可选参数。该参数在"IPADDRTYPE"配置为"IPV6"时为条件可选参数。  参数含义：该参数用于指定迁移目的路径的对端IPv6类型地址。  数据来源：全网规划  取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。  默认值：无  配置原则：  本参数取值与ADD PNFPROFILE命令中的IPV6ADDRESS1、IPV6ADDRESS2、IPV6ADDRESS3、IPV6ADDRESS4其中一个相同。 需要与SRCIPV6ADDR、DSTIPV6ADDR1、DSTIPV6ADDR2不同。 当DSTIPV6ADDR1、DSTIPV6ADDR2和DSTIPV6ADDR3均为空时，表示迁移至任意路径。 |

## 使用实例

- 当希望增加upf1进待迁移队列时，使用如下命令：

  ```
  MIG PFCPSESSION: ACTIONTYPE=ADD, ADDMIGTYPE=UPF, NFINSTANCENAME="upf1", IPADDRTYPE=IPV4, SRCIPV4ADDR="192.168.0.1", DSTIPV4ADDR1="192.168.0.2";
  ```
- 当希望从待迁移队列删除upf1时，使用如下命令：

  ```
  MIG PFCPSESSION: ACTIONTYPE=REMOVE, MIGTYPE=UPF, NFINSTANCENAME="upf1";
  ```
- 当希望开始迁移时，使用如下命令：

  ```
  MIG PFCPSESSION: ACTIONTYPE=START;
  ```
- 当希望停止upf1的迁移时，使用如下命令：

  ```
  MIG PFCPSESSION: ACTIONTYPE=STOP, MIGTYPE=UPF, NFINSTANCENAME="upf1";
  ```
- 当希望清除已启动任务时，使用如下命令：

  ```
  MIG PFCPSESSION: ACTIONTYPE=CLEAR, MIGTYPE=UPF;
  ```