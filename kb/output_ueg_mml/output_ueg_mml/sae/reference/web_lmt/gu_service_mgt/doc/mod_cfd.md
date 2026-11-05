# 修改CFD业务(MOD CFD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户提供登记和撤销CFD业务。此命令支持单用户处理，同时也支持连续以及不连续的用户ID批处理。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- 如果PROV=TRUE，此命令用于提供和修改CFD业务定制信息，如果PROV=FALSE，此命令是用于删除CFD业务。
- 如果PROV=TRUE，参数VALIDCCF，SUPINTERCFD，NFS，NCS，FTN，BSG和NRTIME是可选的，如果用户已经提供了CFD业务，操作员能够修改CFD用户的定制信息；如果用户没有提供CFD业务，操作员给用户提供CFD业务。如果PROV=FALSE，参数SUPINTERCFD，NFS，NCS，FTN和NRTIME不显示，并且BSG，VALIDCCF是可选的。
- 当用户已经提供了CFD业务，操作员可以在不同的基本业务组中进行。PROV等于TRUE，FTN应该显示，并且根据基本业务组确定BSG参数。如果BSG参数是缺省的，CFD业务被激活，用于所有基本业务组。
- 当用户已经提供了CFD业务，操作员可以在所有或一些基本业务组中删除。PROV等于FALSE并且BSG是可选的，如果参数BSG是缺省的或等于ALL，CFD业务在基本业务组被删除。如果BSG等于除ALL以外的其它值时，CFD业务在特定的基本业务组中被删除。
- 当CFD代替CFNRy业务时，NRTIME用于指定无应答定时器。如果NRTIME是缺省的，从HLR业务配置中获取无应答定时器（通过**LST MAPSERV**命令查询，**SET MAPSERV**命令设置）。当FTN缺省时，BSG和NRTIME参数不应该显示。
- 当CFD替代CFNRy、CFB业务时，NFS用于指定是否通知前转用户。如果NFS是缺省的，从HLR业务配置中获取是否通知前转用户（通过**LST MAPCONF**命令查询，**SET MAPCONF**命令设置）。
- 当CFD替代CFB、CFNRy、CFNRc时，NCS用于指定是否通知主叫用户。如果NCS是缺省的，从HLR业务配置中获取是否通知主叫用户（通过**LST MAPCONF**命令查询，**SET MAPCONF**命令设置）。
- 当被叫用户签约了“CS与VoLTE补充业务数据一致性”特性时，该用户的前转号码仅可以设置“CFD通知前转号码”参数，如果设置为“CFD替代的CFB前转号码”、“CFD替代的CFNRy前转号码”或“CFD替代的CFNRc前转号码”时，前转号码均无效。
- 被叫用户首次设置前转号码时：
  - “CFD替代的CFB前转号码”、“CFD替代的CFNRy前转号码”、“CFD替代的CFNRc前转号码”和“CFD通知前转号码”四个参数至少存在一个。
  - 当设置参数“CFD替代的CFB前转号码”、“CFD替代的CFNRy前转号码”和“CFD替代的CFNRc前转号码”中一个或多个时，不能设置参数“CFD通知前转号码”。
  - 当设置参数“CFD通知前转号码”时，不能设置参数“CFD替代的CFB前转号码”、“CFD替代的CFNRy前转号码”和“CFD替代的CFNRc前转号码”中任意一个。

## 参数说明

