# 查询IMSI号段属性(LST IWFIMSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询IMSI号段属性的 配置信息：

- 若要查询全部IMSI号段属性配置信息时，请不要输入“IMSI前缀”。
- 若要查询指定IMSI号段属性精确配置信息时，请输入“IMSI前缀”。

## 注意事项

若未指定“IMSI前缀”进行查询时，当记录数超过1000条时，需要输入“保存文件名”参数指定保存查询结果的文件名称。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                           |
|:--------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数 参数含义：用于指示系统按照哪个IMSI前缀来查询IMSI号段的属性精确配置信息；若不输入，则表示查询所有IMSI号段的属性配置信息。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 配置原则：无。                                                                           |
| SAVEAS  | 保存文件名  | 可选必选说明：可选参数 参数含义：用于标识保存查询结果的文件名称。 取值范围：长度不超过20的字符串。 默认值：无 配置原则： 当查询结果的记录数超过1000条时必须输入该参数，将查询结果保存在文件中，否则会报错“ERR4121：查询结果已经超过1000条，需要指定保存文件名进行查询。”保存文件名参数指定的文件，可以通过“PGW Web LMT”界面右上角的“文件管理器”下载。 |

## 使用实例

1. 查询“IMSI前缀”为“46000”的属性精确配置信息：

   ```
   LST IWFIMSI: IMSIPRE="46000";
   ```

   ```
   %%LST IWFIMSI: IMSIPRE="46000";%%
   RETCODE = 0 SUCCESS0001:操作成功

                          IMSIPRE = 46000
                             MODE = UDM
                              PID = 2
                         AUTHTYPE = MAP
                              SSN = 149
                          NUMPLAN = IMSI
                         NODETYPE = 16
                           PLMNID = 12345
                     NGSUSERTPLID = 0
                         SERVLIST = 0
                            HLRSN = 0
                       NGSRATSUPP = TRUE
                         OMUHLRSN = 1
                      LIRHOSTFLAG = TRUE
                      ULRHOSTFLAG = TRUE
                   USERECOREDHOST = TRUE

   Total count = 16

   There is together 1 report

   ---    END
   ```
2. 查询所有IMSI号段的配置信息：

   ```
   LST IWFIMSI:;
   ```

   ```
   %%LST IWFIMSI:;%%
   RETCODE = 0 SUCCESS0001:操作成功

   IMSIPRE          MODE             PID              AUTHTYPE         SSN              NUMPLAN          NODETYPE         PLMNID           NGSUSERTPLID     SERVLIST         HLRSN            NGSRATSUPP       OMUHLRSN         LIRHOSTFLAG      ULRHOSTFLAG      USERECOREDHOST
   46000            UDM              2                MAP              149              IMSI             16               12345            0                0                0                TRUE             1                TRUE             TRUE             TRUE
   46001            IWF              2                MAP              149              IMSI             16               12345            1                5                1                TRUE             1                TRUE             TRUE             TRUE
   46002            BlackList        0                MAP              0                IMSI             0                NULL             0                0                0                FALSE            0                FALSE            FALSE            FALSE
   46003            AuthOnly         2                MAP              149              IMSI             16               NULL             0                0                0                FALSE            1                FALSE            FALSE            FALSE
   46005            SQNSYNC          2                MAP              149              IMSI             16               NULL             0                0                0                FALSE            1                FALSE            FALSE            FALSE

   Total count = 5     

   There is together 1 report

   ---    END
   ```
3. 查询结果记录数为1500条时，设置保存文件名为“iwfimsi”，将查询结果保存在文件中：

   ```
   LST IWFIMSI: SAVEAS="iwfimsi";
   ```

   ```
   %%LST IWFIMSI: SAVEAS="iwfimsi";%%
   RETCODE = 0 SUCCESS0001:操作成功

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD IWFIMSI**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                        | 原因分析                             | 处理建议                                                             |
|:--------|:-----------------------------|:---------------------------------|:-----------------------------------------------------------------|
| ERR3007 | 记录不存在                        | 实际输入的参数“IMSI前缀”对应的IMSI号段属性数据不存在。 | 核实正确的IMSI号段，如果确定输入无误，证明该IMSI号段属性已删除，查询不到该号段数据，否则重新输入正确的“IMSI前缀”。 |
| ERR4121 | 查询结果已经超过1000条，需要指定保存文件名进行查询。 | 查询结果超过1000条，但未输入参数“保存文件名”。       | 输入参数“保存文件名”，将查询结果保存在文件中。                                         |