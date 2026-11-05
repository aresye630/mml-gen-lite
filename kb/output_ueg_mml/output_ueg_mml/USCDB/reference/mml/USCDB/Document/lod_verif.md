# 加载证书文件(LOD VERIF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**说明** 

- 当**SET NEWCERTSWITCH**的参数“证书开关”取值为“OFF（关闭）”时，**LOD VERIF**命令功能有效，此时PGW作为客户端和服务端的数字证书以及ClickHouse TLS数字证书使用该命令进行加载和更新。
- 当**SET NEWCERTSWITCH**的参数“证书开关”取值为“ON（打开）”时，**LOD VERIF**命令功能无效，此时ClickHouse TLS证书为内部证书，无需加载和更新，PGW作为客户端和服务端数字证书的加载和更新方法请参考产品手册“通过网管MAE-Access加载或更新证书”或“通过OM Portal加载或更新证书”章节。

**SET NEWCERTSWITCH**的参数“证书开关”取值可通过在“CSP MML命令”界面执行**LST NEWCERTSWITCH**命令查询。

该命令用于加载HTTPS安全证书文件或者ClickHouse TLS数字证书文件。

本命令的使用场景为：

- 当客户端（业务发放系统）需要使用HTTPS协议和服务端进行安全通信时，使用此命令对“连接类型”为“SOAP”、“MML”、“HTTP”、THIRDNOTIFY或“REST”的相关数字证书进行加载。

  **说明** 

  - 当客户端通过PGW Web LMT或DMS WebUI使用HTTPS协议与服务端通信，和网元内使用FTPS进行文件传输时，需要使用“连接类型”为“WEBLMT”的“CAVERIF(CA证书)”或“ROOTVERIF(根证书)”、“DEVVERIF(设备证书)”和“KEYFILE(密钥文件)”。
  - 安装USCDB网元时已不再默认加载华为证书文件，客户需要自行申请并部署商用证书文件。
- 当PGW作为客户端需要使用HTTPS协议与服务端（远端站点）进行安全通信时，使用此命令对“连接类型”为“SOAP”或“MML”的相关数字证书进行加载。
- 当ClickHouse服务端和NDF、PGW、DMA和DBG模块使用TLS协议进行通信时，使用此命令对“连接类型”为“PHYDB”的相关字证书进行加载。
- 当需要对证书文件进行替换时，需要先通过**CLR VERIF**清除旧证书后，再使用本命令进行新证书的加载。

## 注意事项

- 在加载SOAP、MML、HTTP、REST或PHYDB类型的证书之前，需要确认如下配置和操作已经完成。

  - 客户已申请到SOAP、MML、HTTP、REST或PHYDB类型的商用证书文件包，并通过OM Portal的文件传输服务上传到“CGPLite文件 > 网元文件”文件夹内。上传方法可参考产品文档中“GUI参考 > 文件传输”。
  - 根据图1所示，通过执行**ADD PORT**命令设置“端口子类型”来为网元添加SOAP、MML、HTTP或REST端口。

    **图1** 数据顺序配置图
