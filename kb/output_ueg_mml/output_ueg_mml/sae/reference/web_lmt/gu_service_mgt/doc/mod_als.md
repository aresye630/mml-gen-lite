# 修改ALS业务(MOD ALS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改用户的ALS业务签约情况。为未签约ALS业务的用户提供该业务，或者为已签约ALS业务的用户撤销该业务。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- PROV=TRUE，表示给用户提供ALS业务。如果给单个用户提供，只有IMSI/ISDN与LINE2NUM同时出现；如果给多个号码不连续用户提供，只有IMSIFILE/ISDNFILE出现，文件包含多个不连续的IMSI/MSISDN号码及其对应的第二条线路的MSISDN号码。
- PROV=FALSE，表示给用户撤销ALS业务。如果给单个用户撤销，只有IMSI/ISDN出现；如果给多个号码连续用户撤销，只有IMSI/ISDN与RECORDCOUNT同时出现；如果给多个号码不连续用户撤销，只有IMSIFILE/ISDNFILE出现，文件包含多个不连续的IMSI/MSISDN号码。
- “RECORDCOUNT”参数不能与“IMSIFILE”或“ISDNFILE”同时存在。
- GPRS用户不能签约ALS业务。
- ALS业务还与其他许多业务存在冲突，不能同时签约。这些业务包括：COMISDN、MIMSI、多SIM、多SIM增强、一卡多号多Profile、Home Zone、M2M COMISDN和M2M ISDN-Less。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                 |
|:------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                      |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                    |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                  |
| IMSIFILE    | IMSI文件名   | IMSI文件名，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码，或者多个不连续IMSI号码及其对应的第二条线路的MSISDN号码。每行包括一个IMSI号码，或者包括一个IMSI号码及其对应的第二条线路的MSISDN号码。           |
| ISDNFILE    | MSISDN文件名 | ISDN文件名，1～16个字母或数字组成。 ISDNFILE包含多个不连续的MSISDN号码，或者多个不连续的MSISDN号码及其对应的第二条线路的MSISDN号码。每行包括一个MSISDN号码，或者包括一个MSISDN号码及其对应的第二条线路的MSISDN号码。 |
| PROV        | 是否提供ALS业务 | 提供还是撤销ALS业务。 TRUE(1)：提供。FALSE(0)：撤销。                                                                                                 |
| LINE2NUM    | 线路2MSISDN | 仅当本命令中的“是否提供ALS业务”参数为“TRUE”时该参数有效。Line2号码，即ALS业务第二条线路的MSISDN号码。                                                                      |

## 使用实例

1. 运营商为IMSI号码是460000009123456的用户提供ALS业务，并指定第二条线路的MSISDN号码为138075501234566。

   ```
   MOD ALS: IMSI="460000009123456", PROV=TRUE, LINE2NUM="138075501234566";
   ```
2. 运营商为IMSI号码是460000009123455、460000009123466和460000009123477的用户提供ALS业务，对应第二条线路的MSISDN号码分别为8613900001255、8613900001266和8613900001277。

   1. 编写IMSIFILE，文件名称为IMSIBAT，内容如下：

      460000009123455 8613900001255

      460000009123466 8613900001266

      460000009123477 8613900001277
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行MOD ALS命令提供ALS业务。

      ```
      MOD ALS: IMSIFILE="IMSIBAT.txt", PROV=TRUE;
      ```