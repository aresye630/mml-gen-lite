# 修改M2MCISDN业务(MOD M2MCISDN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于为M2M用户提供、修改或撤销M2M Common MSISDN业务。

签约M2M Common MSISDN业务后，多个IMSI及其对应的MSISDN通过相同的Common MSISDN号码建立一个群组，群组对外呈现的号码是同一Common MSISDN号码。

## 注意事项

- 使用本命令的用户必须为M2M用户。
- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

  M2M Common MSISDN业务还与其他许多业务存在冲突，不能同时签约。这些业务包括：COMISDN、MIMSI、多SIM、多SIM增强、GROUPSIM、一卡多号多Profile、Home Zone、FM、ALS、LINKED SIM和M2M ISDN-Less。

## 参数说明

| 参数标识        | 参数名称           | 参数说明                                                                                                                                                                                                                                                    |
|:------------|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI           | 用于标识需要增加/修改/删除哪个IMSI号码的用户的M2M Common MSISDN号码。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                            |
| ISDN        | MSISDN         | 用于标识需要增加/修改/删除哪个MSISDN号码的用户的M2M Common MSISDN号码。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                          |
| RECORDCOUNT | 用户个数           | 用于标识需要增加/修改/删除M2M Common MSISDN号码的用户数目。 当需要为连续号码的多个用户增加/修改/删除M2M Common MSISDN号码时配置该参数，配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，对连续号码的多个用户进行操作。 取值范围：1～100000 默认值：无。 说明：该参数是对连续号码的多个用户操作，当只有一个用户时，该参数不必配置。当一次设置的用户个数很多时，对系统性能无影响，但设置的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名        | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的需要签约或去签约用户类别业务的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“modm2mcisdn.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                                                |
| ISDNFILE    | MSISDN文件名      | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的需要签约或去签约用户类别业务的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“modm2mcisdn.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16个字母或数字组成的字符串。 默认值：无。                                                          |
| PROV        | 是否提供M2MCISDN号码 | 用于标识是否为M2M用户提供M2MCISDN号码。 取值范围：TRUE：增加或修改M2M用户的Common MSISDN号码。FALSE：删除M2M用户的Common MSISDN。 默认值：无。                                                                                                                                                      |
| M2MCISDN    | M2MCISDN号码     | 仅当本命令中的“是否提供M2MCISDN号码”为“TRUE”时该参数有效。用于标识M2M用户增加或修改后的新的Common MSISDN号码。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                   |

## 使用实例

1. 修改“IMSI”号码为“460000009123456”的M2M用户的M2M Common MSISDN业务，“是否提供M2MCISDN号码”为“TRUE”，“M2MCISDN号码”为“8613900001238”，命令如下：

   ```
   MOD M2MCISDN: IMSI="460000009123456", PROV=TRUE, M2MCISDN="8613900001238";
   ```
2. 修改3个连续号码的M2M用户的M2M Common MSISDN业务，这三个用户为“MSISDN”号码分别为“8613900001234”、“8613900001235”、“8613900001236”，“是否提供M2MCISDN号码”为“TRUE”，“M2MCISDN号码”为“8613900001238”，命令如下：

   ```
   MOD M2MCISDN: ISDN="8613900001234", RECORDCOUNT=3, PROV=TRUE, M2MCISDN="8613900001238";
   ```
