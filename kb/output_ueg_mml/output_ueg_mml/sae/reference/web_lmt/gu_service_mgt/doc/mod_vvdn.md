# 修改VVDN业务(MOD VVDN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改用户的VVDN（Voice&Videophone Dual Number）业务签约情况。为未签约VVDN业务的用户提供该业务，或者为已签约VVDN业务的用户撤销该业务。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时出现。

  VVDN业务还与其他许多业务存在冲突，不能同时签约。这些业务包括：COMISDN、多SIM、多SIM增强和一卡多号多Profile。

## 参数说明

| 参数标识        | 参数名称         | 参数说明                                                                                |
|:------------|:-------------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI         | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                     |
| ISDN        | MSISDN       | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数         | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名      | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                      |
| ISDNFILE    | MSISDN文件名    | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                |
| PROV        | 是否提供语音视频双号业务 | 提供还是撤销VVDN业务。 TRUE：提供。 FALSE：撤销。                                                    |

## 使用实例

1. 运营商为IMSI号码是460000009123456的用户提供VVDN业务。

   MOD VVDN: IMSI="460000009123456", PROV=TRUE;
2. 运营商为IMSI号码是460000009123455、460000009123466和460000009123477的用户提供VVDN业务。

   1. 编写IMSIFILE，文件名称为IMSIBAT，内容如下：

      460000009123455

      460000009123466

      460000009123477
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行MOD VVDN命令提供VVDN业务。

      MOD VVDN: IMSIFILE="IMSIBAT", PROV=TRUE;