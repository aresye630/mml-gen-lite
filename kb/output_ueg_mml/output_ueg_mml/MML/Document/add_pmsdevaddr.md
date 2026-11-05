# 添加PMS设备地址(ADD PMSDEVADDR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为配置类命令，用于在配置数据库中增加一条PMS设备地址信息数据记录。

当需要根据规划，为系统配置PMS Web UI的登录地址时，需要执行本命令。

当系统配置多个PMS设备地址，且FTP参数取值为“NO”时，则每个PMS设备地址均支持提供UPCF Web UI服务。

## 注意事项

- IPv4类型的IP地址不能配置如下非法IP地址：“127.0.0.1”、“0.0.0.0”、“255.255.255.255”、“224.0.0.1”。
- IPv6类型的IP地址不支持混合方式表达，即xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:d.d.d.d，其中x表示一个十六进制数（0～9或A～F），而d.d.d.d表示一个IPv4地址。
- IPv6类型的IP地址不支持以下特殊地址的配置，其中x表示一个十六进制数（0～9或A～F）：

  - 0000:0000:0000:0000:0000:0000:0000:0000
  - FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
  - 0000:0000:0000:0000:0000:0000:0000:0001
  - FFxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
  - FE8x:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
  - FE9x:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
  - FEAx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
  - FEBx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
- PMS/NTS/DRS/HLB/DLB/NLF/LDAP设备的IP地址（包括IPv4地址和IPv6地址）需要唯一，任意两种设备的IP地址不能重复。
- 执行该命令添加PMS设备地址时，需要重启PMS服务后才能生效：
  1. 登录“UPCF MML命令”界面；
  2. 执行**RST MSPROCESS**命令重启PMS服务：

     ```
     RST MSPROCESS: PROCOBJECT=PROCNAME, PROCNAME="CELL_PcfPms";
     ```

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                            |
|:------------|:-------|:------------------------------------------------------------------------------------------------|
| DEVAID      | 设备地址标识 | 可选必选说明：必选参数 参数含义：用于在UPCF配置库中定义一条本地设备地址信息。 取值范围：0～31 默认值：无。 配置原则：无。                              |
| VPNINDEX    | VPN索引  | 可选必选说明：必选参数 参数含义：用于标识CSLB业务IP的VPN索引。 取值范围：0～31 默认值：无。 配置原则：无。                                   |
| IPVER       | IP版本   | 可选必选说明：必选参数 参数含义：用于指定设备IP地址的IP版本类型。 取值范围： IPV4(IPV4)IPV6(IPV6) 默认值：无。 配置原则：无。                   |
| IP          | IPV4地址 | 可选必选说明：可选参数 参数含义：仅当“IP版本”选择“IPV4(IPV4)”时该参数需要配置，用于表示PMS设备的IPv4地址。 取值范围：IPv4地址 默认值：无。 配置原则：无。    |
| IPV6        | IPV6地址 | 可选必选说明：可选参数 参数含义：仅当“IP版本”选择“IPV6(IPV6)”时该参数需要配置，用于表示PMS设备的IPv6地址。 取值范围：IPv6地址 默认值：无。 配置原则：无。    |
| FTP         | FTP    | 可选必选说明：可选参数 参数含义：用于标识是否使用FTP协议。当取值为“Yes”时，不提供PMS WEB UI服务。 取值范围： YES(是)NO(否) 默认值：NO(否)。 配置原则：无。 |
| DESCRIPTION | 描述     | 可选必选说明：可选参数 参数含义：用于描述设备IP地址的用途。 取值范围：长度不超过32位的字符串 默认值：无。 配置原则：无。                                |

## 使用实例

1. 增加IPv4类型的PMS设备地址信息。“设备地址标识”为“1”，“VPN索引”为“1”，“IP版本”为“IPV4(IPV4)”，“IPV4地址”为“192.168.0.130”，“FTP”为“YES(Yes)”，“描述”为“PMS\_IPV4”。

   ```
   ADD PMSDEVADDR: DEVAID=1, VPNINDEX=1, IPVER=IPV4, IP="192.168.0.130", FTP=YES, DESCRIPTION="PMS_IPV4";
   ```
2. 增加IPv6类型的PMS设备地址信息。“设备地址标识”为“2”，“VPN索引”为“2”，“IP版本”为“IPV6(IPV6)”，“IPV6地址”为“2001:0db8:1fff:ffff:ffff:ffff:ffff:ffff”，“FTP”为“NO(No)”，“描述”为“PMS\_IPV6”。

   ```
   ADD PMSDEVADDR: DEVAID=2, VPNINDEX=2, IPVER=IPV6, IPV6="2001:0db8:1fff:ffff:ffff:ffff:ffff:ffff", FTP=NO, DESCRIPTION="PMS_IPV6";
   ```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释                     | 原因分析                                                     | 处理建议                                                                                                                                              |
|------:|:--------------------------|:---------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| 58107 | 设备地址冲突。                   | PMS/NTS/DRS/HLB/DLB/NLF/LDAP设备的IP地址需要唯一，任意两种设备的IP地址不能重复。 | 修改IP地址，重新执行本命令增加设备地址。                                                                                                                             |
| 57816 | 该类型的IP地址已经存在。             | IPv4地址：输入的“IP”已经存在。IPv6地址：输入的“IPV6”已经存在。                 | IPv4地址：执行LST PMSDEVADDR命令查询全部的PMS设备IPv4地址信息。重新执行本命令，并确保输入的“IP”和已存在的不一样。 IPv6地址：执行LST PMSDEVADDR命令查询全部的PMS设备IPv6地址信息。重新执行本命令，并确保输入的“IPV6”和已存在的不一样。 |
| 58206 | 配置的PMSDEVADDR对象数量超过最大数16。 | 当前存在的PMSDEVADDR对象数量超过最大数16。                              | 执行LST PMSDEVADDR命令查询全部的PMS设备地址信息。执行RMV PMSDEVADDR，将不需要的地址信息删除。重新执行本命令，并确保PMSDEVADDR对象数量不超过16。                                                     |