- “用途类型”为“SERVER(服务端)”的SOAP类型证书文件加载完成后，还需要通过**MOD INSP**设置“TLSMODE（TLS工作模式）”为“3”（HTTPS模式）。需要指出的是，修改后需要执行**RST MODULE**命令重启所有的PGW进程才能生效。本操作可能会导致短暂的业务发放指令执行失败，为确保系统的安全与稳定运行，除非紧急排除故障的需要，一般建议在系统话务量少的时间段（例如凌晨2:00～4:00）执行，并提前通知客户做好准备。
- “用途类型”为“SERVER(服务端)”的MML类型证书文件加载完成后，还需要通过**ADD PORT**/**MOD PORT**命令设置参数“端口子类型”为“PORT\_FOR\_MML”或“PORT\_FOR\_LMT\_MML” 且“是否使用HTTPS”为“YES”，“MMLTLSAUTHSWITCH（MML TLS鉴权开关）”为“0”（即设置为单向验证）。需要指出的是，修改后需要执行**RST MODULE**命令重启所有的PGW进程才能生效。本操作可能会导致短暂的业务发放指令执行失败，为确保系统的安全与稳定运行，除非紧急排除故障的需要，一般建议在系统话务量少的时间段（例如凌晨2:00～4:00）执行，并提前通知客户做好准备。
- “用途类型”为“CLIENT(客户端)”的SOAP类型或MML类型证书文件加载完成后，还需要通过**ADD PSITE**/**MOD PSITE**命令设置MML或SOAP接口的参数“是否使用HTTPS”为“YES”。需要指出的是，修改后需要执行**RST MODULE**命令重启所有的PGW进程才能生效。本操作可能会导致短暂的业务发放指令执行失败，为确保系统的安全与稳定运行，除非紧急排除故障的需要，一般建议在系统话务量少的时间段（例如凌晨2:00～4:00）执行，并提前通知客户做好准备。
- 证书文件加载成功后，需要手动删除服务器上的证书文件。
- 待加载的证书文件包大小不能超过1MB，证书文件大小不能超过8000字节。
- 待加载的证书文件只支持Pem格式。
- “连接类型”为“WEBLMT”时，执行此命令后需要执行**RST MODULE**命令重启所有PGW模块、所有DMA模块、网关类型为PGW的DPU模块、和DMA类型的DPU模块。
- “连接类型”为“PHYDB”时：
  - 加载服务端证书后，需要执行**RST MODULE**命令，重启全部的NDF模块。
  - 加载客户端证书后，需要执行**RST MODULE**命令，重启全部的NDF、PGW、DMA和DBG模块，不重启全部的NDF、PGW、DMA和DBG模块会上报ALM-14011 连接物理库失败告警。
