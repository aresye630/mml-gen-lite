# 查询M2MCISDN业务(LST M2MCISDN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户的M2M Common MSISDN业务：

- 若需要查询单个用户的M2M Common MSISDN业务，请输入“IMSI”或“MSISDN”。
- 若需要查询多个连续用户的M2M Common MSISDN业务，请输入“IMSI”或“MSISDN”与“用户个数”的组合。
- 若需要查询多个不连续用户的M2M Common MSISDN业务，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                               |
|:------------|:----------|:---------------------------------------------------|
| IMSI        | IMSI      | 用于指示系统需要查询哪个IMSI号码的用户的M2M Common MSISDN业务。         |
| ISDN        | MSISDN    | 用于指示系统需要查询哪个MSISDN号码的用户的M2M Common MSISDN业务。       |
| RECORDCOUNT | 用户个数      | 用于指示系统需要查询连续多少个用户的M2M Common MSISDN业务。             |
| IMSIFILE    | IMSI文件名   | 用于指示系统需要查询哪个IMSI批操作文件中包含的用户的M2M Common MSISDN业务。   |
| ISDNFILE    | MSISDN文件名 | 用于指示系统需要查询哪个MSISDN批操作文件中包含的用户的M2M Common MSISDN业务。 |

## 使用实例

1. 查询“IMSI”号码为“460000009123456”的用户的M2M Common MSISDN业务：

   ```
   LST M2MCISDN: IMSI="460000009123456";
   ```

   ```
   %%LST M2MCISDN: IMSI="460000009123456";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 46000000912345
                         M2MCISDN = 8613900001235

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“IMSI”号码为“460000009123456”、“460000009123457”、“460000009123458”的连续3个用户的M2M Common MSISDN业务：

   ```
   LST M2MCISDN: IMSI="460000009123456", RECORDCOUNT=3;
   ```

   ```
   %%LST M2MCISDN: IMSI="460000009123456", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：16. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“MSISDN文件名”为“lstm2mcisdn.txt”的用户的M2M Common MSISDN业务：

   ```
   LST M2MCISDN: IMSIFILE="lstm2mcisdn.txt";
   ```

   ```
   %%LST M2MCISDN: IMSIFILE="lstm2mcisdn.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：3432334. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**MOD M2MCISDN**

命令的参数说明，表1列出的是未包含在

**MOD M2MCISDN**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                      |
|:--------|:-------------------------------------------|
| 批操作ID   | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释         | 原因分析                                                                                               | 处理建议                                                                                                                                                               |
|:--------|:--------------|:---------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值        | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                                                           |
| ERR1005 | 文件未找到         | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                                                                 |
| ERR1009 | 参数丢失          | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                                                                        |
| ERR1010 | 参数冲突          | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。                                            |
| ERR1025 | 批操作文件中格式非法    | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                                                                       |
| ERR1033 | 您没有权限对该用户进行设置 | 输入的“IMSI”或“MSISDN”不在ADD VHLRRANGE命令设置的虚拟HLR号段管理范围内。                                                | 核实用户的IMSI号码或MSISDN号码，按照以下步骤操作：执行LST SUB命令输入“IMSI”或“MSISDN”查询用户所在的“HLRSN”。登录系统管理界面执行LST VHLRRANGE命令输入“HLRSN”查询所在虚拟HLR的号段管理范围，确保输入的“IMSI”或“MSISDN”在所查询的虚拟HLR号段管理范围内。 |
| ERR1118 | 参数重复          | 重复输入了该命令中的任意参数。                                                                                    | 核实输入的命令，若命令中任意参数输入了两次以上，则删除多余的重复参数后，重新执行该命令。                                                                                                                       |
| ERR3001 | 用户未开户         | 输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                                      | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，则在执行此命令前先通过ADD SUB命令给用户开户。                                                                          |