| 参数标识             | 参数名称              | 参数说明                                                                                                                                                                                                                                                                                               |
|:-----------------|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI             | IMSI              | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                                                                                                                                                                                                                                              |
| ISDN             | MSISDN            | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                                                                                                                                                                                                                                            |
| RECORDCOUNT      | 用户个数              | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                                                |
| IMSIFILE         | IMSI文件名           | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。 可选参数。                                                                                                                                                                                                                                            |
| ISDNFILE         | MSISDN文件名         | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。 可选参数。                                                                                                                                                                                                                                          |
| PROV             | 是否提供CFD业务         | 提供还是撤销CFD业务。 取值范围： TRUE(1)：提供 FALSE(0)：撤销 必选参数。                                                                                                                                                                                                                                                    |
| VALIDCCF         | CFD替代的条件呼叫前转业务    | 使用CFD替代的条件呼叫前转业务，包括CFB、CFNRy和CFNRc。 可以选择多个业务或其中一个业务。如选择多个业务，两个业务之间用“&”隔开。 撤销CFD业务时，BSG参数和VALIDCCF参数不能同时设定。  说明： 第一次签约CFD时，替代业务如果没有设置，则VALIDCCF选择全部的CCF;非第一次签约CFD时，替代业务如果没有设置，则VALIDCCF保持之前设置不变。                                                                                                    |
| SUPINTERCFD      | 国际漫游时是否支持CFD业务    | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。当用户国际漫游时，是否支持CFD业务。 取值范围： TRUE(1)：支持FALSE(0)：不支持 缺省值为TRUE。                                                                                                                                                                                                       |
| NFS              | 通知前转用户            | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。发生前转时，是否通知前转用户。 可选参数。                                                                                                                                                                                                                                            |
| NCS              | 通知主叫用户            | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。发生前转时，是否通知主叫用户。 可选参数。                                                                                                                                                                                                                                            |
| FTN              | CFD通知前转号码         | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD通知前转号码，为有效的国际格式号码。 取值范围：1～16位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                              |
| PROPERTY         | CFD通知前转号码属性       | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD通知前转号码的属性。 取值范围： INTERNATIONAL：国际号码 NATIONAL：国内号码 可选参数。                                                                                                                                                                                                       |
| CFBFTN           | CFD替代的CFB前转号码     | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD替代的CFB前转号码，为有效的国际格式号码。 取值范围：1～16位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                          |
| CFBFTNPROPERTY   | CFD替代的CFB前转号码属性   | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD替代的CFB前转号码的属性。 取值范围： INTERNATIONAL：国际号码 NATIONAL：国内号码 可选参数。                                                                                                                                                                                                   |
| CFNRYFTN         | CFD替代的CFNRy前转号码   | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD替代的CFNRy前转号码，为有效的国际格式号码。 取值范围：1～16位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                        |
| CFNRYFTNPROPERTY | CFD替代的CFNRy前转号码属性 | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD替代的CFNRy前转号码的属性。 取值范围： INTERNATIONAL：国际号码 NATIONAL：国内号码 可选参数。                                                                                                                                                                                                 |
| CFNRCFTN         | CFD替代的CFNRc前转号码   | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD替代的CFNRc前转号码，为有效的国际格式号码。 取值范围：1～16位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                        |
| CFNRCFTNPROPERTY | CFD替代的CFNRc前转号码属性 | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD替代的CFNRc前转号码的属性。 取值范围： INTERNATIONAL：国际号码 NATIONAL：国内号码 可选参数。                                                                                                                                                                                                 |
| BSG              | 基本业务组             | CFD业务适用的基本业务群。 ALL：All Applicable Services(TS1X，TS6X，BS2X，BS3X)，所有可应用的基本业务TS1X：Telephony Service，话音业务TS6X：Facsimile Service Group，传真业务BS2X：Asynchronous Bearer Service，异步承载业务BS3X：Synchronous Bearer Service，同步承载业务TSDX：Custom Supplementary Service，自定义补充业务 可选参数。撤销CFD业务时，BSG参数和VALIDCCF参数不能同时设定。 |
| NRTIME           | 无应答时间             | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。CFD前转的等待时间，5～60秒。如：无应答时间设为20，当呼叫该用户，无应答时间超过20，呼叫将被前转。有效值为5，10，15，20，25，30、35、40、45、50、55、60。 缺省值为30秒。 可选参数。                                                                                                                                                      |
| SUPSHORTNUM      | 是否短号码             | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。登记的CFD前转号码是否为短号。 取值范围： TRUE：短号码 FALSE：非短号码 缺省值为FALSE。 可选参数。                                                                                                                                                                                                      |
| ACTCFD           | 是否激活CFD           | 仅当本命令中的“是否提供CFD业务”参数为“TRUE”时该参数有效。是否激活CFD。 取值范围： TRUE：激活 FALSE：不激活 缺省值为TRUE。 可选参数。                                                                                                                                                                                                                 |

## 使用实例

（1） 提供CFD业务

MOD CFD: ISDN="8612345432123", RECORDCOUNT=2,PROV=TRUE, NFS=TRUE,NCS=TRUE, FTN="8613324504261";

MOD CFD: ISDN="8612345432123", RECORDCOUNT=10000, PROV=TRUE, NFS=TRUE,NCS=TRUE, FTN="8613324504261", BSG=TS1X, NRTIME=30;

MOD CFD: IMSIFILE="imsi.txt", PROV=TRUE, NFS=TRUE,NCS=TRUE, FTN="8613324504261", BSG=TS1X, NRTIME=30;

（2） 登记CFD业务

MOD CFD: IMSI="46012345432123", PROV=TRUE, NFS=TRUE,NCS=FALSE ;

MOD CFD: IMSI="46012345432123", PROV=TRUE, NFS=TRUE, NCS=TRUE, FTN="8613324504261", BSG=BS2X, NRTIME=20;

（3） 撤销CFD业务

MOD CFD: IMSI="46012345432123", PROV=FALSE, BSG=BS2X;

（4）当需要为用户去签约“CFD替代的条件呼叫前转业务”为“CFB&CFNRy”的前转业务时，需要执行如下命令：

`MOD CFD: IMSI="46012345432123", PROV=FALSE, VALIDCCF=CFB&CFNRy, BSG=ALL;`