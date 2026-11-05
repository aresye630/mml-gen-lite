# 修改ODB-POS业务(MOD ODBPOS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改运营商决定的闭锁－闭锁分组业务。

执行此命令后，系统将向SGSN/MME下发插入用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称                  | 参数说明                                                                                                                                    |
|:------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI                  | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                         |
| ISDN        | MSISDN                | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                       |
| RECORDCOUNT | 用户个数                  | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                     |
| IMSIFILE    | IMSI文件名               | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                                                           |
| ISDNFILE    | MSISDN文件名             | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                                                         |
| ODBPOS      | ODB-闭锁分组业务            | 运营商决定的闭锁－闭锁分组业务。 NOBPOS：不闭锁分组业务。 BAPOS：闭锁所有的分组业务。 BHPLMNAPROAM：当接入点在HPLMN并且用户在VPLMN漫游时闭锁分组业务。 BALLAPROAM：当接入点在VPLMN并且用户在VPLMN漫游时闭锁分组业务。 |
| ODBPOSTYPE  | ODB-闭锁PDP上下文激活有效的标识类型 | 分组业务的PDP上下文激活有效的标识类型。 BOTH：对MS和网络发起的PDP上下文激活都有效。 MSInit：只对MS发起的PDP上下文激活有效。 NetworkInit：只对网络发起的PDP上下文激活有效。                               |

## 使用实例

运营商为IMSI号码是460000009123456的用户应用ODB-POS业务，闭锁的类型为BAPOS，标识对网络发起的PDP上下文激活有效。命令如下：

MOD ODBPOS: IMSI="460000009123456",ODBPOS=BAPOS, ODBPOSTYPE=NetworkInit;