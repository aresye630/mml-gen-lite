# 修改ODB-PB1业务(MOD ODBPB1)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供或撤销ODB PLMN特定闭锁类型1（目前为闭锁国内长途）业务。

执行此命令后，系统将向VLR/SGSN/MME下发插入用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或SDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                |
|:------------|:--------------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI          | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                     |
| ISDN        | MSISDN        | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数          | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名       | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                       |
| ISDNFILE    | MSISDN文件名     | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                     |
| ODBPB1      | 是否提供ODB-PB1业务 | 是否应用运营商决定的闭锁-PLMN闭锁类型1（目前为闭锁国内长途呼叫）。 TRUE：应用FALSE：不应用                               |

## 使用实例

运营商为IMSI号码是460000009012345的用户提供ODB-PB1业务。命令如下：

MOD ODBPB1: IMSI="460000009012345", ODBPB1=TRUE;