3. 撤销3个非连续号码的M2M用户的M2M Common MSISDN业务，这三个用户的MSISDN号码分别为“8613900001231”、“8613900001233”、“8613900001235”，已保存在“MSISDN文件名”为“modm2mcisdn.txt”的文件中，并通过文件管理功能上传到指定目录，“是否提供M2MCISDN号码”为“FALSE”，命令如下：

   ```
   MOD M2MCISDN: ISDNFILE="modm2mcisdn.txt", PROV=FALSE;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                       | 原因分析                                                                                                                                            | 处理建议                                                                                                                                                                                                                                                               |
|:--------|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值                      | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。当“是否提供M2MCISDN号码”为“TRUE”时，参数“M2MCISDN号码”的取值不是1～15位十进制数字组成的字符串。          | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                                                                                                                                                   |
| ERR1005 | 文件未找到                       | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                                                                | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                                                                                                                                                                 |
| ERR1009 | 参数丢失                        | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。当“是否提供M2MCISDN号码”为“TRUE”时，没有输入参数“M2MCISDN号码”。                                        | 根据实际情况，重新输入参数，确保满足如下要求：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。“是否提供M2MCISDN号码”为“TRUE”时，参数“M2MCISDN号码”必须出现。                                                                                                                                      |
| ERR1010 | 参数冲突                        | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。当“是否提供M2MCISDN号码”为“FALSE”时，参数“M2MCISDN号码”被输入。 | 根据实际情况，重新输入参数，确保满足如下要求：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。“是否提供M2MCISDN号码”为“FALSE”时，不出现参数“M2MCISDN号码”。                                                                                                |
| ERR1025 | 批操作文件中格式非法                  | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                                                                           | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                                                                                                                                                                       |
| ERR1033 | 您没有权限对该用户进行设置               | 输入的“IMSI”或“MSISDN”不在ADD VHLRRANGE命令设置的虚拟HLR号段管理范围内。                                                                                             | 核实用户的IMSI号码或MSISDN号码，按照以下步骤操作：执行LST SUB命令输入“IMSI”或“MSISDN”查询用户所在的“HLRSN”。登录系统管理界面执行LST VHLRRANGE命令输入“HLRSN”查询所在虚拟HLR的号段管理范围，确保输入的“IMSI”或“MSISDN”在所查询的虚拟HLR号段管理范围内。                                                                                                 |
| ERR1118 | 参数重复                        | 重复输入了该命令中的任意参数。                                                                                                                                 | 核实输入的命令，若命令中任意参数输入了两次以上，则删除多余的重复参数后，重新执行该命令。                                                                                                                                                                                                                       |
| ERR3001 | 用户未开户                       | 输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                                                                                   | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，则在执行该命令前先通过ADD SUB命令给用户开户。                                                                                                                                                                          |
| ERR4053 | 非M2M用户不能设置M2M Common MSISDN | 设置“M2MCISDN号码”参数的用户不是M2M用户。                                                                                                                     | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，需要为用户签约M2M Common MSISDN业务，则在执行此命令前先通过MOD USERCATEGORY命令将用户修改为M2M用户。                                                                                                                                                                 |
| ERR4056 | 业务冲突，用户已经签约MIMSI业务          | 用户签约M2M Common MSISDN业务前已经签约MIMSI业务。                                                                                                            | M2M Common MSISDN业务不能与MIMSI业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD MIMSI命令给用户去签约MIMSI业务。                                                                                                                                                                |
| ERR4057 | 业务冲突，用户已经签约多SIM业务           | 用户签约M2M Common MSISDN业务前已经签约多SIM业务。                                                                                                             | M2M Common MSISDN业务不能与多SIM业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD MSIM命令给用户去签约多SIM业务。                                                                                                                                                                   |
| ERR4058 | 业务冲突，用户已经签约COMISDN业务        | 用户签约M2M Common MSISDN业务前已经签约COMISDN业务。                                                                                                          | M2M Common MSISDN业务不能与COMISDN业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD COMISDN命令给用户去签约COMISDN业务。                                                                                                                                                          |
| ERR4059 | 业务冲突，用户已经签约GROUPSIM业务       | 用户签约M2M Common MSISDN业务前已经签约GROUPSIM业务。                                                                                                         | M2M Common MSISDN业务不能与GROUPSIM业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD GROUPSIM命令给用户去签约GROUPSIM业务。                                                                                                                                                       |
| ERR4060 | 业务冲突，用户已经签约多号码用户群组业务        | 用户签约M2M Common MSISDN业务前已经签约多号码用户群组业务。                                                                                                          | M2M Common MSISDN业务不能与多号码用户群组业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD MNUG命令给用户去签约多号码用户群组业务。                                                                                                                                                             |
| ERR4061 | 业务冲突，用户已经签约多号码业务            | 用户签约M2M Common MSISDN业务前已经签约ALS、VVDN业务，或已使用SET MULTISDN命令签约多号码类业务。                                                                              | M2M Common MSISDN业务不能与ALS、VVDN业务，以及SET MULTISDN命令签约的多号码类业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先执行LST SUB命令仅输入用户的“IMSI”或“MSISDN”，查看输出结果项：显示“ALS”为“PROV”，执行MOD ALS命令给用户去签约ALS业务。显示“VVDN”为“PROV”，执行MOD VVDN命令给用户去签约VVDN业务。显示多个“ISDN”，执行SET MULTISDN命令删除用户所有辅号码。 |
| ERR4062 | 业务冲突，用户已经签约FM业务             | 用户签约M2M Common MSISDN业务前已经签约Follow Me业务。                                                                                                        | M2M Common MSISDN业务不能与Follow Me业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD FM命令给用户去签约Follow Me业务。                                                                                                                                                           |
| ERR4064 | 业务冲突，用户已经签约Home Zone业务      | 用户签约M2M Common MSISDN业务前已经签约Home Zone业务。                                                                                                        | M2M Common MSISDN业务不能与Home Zone业务同时签约。如果需要用户签约M2M Common MSISDN业务，则在执行此命令前需先使用MOD HZ命令给用户去签约Home Zone业务。                                                                                                                                                           |