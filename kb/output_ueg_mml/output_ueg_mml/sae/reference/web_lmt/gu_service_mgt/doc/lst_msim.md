# 查询多SIM业务(LST MSIM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询多SIM群组的签约信息，包括：多SIM业务类型，当前激活用户，多SIM成员号码等信息。

- 若要按多SIM群组主用户的IMSI号码来查询多SIM群组的签约信息，请输入“主IMSI号码”参数，其他参数不输入。
- 若要按多SIM群组主用户的MSISDN号码来查询多SIM群组的签约信息，请输入“主MSISDN号码”参数，其他参数不输入。

## 注意事项

“主IMSI号码”和“主MSISDN号码”是互斥参数，有且只能有一个参数出现。

## 参数说明

| 参数标识   | 参数名称      | 参数说明                                          |
|:-------|:----------|:----------------------------------------------|
| IMSI   | 主IMSI号码   | 用于指示系统需要按照哪个多SIM群组主用户的IMSI号码来查询多SIM群组的签约信息。   |
| ISDN   | 主MSISDN号码 | 用于指示系统需要按照哪个多SIM群组主用户的MSISDN号码来查询多SIM群组的签约信息。 |

## 使用实例

1. 查询“主IMSI号码”为“460111102102001”的用户的多SIM业务签约情况。命令如下：

   ```
   LST MSIM: IMSI="460111102102001";
   ```

   ```
   %%LST MSIM: IMSI="460111102102001";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                                 IMSI = 460111102102001
                                 ISDN = 86111102102001
                             MSIMTYPE = ActiveByUSSD
                           RESTRICTMO = FALSE

                         Member Number             ACTIVE          ORDERID    SMSMTALLOW
                         460111102102001            NO                1          TRUE
                         460111102102002            NO                2          FALSE
                         460111102102003           YES                3          FALSE
                         460111102102004            NO                4          FALSE

   Total count = 8

   There is together 1 report

   ---    END
   ```
2. 查询“主MSISDN号码”为“86111102102001”的用户的多SIM业务签约情况。命令如下：

   ```
   LST MSIM: ISDN="86111102102001";
   ```

   ```
   %%LST MSIM: ISDN="86111102102001";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                                 IMSI = 460111102102001
                                 ISDN = 86111102102001
                             MSIMTYPE = ActiveByUSSD
                           RESTRICTMO = FALSE

                         Member Number             ACTIVE          ORDERID    SMSMTALLOW
                         460111102102001           NO                1          TRUE
                         460111102102002           NO                2          FALSE
                         460111102102003           YES               3          FALSE
                         460111102102004           NO                4          FALSE
   Total count = 8

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD MSIM**命令的参数说明，表1列出的是未包含在**MOD MSIM**命令参数说明中的输出项。

| 输出项名称   | 输出项解释          |
|:--------|:---------------|
| MTISDN  | 激活用户的MSISDN号码。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释   | 原因分析                                  | 处理建议                                                                                           |
|:--------|:--------|:--------------------------------------|:-----------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 输入的界面参数不在取值范围内。                       | 参考MOD MSIM命令的参数说明，重新输入取值范围内的参数值。                                                               |
| ERR1009 | 参数丢失    | “主IMSI号码”和“主MSISDN号码”两个参数一个都没有输入。     | 根据实际情况，重新输入参数，确保“主IMSI号码”和“主MSISDN号码”两个参数必须有且只能有一个参数出现的条件。                                     |
| ERR1010 | 参数冲突    | “主IMSI号码”和“主MSISDN号码”两个参数同时输入。        | 根据实际情况，重新输入参数，确保“主IMSI号码”和“主MSISDN号码”两个参数必须有且只能有一个参数出现的条件。                                     |
| ERR3001 | 用户未开户   | 用户输入的参数“主IMSI号码”或“主MSISDN号码”对应的用户未开户。 | 检查用户的“主IMSI号码”或“主MSISDN号码”，如果确定输入无误，证明实际输入的参数“主IMSI号码”或“主MSISDN号码”对应的用户未开户，请先通过ADD SUB命令给用户开户。 |