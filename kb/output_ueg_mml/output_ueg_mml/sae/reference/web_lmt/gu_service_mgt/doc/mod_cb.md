# 修改闭锁业务(MOD CB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户签约或去签约闭锁业务（BAOC、BOIC、BOICEXHC、BORO、BAIC、BICROM）。

如果UDM支持签约管理优化（执行**SET MAPCONF**命令将“用户被锁后是否允许操作相关补充业务”设置为“TRUE”），即使用户停机，包括运营商锁（LCK）和用户锁（SABLCK），用户的业务签约变更仍可继续进行。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- 条件参数IMSI、ISDN必须且只能有一个存在。
- 参数BAOC、BOIC、BOICEXHC、BORO、BAIC、BICROM至少选一个。

## 参数说明

| 参数标识        | 参数名称           | 参数说明                                                                                |
|:------------|:---------------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI           | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                |
| ISDN        | MSISDN         | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                              |
| RECORDCOUNT | 用户个数           | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名        | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                  |
| ISDNFILE    | MSISDN文件名      | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行，16个以内的字母或数字组成的字符串。              |
| BAOC        | 是否提供BAOC业务     | 是否提供BAOC业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                             |
| BOIC        | 是否提供BOIC业务     | 是否提供BOIC业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                             |
| BOICEXHC    | 是否提供BOICEXHC业务 | 是否提供BOICEXHC业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                         |
| BORO        | 是否提供BORO业务     | 是否提供BORO业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                             |
| BAIC        | 是否提供BAIC业务     | 是否提供BAIC业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                             |
| BICROM      | 是否提供BICROM业务   | 是否提供BICROM业务。 取值范围： TRUE：提供FALSE：撤销 可选参数。                                           |

## 使用实例

为IMSI号码为460000009123456的用户签约禁止所有出呼叫、禁止国际出呼叫、禁止所有除归属国外的国际出呼叫、当漫游出归属PLMN国家后的禁止出呼叫、所有入呼叫业务、当漫游出归属PLMN国家后的禁止入呼叫业务。

MOD CB: IMSI="460000009123456", BAOC=TRUE, BOIC=TRUE, BOICEXHC=TRUE, BORO=TRUE, BAIC=TRUE, BICROM=TRUE;