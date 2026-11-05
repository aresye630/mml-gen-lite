# 增加网元业务IP地址(ADD SRVIPADDR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该命令属于高危命令，该操作可能会导致业务中断或者ESN发生变动从而导致License失效。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于增加设备间业务通信的IP地址，包括：

- FE与BE之间
- 主用BE与容灾BE之间
- WebLMT和PGW之间
- 业务发放系统和PGW之间

## 注意事项

- 如果“业务IP类型”为“PGW(PGW)”，则需要根据USCDB连接的业务发放系统和连接PGW Web LMT的IP地址进行相关配置：
  - 业务发放系统和PGW Web LMT的IP属于同一网段，此时，用于连接业务发放系统和PGW Web LMT的IP地址相同，则只需配置“IPV4IP1”。
  - 业务发放系统和PGW Web LMT的IP属于不同网段，则“IPV4IP1”和“IPV4IP2”都需要配置，“IPV4IP1”用于连接业务发放系统，“IPV4IP2”用于连接PGW Web LMT。
- 如果“业务IP类型”为“PGW(PGW)”或“DMA(DMA)”，当增加IP前有FTP或者SFTP服务，则执行本命令后需要在本端Location通过****ACT FTPSERVICE****命令重新激活FTP或SFTP服务。
- 如果“业务IP类型”为“PGW(PGW)”，请在增加IP地址后执行****RST MODULE****重启所有的PGW模块。
- 如果“业务IP类型”为“PRV(PRV)”，请在增加IP地址后执行****RST MODULE****重启所有的PGW模块。
- 如果“业务IP类型”为“DMA(DMA)”或“PGW(PGW)”，在增加IP地址后需要执行**RST MODULE**命令重启对应的DPU模块才能生效。
- 当通过**RMV SRVIPADDR**命令删除“业务IP类型”为“DMA(DMA)”或“PGW(PGW)”的IP地址，又执行该命令增加“业务IP类型”为“DMA(DMA)”或“PGW(PGW)”的IP地址时，建议将对应的“DPU模块号”设置与之前删除的“DPU模块号”相同，此时在增加IP地址后只需要执行**RST MODULE**命令重启对应的DPU模块就能生效。如果不同，在增加IP地址后需要执行如下操作才能生效。
  1. 执行**STP MODULE**命令停止该命令新设置的“DPU模块号”。此处以“模块号”为“40”和“45”举例。

     ```
     STP MODULE: MID=40, MT=DPU;
     STP MODULE: MID=45, MT=DPU;
     ```
  2. 执行如下命令清理DPU进程。

     ```
     CLR MSPROCESS: RANGE=BYNAME, PROCESSNAME="CELL_UdrDpu";
     CLR MSPROCESS: RANGE=BYNAME, PROCESSNAME="CELL_UdrDmaDpu";
     ```
  3. 执行**STR MODULE**命令启动该命令新设置的“DPU模块号”。

     ```
     STR MODULE: MID=40;
     STR MODULE: MID=45;
     ```
- 当“IP类型”为“IPV4(IPV4)”时，地址、网关和子网掩码匹配的IP类型必须为IPv4。
- 当“IP类型”为“IPV6(IPV6)”时，地址、网关和前缀长度匹配的IP类型必须为IPv6。
- 在执行本命令前，请“登录USCDB MML命令界面”执行**LST L3VPNINST**、**LST VPNINSTAF**和**LST AUTOSCALINGSERVICE**命令查询待配置的VPN名称是否在报文中存在，如果**LST L3VPNINST**、**LST VPNINSTAF**和**LST AUTOSCALINGSERVICE**报文中不存在，请使用**ADD L3VPNINST**、**ADD VPNINSTAF**和**ADD AUTOSCALINGSERVICE**命令进行配置。
- 该命令不允许进行批操作。
- BE的ESN信息与License有关，BE的ESN是由首个与该BE对接成功的FE对应的ESN和通过**ADD SRVIPADDR**添加的PGW类型的IP1地址通过加密算法处理后获得。执行该命令可能会导致ESN变动，一旦ESN变动则需要重新申请License文件，请谨慎操作。
- 当“业务IP类型”取值为“DSG(DSG)”时，IP个数需根据交换机是否支持“SCTP协议基于端口号的ECMP负载均衡”功能确定：

  **说明** 

  当交换机不是华为设备时，请联系对应厂商确认交换机是否支持“SCTP协议基于端口号的ECMP负载均衡”功能。

  - 当交换机不支持“SCTP协议基于端口号的ECMP负载均衡”功能时，IP个数需根据IPU虚拟机（裸机场景为IPU POD，UDM和UPCF为cslbipc8-pod，USC为cslbip-pod）个数决定，IPU个数为偶数时，IP数量与IPU个数相同。IPU个数为奇数时，IP数量则为IPU个数加一。
  - 当交换机支持“SCTP协议基于端口号的ECMP负载均衡”功能时，申请1个IP地址。
