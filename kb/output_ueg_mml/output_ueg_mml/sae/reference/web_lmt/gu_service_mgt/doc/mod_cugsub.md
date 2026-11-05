# 修改CUG业务(MOD CUGSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供、撤销或修改用户的CUG（Closed User Group）业务。

执行**MOD CUGSUB**签约CUG业务后，用户可以进行群内呼叫。如果用户需要进行CUG群间呼叫，还需要执行MOD CUGFTR命令签约CUG特征数据。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT参数一定不能与IMSIFILE或ISDNFILE同时出现。
- 如果PROV=FALSE，此命令用于撤销CUG业务，所以不需要提供INDEX、BSG和INTRACUG参数。
- 如果PROV=TRUE，此命令用于添加新的CUG业务或者修改已经存在的CUG业务数据。

  如果是添加新的CUG业务，INDEX和BSG参数必须出现，INTRACUG为可选参数。

  如果是修改已存在的CUG业务数据，则INDEX、BSG和INTRACUG参数中至少有一个必须出现。

- 每个用户最多允许签约10个CUG Interlock。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                        |
|:------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                             |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                                           |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                         |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                                                                                                          |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                                                                                                      |
| PROV        | 是否提供CUG业务 | 提供还是撤销CUG业务。 TRUE：提供FALSE：撤销                                                                                                                                                                |
| INTERLOCK   | CUG连锁码    | 网络用来唯一标识一个CUG的标志。 其设置格式与全局设置CUGFORMAT有关。当CUGFORMAT为Original时，INTERLOCK是只能由8位数字组成的字符串（可以是十进制也可以是十六进制）。当CUGFORMAT为DecHex时，INTERLOCK是只能由8～9位十进制数字组成的字符串。如果输入9位，最后5位最大只能是65535（十进制）。            |
| INDEX       | CUG索引     | 仅当本命令中的“是否提供CUG业务”参数为“TRUE”时该参数有效。 用户标识所在的CUG的索引值，值域为0～32767。                                                                                                                               |
| BSG         | 基本业务组     | 仅当本命令中的“是否提供CUG业务”参数为“TRUE”时该参数有效。 CUG适用的BSG（Basic Service Group）。可以选择所有的基本业务，也可以选择其中的几种或一种。CUG适用的基本业务必须事先已经签约，否则CUG业务签约不成功。 ALL：所有基本业务TS1X：语音业务TS6X：传真业务BS2X：异步承载业务BS3X：同步承载业务             |
| INTRACUG    | CUG群内呼叫限制 | 仅当本命令中的“是否提供CUG业务”参数为“TRUE”时该参数有效。 CUG群内呼叫限制，取值范围如下： NO_CUGBAR：CUG群内用户呼叫没有限制，即：CUG群内用户可以发起呼叫，也可以接收呼叫。IC_CUGBAR：CUG用户呼入闭锁，即：CUG群内用户可以发起呼叫而不能接收呼叫。OC_CUGBAR：CUG用户呼出闭锁，即：CUG群内用户可以接收呼叫而不能发起呼叫。 |

## 使用实例

1. 运营商为IMSI号码是460123456012345的用户签约CUG业务。CUG连锁码为46000000，CUG索引值为4， 适用的基本业务为语音业务和传真业务，CUG群内呼叫无限制。

   MOD CUGSUB: IMSI="460123456012345", PROV=TRUE, INTERLOCK="46000000", INDEX=4, BSG=TS1X&TS6X, INTRACUG=NO\_CUGBAR;
2. 运营商为IMSI号码是460000009123455、460000009123466和460000009123477用户签约CUG业务。 CUG连锁码为46000000，CUG索引值为4，适用的基本业务为语音业务和传真业务，CUG群内呼叫无限制。

   1. 编写IMSIFILE，文件名称为IMSIBAT.txt，内容如下：

      460000009123455

      460000009123466

      460000009123477
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行**MOD CUGSUB**命令提供CUG业务。

      MOD CUGSUB: IMSIFILE="IMSIBAT.txt", PROV=TRUE, INTERLOCK="46000000", INDEX=4, BSG=TS1X&TS6X, INTRACUG=NO\_CUGBAR;