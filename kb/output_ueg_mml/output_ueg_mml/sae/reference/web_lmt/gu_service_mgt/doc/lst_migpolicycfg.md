# 查询割接策略模板(LST MIGPOLICYCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为配置类命令，用于在配置数据库中查询割接策略配置信息：

- 若需要查询某个HLR下所有割接策略模板记录信息，请输入“HLR序列号”参数。
- 若需要查询某个割接策略模板记录的详细信息，请输入“HLR序列号”和“割接策略ID”参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                           |
|:-------------|:-------|:-------------------------------|
| HLRSN        | HLR序列号 | 用于标识系统需要按照哪个HLR序列号来查询割接策略模板数据。 |
| MIG_POLICYID | 割接策略ID | 用于标识系统需要按照哪个割接策略ID来查询割接策略模板数据。 |

## 使用实例

1. 查询“HLR序列号”为“1”模板的所有割接策略信息：

   ```
   LST MIGPOLICYCFG: HLRSN=1;%%
   ```

   ```
   LST MIGPOLICYCFG: HLRSN=1;
   RETCODE = 0 SUCCESS0001:操作成功

                  MIG_POLICYID   POLICY_NAME
                  0              <NULL>
                  5000           <NULL>

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”且“割接策略ID”为“0”模板的所有割接策略信息：

   ```
   LST MIGPOLICYCFG: HLRSN=1, MIG_POLICYID=0;
   ```

   ```
   %%LST MIGPOLICYCFG: HLRSN=1, MIG_POLICYID=0;%%
   RETCODE = 0 SUCCESS0001:操作成功

                     MIG_POLICYID = 0
                      POLICY_NAME = a
                       ROUTE_TYPE = IMSI_TYPE
              WHETHER_FORWARD_MAP = TRUE
                            HLRNO = 1
                       ROUTE_TYPE = MSISDN_TYPE
              WHETHER_FORWARD_MAP = TRUE
                              PID = 1
                       ROUTE_TYPE = ATI_TYPE
                 WHETHER_SEND_ATI = TRUE
                            HLRNO = 2
                       ROUTE_TYPE = EPS_TYPE
     WHETHER_FORWARD_EPS_DIAMETER = TRUE
                              PID = 2
                       ROUTE_TYPE = IMS_TYPE
     WHETHER_FORWARD_IMS_DIAMETER = TRUE
                              PID = 3

   Total count = 17

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD MIGPOLICYCFG**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                            | 处理建议                                                           |
|:--------|:----------|:--------------------------------|:---------------------------------------------------------------|
| ERR3007 | 模板未定义     | “割接策略ID”未定义。                    | 根据实际情况，重新输入已定义的“割接策略ID”，通过该命令查询已定义的“割接策略ID”。                   |
| ERR3097 | HLR序列号未定义 | 参数“HLR序列号”的取值未预先定义，对应序号的HLR不存在。 | 根据实际情况,重新输入参数“HLR序列号”的取值，确保其取值已被定义。已定义的“HLR序列号”可通过LST HLRSN查询。 |