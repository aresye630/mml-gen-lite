# 查询（Vo）LTE自动开户IMEI前缀限制(LST LTEAUTOFORBIDIMEIPRE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询控制自动开户的用户IMEI号码前缀信息。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                         |
|:-----------|:-------|:-------------------------------------------------------------|
| IMEIPREFIX | IMEI前缀 | 用于指示系统需要按照哪个IMEI号码前缀来查询控制自动开户的IMEI号码前缀信息；若不输入则表示所有的IMEI号码前缀。 |

## 使用实例

1. 查询控制自动开户的全部IMEI号码前缀信息：

   ```
   LST LTEAUTOFORBIDIMEIPRE:;
   ```

   ```
   %%LST LTEAUTOFORBIDIMEIPRE:;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  IMEIPREFIX      FORBID_LTEAUTOPROV     FORBID_VOWIFI_AUTOPROV
                  47000           FORBID                 NOT_CTRL
                  47001           FORBID                 FORBID
                  4700123456789   FORBID                 FORBID

   Total count = 3

   There is together 3 report

   ---    END
   ```
2. 查询IMEI号码前缀为“47000”的用户进行自动开户的控制规则，需要执行如下操作：

   ```
   LST LTEAUTOFORBIDIMEIPRE: IMEIPREFIX="47000";
   ```

   ```
   %%LST LTEAUTOFORBIDIMEIPRE: IMEIPREFIX="47000";%%
   RETCODE = 0 SUCCESS0001:操作成功

                       IMEIPREFIX = 47000
               FORBID_LTEAUTOPROV = FORBID
           FORBID_VOWIFI_AUTOPROV = NOT_CTRL

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                | 处理建议                                                        |
|:--------|:--------|:--------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数“IMEI前缀”的取值不是1～15位十进制数字组成的字符串。                                                                                    | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                            |
| ERR3007 | 记录不存在   | 可能原因为如下之一：若执行该命令时未输入参数，则系统未使用MOD LTEAUTOFORBIDIMEIPRE添加过控制自动开户的用户IMEI号码前缀信息。若执行该命令时输入了“IMEI前缀”，则输入的“IMEI前缀”数据记录不存在。 | 根据实际情况，选择是否使用MOD LTEAUTOFORBIDIMEIPRE添加控制自动开户的用户IMEI号码前缀信息。 |