# 修改SCPBWADDR业务(MOD SCPBWADDR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供/撤销用户的SCPBWADDR业务。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                      |
|:------------|:----------|:----------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                           |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                         |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                       |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                             |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                           |
| PROV        | 操作类型      | 取值范围： ADD：增加一条SCP记录。MOD：修改一条SCP记录。DEL：删除一条SCP记录。DEL_ALL：删除用户所有SCP记录。 必选参数。                                |
| SCPADDR     | SCP地址     | 仅当本命令中的“操作类型”参数为“ADD”、“MOD”或“DEL”时该参数有效。地址号码，15位以内数字组成的字符串。                                               |
| ALLOWSERV   | 允许查询的业务列表 | 仅当本命令中的“操作类型”参数为“ADD”、或“MOD”时该参数有效。允许查询的业务列表，包括OCSI、TCSI、CF、CB和ODB。 可以选择多个业务或其中一个业务。如选择多个业务，两个业务之间用“&”隔开。 |

## 使用实例

1. 运营商为IMSI号码是460000009012345的用户签约SCPBWADDR业务。命令如下：

   MOD SCPBWADDR: IMSI="460000009012345", PROV=ADD, SCPADDR="8613901000", ALLOWSERV=OCSI;
2. 为IMSI号码为460000009012345的用户删除一条SCP地址记录。命令如下：

   MOD SCPBWADDR: IMSI="460000009012345", PROV=DEL, SCPADDR="8613901000";