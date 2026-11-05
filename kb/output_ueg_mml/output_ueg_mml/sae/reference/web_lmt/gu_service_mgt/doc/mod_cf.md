# 修改前转业务(MOD CF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来同时签约或同时去签约呼叫前转业务（CFU、CFB、CFNRC和CFNRY）。

此操作也可用来为已经签约CFU、CFB、CFNRC和CFNRY的用户修改CFU、CFB、CFNRC和CFNRY业务的属性。

如果UDM支持签约管理优化（执行**SET MAPCONF**命令将“用户被锁后是否允许操作相关补充业务”设置为“TRUE”），即使用户停机，包括运营商锁（LCK）和用户锁（SABLCK），闭锁入呼叫和出呼叫，用户的业务签约变更仍可继续进行。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- 条件参数IMSI、ISDN必须且只能有一个存在。
- 参数CFUPROV、CFBPROV、CFNRYPROV和CFNRCPROV至少选一个。
- 如果CFBPROV=TRUE或CFNRYPROV=TRUE，则参数NCS、NFS、COU和OFAID为可选。
- 如果CFUPROV=TRUE，参数NCS、COU和OFAID为可选。
- 如果CFNRCPROV=TRUE，参数NCS、COU和OFAID为可选。
- 当用户签约CFU、CFB、CFNRy、CFNRc业务中的一个或几个时，如果NCS是缺省的，从HLR配置中获取NCS（通过**LST MAPCONF**命令查询，**SET MAPCONF**命令修改）。
- 当用户签约CFB或CFNRy时，如果NFS是缺省的，从HLR配置中获取NFS（通过**LST MAPCONF**命令查询，**SET MAPCONF**命令修改）。
- 当用户签约CFU、CFB、CFNRy、CFNRc业务中的一个或几个时，如果COU是缺省的，从HLR配置中获取COU（通过**LST MAPSERV**命令查询，**SET MAPSERV**命令修改）。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                                                                                                          |
|:------------|:------------|:------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI        | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                                                          |
| ISDN        | MSISDN      | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                                                                        |
| RECORDCOUNT | 用户个数        | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                           |
| IMSIFILE    | IMSI文件名     | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行。 取值范围：16个以内的字母或数字组成的字符串。                                                      |
| ISDNFILE    | MSISDN文件名   | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。 取值范围：16个以内的字母或数字组成的字符串。                                                  |
| CFUPROV     | 是否提供CFU业务   | 提供还是撤销CFU业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                                                                      |
| CFBPROV     | 是否提供CFB业务   | 提供还是撤销CFB业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                                                                      |
| CFNRCPROV   | 是否提供CFNRC业务 | 提供还是撤销CFNRC业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                                                                    |
| CFNRYPROV   | 是否提供CFNRY业务 | 提供还是撤销CFNRY业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                                                                    |
| OFAID       | OFA模板ID     | OFA模板ID。 取值范围：0～65535。 255和65535表示去签约OFA模板ID。 可选参数。                                                                           |
| NFS         | 是否通知前转用户    | 发生前转时，是否通知前转用户。 取值范围： TRUE：通知FALSE：不通知 可选参数。                                                                                  |
| NCS         | 是否通知主叫用户    | 发生前转时，是否通知主叫用户。 取值范围： TRUE：通知FALSE：不通知 可选参数。                                                                                  |
| COU         | 用户控制属性      | 用户控制属性。 取值范围： OPERATOR：CF业务的登记、激活、去登记、去激活由运营商控制，可通过Web UI设置。SUBSCRIBER：CF业务的登记、激活、去登记、去激活不仅由运营商控制，也可以由用户控制。用户可直接通过MS操作。 可选参数。 |

## 使用实例

1. 为IMSI号码是460000009123456的用户提供CFU业务，采用模板ID为2的OFA模板，发生前转时通知主叫用户。

   MOD CF: IMSI="460000009123456", CFUPROV=TRUE, OFAID=2, NCS=TRUE, COU=OPERATOR;
2. 为IMSI号码是460000009123456的用户撤销CFU前转业务。

   MOD CF: IMSI="460000009123456", CFUPROV= FALSE;