- 当“证书类型”参数取值为“CRLF(证书吊销列表文件)”时，支持“SOAP”、“HTTP”、“MML”和“REST”类型的HTTPS连接。
- 本命令最多可以添加256条数据记录。
- 密码长期使用会增加被盗窃和破解的风险，而且使用的时间越长，被盗窃和破解的风险越高。定期修改密码可以有效防范这种情况的发生，因此强烈建议您定期修改密码。

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VERIFID     | 证书ID    | 用于指定要加载证书的ID编号。 取值范围：0～1023 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| USTYPE      | 用途类型    | 用于指定要加载的证书用途。 取值范围：SERVER(服务端)：PGW作为服务端用于营帐接入时使用。ClickHouse作为服务端用于PGW、DMA、NDF、DBG模块接入时使用。 CLIENT(客户端)：PGW作为客户端用于将营帐指令转发给远端站点时使用。PGW作为第三方订阅通知客户端时使用。PGW、DMA、NDF、DBG模块作为客户端与ClickHouse服务端使用TLS协议进行通信时使用。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VERIFTYPE   | 证书类型    | 用于指定要加载的证书类型。 该参数的配置原则是：当客户端（业务发放系统）需要使用HTTPS协议和服务端进行安全通信时、当PGW作为客户端需要使用HTTPS协议与服务端（远端站点）进行安全通信时、当ClickHouse服务端和NDF、PGW、DMA和DBG模块使用TLS协议进行通信时或者需要进行证书替换时，需要加载“CAVERIF(CA证书)”、“DEVVERIF(设备证书)”、“KEYFILE(密钥文件)”和“CRLF(证书吊销列表文件)”。 取值范围： “ROOTVERIF(根证书)”：根证书是由认证中心颁发的证书，是证书链的起始点。通常情况下不需要加载此证书。仅当无法保证节点证书（例如“CA证书”）可信时，才需要加载根证书进行验证。“CAVERIF(CA证书)”：认证节点颁发的证书，用于客户端和服务端相互验证合法性。“DEVVERIF(设备证书)”：包含了设备信息和设备公钥证书，用于对端验证本端的身份，并使用公钥加密要发送给对端的信息。“KEYFILE(密钥文件)”：存放在设备的私钥文件，用于服务端和客户端之间消息的加密和解密。“CRLF(证书吊销列表文件)”：证书吊销列表文件，用于在建立TLS/SSL连接时校验对端的设备证书是否在吊销列表中，如果是已经被吊销的证书，则无法建立连接。 说明： “CRLF(证书吊销列表文件)”仅在“用途类型”为“SERVER”时可配置。 默认值：无。                                                                                                                                                                                                                                                                            |
| VPKGNAME    | 证书文件包名称 | 用于指定要加载的证书文件包的名称。 证书文件包名称可从已上传到“网元文件”类别的文件夹内获取。 取值范围：长度不超过128字节的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VNAME       | 证书文件名   | 用于指定要加载的证书文件名。 证书文件名称包含在证书文件包中，可从已上传到“网元文件”类别的文件夹内的证书文件包中获取。 取值范围：长度不超过128字节的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CONNTYPE    | 连接类型    | 仅当本命令中的“证书类型”参数为“ROOTVERIF(根证书)”、“CAVERIF(CA证书)”、“DEVVERIF(设备证书)”、“KEYFILE(密钥文件)”或“CRLF(证书吊销列表文件)”时该参数有效。用于指定要加载的证书用于支持哪种类型的HTTPS连接。 取值范围：MML(MML)：当业务发放系统需要通过MML端口与服务端进行HTTPS通信时、当PGW作为客户端需要通过MML端口使用HTTPS协议与远端站点进行安全通信时或者需要对MML类型的证书文件进行替换时使用。“用途类型”为“SERVER”和“CLIENT”时均可配置。 SOAP(SOAP)：当业务发放系统需要通过SOAP端口与服务端进行HTTPS通信时、当PGW作为客户端需要通过SOAP端口使用HTTPS协议与远端站点进行安全通信时或者需要对SOAP类型的证书文件进行替换时使用。“用途类型”为“SERVER”和“CLIENT”时均可配置。WEBLMT(WEBLMT)：当需要对PGW Web LMT或DMS WebUI类型的证书文件进行加载或替换时使用。“用途类型”为“SERVER”时可配置。REST(REST)：当业务发放系统需要通过REST端口与服务端进行HTTPS通信时或者需要对REST类型的证书文件进行替换时使用。“用途类型”为“SERVER”时可配置。HTTP(HTTP)：当业务发放系统需要通过HTTP端口与服务端进行HTTPS通信时或者需要对HTTP类型的证书文件进行替换时使用。“用途类型”为“SERVER”时可配置。THIRDNOTIFY(THIRDNOTIFY)：当业务发放系统需要与第三方订阅通知服务端进行加密通信时使用。“用途类型”为“CLIENT(客户端)”时可配置。PHYDB(PHYDB)：当PGW、DMA、NDF、DBG作为客户端需要通过PHYDB端口与服务端ClickHouse使用TLS协议进行通信或需要对PHYDB类型的证书文件进行替换时使用。“用途类型”为“SERVER”和“CLIENT”时均可配置。 默认值：无。 |
| SERVICETYPE | 业务类型    | 用于指定要加载的证书用于哪种类型的业务。 当参数“连接类型”选择“MML”、“SOAP”、“HTTP”或“REST”时此参数有效。 该参数的配置原则是：除了“USCDB”类型以外，其他的业务类型根据加载的业务插件包不同而不同。 取值范围：长度不超过128字节的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VPWD        | 证书密码    | 用于指定要加载的证书的密码。 当参数“证书类型”选择“密钥文件”时此参数有效。 设备只有通过密码验证后才能对私钥文件进行解密并读取文件内容信息。 取值范围：由数字（0~9）、字母（a~z和A~Z）或“~”、“!”、“#”、“^”、“_”、“=”、“+”、“:”、“,”和“.”特殊字符组成的长度不超过32字节的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 使用实例

