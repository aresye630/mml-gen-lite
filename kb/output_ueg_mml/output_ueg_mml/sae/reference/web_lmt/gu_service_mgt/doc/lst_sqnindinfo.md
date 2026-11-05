# 查询SQN的IND分域配置(LST SQNINDINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

本命令用于查询SQNINDINFO配置记录中SQN IND签约的域。

- 若需要查询某个“HLR序列号”下的所有“IND分域序列号”信息，请输入参数“HLR序列号”。
- 若需要查询单条SQNINDINFO配置记录，请输入参数“HLR序列号”和“IND分域序列号”。该操作场景下，执行本命令会分别返回每个IND配置的域，以及每个域的范围，如果IND未配置域，则查询结果显示“NULL”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                               |
|:-------|:---------|:---------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号   | 可选必选说明：必选参数 参数含义：用于标识待查询的IND分域记录所在的HLR序列号。该参数必须先由ADD HLRSN令定义，然后才能在此处引用。 取值范围：1～255 默认值：无。 配置原则：无。 |
| INDSNO | IND分域序列号 | 可选必选说明：可选参数 参数含义：标识要查询哪一个IND分域序列号的SQNINDINFO配置记录。 取值范围：0～65534 默认值：无。 配置原则：无。                      |

## 使用实例

- 查询“HLR序列号”为“1”、“IND分域序列号”为“1”的配置记录：

  ```
  LST SQNINDINFO: HLRSN=1, INDSNO=1;
  ```

  ```
  %%LST SQNINDINFO: HLRSN=1, INDSNO=1;%%
  RETCODE = 0 SUCCESS0001:操作成功

                           HLRSN = 1
                          INDSNO = 1

  "Domain of per IND"
                            IND0 = CS
                            IND1 = PS
                            IND2 = LTE
                            IND3 = IMS
                            IND4 = BSF
                            IND5 = AAA
                            IND6 = NGC
                            IND7 = NULL
                            IND8 = NULL
                            IND9 = NULL
                           IND10 = NULL
                           IND11 = NULL
                           IND12 = NULL
                           IND13 = NULL
                           IND14 = NULL
                           IND15 = NULL
                           IND16 = NULL
                           IND17 = BSF
                           IND18 = NULL
                           IND19 = NULL
                           IND20 = NULL
                           IND21 = NULL
                           IND22 = NULL
                           IND23 = NULL
                           IND24 = NULL
                           IND25 = NULL
                           IND26 = NULL
                           IND27 = NULL
                           IND28 = NULL
                           IND29 = NULL
                           IND30 = NULL
                           IND31 = NULL

  "IND of per Domain"
                              CS = 0~0
                              PS = 1~1
                             LTE = 2~2
                             IMS = 3~3
                             BSF = 4~4,17~17
                             AAA = 5~5
                             NGC = 6~6

  Total count = 41

  There is together 1 report

  ---    END
  ```
- 查询“HLR序列号”为“1”时所有“IND分域序列号”信息：

  ```
  LST SQNINDINFO: HLRSN=1;
  ```

  ```
  %%LST SQNINDINFO: HLRSN=1;%%
  RETCODE = 0 SUCCESS0001:操作成功

                 HLRSN        INDSNO
                 1            1
                 1            10
                 1            25
                 1            33
                 1            65
                 1            88
                 1            100
                 1            1111
                 1            65533
                 1            65534

  Total count = 10

  There is together 1 report

  ---    END
  ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                          | 处理建议                                                                                                                                                |
|:--------|:--------|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | 可能原因如下：待查询的“HLR序列号”未定义。同时输入“HLR序列号”和“IND分域序列号”，“IND分域序列号”未定义。 | 建议如下处理：“HLR序列号”未定义时，执行LST HLRSN命令查询已配置的“HLR序列号”，然后执行本命令查询。“IND分域序列号”未定义时，执行本命令仅输入“HLR序列号”查询当前HLRSN对应的“IND分域序列号”，然后输入已存在的“HLR序列号”和“IND分域序列号”执行本命令查询。 |