# 查询（Vo）LTE自动开户IMSI前缀限制(LST LTEAUTOFORBIDIMSIPRE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询控制自动开户的用户IMSI号码前缀信息。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                         |
|:-----------|:-------|:-------------------------------------------------------------|
| IMSIPREFIX | IMSI前缀 | 用于指示系统需要按照哪个IMSI号码前缀来查询控制自动开户的IMSI号码前缀信息；若不输入则表示所有的IMSI号码前缀。 |

## 使用实例

1. 查询控制自动开户的全部IMSI号码前缀信息：

   ```
   LST LTEAUTOFORBIDIMSIPRE:;
   ```

   ```
   %%LST LTEAUTOFORBIDIMSIPRE:;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  IMSIPREFIX      LTEAUTOPROV     VOWIFI_AUTOPROV     NSAAUTOPROV     LTENSAAUTOPROV
                  46000           23G-4G_VoLTE    AUTOPROV            NOT_SUPPORT     NOT_SUPPORT
                  46001001        234G-4G_VoLTE   AUTOPROV                            PROVANDMODNGRAN

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询IMSI号码前缀为“46000”的用户进行自动开户的控制规则，需要执行如下操作：

   ```
   LST LTEAUTOFORBIDIMSIPRE: IMSIPREFIX="46000";
   ```

   ```
   %%LST LTEAUTOFORBIDIMSIPRE: IMSIPREFIX="46000";%%
   RETCODE = 0 SUCCESS0001:操作成功

                       IMSIPREFIX = 46000
                      LTEAUTOPROV = 23G-4G_VoLTE
                  VOWIFI_AUTOPROV = AUTOPROV
                      NSAAUTOPROV = NOT_SUPPORT
                   LTENSAAUTOPROV = NOT_SUPPORT

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

| 输出项名称          | 输出项解释                                                                                                                           |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------|
| NSAAUTOPROV    | 用于返回UDM是否启用NSA自动开户特性。执行MOD LTEAUTOFORBIDIMSIPRE命令设置“是否启用NSA自动开户特性”参数后，该输出项才会显示取值。如果输出项取值为空或者不输出该输出项，则对应的参数不生效、不控制对应的业务。         |
| LTENSAAUTOPROV | 用于返回UDM是否支持同时开通LTE和NSA业务。执行MOD LTEAUTOFORBIDIMSIPRE命令设置“是否支持同时开通LTE和NSA业务”参数后，该输出项才会显示取值。如果输出项取值为空或者不输出该输出项，则对应的参数不生效、不控制对应的业务。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                | 处理建议                                                        |
|:--------|:--------|:--------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数“IMSI前缀”的取值不是1～15位十进制数字组成的字符串。                                                                                    | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                            |
| ERR3007 | 记录不存在   | 可能原因为如下之一：若执行该命令时未输入参数，则系统未使用MOD LTEAUTOFORBIDIMSIPRE添加过控制自动开户的用户IMSI号码前缀信息。若执行该命令时输入了“IMSI前缀”，则输入的“IMSI前缀”数据记录不存在。 | 根据实际情况，选择是否使用MOD LTEAUTOFORBIDIMSIPRE添加控制自动开户的用户IMSI号码前缀信息。 |