1. 在SUP-FE网元开局时，用户要求业务发放系统通过SOAP端口与服务端进行HTTPS通信，不需要对客户端进行验证。此时需要进行如下操作：

   1. 上传证书文件包“SUP-FE\_SOAP.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为SOAP端口。
   3. 分别加载CA证书、设备证书、密钥文件，“证书ID”分别定义为3、4和5。

      ```
      LOD VERIF: VERIFID=3, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_CA", CONNTYPE=SOAP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=4, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_DEVVERIF", CONNTYPE=SOAP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=5, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_KEY", CONNTYPE=SOAP, SERVICETYPE="SUP-FE", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**MOD INSP**命令设置软件参数“TLSMODE（TLS工作模式）”为“3”，“HTTPSAUTHSWITCH（HTTPS鉴权开关）”为“0”。
   5. 执行**RST MODULE**命令重启PGW进程使配置生效。
2. 在SUP-FE网元开局时，用户要求业务发放系统通过SOAP端口与服务端进行HTTPS通信，需要对客户端进行验证且需要校验对端的证书是否在吊销列表中。此时需要进行如下操作：

   1. 上传证书文件包“SUP-FE\_SOAP.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为SOAP端口。
   3. 分别加载CA证书、设备证书、密钥文件和证书吊销列表文件，“证书ID”分别定义为3、4、5和6。

      ```
      LOD VERIF: VERIFID=3, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_CA", CONNTYPE=SOAP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=4, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_DEVVERIF", CONNTYPE=SOAP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=5, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_KEY", CONNTYPE=SOAP, SERVICETYPE="SUP-FE", VPWD="******";
      LOD VERIF: VERIFID=6, USTYPE=SERVER, VERIFTYPE=CRLF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_CRLF", SERVICETYPE="SUP-FE";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**MOD INSP**命令设置软件参数“TLSMODE（TLS工作模式）”为“3”，“HTTPSAUTHSWITCH（HTTPS鉴权开关）”为“1”。
   5. 执行**RST MODULE**命令重启PGW进程使配置生效。
3. 在SUP-FE网元开局时，用户要求业务发放系统通过REST端口与服务端进行HTTPS通信。此时需要进行如下操作：

   1. 上传证书文件包“SUP-FE\_REST.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为REST端口。
   3. 分别加载CA证书、设备证书和密钥文件，“证书ID”分别定义为6、7和8。

      ```
      LOD VERIF: VERIFID=6, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_REST.zip", VNAME="SUP-FE_REST_CA", CONNTYPE=REST, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=7, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_REST.zip", VNAME="SUP-FE_REST_DEVVERIF", CONNTYPE=REST, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=8, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_REST.zip", VNAME="SUP-FE_REST_KEY", CONNTYPE=REST, SERVICETYPE="SUP-FE", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**RST MODULE**命令重启PGW进程使配置生效。
4. 在SUP-FE网元开局时，用户要求业务发放系统通过HTTP端口与服务端进行HTTPS通信。此时需要进行如下操作：

   1. 上传证书文件包“SUP-FE\_HTTP.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为HTTP端口。
   3. 分别加载CA证书、设备证书和密钥文件，“证书ID”分别定义为6、7和8。

      ```
      LOD VERIF: VERIFID=6, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_HTTP.zip", VNAME="SUP-FE_HTTP_CA", CONNTYPE=HTTP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=7, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_HTTP.zip", VNAME="SUP-FE_HTTP_DEVVERIF", CONNTYPE=HTTP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=8, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_HTTP.zip", VNAME="SUP-FE_HTTP_KEY", CONNTYPE=HTTP, SERVICETYPE="SUP-FE", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**RST MODULE**命令重启PGW进程使配置生效。
