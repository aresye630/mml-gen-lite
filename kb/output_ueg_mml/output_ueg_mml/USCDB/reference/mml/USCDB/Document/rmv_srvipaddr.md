# 删除网元业务IP地址(RMV SRVIPADDR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

该命令属于高危命令，该操作可能会导致业务中断或者ESN发生变动从而导致License失效。因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于删除网元业务IP地址。

## 注意事项

- 删除“业务IP类型”为“DSG(DSG)”的网元业务IP地址会导致FE和BE或者BE与BE的通信中断，导致业务中断，请谨慎执行此命令。
- 删除“业务IP类型”为“PGW(PGW)”的网元业务IP地址会影响业务发放系统/PGW Web LMT连接和容灾文件传输，导致业务中断，请谨慎执行此命令。
- 删除“业务IP类型”为“PGW(PGW)”的网元业务IP地址会导致UDR ESN变更，从而影响License的使用。
- 删除“业务IP类型”为“DMA(DMA)”的网元业务IP地址会导致对端FTP服务器通信中断，导致业务中断，请谨慎执行此命令。
- 删除“业务IP类型”为“PGW(PGW)”的网元IP地址后，请执行**RST MODULE**重启所有的PGW模块。
- 删除“业务IP类型”为“PRV(PRV)”的网元IP地址后，请执行**RST MODULE**重启所有的PGW模块。
- 删除“业务IP类型”为“DMA(DMA)”或“PGW(PGW)”的网元IP地址后，请执行**RST MODULE**重启对应的DPU模块。
- 如果软参LDAPSWITCH的值为1，删除最后一个“业务IP类型”为“DSG(DSG)”的网元IP地址会导致该网元下的所有DSG模块重启，请谨慎执行此命令。
- 如果IP地址对应的“业务IP类型”是“DSG(DSG)”，且该IP地址被DSG链路中心引用时，不允许删除此IP。可以使用**LST DSGLINKCTRL**命令查询DSG链路中心配置。

- 该命令不允许进行批操作。
- BE的ESN信息与License有关，BE的ESN是由首个与该BE对接成功的FE对应的ESN和通过**ADD SRVIPADDR**添加的PGW类型的IP1地址通过加密算法处理后获得。执行该命令可能会导致ESN变动，一旦ESN变动则需要重新申请License文件，请谨慎操作。
- 使用**LST SRVIPADDR**查询网元业务IP地址配置信息，如有其他“业务IP类型”正在使用该IP地址，系统则不删除该IP地址对应路由。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                |
|:----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRVINDEX  | 业务IP索引 | 标识一个IP地址的关键字段，用于指定需要删除哪一条业务IP索引配置的IP地址。 操作员可以使用LST SRVIPADDR命令查询获得。                                                                                                                                                                                                                                                                 |
| SRVIPTYPE | 业务IP类型 | 标识业务IP的类型，用于指定需要删除哪一业务IP类型配置的业务IP信息。 取值范围： DSG(DSG)：表示当前业务IP使用于DSG模块，配置本地Location和远端Location连接时使用。PGW(PGW)：表示当前业务IP使用于PGW模块，配置PGW和业务发放系统或Web LMT连接时使用。DMA(DMA)：表示当前业务IP使用于DMA模块，配置DMA和对端FTP/SFTP服务器连接时使用。PRV(PRV)：表示当前业务IP使用于PGW模块，配置PGW和业务发放系统连接时使用，可以作为PGW和订阅通知客户端IP，支持MML、SOAP和REST业务发放接口，不提供Web LMT和SSH服务，不支持FTP、SFTP接入。 默认值：无。 |

## 使用实例

删除业务IP地址。

1. 登录“USCDB MML命令”界面，执行**RMV SRVIPADDR**命令删除“业务IP索引”为“1”，“业务IP类型”为“PGW”的IP地址：

   ```
   RMV SRVIPADDR: SRVINDEX=1, SRVIPTYPE=PGW;
   ```

2. 删除IP地址后重启所有的PGW模块和对应的DPU模块。
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

|    错误码 | 错误码解释                                               | 原因分析                                                 | 处理建议                                                                                                                                                                              |
|-------:|:----------------------------------------------------|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 256034 | 记录不存在。                                              | 输入的“业务IP索引”错误。输入的“业务IP类型”错误。输入的“业务IP索引”与“业务IP类型”不匹配。 | 执行LST SRVIPADDR查询已存在的记录，然后执行本命令删除，确保删除的为可查询记录。                                                                                                                                    |
| 275075 | 该DPU模块对应的IP地址已被使用。                                  | 输入的IP已被使用。                                           | 请执行LST NOTIFYCFG命令查询该IP是否有PGW订阅通知配置，确认使用后执行RMV NOTIFYCFG命令进行删除。                                                                                                                   |
| 275156 | IP已被使用，请使用RMV FTPSERVER 删除SERVERIP为此IP的配置。          | 输入的IP已被使用。                                           | 请使用RMV FTPSERVER删除SERVERIP为此IP的配置。                                                                                                                                                |
| 275385 | IP已被使用，请使用RMV RFTPSEVER删除LOCALIP为此IP的配置然后重新配置本地IP。  | 输入的IP已被使用。                                           | 请使用RMV RFTPSERVER删除LOCALIP为此IP的配置。                                                                                                                                                |
| 275386 | IP已被使用，请使用RMV RSFTPSEVER删除LOCALIP为此IP的配置然后重新配置本地IP。 | IP已被使用，请使用RMV RSFTPSEVER删除LOCALIP为此IP的配置然后重新配置本地IP。  | 请使用RMV RSFTPSERVER删除LOCALIP为此IP的配置。                                                                                                                                               |
| 302023 | IP地址已经被其它记录引用。                                      | IP地址已经被其它记录引用。                                       | 此IP被其他记录引用，可执行LST RIPADDR、LST SOAPLNK、LST TCPLNK、LST HTTPLNK、LST PSITE、LST SSOLNK命令查看IP地址是否被引用，确认引用后再执行RMV RIPADDR、RMV SOAPLNK、RMV TCPLNK、RMV HTTPLNK、RMV PSITE、RMV SSOLNK命令进行删除。 |
| 302545 | IP被链路中心使用，请先修改DSG链路中心的IP。                           | 待删除的IP地址已经被链路中心使用。                                   | 执行LST DSGLINKCTRL命令查询DSG链路中心配置，如果要删除此IP，请先修改或删除DSG链路中心配置。                                                                                                                         |