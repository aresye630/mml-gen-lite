# 查询地址限制（LST BWADDR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询地址限制表中的地址信息：

- 若需要查询MAP请求消息的缺省处理规则，则输入“HLR序列号”，“操作类型”选择“DEFRULE”。
- 若需要查询地址限制表中全部地址，则输入“HLR序列号”，“操作类型”选择“ALL”。
- 若需要查询地址限制表中指定的地址，则输入“HLR序列号”，“操作类型”选择“ONE”并且输入“地址号码”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                      |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询地址限制表中的地址信息。                                                                           |
| OPTYPE | 操作类型   | 用于指示系统按照哪种操作类型来查询地址限制表中的地址信息。 取值范围： DEFRULE：查询MAP请求消息的缺省处理规则。 ALL：查询地址限制表中全部地址。 ONE：查询地址限制表中指定的地址。 默认值：无。 |
| ADDR   | 地址号码   | 仅当参数“操作类型”为“ONE”时该参数有效。用于指示系统需要按照哪个地址号码查询地址限制表中的地址信息。                                                     |

## 使用实例

1. 查询MAP请求消息的缺省处理规则：

   `LST BWADDR: HLRSN=1, OPTYPE=DEFRULE;`

   ```
   %%LST BWADDR: HLRSN=1, OPTYPE=DEFRULE;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "SRIFORSM"      "SRIFORGPRS"    "ATI"           "SRI"           "ATSI"          "USSDR"               "ATM"           "SRIFORLCS"     "PURGEMS"             "ISTALERT"            "REGISTERSS"          "ERASESS"             "ACTIVATESS"          "DEACTIVATESS"        "INTERROGATESS"       "REGISTERPWD"         "PUSSDR"              "SENDIMSI"            "READYFORSM"          "RSD"                 "SENDPARAMETERS"      "USSDN"               "REPORTSMDELSTA"      "FAILUREREPORT"
           ALLOWABLE       ALLOWABLE       ALLOWABLE       ALLOWABLE       ALLOWABLE       ALLOWABLE             ALLOWABLE       ALLOWABLE       ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE             ALLOWABLE

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询地址限制表中全部地址信息：

   `LST BWADDR: HLRSN=1, OPTYPE=ALL;`

   ```
   %%LST BWADDR: HLRSN=1, OPTYPE=ALL;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "ADDRESS"        "SRIFORSM"      "SRIFORGPRS"    "ATI"           "SRI"           "ATSI"          "USSDR"         "ATM"           "SRIFORLCS"     "PURGEMS"             "ISTALERT"            "REGISTERSS"          "ERASESS"             "ACTIVATESS"          "DEACTIVATESS"        "INTERROGATESS"       "REGISTERPWD"         "PUSSDR"              "SENDIMSI"            "READYFORSM"          "RSD"                 "SENDPARAMETERS"      "USSDN"               "REPORTSMDELSTA"      "FAILUREREPORT"
           123456           <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>                <NULL>                FORBIDDEN             <NULL>                <NULL>                <NULL>                FORBIDDEN             <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>
           12345            <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                ALLOWABLE             <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>
           123              ALLOWABLE       <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                ALLOWABLE             <NULL>

   Total count = 3

   There is together 1 report

   ---    END
   ```
3. 查询地址限制表中“地址号码”为“123456”的地址信息：

   `LST BWADDR: HLRSN=1, OPTYPE=ONE, ADDR="123456";`

   ```
   %%LST BWADDR: HLRSN=1, OPTYPE=ONE, ADDR="123456";%%
   RETCODE = 0 SUCCESS0001:操作成功

           "ADDRESS"        "SRIFORSM"      "SRIFORGPRS"    "ATI"           "SRI"           "ATSI"          "USSDR"         "ATM"           "SRIFORLCS"     "PURGEMS"             "ISTALERT"            "REGISTERSS"          "ERASESS"             "ACTIVATESS"          "DEACTIVATESS"        "INTERROGATESS"       "REGISTERPWD"         "PUSSDR"              "SENDIMSI"            "READYFORSM"          "RSD"                 "SENDPARAMETERS"      "USSDN"               "REPORTSMDELSTA"      "FAILUREREPORT"
           123456           <NULL>          ALLOWABLE       <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>          <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>                <NULL>

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET BWADDR**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                          | 处理建议                                                                                                                                    |
|:--------|:--------|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | 可能原因为如下之一：输入的“HLR序列号”不存在。参数“操作类型”设置为“ONE”时，输入的“地址号码”对应的记录不存在。 | 根据实际情况选择：核实输入的“HLR序列号”，重新输入参数，确保输入的“HLR序列号”已存在，可通过LST HLRSN命令查询。核实输入的“地址号码”，重新输入参数，确保输入的“地址号码”已经在SET BWADDR命令中参数“操作类型”设置为“ADD”时添加了记录信息。 |
| ERR1004 | 无效的参数值  | 输入的参数取值不在其取值范围内。                                              | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                        |