- 如果IP地址相同，“业务类型”必须不同。

## 参数说明

| 参数标识        | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                                       |
|:------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRVINDEX    | 业务IP索引               | 用于指定业务IP地址对应的业务IP索引。 当指定的“业务IP类型”为“DSG”或“PRV”时，输入的“业务IP索引”不能与已存在的DPU模块号冲突。执行LST MODULE命令查看“模块类型”为“DPU”对应的模块号。 取值范围：1～4080 默认值：无。                                                                                                                                                                           |
| SRVIPTYPE   | 业务IP类型               | 用于指定业务IP类型。 取值范围： DSG(DSG)：表示当前业务IP使用于DSG模块，配置本地Location和远端Location连接时使用。PGW(PGW)：表示当前业务IP使用于PGW模块，配置PGW和业务发放系统或Web LMT连接时使用。DMA(DMA)：表示当前业务IP使用于DMA模块，配置DMA和对端FTP/SFTP服务器连接时使用。PRV(PRV)：表示当前业务IP使用于PGW模块，配置PGW和业务发放系统连接时使用，可以作为PGW和订阅通知客户端IP，支持MML、SOAP和REST业务发放接口，不提供Web LMT和SSH服务，不支持FTP、SFTP接入。 默认值：无。 |
| DPUMID      | DPU模块号               | 用于表示为PGW或DMA提供服务的DPU模块号。仅当本命令中的“业务IP类型”为“PGW”或“DMA”时，该参数有效。DPU模块号先由ADD MODULE命令定义，然后才能在此处索引。 取值范围：1～4080 默认值：无。                                                                                                                                                                                            |
| IPVER       | IP类型                 | 用于表示IP地址类型。 取值范围： IPV4(IPV4)：当系统要求使用IPv4类型的IP地址时选择此选项。 IPV6(IPV6)：当系统要求使用IPv6类型的IP地址时选择此选项。 默认值：无。                                                                                                                                                                                                         |
| IP1VPNNAME  | IP地址1的VPN名称          | 用于指定“本地Location IPV4地址1”或“本地Location IPV6地址1”的VPN名称。该参数必须先由ADD L3VPNINST、ADD VPNINSTAF和ADD AUTOSCALINGSERVICE命令定义后才能在此处引用。 取值范围：长度不超过31的字符串。 默认值：无。                                                                                                                                                        |
| IPV4IP1     | 本地Location IPV4地址1   | 仅当本命令中的“IP类型”参数选择为“IPV4(IPV4)”时该参数有效，用于指定IPv4类型的本地IP地址，由运营商统一规划。 取值范围：IPv4格式的地址。 默认值：无。                                                                                                                                                                                                                    |
| IPV4GW1     | 本地Location IPV4网关1   | 仅当本命令中的“IP类型”参数选择为“IPV4(IPV4)”时该参数有效，用于指定本地IP地址的网关，由运营商统一规划。 取值范围：IPv4格式的地址。 默认值：无。                                                                                                                                                                                                                        |
| IPV4MASK1   | 本地Location IPV4子网掩码1 | 仅当本命令中的“IP类型”参数选择为“IPV4(IPV4)”时该参数有效，用于指定本地IP地址的子网掩码，由运营商统一规划。 取值范围：IPv4格式的地址。 默认值：无。  说明： 此参数值只能输入255.255.255.255。如果不输入或输入其他值，系统均会按255.255.255.255处理。                                                                                                                                                     |
| IPV6IP1     | 本地Location IPV6地址1   | 仅当本命令中的“IP类型”参数选择为“IPV6(IPV6)”时该参数有效，用于指定IPv6类型的本地IP地址，由运营商统一规划。IPv6格式为“xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”，例如：2001:0DB8:02de:0000:0000:0000:0000:0e13。 取值范围：IPv6格式的地址。 默认值：无。                                                                                                                        |
| IPV6GW1     | 本地Location IPV6网关1   | 仅当本命令中的“IP类型”参数选择为“IPV6(IPV6)”时该参数有效，用于指定本地IP地址的网关，由运营商统一规划。IPv6格式为“xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”，例如：2001:0DB8:02de:0000:0000:0000:0000:0e13。 取值范围：IPv6格式的地址。 默认值：无。                                                                                                                            |
| IPV6MASK1   | 本地Location IPV6前缀长度1 | 仅当本命令中的“IP类型”参数选择为“IPV6(IPV6)”时该参数有效，用于指定本地IPv6地址网段的前缀长度，由运营商统一规划。 取值范围：1～128 默认值：无。                                                                                                                                                                                                                       |
| IP2VPNNAME  | IP地址2的VPN名称          | 用于指定“本地Location IPV4地址2”或“本地Location IPV6地址2”的VPN名称。该参数必须先由ADD L3VPNINST、ADD VPNINSTAF和ADD AUTOSCALINGSERVICE命令定义后才能在此处引用。 取值范围：长度不超过31的字符串。 默认值：无。                                                                                                                                                        |
| IPV4IP2     | 本地Location IPV4地址2   | 仅当本命令中的“IP类型”参数选择为“IPV4(IPV4)”时该参数有效，用于指定IPv4类型的本地IP地址，由运营商统一规划。 取值范围：IPv4格式的地址。 默认值：无。                                                                                                                                                                                                                    |
| IPV4GW2     | 本地Location IPV4网关2   | 仅当本命令中的“IP类型”参数选择为“IPV4(IPV4)”时该参数有效，用于指定本地IP地址的网关，由运营商统一规划。 取值范围：IPv4格式的地址。 默认值：无。                                                                                                                                                                                                                        |
| IPV4MASK2   | 本地Location IPV4子网掩码2 | 仅当本命令中的“IP类型”参数选择为“IPV4(IPV4)”时该参数有效，用于指定本地IP地址的子网掩码，由运营商统一规划。 取值范围：IPv4格式的地址。 默认值：无。  说明： 此参数值只能输入255.255.255.255。如果不输入或输入其他值，系统均会按255.255.255.255处理。                                                                                                                                                     |
| IPV6IP2     | 本地Location IPV6地址2   | 仅当本命令中的“IP类型”参数选择为“IPV6(IPV6)”时该参数有效，用于指定IPv6类型的本地IP地址，由运营商统一规划。IPv6格式为“xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”，例如：2001:0DB8:02de:0000:0000:0000:0000:0e13。 取值范围：IPv6格式的地址。 默认值：无。                                                                                                                        |
| IPV6GW2     | 本地Location IPV6网关2   | 仅当本命令中的“IP类型”参数选择为“IPV6(IPV6)”时该参数有效，用于指定本地IP地址的网关，由运营商统一规划。IPv6格式为“xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx”，例如：2001:0DB8:02de:0000:0000:0000:0000:0e13。 取值范围：IPv6格式的地址。 默认值：无。                                                                                                                            |
| IPV6MASK2   | 本地Location IPV6前缀长度2 | 仅当本命令中的“IP类型”参数选择为“IPV6(IPV6)”时该参数有效，用于指定本地IPv6地址网段的前缀长度，由运营商统一规划。 取值范围：1～128 默认值：无。                                                                                                                                                                                                                       |
| SERVICETYPE | 业务类型                 | 用于定义待增加模块的业务类型，即对应的插件包类型。仅当本命令中的“业务IP类型”参数为“DSG”时，该参数有效。该参数在USCDB下唯一，通过LOD FEPLUG命令加载FE插件后在此引用。 取值范围：长度不超过128的字符串。 默认值：无。                                                                                                                                                                                  |

