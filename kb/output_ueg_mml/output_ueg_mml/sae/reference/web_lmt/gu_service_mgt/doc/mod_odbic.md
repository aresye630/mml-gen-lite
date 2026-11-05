# 修改ODB-BIC业务(MOD ODBIC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改指定用户应用的ODB-BIC业务种类。

如果UDM支持签约管理优化（执行**SET MAPCONF**命令将“用户被锁后是否允许操作相关补充业务”设置为“TRUE”），即使已执行**MOD LCK**命令禁止用户呼入，仍可以执行该命令修改用户的“ODB-闭锁入呼叫”业务。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或SDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                           |
|:------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                              |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                            |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                                                                                                  |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                                                                                                |
| ODBIC       | ODB-闭锁入呼叫 | 闭锁入呼叫的种类。 NOBIC：不闭锁入呼叫。 BAIC：闭锁所有入呼叫。 BICROAM：当漫游出HPLMN (Home PLMN)国家时，闭锁入呼叫。 BICCROSSDOMESTIC：当漫游到国内跨网，闭锁入呼叫。 BICROAMORCROSSDOMESTIC：当漫游出HPLMN (Home PLMN)国家或者漫游在国内跨网时，闭锁入呼叫。 |

## 使用实例

运营商为IMSI号码是460000009012345应用ODB-BIC业务，闭锁的类型为闭锁所有入呼叫。命令如下：

MOD ODBIC: IMSI="460000009012345", ODBIC=BAIC;