5. 客户端（PGW Web LMT或DMS WebUI）与服务端之间使用HTTPS协议进行通信时，服务端由于证书失效，需要重新加载证书。此时需要进行如下操作：

   1. 上传证书文件包“USCDB\_WEBLMT.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 分别加载CA证书、设备证书和密钥文件，“证书ID”分别定义为0、1和2。

      ```
      LOD VERIF: VERIFID=0, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="USCDB_WEBLMT.zip", VNAME="SUP-FE_WEBLMT_CA", CONNTYPE=WEBLMT, SERVICETYPE="USCDB";
      LOD VERIF: VERIFID=1, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="USCDB_WEBLMT.zip", VNAME="SUP-FE_WEBLMT_DEVVERIF", CONNTYPE=WEBLMT, SERVICETYPE="USCDB";
      LOD VERIF: VERIFID=2, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="USCDB_WEBLMT.zip", VNAME="SUP-FE_WEBLMT_KEY", CONNTYPE=WEBLMT, SERVICETYPE="USCDB", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   3. 执行**MOD INSP**命令设置软件参数“WEBLMTHTTPSSWITCH（weblmt https控制开关）”为“1”。
   4. 执行**RST MODULE**命令重启所有PGW模块、所有DMA模块、网关类型为PGW的DPU模块、和DMA类型的DPU模块使配置生效。
6. 在SUP-FE网元开局时，用户要求业务发放系统通过MML端口与服务端进行HTTPS通信，不需要对客户端进行验证。此时需要进行如下操作：
   1. 上传证书文件包“SUP-FE\_MML.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为MML端口。
   3. 分别加载CA证书、设备证书、密钥文件，“证书ID”分别定义为3、4和5。

      ```
      LOD VERIF: VERIFID=3, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_MML.zip", VNAME="SUP-FE_MML_CA", CONNTYPE=MML, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=4, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_MML.zip", VNAME="SUP-FE_MML_DEVVERIF", CONNTYPE=MML, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=5, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_MML.zip", VNAME="SUP-FE_MML_KEY", CONNTYPE=MML, SERVICETYPE="SUP-FE", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**ADD PORT**/**MOD PORT**命令设置参数“端口子类型”为“PORT\_FOR\_MML” 且“是否使用HTTPS”为“YES”，执行**MOD INSP**命令设置“MMLTLSAUTHSWITCH（MML TLS鉴权开关）”为“0”（即设置为单向验证）。
   5. 执行**RST MODULE**命令重启PGW进程使配置生效。
