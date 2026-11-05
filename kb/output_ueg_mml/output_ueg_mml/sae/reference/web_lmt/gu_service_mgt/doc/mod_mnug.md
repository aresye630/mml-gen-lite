# 修改多号码用户群组业务(MOD MNUG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用来为用户修改多号码用户群组业务数据，即一卡多号多profile业务数据、LINKED SIM业务数据。

- 一卡多号多profile业务：可以使用该命令通过一个主MSISDN号码，给用户绑定或去绑定其他MSISDN号码，一个用户最多拥有9个MSISDN成员号码；还可以通过此命令修改激活的MSISDN号码和TCR属性。如果修改了激活的MSISDN号码且原激活号码在网时，会向原激活号码下发CancelLocation消息。

  一卡多号多Profile业务还与其他许多业务存在冲突，不能同时签约。这些业务包括：COMISDN、MIMSI、多SIM、多SIM增强、GROUPSIM、一卡多号、VVDN、FM、ALS、LINKED SIM、M2M COMISDN和M2M ISDN-Less。
- LINKED SIM业务：通过对两个独立的用户（两对独立的IMSI与ISDN）建立关联的方式，控制其中一个用户作为激活状态的用户，当对未激活状态的用户进行寻呼或发短消息时，呼叫接续到激活状态用户，短消息被激活状态用户接收。

  LINKED SIM业务还与其他许多业务存在冲突，不能同时签约。这些业务包括：COMISDN、MIMSI、多SIM、多SIM增强、GROUPSIM、一卡多号多Profile、Home Zone、M2M COMISDN和M2M ISDN-Less。

签约多号码用户群组业务的两个用户，必须都已经成功开户，并且未签约多号码用户群组业务。撤销多号码用户群组业务的用户，必须已经成功开户，并且已经签约多号码用户群组业务。

## 注意事项

- IMSI、MSISDN、IMSISIMSIFILE、IMSISISDNFILE、ISDNSIMSIFILE和ISDNSISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSISIMSIFILE、IMSISISDNFILE、ISDNSIMSIFILE或ISDNSISDNFILE同时存在。

- 如果提供LINKED SIM业务，PROV＝TRUE，SIMSI、SISDN是条件可选参数，任何一个参数出现即可；如果撤销LINKED SIM业务，PROV= FALSE，SIMSI、SISDN不出现。
- 如果提供一卡多号多profile业务，PROV＝TRUE，GTYPE=MISDN，SIMSI、SISDN是条件可选参数，任何一个参数出现即可；如果删除一卡多号多profile用户群组的某个成员号码，PROV＝FALSE，SIMSI、SISDN是条件可选参数，任何一个参数出现即可；撤销一卡多号多profile业务，PROV= FALSE，SIMSI、SISDN不出现。

- 如果PROV=FALSE时，批操作参数为IMSISIMSIFILE或ISDNSISDNFILE。IMSISIMSIFILE文件中只需用户的IMSI号码，ISDNSISDNFILE文件中只需要用户的ISDN号码。
- 在混合组网下，如存在异常场景下进行跨SP数据迁移时，需要通过设置“USERDATAMIGEXCEPENHANCESW（用户数据迁移容错能力增强开关）”软参支持数据的兼容处理，避免因为UDB和PaasDB数据模型不一致而处理失败。
  - 插件包schemamap.xml文件中配置RDN冲突节点（rdnconflictexcepproc），即从5G接入查询4G用户和用户数据迁移过程中该节点存在冲突记录时，若该软参为“1”，根据timestampfield配置字段取最新的一条数据，无timestampfield配置，随机取一条数据；若软参为“0”，则从5G接入查询4G用户和迁移失败。
  - 插件包schemamap.xml文件中配置无父节点的节点（noparentnodeexcepproc），即从5G接入查询4G用户和用户数据迁移过程中该节点无父节点记录时，若软参为“1”，忽略该节点数据不处理；若软参为“0”，则从5G接入查询4G用户和迁移失败。
- 当“添加或删除组成员号码”参数为“TRUE”时，“SIMSI”或“SISDN”参数对应的成员用户不能在网。可以执行**LST DYNSUB**命令查询用户是否在VLR或SGSN注册在网。

## 参数说明

