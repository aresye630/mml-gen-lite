# 查询PGW业务消息侦听端口(LST PORT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询PGW使用的相关端口的配置信息。

- 若需要查询PGW使用的全部相关端口的概要信息，请不要输入任何参数。
- 若需要查询PGW使用的某个端口的详细信息，请输入“端口号”或其他参数或这些参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称         | 参数说明                                                                           |
|:-------------|:-------------|:-------------------------------------------------------------------------------|
| PORTNO       | 端口号          | 用于指示系统需要按照哪个端口号来查询端口数据；若不输入，则表示所有的端口号。                                         |
| PORTTYPE     | 端口类型         | 用于指示系统需要按照哪个端口类型来查询端口数据；若不输入，则表示所有的端口类型。                                       |
| PORTTYPENAME | 端口子类型        | 用于指示系统需要按照哪个端口子类型来查询端口数据；若不输入，则表示所有的端口子类型。                                     |
| DISABLEPORT  | 是否屏蔽本端口      | 用于指示系统需要按照“屏蔽端口”还是“非屏蔽端口”来查询端口数据；若不输入，则表示全部的“屏蔽端口”和“不屏蔽端口”。                    |
| PORTBUSSTYPE | 端口业务类型       | 用于指示系统需要按照哪个端口业务类型来查询端口数据；若不输入，则表示所有的端口业务类型。                                   |
| PORTSHKTYP   | 端口的握手类型      | 用于指示系统需要按照哪个握手类型来查询端口数据；若不输入，则表示所有的握手类型。                                       |
| PORTCONTENT  | 端口的握手内容      | 用于指示系统需要按照握手消息内容来查询端口数据；若不输入，则表示所有的握手消息内容。                                     |
| SHKLEN       | 握手消息长度       | 用于指示系统需要按照握手消息长度来查询端口数据；若不输入，则表示所有的握手消息长度。                                     |
| SNDSHKIMM    | 是否连接立即发送握手消息 | 用于指示系统需要按照“连接立即发送握手消息”还是“连接后不发送握手消息”来查询端口数据；若不输入，则表示查询时不区分连接后是否立即发送握手消息。       |
| HEADERAUTH   | 是否使用头域鉴权     | 用于指示系统需要按照“使用头域鉴权”还是“不使用头域鉴权”来查询端口数据；若不输入，则表示不区分是否使用头域鉴权。                      |
| RETURNHEADER | 是否返回头域       | 用于指示系统需要按照“返回头域”还是“不返回头域”来查询端口数据；若不输入，则表示查询时不区分是否返回头域。                         |
| HTTPS        | 是否使用HTTPS    | 用于指示系统需要按照“使用HTTPS”还是“不使用HTTPS”来查询端口数据；若不输入，则表示查询时不区分是否使用HTTPS。                |
| HTTPVER      | HTTP协议版本     | 用于指示系统需要按照“HTTP1.1”还是“HTTP2.0”来查询端口数据；若不输入，则表示查询时不区分协议版本是“HTTP1.1”还是“HTTP2.0”。 |

## 使用实例

1. 查询PGW使用的全部相关端口信息：

   ```
   LST PORT:;
   ```

   ```
   %%LST PORT:;%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
   端口号        端口类型         端口子类型                              是否屏蔽本端口           端口业务类型          端口的握手类型        端口的握手内容             握手消息长度             是否连接立即发送握手消息       是否使用头域鉴权            是否返回头域   是否使用HTTPS   HTTP协议版本   转发端口  转发端口定制报文

    80           PORT_FOR_WEBLMT  PGW提供给Web LMT Server侦听的端口       否                       USCDB                 NULL                  NULL                       NULL                      NULL                            NULL                        NULL           NULL            NULL            否        NULL
    6001         PORT_FOR_PROV    PGW开放给业务发放系统的REST服务端口     否                       SUP-FE                NULL                  NULL                       NULL                      NULL                            是                          NULL           否              HTTP1.1         否        NULL
    6002         PORT_FOR_PROV    PGW开放给业务发放系统的REST服务端口     否                       GU-HLR                NULL                  NULL                       NULL                      NULL                            是                          NULL           是              HTTP1.1         否        NULL
    7776         PORT_FOR_PROV    PGW开放给业务发放系统的MML服务端口      否                       USCDB                 RSPWITHRPT            SHK-HAND                   NULL                      NULL                            NULL                        NULL           NULL            NULL            否        NULL
    7777         PORT_FOR_PROV    PGW开放给业务发放系统的MML服务端口      否                       GU-HLR                NORMAL                SHK-HND                    9                         SNDIMMEDIATELY                  NULL                        NULL           NULL            NULL            否        NULL
    7778         PORT_FOR_WEBLMT  PGW提供给Web LMT Server的MML服务端口    否                       USCDB                 RSPWITHRPT            SHK-HAND                   NULL                      NULL                            NULL                        NULL           NULL            NULL            否        NULL
    8001         PORT_FOR_PROV    PGW开放给业务发放系统的SOAP服务端口     否                       USCDB                 NULL                  NULL                       NULL                      NULL                            否                          否             NULL            NULL            否        NULL
    8002         PORT_FOR_PROV    PGW开放给业务发放系统的SOAP服务端口     否                       SUP-FE                NULL                  NULL                       NULL                      NULL                            是                          是             NULL            NULL            否        NULL
    8003         PORT_FOR_PROV    PGW开放给业务发放系统的SOAP服务端口     否                       GU-HLR                NULL                  NULL                       NULL                      NULL                            否                          是             NULL            NULL            否        NULL
    31943        PORT_FOR_DMSWEB  用于DMS登录的端口                       否                       USCDB                 NULL                  NULL                       NULL                      NULL                            NULL                        NULL           NULL            NULL            否        NULL
   (结果个数 = 10)

   ---    END
   ```
2. 查询PGW使用的相关端口信息，“业务类型”为“SUP-FE”：

   ```
   LST PORT: PORTBUSSTYPE="SUP-FE";
   ```

   ```
   %%LST PORT: PORTBUSSTYPE="SUP-FE";%%
   RETCODE = 0  操作成功

   操作结果如下
   ------------------------
    端口号       端口类型       端口子类型                           是否屏蔽本端口           端口业务类型          端口的握手类型          端口的握手内容             握手消息长度  是否连接立即发送握手消息  是否使用头域鉴权  是否返回头域   是否使用HTTPS   HTTP协议版本   转发端口  转发端口定制报文

    6001         PORT_FOR_PROV  PGW开放给业务发放系统的REST服务端口  否                       SUP-FE                NULL                    NULL                       NULL          NULL                      是                 NULL          否              HTTP1.1        否        NULL
    8002         PORT_FOR_PROV  PGW开放给业务发放系统的SOAP服务端口  否                       SUP-FE                NULL                    NULL                       NULL          NULL                      是                 是            NULL            NULL           否        NULL
   (结果个数 = 2) 

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**ADD PORT**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释                                           | 原因分析           | 处理建议                                                                                                                                 |
|-------:|:------------------------------------------------|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| 275019 | 参数取值无效：参数PORTBUSSTYPE所示的插件包不存在，请确认已经成功加载了该FE插件。 | 未加载端口业务类型的插件包。 | 通过LST FEPLUG命令查询加载的“FE类型名称”，“FE类型名称”即“端口业务类型”。 若“端口业务类型”加载成功，请在执行该命令时输入正确的端口业务类型名称。若“端口业务类型”加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。 |