## 使用实例

在某开局场景下，增加本端网元的业务IP地址：

1. 登录“USCDB MML命令”界面。执行**ADD SRVIPADDR**命令，增加“业务IP索引”为“1”，“业务IP类型”为“PGW”，“DPU模块号”为“40”，“IP类型”为“IPV4(IPV4)”，“IP地址1的VPN名称”为“VN1”，“本地Location IPV4地址1”为“192.168.100.1”，“本地Location IPV4网关1”为“192.168.100.0”，“本地Location IPV4子网掩码1”为“255.255.255.255”，“IP地址2的VPN名称”为“VN2”，“本地Location IPV4地址2”为“192.168.200.1”，“本地Location IPV4网关2”为“192.168.200.0”，“本地Location IPV4子网掩码2”为“255.255.255.255”的本端网元业务IP地址：

   ```
   ADD SRVIPADDR: SRVINDEX=1, SRVIPTYPE=PGW, DPUMID=40, IPVER=IPV4, IP1VPNNAME="VN1", IPV4IP1="192.168.100.1", IPV4GW1="192.168.100.0", IPV4MASK1="255.255.255.255", IP2VPNNAME="VN2", IPV4IP2="192.168.200.1", IPV4GW2="192.168.200.0", IPV4MASK2="255.255.255.255";
   ```