| 参数标识          | 参数名称         | 参数说明                                                                                                               |
|:--------------|:-------------|:-------------------------------------------------------------------------------------------------------------------|
| IMSI          | IMSI         | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                                                              |
| ISDN          | MSISDN       | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                                                            |
| RECORDCOUNT   | 用户个数         | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                |
| IMSISIMSIFILE | IMSISIMSI文件名 | IMSISIMSI文件名称，1～16个字母或数字组成。IMSISIMSIFILE包含多个不连续的IMSI和SIMSI号码。 可选参数。                                                |
| IMSISISDNFILE | IMSISISDN文件名 | IMSISISDN文件名称，1～16个字母或数字组成。IMSISISDN包含多个不连续的IMSI和SISDN号码。 可选参数。                                                    |
| ISDNSIMSIFILE | ISDNSIMSI文件名 | ISDNSIMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的ISDN和SIMSI号码。 可选参数。                                                     |
| ISDNSISDNFILE | ISDNSISDN文件名 | ISDNSISDN文件名称，1～16个字母或数字组成。ISDNSISDN包含多个不连续的ISDN和SISDN号码。 可选参数。                                                    |
| PROV          | 添加或删除组成员号码   | 添加或删除组成员号码。 TRUE：添加 FALSE：删除 必选参数。                                                                                 |
| GTYPE         | 多号码群组类型      | 多号码群组类型。 MISDN：一卡多号多Profile用户群组 EIMSI：LINKED SIM用户群组 默认值：MISDN 如果参数“PROV”设置为“FALSE”，此参数不必设置。                       |
| SIMSI         | SIMSI        | 仅当本命令中的“添加或删除组成员号码”参数为“TRUE”或“FALSE”时该参数有效。成员用户的IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                    |
| SISDN         | SISDN        | 仅当本命令中的“添加或删除组成员号码”参数为“TRUE”或“FALSE”时该参数有效。成员用户的MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                  |
| TCR           | 成员号码被叫权限     | 成员号码的被叫权限，表示成员用户是否能够接受被叫以及短消息。 取值范围： PCALL：允许接收被叫和短消息NCALL：不能接收被叫和短消息 默认值：PCALL  说明： 当“GTYPE”的取值为“MISDN”时，此参数才会出现。 |
| ACTISDN       | 是否激活成员号码     | 是否激活该成员号码。 取值范围： NONE：不进行操作TRUE：激活 默认值：NONE  说明： 当“GTYPE”的取值为“MISDN”时，此参数才会出现。                                     |

## 使用实例

1. 运营商为IMSI号码是460000009012345和IMSI号码是460000000912345的两个用户提供LINKED SIM业务。例如：

   MOD MNUG: IMSI="460000009012345", PROV=TRUE, GTYPE=EIMSI, SIMSI="460000000912345";
2. 运营商为MSISDN号码是861390755111111和MSISDN号码是861390755222222的两个用户提供一卡多号多Profile业务， 其中主号码是861390755111111，成员号码为861390755222222。例如：

   MOD MNUG: ISDN="861390755111111", PROV=TRUE, GTYPE=MISDN, SISDN="861390755222222", TCR=PCALL, ACTISDN=TRUE;
3. 运营商为IMSI号码是460000000000001、460000000000006和460000000000009的用户提供LINKED SIM业务，对应第二个用户的IMSI号码是460000000000003、460000000000005、460000000000007。

   1. 编写IMSIFILE，文件名称为IMSIPROV.txt，内容如下：

      460000000000001 460000000000003

      460000000000006 460000000000005

      460000000000009 460000000000007
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行MOD MNUG命令提供LINKED SIM业务。

      MOD MNUG: IMSISIMSIFILE="IMSIPROV.txt", PROV=TRUE, GTYPE=EIMSI;
4. 运营商为IMSI号码是460000000000001、460000000000006和460000000000009的用户去签约多号码用户群组业务。

   1. 编写IMSIFILE，文件名称为IMSI.txt，内容如下：

      460000000000001

      460000000000006

      460000000000009
   2. 通过Web UI上的文件选项将文件上传到指定位置。
   3. 执行MOD MNUG命令去签约多号码用户群组业务。

      MOD MNUG: IMSISIMSIFILE="IMSI.txt", PROV=FALSE;

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 消息解释            | 原因分析                                                 | 处理建议                                                                                      |
|:--------|:----------------|:-----------------------------------------------------|:------------------------------------------------------------------------------------------|
| ERR3272 | 群组成员不能是特殊号码     | 用户已签约以下一个或多个业务： ALSFMVVDNMULTISDNMIMSI               | 使用LST SUB命令，查看用户签约了哪些冲突业务，再根据实际情况，确认可以去签约相关冲突业务，重新执行本命令为用户修改多号码用户群组业务数据。                  |
| ERR3276 | 输入的成员用户已经在网络中使用 | 当“添加或删除组成员号码”参数为“TRUE”时，“SIMSI”或“SISDN”参数对应的成员用户已在网。 | 当“添加或删除组成员号码”参数为“TRUE”时，确保“SIMSI”或“SISDN”参数对应的成员用户不在网。可以执行LST DYNSUB命令确保用户未在VLR或SGSN注册在网。 |