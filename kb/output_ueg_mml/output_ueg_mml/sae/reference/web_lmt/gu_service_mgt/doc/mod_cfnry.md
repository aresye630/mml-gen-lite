# 修改CFNRy业务(MOD CFNRY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户签约CFNRy业务。CFNRy签约后，必须登记前转号码才能使用。

此操作也可用来为已经签约CFNRy的用户修改CFNRy业务的属性。

如果UDM支持签约管理优化（执行**SET MAPCONF**命令将“用户被锁后是否允许操作相关补充业务”设置为“TRUE”），即使用户停机，包括运营商锁（LCK）和用户锁（SABLCK），闭锁入呼叫和出呼叫，用户的业务签约变更仍可继续进行。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果PROV=FALSE，参数OFAID、NCS、NFS和COU不需要提供。
- 如果PROV=TRUE，参数NCS、NFS、COU和OFAID为可选参数。
- 当用户签约CFNRy时，如果NFS或NCS缺省，从HLR配置中获取NFS或NCS（通过**LST MAPCONF**命令查询，**SET MAPCONF**命令修改）。
- 当用户签约CFNRy时，如果COU缺省，从HLR配置中获取COU（通过**LST MAPSERV**命令查询，**SET MAPSERV**命令修改）。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                                                                                                                                                |
|:------------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI        | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                                                                                                               |
| ISDN        | MSISDN      | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                                                                                                             |
| RECORDCOUNT | 用户个数        | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                 |
| IMSIFILE    | IMSI文件名     | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。 可选参数。                                                                                                             |
| ISDNFILE    | MSISDN文件名   | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。 可选参数。                                                                                                           |
| PROV        | 是否提供CFNRy业务 | 提供还是撤销CFNRy业务。 TRUE：提供FALSE：撤销 必选参数。                                                                                                                                |
| OFAID       | OFA模板ID     | 仅当本命令中的“是否提供CFNRy业务”参数为“TRUE”时该参数有效。OFA模板ID，值域0～65535。 255和65535表示去签约OFA模板ID。 可选参数。                                                                                 |
| NFS         | 是否通知前转用户    | 仅当本命令中的“是否提供CFNRy业务”参数为“TRUE”时该参数有效。发生前转时，是否通知前转用户。 TRUE：通知FALSE：不通知 可选参数。                                                                                          |
| NCS         | 是否通知主叫用户    | 仅当本命令中的“是否提供CFNRy业务”参数为“TRUE”时该参数有效。发生前转时，是否通知主叫用户。 TRUE：通知FALSE：不通知 可选参数。                                                                                          |
| COU         | 用户控制属性      | 仅当本命令中的“是否提供CFNRy业务”参数为“TRUE”时该参数有效。用户控制属性。 OPERATOR：CFNRy业务的登记、激活、去登记、去激活由运营商控制，可通过Web UI设置。 SUBSCRIBER：CFNRy业务的登记、激活、去登记、去激活不仅由运营商控制，也可以由用户控制。用户可以直接通过MS操作。 可选参数。 |

## 使用实例

1. 为IMSI起始号码为460000009123456的4个用户提供CFNRy业务，采用模板ID为4的OFA模板，发生前转时通知前转用户和主叫用户，CFNRy业务的登记、激活由用户控制。例如：

   MOD CFNRY: IMSI="460000009123456", RECORDCOUNT=4, PROV=TRUE, OFAID=4, NFS=TRUE, NCS=TRUE, COU=SUBSCRIBER;
2. 为IMSI号码为460000009123456的用户撤销CFNRy业务，例如：

   MOD CFNRY: IMSI="460000009123456", PROV=FALSE;