2. 增加IP地址后重启所有的PGW模块和对应的DPU模块。
   - 方法一：逐一重启模块。
     1. 登录“USCDB MML命令”界面。
     2. 执行**LST MODULE**命令查询所有“模块类型”为“PGW”的模块的配置信息：

        ```
        LST MODULE: MT=PGW;
        ```

        ```
        %%LST MODULE: MT=PGW;%%
        RETCODE = 0  操作成功

        操作结果如下
        ------------
             模块号  =  7
           模块类型  =  PGW
           业务类型  =  USCDB
        主用Pod名称  =  usdid3aservice380-0
        备用Pod名称  =  usdid3bservice380-0
           模块名称  =  PGW7
        (结果个数 = 1)

        ---    END
        ```
     3. 2.b中执行**LST MODULE**命令查询结果显示只有“模块号”为“7”的模块为PGW模块，执行**RST MODULE**命令重启所有的PGW模块：

        ```
        RST MODULE: MID=7, MT=PGW;
        ```
     4. 执行**RST MODULE**命令重启“模块号”为“40”的DPU模块：

        ```
        RST MODULE: MID=40, MT=DPU;
        ```
   - 方法二：批量重启模块。
     1. 登录“CSP MML命令”界面。
     2. 执行**RST MDUTYPE**命令重启所有“模块类型”为“PGW”的模块，“网元ID”为USCDB网元ID，此处为“380”。

        ```
        RST MDUTYPE: MEID=380, DESC="PGW", HAST=ALL;
        ```
     3. 执行**RST MODULE**命令重启对应的DPU模块。

        重启“网元ID”为“380”，“模块号”为“40”，“Pod名”称为“usdid3aservice380-0”的DPU模块。

        ```
        RST MODULE: MEID=380, MN=40, VMNAME="usdid3aservice380-0";
        ```

        重启“网元ID”为“380”，“模块号”为“40”，“Pod名称”为“usdid3bservice380-0”的DPU模块。

        ```
        RST MODULE: MEID=380, MN=40, VMNAME="usdid3bservice380-0";
        ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                                   | 原因分析                                                                                                                         | 处理建议                                                                                                                                                                                    |
|-------:|:--------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 250098 | 参数取值无效：参数SERVICETYPE的取值不存在，请确认已经成功加载了该FE插件。             | 输入的“业务类型”不存在。                                                                                                                | 通过LST FEPLUG命令查询加载的“FE类型名称”，“FE类型名称”即“业务类型”。 若业务类型加载成功，请在执行该命令时输入正确的业务类型名称。若业务类型加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。                                                                |
| 260069 | IP地址的类型不匹配。                                             | 输入的IP地址类型和“IP类型”参数设置的IP类型不一致。                                                                                                | 请重新输入，确保输入的IP地址类型和“IP类型”参数设置的IP类型一致。                                                                                                                                                    |
| 260194 | 网关类型为DMA的DPU IP已配置。                                     | 当“业务IP类型”为“DMA”，配置两条不同“IP类型”的网元业务IP地址记录时，输入的“DPU模块号”必须相同。                                                                    | 执行LST SRVIPADDR命令，输入“业务IP类型”为“DMA”，查询该条网元业务IP地址记录配置的“DPU模块号”。重新执行本命令，输入查询的“DPU模块号”。                                                                                                     |
| 260457 | 该业务IP类型的IPv4 DPU IP已经配置。                                | 输入的“业务IP类型”已经配置了IPv4地址。                                                                                                      | PGW业务IP类型支持在同一个DPU模块上配置一条IPv4及一条IPv6记录，不允许配置2条或2条以上同样类型的IP记录。DMA业务IP类型支持在同一个DPU模块上配置两条IPv4及两条IPv6记录，不允许配置3条或3条以上同样类型的IP记录。 已配置的IP记录可以执行LST SRVIPADDR命令查询。                               |
| 260458 | 该业务IP类型的IPv6 DPU IP已经配置。                                | 输入的“业务IP类型”已经配置了IPv6地址。                                                                                                      | PGW业务IP类型支持在同一个DPU模块上配置一个IPv4及一个IPv6记录，不允许配置2条或2条以上同样类型的IP记录。DMA业务IP类型支持在同一个DPU模块上配置两条IPv4及两条IPv6记录，不允许配置3条或3条以上同样类型的IP记录。 已配置的IP记录可以执行LST SRVIPADDR命令查询。                               |
| 260511 | 参数取值无效：参数IP1VPNNAME和IP2VPNNAME的取值不能只为空格。                | 输入的“IP地址1的VPN名称”和“IP地址2的VPN名称”只为空格。                                                                                          | 请重新输入“IP地址1的VPN名称”和“IP地址2的VPN名称”，为非全空格的有效值。                                                                                                                                             |
| 260568 | SRVINDEX与DPU模块ID冲突，请添加与DPU模块ID不相同的SRVINDEX。             | 当指定的“业务IP类型”为“DSG”或“PRV”时，输入的“业务IP索引”与已存在的DPU模块号冲突。                                                                          | 执行LST MODULE命令查看“模块类型”为“DPU”对应的模块号。重新执行本命令，当指定的“业务IP类型”为“DSG”或“PRV”时，确保输入的“业务IP索引”与查询出的DPU模块号不一致。                                                                                       |
| 274510 | 要增加的IP地址索引或该类型的IP地址已存在。                                 | 输入的“业务IP索引”已存在。输入的“业务IP索引”和“业务IP类型”组合已经存在。                                                                                   | 执行LST SRVIPADDR命令，查看已存在的“业务IP索引” 和IP地址，重新执行本命令增加IP地址，确保其与查询结果不重复。                                                                                                                       |
| 275069 | 网关类型为PGW的DPU IP已配置。                                     | 当“业务IP类型”为“PGW”，配置两条不同“IP类型”的网元业务IP地址记录时，输入的“DPU模块号”必须相同。                                                                    | 执行LST SRVIPADDR命令，输入“业务IP类型”为“PGW”，查询该条网元业务IP地址记录配置的“DPU模块号”。重新执行本命令，输入查询的“DPU模块号”。                                                                                                     |
| 302007 | 该DPU 模块不存在。                                             | 指定的“DPU模块号”不存在。                                                                                                              | 执行LST MODULE命令确认该DPU模块是否存在，确认不存在后通过ADD MODULE命令加载该模块。                                                                                                                                   |
| 302008 | 参数DPUMID指定的模块的类型不是DPU。                                  | 参数“DPU模块号”指定的模块的类型不是DPU。                                                                                                     | 执行LST MODULE命令查看存在的DPU模块，输入已存在的“DPU模块号”。                                                                                                                                                |
| 302014 | 该DPU IP 配置已存在。                                          | 该DPU IP配置已存在。                                                                                                                | 执行LST SRVIPADDR命令查询该DPU的IP配置，请重新输入正确的IP配置，确保其与查询的DPU IP配置不冲突。                                                                                                                           |
| 302016 | 本地Location IP地址1和本地Location IP地址2重复。                    | 输入的“本地Location IP地址1”和“本地Location IP地址2”相同。                                                                                  | 请重新输入新的“本地Location IP地址1”和“本地Location IP地址2”，确保两者IP不一致。                                                                                                                                 |
| 302587 | IP地址2的VPN名称必须和本地Location IPV4地址2或者本地Location IPV6地址2共存。 | 只输入“IP地址2的VPN名称”，未输入“本地Location IPV4地址2”或“本地Location IPV6地址2”。只输入“本地Location IPV4地址2”或“本地Location IPV6地址2”，未输入“IP地址2的VPN名称”。 | 重新执行本命令，增加IP地址，确保“IP地址2的VPN名称”与“本地Location IPV4地址2”或“本地Location IPV6地址2”，同时配置或同时不配置。                                                                                                    |
| 302588 | 业务IP类型为PRV的IP地址已配置。                                     | “业务IP类型”为“PRV”的IP地址只能配置一条“IP类型”为“IPV4”和一条“IP类型”为“IPV6”的记录。                                                                   | 执行LST SRVIPADDR命令，查询已配置的“业务IP类型”为“PRV”的网元IP地址信息。请配置和当前“IP类型”不一致的“业务IP类型”为“PRV”的网元IP地址记录；或执行RMV SRVIPADDR命令，删除当前“业务IP类型”为“PRV”的网元IP地址记录，然后重新执行本命令。 说明： 执行RMV SRVIPADDR命令可能会导致业务中断，请谨慎操作。 |
| 332602 | 该IP地址已存在。                                               | 该IP地址已配置。                                                                                                                    | 执行LST SRVIPADDR命令，查询已配置的IP地址。重新执行本命令，增加IP地址，确保新增的IP地址不与已配置的IP地址重复。                                                                                                                      |
| 337164 | 只能在一个DPU模块上增加DMA类型IP。                                   | 当“业务IP类型”为“DMA”，配置不同网元业务IP地址记录时，输入的“DPU模块号”必须相同。                                                                             | 执行LST SRVIPADDR命令，输入“业务IP类型”为“DMA”，查询该条网元业务IP地址记录配置的“DPU模块号”。重新执行本命令，输入查询的“DPU模块号”。                                                                                                     |