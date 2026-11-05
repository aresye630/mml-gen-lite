# 修改ODB-ROAM业务(MOD ODBROAM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改指定用户应用的ODB-ROAM业务种类。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或SDNFILE同时存在。
- 当参数“ODBROAM”取值为“BROHPLMN”、“BROHPLMNC”或“BROHPLMNCGPRS”时，从HLR业务配置中获取ODBROAM是否控制EPC域（通过**LST MAPCONF**命令查询，**SET MAPCONF**命令设置），再根据主机名或域名检查网络类型，判断是否需要增加对该用户EPC域的漫游闭锁。
- 该命令的“ODB-PS域闭锁用户漫游种类”和PS域用户的“ODB-闭锁用户漫游种类”是否生效由命令**SET MAPSERV**的“PS域闭锁漫游生效参数”参数决定。

## 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                                                                                                                                                                                           |
|:------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI            | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                                                                                                                |
| ISDN        | MSISDN          | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                                                                                                                              |
| RECORDCOUNT | 用户个数            | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                            |
| IMSIFILE    | IMSI文件名         | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                                                                                                                                                                                                  |
| ISDNFILE    | MSISDN文件名       | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                                                                                                                                                                                                |
| ODBROAM     | ODB-闭锁用户漫游种类    | 运营商决定的闭锁－闭锁用户漫游。 NOBAR：不闭锁。 BROHPLMN：当用户漫游出归属PLMN时，闭锁漫游。 BROHPLMNC：当用户漫游出归属PLMN国家时，闭锁漫游。 BROHPLMNCGPRS：当用户漫游出归属PLMN国家时，闭锁PS域网络漫游。                                                                                                                                              |
| PSODBROAM   | ODB-PS域闭锁用户漫游种类 | 用于控制PS域私有闭锁用户漫游种类。 取值范围： BROLOCDOMEGPRS：当用户漫游到国内本网时，闭锁漫游。BROCROSSDOMESTICGPRS：当用户漫游到国内跨网时，闭锁漫游。BROLOCINTERGPRS：当用户漫游到国际本网时，闭锁漫游。BROCROSSINTERGPRS：当用户漫游到国际跨网时，闭锁漫游。 说明：用户可以签约多个PS域私有闭锁用户漫游种类，并用“&”连接，例如，BROLOCDOMEGPRS&BROCROSSDOMESTICGPRS&BROLOCINTERGPRS&BROCROSSINTERGPRS。 |

## 使用实例

运营商为IMSI号码是460000009123456 的用户应用ODB-ROAM业务，闭锁的类型为闭锁出归属PLMN国家漫游。命令如下：

MOD ODBROAM: IMSI="460000009123456", ODBROAM= BROHPLMNC;