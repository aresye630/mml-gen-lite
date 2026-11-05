# 查询高价值业务（LST GJZCONF）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询高价值业务配置信息。

- 若需要查询全部的高价值业务配置信息，不输入任何参数。
- 若需要查询某个“HLR序列号”的高价值业务配置信息，请输入“HLR序列号”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                    |
|:-------|:-------|:----------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 可选必选说明：可选参数 参数含义：用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。 取值范围：1～255 默认值：无。 配置原则：无。 |

## 使用实例

1. 查询全部的高价值业务配置信息。

   ```
   LST GJZCONF:;
   ```

   ```
   %%LST GJZCONF:;%%
   RETCODE = 0 SUCCESS0001:操作成功
    
   HLRSN    AREATYPE                                                    APNDNNLIST
   1        LOCAL&LOCALDOMESTIC&CROSSDOMESTIC&LOCALAREA&CROSSAREA       "Mnet.com"&"Cnet.com"
   2        LOCAL&LOCALDOMESTIC&CROSSDOMESTIC&LOCALAREA&CROSSAREA       CMNET 
    
   Total count = 2  

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的高价值业务配置信息。

   ```
   LST GJZCONF: HLRSN=1;
   ```

   ```
   %%LST GJZCONF: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             HLRSN = 1
                          AREATYPE = LOCAL&LOCALDOMESTIC&CROSSDOMESTIC&LOCALAREA&CROSSAREA
                        APNDNNLIST = "Mnet.com"&"Cnet.com"

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD GJZCONF**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                                       | 处理建议                                                                                  |
|:--------|:----------|:-------------------------------------------|:--------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值    | 界面输入的“HLR序列号”参数不在相应的参数取值范围内。               | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。                                                     |
| ERR3007 | 记录不存在     | “是否提供业务”取值为“FALSE”时，输入的“HLR序列号”未配置高价值业务数据。 | 根据实际情况，重新输入“HLR序列号”的取值，确保该“HLR序列号”已配置高价值业务数据，或设置“是否提供业务”取值为“TRUE”为该“HLR序列号”配置高价值业务数据。 |
| ERR3097 | HLR序列号未定义 | “HLR序列号”未定义。                               | 根据实际情况，重新输入“HLR序列号”的取值，或先由ADD HLRSN命令定义“HLR序列号”，然后才能在此处引用。                            |