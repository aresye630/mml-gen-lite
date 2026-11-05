# 修改eMLPP业务(MOD EMLPP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改用户的eMLPP业务签约情况。为未签约eMLPP业务的用户提供该业务，或者为已签约eMLPP业务的用户撤销该业务。

此操作也可为用户修改eMLPP控制属性。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果PROV=TRUE，表示提供eMLPP业务，参数EMLPP\_MAX和EMLPP\_DEF必须出现；如果PROV=FALSE，表示撤销eMLPP业务，参数EMLPP\_MAX和EMLPP\_DEF不能出现。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                                                                                                                             |
|:------------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI        | IMSI号码， E.212格式的编码，6～15位的十进制数字。                                                                                                                  |
| ISDN        | MSISDN      | MSISDN号码，E.164格式的编码，1～15位的十进制数字。                                                                                                                 |
| RECORDCOUNT | 用户个数        | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                              |
| IMSIFILE    | IMSI文件名     | IMSI文件名称，由16个以内的数字或字母组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                                                                              |
| ISDNFILE    | MSISDN文件名   | MSISDN文件名称，由16个以内的数字或字母组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。                                                                        |
| PROV        | 是否提供eMLPP业务 | 提供还是撤销eMLPP业务。 TRUE：提供FALSE：撤销                                                                                                                   |
| EMLPP_MAX   | eMLPP最大优先级  | 仅当参数“是否提供eMLPP业务”取值为“TRUE”时该参数有效。eMLPP业务提供7个级别的eMLPP优先级：A、B、0、1、2、3、4。 优先级A最高，4最低。 其中最高两个优先级A和B供网络运营商内部使用，其它5个级别供用户使用。                           |
| EMLPP_DEF   | eMLPP缺省优先级  | 仅当参数“是否提供eMLPP业务”取值为“TRUE”时该参数有效。eMLPP缺省优先级不能高于eMLPP最大优先级。 eMLPP业务提供7个级别的eMLPP优先级：A、B、0、1、2、3、4。 优先级A最高，4最低。 其中最高两个优先级A和B供网络运营商内部使用，其它5个级别供用户使用。 |
| EMLPP_COU   | eMLPP控制属性   | EMLPP控制属性。 取值范围： OPERATOR：EMLPP业务的缺省优先级由运营商控制，用户无权控制。SUBSCRIBER：EMLPP业务的缺省优先级不仅可以由运营商控制，也可以由用户控制。用户可以直接通过MS操作。                                   |

## 使用实例

1. 为IMSI号码是460000009123456的用户提供eMLPP业务，并指定eMLPP最大优先级为0，eMLPP缺省优先级为1。

   MOD EMLPP: IMSI="460000009123456", PROV=TRUE, EMLPP\_MAX=priorityLevel0, EMLPP\_DEF=priorityLevel1;
2. 为IMSI号码是460000009123455、460000009123466和460000009123477的用户提供eMLPP业务，并指定eMLPP最大优先级为0，eMLPP缺省优先级为1。

   (1) 编写IMSIFILE，文件名称为IMSIBAT，内容如下：

   460000009123455

   460000009123466

   460000009123477

   (2) 通过Web UI上的文件选项将文件上传到指定位置。

   (3) 执行MOD EMLPP命令提供eMLPP业务。

   MOD EMLPP: IMSIFILE="IMSIBAT", PROV=TRUE, EMLPP\_MAX=priorityLevel0, EMLPP\_DEF=priorityLevel1;