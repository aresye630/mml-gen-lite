# 修改CUG特征数据(MOD CUGFTR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来修改或删除用户的CUG业务的特征数据。

执行**MOD CUGFTR**命令签约CUG特征用户数据前，用户必须事先执行MOD CUGSUB命令签约CUG业务。

执行此命令后，系统将向VLR下发插入用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果PROV=FALSE，此命令用于删除CUG业务的特征列表（feature list），所以参数PRFCUG，PRFCUGPROV和INTERCUG不会出现。
- 如果PROV=TRUE，此命令用于添加新的CUG业务特征数据或者修改已经存在的CUG业务特征数据。如果是添加新的CUG业务特征列表（feature list），INTERCUG的默认值为ONLY\_CUG。
- 如果PRFCUGPROV=TRUE，表示签约一个优先的CUG，故参数PRFCUG必须出现；如果PRFCUGPROV=FALSE，表示删除一个优先的CUG，故参数PRFCUG不需要出现。
- PRFCUG必须在签约CUG时已经定义。
- 每个用户最多允许签约5个CUG特征列表。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                                                                                                                                                                                                                                 |
|:------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI        | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                                                                                      |
| ISDN        | MSISDN      | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                                                                                                    |
| RECORDCOUNT | 用户个数        | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                  |
| IMSIFILE    | IMSI文件名     | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                                                                                                                                                                   |
| ISDNFILE    | MSISDN文件名   | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                                                                                                                                                               |
| PROV        | 是否提供CUG特征列表 | 提供还是撤销CUG特征列表（featrue list）。 TRUE：提供FALSE：撤销                                                                                                                                                                                                         |
| BSG         | 基本业务组       | CUG适用的BSG（Basic Service Group）。CUG适用的基本业务必须事先已经签约，否则CUG业务签约不成功。 ALL：所有基本业务TS1X：语音业务TS6X：传真业务BS2X：异步承载业务BS3X：同步承载业务                                                                                                                                   |
| INTERCUG    | CUG群间限制     | 仅当本命令中的“是否提供CUG特征列表”参数为“TRUE”时该参数有效。CUG群间限制。 ONLY_CUG： 用户只允许在本CUG群内进行呼叫。OA_CUG：Outgoing access，指用户可以呼叫其它CUG群的用户，但不能接收其它CUG群用户的呼叫。IA_CUG：Incoming access，指用户可以接收其它CUG群用户的呼叫，但不能呼叫其它CUG群的用户。IOA_CUG：Outgoing and Incoming access，是指不同的CUG群之间可以互相呼出和呼入。 |
| PRFCUGPROV  | 是否提供优先的CUG  | 仅当本命令中的“是否提供CUG特征列表”参数为“TRUE”时该参数有效。提供还是撤销一个优先的CUG。 TRUE：提供FALSE：撤销                                                                                                                                                                                  |
| PRFCUG      | 优先的CUG索引    | 仅当本命令中的“是否提供CUG特征列表”参数为“TRUE”时该参数有效。优先的CUG的索引，值域为0～32767。 说明： 当MOD CUGSUB的参数“INTRACUG”取值为“OC_CUGBAR”时，此时MOD CUGSUB的CUG索引不能作为MOD CUGFTR的优先的CUG索引。                                                                                                     |

## 使用实例

1. 运营商为IMSI号码是460000009123456的用户添加CUG业务特征数据。该用户已经成功执行MOD CUGSUB命令签约CUG业务基本数据。

   MOD CUGFTR: IMSI="460000009123456", PROV=TRUE, BSG=TS1X;
2. 运营商为IMSI号码是460000009123455、460000009123466和460000009123477的用户添加CUG业务特征数据。以上用户已经成功执行MOD CUGSUB命令签约CUG业务基本数据。

   1. 编写IMSIFILE，文件名称为IMSI.txt，内容如下：

      460000009123455

      460000009123466

      460000009123477
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行**MOD CUGFTR**命令提供CUG业务。

      MOD CUGFTR: IMSIFILE="IMSI.txt", PROV=TRUE, BSG=TS1X;