7. 在SUP-FE网元开局时，用户要求PGW作为客户端通过MML端口与服务端（远端站点）进行HTTPS通信。此时需要进行如下操作：
   1. 上传证书文件包“SUP-FE\_MML.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为MML端口。
   3. 分别加载CA证书、设备证书、密钥文件，“证书ID”分别定义为3、4和5。

      ```
      LOD VERIF: VERIFID=3, USTYPE=CLIENT, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_MML.zip", VNAME="SUP-FE_MML_CA", CONNTYPE=MML, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=4, USTYPE=CLIENT, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_MML.zip", VNAME="SUP-FE_MML_DEVVERIF", CONNTYPE=MML, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=5, USTYPE=CLIENT, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_MML.zip", VNAME="SUP-FE_MML_KEY", CONNTYPE=MML, SERVICETYPE="SUP-FE", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**ADD PSITE**/**MOD PSITE**命令设置MML接口的参数“是否使用HTTPS”为“YES”，
   5. 执行**RST MODULE**命令重启PGW进程使配置生效。
8. 在SUP-FE网元开局时，用户要求PGW作为客户端通过SOAP端口与服务端（远端站点）进行HTTPS通信。此时需要进行如下操作：
   1. 上传证书文件包“SUP-FE\_SOAP.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 执行**ADD PORT**命令设置SUP-FE网元的“端口子类型”为SOAP端口。
   3. 分别加载CA证书、设备证书、密钥文件，“证书ID”分别定义为3、4和5。

      ```
      LOD VERIF: VERIFID=3, USTYPE=CLIENT, VERIFTYPE=CAVERIF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_CA", CONNTYPE=SOAP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=4, USTYPE=CLIENT, VERIFTYPE=DEVVERIF, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_DEVVERIF", CONNTYPE=SOAP, SERVICETYPE="SUP-FE";
      LOD VERIF: VERIFID=5, USTYPE=CLIENT, VERIFTYPE=KEYFILE, VPKGNAME="SUP-FE_SOAP.zip", VNAME="SUP-FE_SOAP_KEY", CONNTYPE=SOAP, SERVICETYPE="SUP-FE", VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   4. 执行**ADD PSITE**/**MOD PSITE**命令设置SOAP接口的参数“是否使用HTTPS”为“YES”，
   5. 执行**RST MODULE**命令重启PGW进程使配置生效。
9. 在USCDB网元开局时，用户要求ClickHouse服务端和NDF、PGW、DMA和DBG模块使用TLS协议进行通信。此时需要进行如下操作：
   1. 上传证书文件包“USCDB\_PHYDB.zip”到CSP OM Portal的“网元文件”类别的文件夹内。
   2. 分别加载服务端和客户端的CA证书、设备证书、密钥文件，服务端“证书ID”分别定义为3、4和5，客户端“证书ID”分别定义为6、7和8。

      ```
      LOD VERIF: VERIFID=3, USTYPE=SERVER, VERIFTYPE=CAVERIF, VPKGNAME="USCDB_PHYDB.zip", VNAME="USCDB_PHYDB_CA", CONNTYPE=PHYDB;
      LOD VERIF: VERIFID=4, USTYPE=SERVER, VERIFTYPE=DEVVERIF, VPKGNAME="USCDB_PHYDB.zip", VNAME="USCDB_PHYDB_DEVVERIF", CONNTYPE=PHYDB;
      LOD VERIF: VERIFID=5, USTYPE=SERVER, VERIFTYPE=KEYFILE, VPKGNAME="USCDB_PHYDB.zip", VNAME="USCDB_PHYDB_KEY", CONNTYPE=PHYDB, VPWD="******";
      ```

      ```
      LOD VERIF: VERIFID=6, USTYPE=CLIENT, VERIFTYPE=CAVERIF, VPKGNAME="USCDB_PHYDB.zip", VNAME="USCDB_PHYDB_CA", CONNTYPE=PHYDB;
      LOD VERIF: VERIFID=7, USTYPE=CLIENT, VERIFTYPE=DEVVERIF, VPKGNAME="USCDB_PHYDB.zip", VNAME="USCDB_PHYDB_DEVVERIF", CONNTYPE=PHYDB;
      LOD VERIF: VERIFID=8, USTYPE=CLIENT, VERIFTYPE=KEYFILE, VPKGNAME="USCDB_PHYDB.zip", VNAME="USCDB_PHYDB_KEY", CONNTYPE=PHYDB, VPWD="******";
      ```

      **说明** 

      密码在命令行输入区域显示为\*\*\*。
   3. 执行**RST MODULE**命令，重启全部的NDF、PGW、DMA和DBG模块，不重启全部的NDF、PGW、DMA和DBG模块会上报ALM-14011 连接物理库失败告警。

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                             | 原因分析                                                             | 处理建议                                                                                                                                    |
|-------:|:--------------------------------------------------|:-----------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
|   1792 | 证书包不存在。                                           | 系统中不存在与“证书文件包名称”匹配的证书包。                                          | 打开“维护 > FTP传输服务”，在“远程目录”的“网元文件”的文件夹下查找并输入正确的证书包名称，然后重新执行本命令。若该文件夹下无证书包，则通过FTP上传需要的证书包到“网元文件”目录下。                                        |
|   1793 | 证书包解压失败。                                          | 证书包压缩的格式不正确。                                                     | 请上传zip压缩格式的证书包到“网元文件”的文件夹下，然后重新执行此命令。                                                                                                   |
|   1795 | 打开证书文件失败，请确认证书名称是否输入正确。                           | 系统中不存在与“证书文件名”匹配的证书。                                             | 查询“网元文件”类别的文件夹下名称为“证书文件包名称”的证书包内所含的“证书文件名”，输入正确的“证书文件名”，然后重新执行本命令。                                                                      |
|   1796 | 证书文件ID已经存在。                                       | 已经加载相同的“证书ID”。                                                   | 通过LST VERIF命令查询已加载的证书，选择一个没有被使用过的“证书ID”然后重新执行本命令。                                                                                       |
|   1877 | 无效的证书包名称。                                         | “证书文件包名称”需要带“.zip”后缀名，并且只能由数字（0～9）、字母（a～z或A～Z）、“_”、“-”、“.”或空格组成。 | 确认正确上传了ZIP压缩格式的证书包，并修改“证书文件包名称”为仅由数字（0～9）、字母（a～z或A～Z）、“_”、“-”、“.”或空格组成的带有“.zip”后缀名的正确名称，最后重新执行本命令。                                      |
|   1878 | 证书不属于同一证书包。                                       | 系统根据“连接类型”和“业务类型”区分组别，同一组证书必须从同一压缩包内加载。                          | 通过LST VERIF命令查询已加载的证书，正确填写需加载新证书的“证书文件包名称”、“连接类型”和“业务类型”，然后重新执行本命令。                                                                     |
|   1879 | 业务类型没有配置端口，不允许加载证书。                               | 加载证书前必须为“业务类型”配置端口。                                              | 使用ADD PORT命令为对应“业务类型”配置端口，然后重新执行本命令。                                                                                                    |
|   1942 | 证书包文件大小超过1MB。                                     | 证书包大小不能超过1MB。                                                    | 请确认获取了正确的证书包文件，然后重新执行本命令。                                                                                                               |
|   1943 | 证书文件大小超过8000字节。                                   | 证书文件大小不能超过8000字节。                                                | 请确认获取了正确的证书文件，然后重新执行本命令。                                                                                                                |
|   1948 | 未知的业务类型。                                          | 输入的“业务类型”在系统中不存在。                                                | 通过LST FEPLUG命令查询加载的“FE类型名称”，“FE类型名称”即“业务类型”。 若“业务类型”加载成功，请在执行该命令时输入正确的业务类型名称。若“业务类型”加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。            |
|   1949 | 证书已添加。                                            | 相同证书不能重复添加。                                                      | 请确认是否需要重新添加，如需重新添加需先执行CLR VERIF命令清除已加载的证书，然后重新执行本命令。                                                                                    |
|   1953 | 已达到最大记录条数限制。                                      | 最多能加载256条证书记录。                                                   | 通过LST VERIF命令查询已加载证书文件，使用CLR VERIF命令清除无需使用的证书文件，然后重新执行本命令。                                                                              |
|   2757 | 客户端不支持证书吊销列表文件。                                   | 当参数“用途类型”为“CLIENT(客户端)”时，“证书类型”不能指定为“CRLF(证书吊销列表文件)”。            | 根据实际情况，重新输入参数，确保当参数“用途类型”为“CLIENT(客户端)”时，“证书类型”不指定为“CRLF(证书吊销列表文件)”。                                                                    |
| 337136 | 当参数CONNTYPE值为REST时，参数SERVICETYPE不能指定为USCDB。       | 当参数CONNTYPE值为REST时，参数SERVICETYPE不能指定为USCDB。                      | 修改“业务类型”，通过LOD VERIF命令重新加载。                                                                                                             |
| 260569 | Weblmt服务端不支持加载证书吊销列表文件。                           | 当参数“证书类型”为“CRLF(证书吊销列表文件)”时，“连接类型”不能指定为“WEBLMT”。                 | 根据实际情况，重新输入参数，确保当参数“证书类型”为“CRLF(证书吊销列表文件)”时，“连接类型”不指定为“WEBLMT”。                                                                         |
| 360014 | 当参数USTYPE选择“SERVER”时，参数CONNTYPE不能选择“THIRDNOTIFY”。 | 参数“用途类型”选择“SERVER”，参数“连接类型”为“THIRDNOTIFY”。                       | 执行本命令时，“用途类型”参数选择为“SERVER”时，“连接类型”参数不能为“THIRDNOTIFY”。                                                                                   |
| 337219 | 证书开关状态为“打开”时，不支持该命令。                              | 已使用命令SET NEWCERTSWITCH设置参数“证书开关”取值为“ON（打开）”。                     | 执行本命令时，命令SET NEWCERTSWITCH的参数“证书开关”取值不能设置为“ON（打开）”。 若仍需执行本命令，需在“CSP MML命令”界面执行命令SET NEWCERTSWITCH设置“证书开关”取值为“OFF（关闭）”，等待1~3分钟后，重新执行本命令。 |
| 260694 | 密码不符合规则。                                          | “证书密码”参数不符合取值范围要求。                                               | 按照参数说明表中的“证书密码”取值范围要求，正确填写该参数后，重新执行本命令。                                                                                                 |