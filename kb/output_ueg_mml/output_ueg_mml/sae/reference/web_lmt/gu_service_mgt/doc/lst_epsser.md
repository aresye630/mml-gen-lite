# 查询EPS业务（LST EPSSER）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户EPS业务数据的配置信息。

- 若需要查询某个用户的EPS业务数据，请输入“IMSI”或“MSISDN”参数中的任意一个。
- 若需要查询连续多个用户的EPS业务数据，请输入以下两组的任意一个：
  - “IMSI”、“用户个数”和“IMSI文件名”。
  - “MSISDN”、“用户个数”和“MSISDN文件名”。

## 注意事项

“IMSI”、“MSISDN”、“IMSI文件名”和“MSISDN文件名”是互斥参数，有且只能有一个参数出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                  |
|:------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 用于指示系统按照哪个IMSI号码查询对应的EPS业务数据。                                                                                                                         |
| ISDN        | MSISDN    | 用于指示系统按照哪个MSISDN号码查询对应的EPS业务数据。                                                                                                                       |
| RECORDCOUNT | 用户个数      | 用于指示系统根据设置的用户个数来查询用户EPS业务数据。 该参数使用约束如下： “IMSI文件名”和“MSISDN文件名”不能输入。“IMSI”或“MSISDN”必须存在一个。如果只有一个用户，该参数不必提供。当一次设置的用户个数很多时，对系统性能无影响，但设置的用户个数越多，消耗的时间越长。   |
| IMSIFILE    | IMSI文件名   | 用于指示系统需要按照哪个IMSI文件名来查询用户的EPS业务数据。                                                                                                                     |
| ISDNFILE    | MSISDN文件名 | 用于指示系统需要按照哪个MSISDN文件名来查询用户的EPS业务数据。                                                                                                                   |
| DETAIL      | 是否返回详细信息  | 用于标识系统是否返回查询的详细信息。 取值范围： TRUE：显示用户详细信息。查询结果包括IMSI、MSISDN、PDN上下文索引值APN以及完整的QOS参数。FALSE：显示用户精简信息。查询结果包含IMSI、MSISDN、PDN上下文索引值以及EPSAPNQOS模板ID。 默认值：FALSE。 |

## 使用实例

1. 查询IMSI号码为“460000009123456”的用户的EPS业务数据，且不返回详细信息：

   ```
   LST EPSSER: IMSI="460000009123456", DETAIL=FALSE;
   ```

   ```
   %%LST EPSSER: IMSI="460000009123456", DETAIL=FALSE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 8613900001234
                    CHARGE_GLOBAL = NONE
            AMBRMAXREQBWUL_GLOBAL = 4294967111
            AMBRMAXREQBWDL_GLOBAL = 4294967222
                   AMBRMAXUL_UNIT = kbps
                   AMBRMAXDL_UNIT = kbps
               DEFAULTNONIPCNTXID = 1
                           CNTXID = 1
                      APNQOSTPLID = 11
                       IPV4ADDIND = DYNAMIC
                      OTHERADDIND = DYNAMIC

   Total count = 12

   There is together 1 report

   ---    END
   ```
2. 查询MSISDN号码为“460456301003017”的用户EPS业务数据，且返回详细信息：

   ```
   LST EPSSER: ISDN="460456301003017", DETAIL=TRUE;
   ```

   ```
   %%LST EPSSER: IMSI="460000009123456", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 8613900001234
                    CHARGE_GLOBAL = NONE
            AMBRMAXREQBWUL_GLOBAL = 4294967111
            AMBRMAXREQBWDL_GLOBAL = 4294967222
                   AMBRMAXUL_UNIT = kbps
                   AMBRMAXDL_UNIT = kbps
               DEFAULTNONIPCNTXID = 1
                           CNTXID = 1
                          PDNTYPE = IPV4
                         QOSTPLID = 11
                       IPV4ADDIND = DYNAMIC
                      OTHERADDIND = DYNAMIC
                       QOSCLASUID = 5
                         PRILEVEL = 1
                    PREEMPTIONCAP = ENABLE
                    PREEMPTIONVUL = ENABLE
                        AMBRMAXUL = 100000
                        AMBRMAXDL = 200000
                      NONIPAPNFLAG = TRUE

   Total count = 20

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1所示。

| 输出项名称       | 输出项解释                                 |
|:------------|:--------------------------------------|
| CNTXID      | PDN上下文索引值。                            |
| APNQOSTPLID | APN QoS模板ID。                          |
| DEFAULTFLAG | 默认标识。                                 |
| RELCLS      | 可靠性级别，具体请参见ADD QOSTPL命令中的参数“可靠性级别”解释。 |
| DELAYCLS    | 延迟级别，具体请参见ADD QOSTPL命令中的参数“延迟级别”解释。   |
| PRECLS      | 优先级别，具体请参见ADD QOSTPL命令中的参数“优先级别”解释。   |
| PEAKTHR     | 峰值吞吐量，具体请参见ADD QOSTPL命令中的参数“峰值吞吐量”解释。 |
| MEANTHR     | 平均吞吐量，具体请参见ADD QOSTPL命令中的参数“平均吞吐量”解释。 |
| APN         | APN名称。                                |
| 其他参数        | 请参见MOD EPSSER命令的参数说明。                 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释         | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:--------------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值        | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失          | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到         | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突          | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3810 | 用户不是EPS用户或未开户 | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户或者不是EPS用户。                                    | 核实IMSI号码或MSISDN号码，确保其对应的用户为EPS用户并验证其正确性，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请参考ADD SUB页面给用户开户。                    |
| ERR1025 | 批操作文件中格式非法    | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |