# 查询NGS对端类型（LST NGSPETYPE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询对端类型信息。

- 如果需要查询某一个“HLR序列号”所有的对端类型记录，请输入“HLR序列号”参数。
- 如果需要查询某一个“PLMNID”所有的对端类型记录，请输入“HLR序列号”和“PLMNID”参数。
- 如果需要查询某一个“AMF Region ID”所有的对端类型记录，请输入“HLR序列号”、“PLMNID”参数和“AMF Region ID”。
- 如果需要查询某一个“AMF Set ID”的对端类型记录，请输入“HLR序列号”、“PLMNID”、“AMF Region ID”和“AMF Set ID”。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN     | HLR序列号        | 可选必选说明：必选参数 参数含义：用于指示系统按照哪个HLR序列号来查询对端类型数据。 取值范围：1～255 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                          |
| PLMN      | PLMNID        | 可选必选说明：可选参数 参数含义：用于指示查询哪个PLMN ID的对端类型数据。 取值范围：5～6位的十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                 |
| AMFREGION | AMF Region ID | 可选必选说明：可选参数 参数含义：用于指示查询哪个AMF Region ID的对端类型数据；若不输入，则表示查询所有的AMF Region ID。 取值范围：0～255 默认值：无。 配置原则：仅当本命令中的“AMF Set ID”参数不为空时，该参数必须配置。                                                                                                                                                                                                                                                                                                            |
| AMFSET    | AMF Set ID    | 可选必选说明：可选参数 参数含义：用于指示查询哪个AMF Set ID的对端类型数据；若不输入，则表示查询所有的AMF Set ID。 取值范围：0～1023 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                 |
| SAVEAS    | 保存文件名         | 可选必选说明：可选参数 参数含义：用于标识保存查询结果的文件名称。当查询结果的NGS对端类型信息记录超过999个时必须输入该参数，将查询结果保存在文件中，否则会报错“ERR4153：报文数量超过上限，需要指定保存文件名进行查询”。 取值范围：长度不超过20的字符串。可由字母、数字或字符组成，字符不能包含“>”、“/”、“?”、“\”、“:”、“*”、“"”、“<”、“|”和“'”。 默认值：无 配置原则： “保存文件名”参数指定的文件存放在主备PGW模块所在虚拟机（裸机POD）上，虚拟机（裸机POD）目录为“/opt/pgw/pgwtmpfile/SYSHLRSN+OPNAME”。SYSHLRSN默认为3位数字，不足3位时前面补0。如：SYSHLRSN=1，OPNAME=admin时，最后一层目录为001admin。保存文件名参数指定的文件，可以通过“PGW Web LMT”界面右上角的“文件管理器”下载。该参数与“PLMNID”参数只能输入一个。 |

## 使用实例

1. 查询“HLR序列号”为“3”的UDM上添加的对端类型数据：

   ```
   LST NGSPETYPE: HLRSN=3;
   ```

   ```
   %%LST NGSPETYPE: HLRSN=3;%%
   RETCODE = 0 SUCCESS0001:操作成功

   PETYPE      PLMN     AMFREGION      AMFSET    TYPE                 NGSNCCTPL      PEERNAME
   AMFREGION   11111    2              NULL      LOCALDOMESTIC        NULL           <NULL>
   PLMN        22222    NULL           NULL      LOCAL                1              MSC01
   AMFREGION   22221    3              NULL      LOCALDOMESTIC        1              <NULL>
   AMFSET      22223    5              6         CROSSDOMESTIC        1              <NULL>
   AMFSET      22223    6              2         LOCALDOMESTIC        1              GGSN

   Total count = 6

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“3”，“PLMNID”为“11113”的UDM上添加的对端类型数据：

   ```
   LST NGSPETYPE: HLRSN=3, PLMN="11113";
   ```

   ```
   %%LST NGSPETYPE: HLRSN=3, PLMN="11113";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                           PETYPE = AMFREGION
                             PLMN = 11113
                        AMFREGION = 3
                             TYPE = CROSSINTERNATIONAL
                        NGSNCCTPL = 1

                           PETYPE = AMFSET
                             PLMN = 11113
                        AMFREGION = 2
                           AMFSET = 3
                             TYPE = LOCALDOMESTIC
                        NGSNCCTPL = 1

                           PETYPE = AMFSET
                             PLMN = 11113
                        AMFREGION = 4
                           AMFSET = 3
                             TYPE = LOCALDOMESTIC
                        NGSNCCTPL = 1

   Total count = 17

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“3”的UDM上添加的对端类型数据，其中“PLMNID”为“11110”，“AMF Region ID”为“3”：

   ```
   LST NGSPETYPE: HLRSN=3, PLMN="11110", AMFREGION=3;
   ```

   ```
   %%LST NGSPETYPE: HLRSN=3, PLMN="11110", AMFREGION=3;%%
   RETCODE = 0 SUCCESS0001:操作成功

                           PETYPE = AMFREGION
                             PLMN = 11110
                        AMFREGION = 3
                             TYPE = LOCAL
                        NGSNCCTPL = 1

                           PETYPE = AMFSET
                             PLMN = 11110
                        AMFREGION = 3
                           AMFSET = 0
                             TYPE = CROSSAREA
                        NGSNCCTPL = 1

   Total count = 11

   There is together 1 report

   ---    END
   ```
4. 查询“HLR序列号”为“1”的UDM上添加的对端类型数据，其中“PLMNID”为“11111”，“AMF Region ID”为“3”，“AMF Set ID”为“1”：

   ```
   LST NGSPETYPE: HLRSN=1, PLMN="11111", AMFREGION=3, AMFSET=1;
   ```

   ```
   %%LST NGSPETYPE: HLRSN=1, PLMN="11111", AMFREGION=3, AMFSET=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                           PETYPE = AMFSET
                             PLMN = 11111
                        AMFREGION = 3
                           AMFSET = 1
                             TYPE = CROSSDOMESTIC
                        NGSNCCTPL = 1

   Total count = 6

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NGSPETYPE**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                   | 原因分析                                                                                                                                      | 处理建议                                                                                             |
|:--------|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| ERR1009 | 参数缺失                    | 原因为如下之一： 必选参数缺失：“HLR序列号”参数缺失。可选参数缺失：输入了“HLR序列号”和“AMF Region ID”参数，未输入“PLMNID”参数。输入了“HLR序列号”和“AMF Set ID”参数，未输入“AMF Region ID”和“PLMNID”参数。 | 重新输入缺失的参数： 当输入“AMF Region ID”参数时必须输入“PLMNID”参数。当输入“AMF Set ID”参数时必须输入“AMF Region ID”和“PLMNID”参数。 |
| ERR1010 | 参数冲突                    | 同时输入了“PLMNID”和“保存文件名”参数。                                                                                                                  | 根据实际情况，重新输入参数，确保满足“PLMNID”和“保存文件名”参数两个参数必须有且只能有一个参数出现。                                           |
| ERR3007 | 记录未定义                   | 参数“PLMNID”、“AMF Region ID”或“AMF Set ID”输入错误。                                                                                              | 输入正确的参数“PLMNID”、“AMF Region ID”或“AMF Set ID”参数值。                                                 |
| ERR3097 | HLR序列号未定义               | 输入的“HLR序列号”参数值没有在ADD HLRSN命令中定义。                                                                                                          | 执行LST HLRSN命令查询虚拟HLR的配置信息，然后输入正确的HLR序列号。                                                         |
| ERR4153 | 报文数量超过上限，需要指定保存文件名进行查询。 | NGS对端类型信息的数量超过了999个。                                                                                                                      | 输入参数“保存文件名”，将查询结果保存在文件中。                                                                         |