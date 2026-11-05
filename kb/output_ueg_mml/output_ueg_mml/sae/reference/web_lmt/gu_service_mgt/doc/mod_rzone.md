# 修改RZONE业务(MOD RZONE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改用户的漫游区域业务签约情况。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                      |
| ISDN        | MSISDN    | ISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                     |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成的字符串。IMSIFILE包含多个不连续的IMSI号码。                                   |
| ISDNFILE    | MSISDN文件名 | MSISDN文件名称，1～16个字母或数字组成的字符串。ISDNFILE包含多个不连续的MSISDN号码。                               |
| RZONE       | RZONE索引   | RZONE业务索引。取值范围为0～9。                                                                 |

## 使用实例

1. 运营商为IMSI号码是460000001234567的用户提供RZONE索引为2的业务。

   MOD RZONE: IMSI="460000001234567", RZONE=2;
2. 运营商为IMSI号码是460000009123455、460000009123466和460000009123477的用户提供RZONE索引为2的业务。
   1. 编写IMSIFILE，文件名称为IMSIBAT，内容如下：

      460000009123455

      460000009123466

      460000009123477
   2. 通过Web UI上的文件选项将文件上传到指定位置
   3. 执行MOD RZONE命令提供RZONE业务。

      MOD RZONE: IMSIFILE="IMSIBAT.txt", RZONE=2;